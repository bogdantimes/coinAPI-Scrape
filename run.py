""" Coinapi key generator and data downloader

Example, try:
python run.py --symbol=BITSTAMP_SPOT_LTC_USD  --source=ohlcv --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --timeout=20
python run.py --exchange=BITSTAMP  --source=ohlcv --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --limit=100000
python run.py --exchange=BITSTAMP  --source=trades --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --limit=100000


Usage:
  run.py (--symbol=<string>... | (--exchange=<string>... | --base=<string>... | --quote=<string>... | --type=<string>...) [--exchange=<string>...] [--base=<string>...] [--quote=<string>...] [--type=<string>...]) --source=<string> --from=<date> [--to=<date>] [--period=<string>]  [--limit=<int>]  [--levels=<int>]  [--path=<path>] [--filetype=<string>] [--proxy_type=<string>] [--timeout=<int>] [--generate_keys=<int>] [--find_n_proxy=<int>]
  run.py (-h | --help)

Arguments:
  --symbol=<string>     Symbol id for requested timeseries, it can be one or more space separated, check https://docs.coinapi.io/#list-all-symbols
  --exchange=<string>     identifier of the exchange where symbol is traded, it can be one or more space separated, check https://docs.coinapi.io/#list-all-symbols
  --base=<string>     FX Spot base asset identifier, for derivatives it’s contact underlying (e.g. BTC for BTC/USD), it can be one or more space separated, check https://docs.coinapi.io/#list-all-symbols
  --quote=<string>     FX Spot quote asset identifier, for derivatives it’s contract underlying (e.g. USD for BTC/USD), it can be one or more space separated, check https://docs.coinapi.io/#list-all-symbols
  --type=<string>     Type of symbol (possible values are: SPOT, FUTURES or OPTION), it can be one or more space separated
  --from=<date>     starting date.
  --source=<string>     the data to be downloaded (ohlcv, trades, quotes, order).

Options:
  -h --help     Show this screen.
  --path=<path>  a directory to save data to [default: out].
  --filetype=<string>  the saved data file type (json, csv) [default: csv].
  --to=<date>  ending date.
  --period=<string>  supported time periods available for requesting OHLCV timeseries data OR to convert data to, check https://docs.coinapi.io/#list-all-periods.
  --limit=<int>  Amount of items to return , minimum is 1, maximum is 100000 [default: 100].
  --levels=<int>  Maximum amount of levels from each side of the book to include in response, max 20 [default: 20].
  --timeout=<int>  request timeout [default: 120].
  --generate_keys=<int>  generate N new coinapi keys.
  --find_n_proxy=<int>  number of proxies to find at a time [default: 100].
  --proxy_type=<string>  type of proxy (None, fresh, list, rotate) [default: None].

"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import asyncio
import json
import os
import random
import re
import urllib
import urllib.parse
import urllib.request
from datetime import datetime
from time import sleep

import dateutil.parser
import requests

try:
    from docopt import docopt
    from schema import Schema, And, Or, Use, SchemaError, Optional
    import names
    from guerrillamail import GuerrillaMailSession
    from fake_useragent import UserAgent
    from proxybroker import Broker
    import pandas as pd
except ImportError:
    exit('One or more of the required libraries is missing\n'
         'Use the following commands to install them:\n'
         'pip install schema\n'
         'pip install docopt\n'
         'pip install names\n'
         'pip install python-guerrillamail\n'
         'pip install fake-useragent\n'
         'pip install proxybroker\n'
         'pip install pandas\n'
         '\n')

periods = ["1SEC", "2SEC", "3SEC", "4SEC", "5SEC", "6SEC", "10SEC", "15SEC", "20SEC", "30SEC", "1MIN", "2MIN", "3MIN",
           "4MIN", "5MIN", "6MIN", "10MIN", "15MIN", "20MIN", "30MIN", "1HRS", "2HRS", "3HRS", "4HRS", "6HRS", "8HRS",
           "12HRS", "1DAY", "2DAY", "3DAY", "5DAY", "7DAY", "10DAY", "1MTH", "2MTH", "3MTH", "4MTH", "6MTH", "1YRS",
           "2YRS", "3YRS", "4YRS", "5YRS"]
proxies_list = []
proxy_type = 'None'
PRODUCTION_URL = 'https://rest.coinapi.io/v1%s'
keys = []
proxy_types = ['None', 'fresh', 'list', 'rotate']
sources = ["ohlcv", "trades", "quotes", "order"]
filetypes = ["json", "csv"]
timeout = 120.0
args = {}


def generate_keys(num=1):
    print('generate_keys', end='\n' * 2)
    i = 0
    while i < num:
        try:
            session = GuerrillaMailSession()
            email_address = session.get_session_state()['email_address'].split('@')[0] + '@' + random.choice(
                ['sharklasers.com', 'guerrillamail.info', 'grr.la', 'guerrillamail.biz', 'guerrillamail.com',
                 'guerrillamail.de', 'guerrillamail.net', 'guerrillamail.org', 'guerrillamailblock.com', 'pokemail.net',
                 'spam4.me'])
            print('_' * 10)
            print(email_address)

            url = "https://rest.coinapi.io/www/freeplan"

            payload = {"email": email_address, "name": names.get_full_name(), "title": names.get_last_name(),
                       "company": random.choice(["1-10", "10-50", "50-250", "250-1000", "1000+"])}

            r = make_prequest("POST", url, json=payload)
            response = r.text

            if "OK" not in response:
                print(response)
                continue

            while True:
                sleep(5)
                email_list = session.get_email_list()
                message = email_list[0].excerpt
                matchObj = re.search(r'API Key: (.*)', message, re.M | re.I)
                key = matchObj and matchObj.group(1)
                if (key):
                    break
                print('waiting for mail')

            i += 1
            print(key)
            tmpKeys = readKeys()
            tmpKeys.append(key)
            keys.append(key)

            with open("keys.json", "w") as f:
                json.dump(tmpKeys, f)
        except  Exception as e:
            print(e)
            sleep(random.randint(10, 60))


def readKeys():
    with open("keys.json", "r") as f:
        return json.load(f)


def parse_args():
    arguments = docopt(__doc__)
    schema = Schema({
        '--from': Or(None, Use(lambda i: datetime.strptime(i, '%Y-%m-%d')),
                     error='--from=date date should be in the format of YYYY-MM-DD '),
        '--to': Or(And(None, Use(lambda i: datetime.now())), Use(lambda i: datetime.strptime(i, '%Y-%m-%d')),
                   error='--to=date date should be in the format of YYYY-MM-DD '),
        '--period': Or(None, And(Use(str), lambda s: s in periods),
                       error='--period=string should be a string in ' + ', '.join(periods)),
        '--source': Or(None, And(Use(str), lambda s: s in sources),
                       error='--source=string should be a string in ' + ', '.join(sources)),
        '--filetype': Or(None, And(Use(str), lambda s: s in filetypes),
                         error='--filetype=string should be a string in ' + ', '.join(filetypes)),
        '--proxy_type': Or(None, And(Use(str), lambda s: s in proxy_types),
                           error='--proxy_type=string should be a string in ' + ', '.join(proxy_types)),
        '--limit': Or(None, And(Use(int), lambda n: 1 <= n <= 100000),
                      error='--limit=N should be integer 1 <= N <= 100000'),
        '--levels': Or(None, And(Use(int), lambda n: 1 <= n <= 20),
                       error='--limit=N should be integer 1 <= N <= 20'),
        '--timeout': Or(None, Use(int)),
        '--find_n_proxy': Or(None, Use(int)),
        '--generate_keys': Or(None, Use(int)),
        '--symbol': Or(None, Use(list)),
        '--exchange': Or(None, Use(list)),
        '--base': Or(None, Use(list)),
        '--quote': Or(None, Use(list)),
        '--type': Or(None, Use(list)),
        '--help': Or(None, Use(bool)),
        '--path': Or(None, And(Use(os.path.realpath), os.path.exists), error='--path=<path> PATH should exist')
    }, ignore_extra_keys=False)
    try:
        return schema.validate(arguments)
    except SchemaError as e:
        exit(e)


def getSymbols():
    print('getSymbols', end='\n' * 2)

    if len(args['--symbol']) > 0:
        return args['--symbol']
    else:
        symbol_ids = []
        symbols = try_keys(lambda api: api.metadata_list_symbols())

        with open(os.path.join(args['--path'], 'list_symbols.json'), "w") as f:
            json.dump(symbols, f)

        for symbol in symbols:
            if (len(args['--exchange']) == 0 or symbol['exchange_id'] in args['--exchange']) \
                    and (len(args['--type']) == 0 or symbol['symbol_type'] in args['--type']) \
                    and (len(args['--base']) == 0 or symbol['asset_id_base'] in args['--base']) \
                    and (len(args['--quote']) == 0 or symbol['asset_id_quote'] in args['--quote']):
                symbol_ids.append(symbol['symbol_id'])

        with open(os.path.join(args['--path'], 'symbol_ids.json'), "w") as f:
            json.dump(symbols, f)

        return symbol_ids


def getTrades(symbols):
    print('getTrades', end='\n' * 2)

    list = {}
    for symbol in symbols:
        next_start = args['--from'].isoformat().split('.')[0]
        symbol_list = []
        while dateutil.parser.parse(next_start).date() < args['--to'].date():
            data = try_keys(lambda api: api.trades_historical_data(symbol, {'time_start': next_start,
                                                                            'time_end':
                                                                                args['--to'].isoformat().split('.')[0],
                                                                            'limit': args['--limit']}))
            if len(data) == 0:
                break
            next_start = data[-1]['time_coinapi'].split('.')[0]
            symbol_list.extend(data)

        data_frame = pd.DataFrame.from_dict(symbol_list)
        list.update({symbol: data_frame})
        save_df(data_frame, symbol)

        if args['--period']:
            print('period')

    return list


def getOrder(symbols):
    print('getOrder', end='\n' * 2)

    list = {}
    for symbol in symbols:
        next_start = args['--from'].isoformat().split('.')[0]
        symbol_list = []
        while dateutil.parser.parse(next_start).date() < args['--to'].date():
            data = try_keys(lambda api: api.orderbooks_historical_data(symbol, {'time_start': next_start,
                                                                                'time_end':
                                                                                    args['--to'].isoformat().split('.')[
                                                                                        0],
                                                                                'limit': args['--limit'],
                                                                                'limit_levels': args['--levels']}))
            if len(data) == 0:
                break
            next_start = data[-1]['time_coinapi'].split('.')[0]
            symbol_list.extend(data)

        data_frame = pd.DataFrame.from_dict(symbol_list)
        list.update({symbol: data_frame})
        save_df(data_frame, symbol)

        if args['--period']:
            print('period')

    return list


def getQuotes(symbols):
    print('getQuotes', end='\n' * 2)

    list = {}
    for symbol in symbols:
        next_start = args['--from'].isoformat().split('.')[0]
        symbol_list = []
        while dateutil.parser.parse(next_start).date() < args['--to'].date():
            data = try_keys(lambda api: api.quotes_historical_data(symbol, {'time_start': next_start,
                                                                            'time_end':
                                                                                args['--to'].isoformat().split('.')[0],
                                                                            'limit': args['--limit']}))
            if len(data) == 0:
                break
            next_start = data[-1]['time_coinapi'].split('.')[0]
            symbol_list.extend(data)

        data_frame = pd.DataFrame.from_dict(symbol_list)
        list.update({symbol: data_frame})
        save_df(data_frame, symbol)

        if args['--period']:
            print('period')

    return list


def getOhlcv(symbols):
    print('getOhlcv', end='\n' * 2)

    list = {}
    for symbol in symbols:
        next_start = args['--from'].isoformat().split('.')[0]
        symbol_list = []
        while dateutil.parser.parse(next_start).date() < args['--to'].date():
            data = try_keys(lambda api: api.ohlcv_historical_data(symbol, {'time_start': next_start,
                                                                           'time_end':
                                                                               args['--to'].isoformat().split('.')[0],
                                                                           'limit': args['--limit'],
                                                                           'period_id': args['--period'] or '1MIN'}))
            if len(data) == 0:
                break
            next_start = data[-1]['time_period_end'].split('.')[0]
            symbol_list.extend(data)

        data_frame = pd.DataFrame.from_dict(symbol_list)
        list.update({symbol: data_frame})
        save_df(data_frame, symbol,
                columns=['time_open', 'price_close', 'volume_traded', 'price_open', 'price_high', 'price_low',
                         'trades_count'],
                header=['Date', 'Close', 'Volume', 'Open', 'High', 'Low', 'Market Cap'])

    return list


def try_keys(call):
    print('try_keys')
    index = 0
    while True:
        try:
            if len(keys) == 0:
                generate_keys(3)

            index = random.randint(0, len(keys) - 1)
            api = CoinAPIv1(keys[index])
            results = call(api)
            if type(results) is list:
                if len(results) >= 50000:
                    print("key consumed: " + keys.pop(index))
                return results
            else:
                print(results)
                print("used key: " + keys.pop(index))
        except Exception as e:
            print(e)
            print("used key: " + keys.pop(index))


def make_prequest(method='get',
                  url=None,
                  headers=dict(),
                  data=None,
                  params=None,
                  auth=None,
                  cookies=None,
                  proxies=None,
                  json=None):
    ua = UserAgent()
    headers.update({'User-Agent': ua.random})

    index = 0
    if proxy_type == 'list' or proxy_type == 'fresh':
        while True:
            try:
                if len(proxies_list) == 0:
                    find_proxy(args['--find_n_proxy'])
                    read_proxies()

                index = random.randint(0, len(proxies_list) - 1)
                r = requests.request(method=method, url=url, headers=headers, data=data, params=params, auth=auth,
                                     cookies=cookies, proxies=proxies_list[index], json=json, timeout=timeout)
                if r.status_code >= 400:
                    print("used proxy: " + proxies_list.pop(index)["http"])
                return r
            except Exception as e:
                print(e)
                print("used proxy: " + proxies_list.pop(index)["http"])
    elif proxy_type == 'rotate':
        while len(proxies_list) > 0:
            try:
                index = random.randint(0, len(proxies_list) - 1)
                r = requests.request(method=method, url=proxies_list[index] + urllib.parse.quote_plus(url),
                                     headers=headers,
                                     data=data,
                                     params=params, auth=auth,
                                     cookies=cookies, json=json, timeout=timeout)
                if 400 <= r.status_code < 500:
                    print(r.text)
                    print("used proxy: " + proxies_list.pop(index))
                else:
                    return r
            except Exception as e:
                print(e)
                print("used proxy: " + proxies_list.pop(index))
    else:
        return requests.request(method=method, url=url, headers=headers, data=data, params=params, auth=auth,
                                cookies=cookies, proxies=proxies, json=json, timeout=timeout)


async def save_proxy(proxies):
    list = []
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        print(proxy.host)
        list.append(
            {"http": ("http://%s:%d" % (proxy.host, proxy.port)),
             "https": ("https://%s:%d" % (proxy.host, proxy.port))})
    with open("proxies.json", "w") as f:
        json.dump(list, f)


def read_proxies():
    global proxies_list
    with open("proxies.json", "r") as f:
        proxies_list = json.load(f)
        return proxies_list


def read_rproxies():
    global proxies_list
    with open("rproxy.json", "r") as f:
        proxies_list = json.load(f)
        return proxies_list


def find_proxy(limit=1000):
    print('find_proxy', end='\n' * 2)
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(broker.find(types=['HTTP', 'HTTPS'], limit=limit),
                           save_proxy(proxies))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)


class HTTPClient:
    def __init__(self, endpoint, headers=dict(), params=dict()):
        self.url = PRODUCTION_URL % endpoint

        if headers.get('X-CoinAPI-Key', None):
            params.update({"apiKey": headers['X-CoinAPI-Key']})
            headers.pop('X-CoinAPI-Key')

        self.params = params
        self.headers = headers

    def perform(self):
        resource = self.url
        if self.params:
            query_string = urllib.parse.urlencode(self.params)
            resource = '%s?%s' % (self.url, query_string)

        raw_response = make_prequest(url=resource).text
        response = json.loads(raw_response)
        return response


class MetadataListExchangesRequest:
    def endpoint(self):
        return '/exchanges'


class MetadataListAssetsRequest:
    def endpoint(self):
        return '/assets'


class MetadataListSymbolsRequest:
    def endpoint(self):
        return '/symbols'


class ExchangeRatesGetSpecificRateRequest:
    def __init__(self,
                 asset_id_base,
                 asset_id_quote,
                 query_parameters=dict()):
        self.asset_id_base = asset_id_base
        self.asset_id_quote = asset_id_quote
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/exchangerate/%s/%s' % (
            self.asset_id_base,
            self.asset_id_quote)


class ExchangeRatesGetAllCurrentRates:
    def __init__(self, asset_id_base):
        self.asset_id_base = asset_id_base

    def endpoint(self):
        return '/exchangerate/%s' % self.asset_id_base


class OHLCVListAllPeriodsRequest:
    def endpoint(self):
        return '/ohlcv/periods'


class OHLCVLatestDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/ohlcv/%s/latest' % self.symbol_id


class OHLCVHistoricalDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/ohlcv/%s/history' % self.symbol_id


class TradesLatestDataAllRequest:
    def __init__(self, query_parameters=dict()):
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/trades/latest'


class TradesLatestDataSymbolRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/trades/%s/latest' % self.symbol_id


class TradesHistoricalDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/trades/%s/history' % self.symbol_id


class QuotesCurrentDataAllRequest:
    def endpoint(self):
        return '/quotes/current'


class QuotesCurrentDataSymbolRequest:
    def __init__(self, symbol_id):
        self.symbol_id = symbol_id

    def endpoint(self):
        return '/quotes/%s/current' % self.symbol_id


class QuotesLatestDataAllRequest:
    def __init__(self, query_parameters=dict()):
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/quotes/latest'


class QuotesLatestDataSymbolRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/quotes/%s/latest' % self.symbol_id

    def limit(self, lim):
        params = self.__with_parameter('limit', lim)
        return QuotesLatestDataSymbolRequest(self.symbol_id, params)

    only = limit


class QuotesHistoricalData:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/quotes/%s/history' % self.symbol_id


class OrderbooksCurrentDataAllRequest:
    def endpoint(self):
        return '/orderbooks/current'


class OrderbooksCurrentDataSymbolRequest:
    def __init__(self, symbol_id):
        self.symbol_id = symbol_id

    def endpoint(self):
        return '/orderbooks/%s/current' % self.symbol_id


class OrderbooksLatestDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/orderbooks/%s/latest' % self.symbol_id


class OrderbooksHistoricalDataRequest:
    def __init__(self, symbol_id, query_parameters=dict()):
        self.symbol_id = symbol_id
        self.query_parameters = query_parameters

    def endpoint(self):
        return '/orderbooks/%s/history' % self.symbol_id


class CoinAPIv1:
    DEFAULT_HEADERS = {
        'Accept': 'application/json'
    }

    def __init__(self, api_key, headers=dict(), client_class=HTTPClient):
        self.api_key = api_key
        header_apikey = {'X-CoinAPI-Key': self.api_key}
        self.headers = {**self.DEFAULT_HEADERS, **headers, **header_apikey}
        self.client_class = client_class

    def with_header(self, header, value):
        old_headers = self.headers
        new_header = {header: value}
        return CoinAPIv1(self.api_key, {**old_headers, **new_header})

    def with_headers(self, additional_headers):
        old_headers = self.headers
        return CoinAPIv1(self.api_key, {**old_headers, **additional_headers})

    def metadata_list_exchanges(self):
        request = MetadataListExchangesRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def metadata_list_assets(self):
        request = MetadataListAssetsRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def metadata_list_symbols(self):
        request = MetadataListSymbolsRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def exchange_rates_get_specific_rate(self,
                                         asset_id_base,
                                         asset_id_quote,
                                         query_parameters=dict()):
        request = ExchangeRatesGetSpecificRateRequest(asset_id_base,
                                                      asset_id_quote,
                                                      query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def exchange_rates_get_all_current_rates(self,
                                             asset_id_base):
        request = ExchangeRatesGetAllCurrentRates(asset_id_base)
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def ohlcv_list_all_periods(self):
        request = OHLCVListAllPeriodsRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def ohlcv_latest_data(self,
                          symbol_id,
                          query_parameters=dict()):
        request = OHLCVLatestDataRequest(symbol_id,
                                         query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def ohlcv_historical_data(self,
                              symbol_id,
                              query_parameters):
        request = OHLCVHistoricalDataRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def trades_latest_data_all(self,
                               query_parameters=dict()):
        request = TradesLatestDataAllRequest(query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def trades_latest_data_symbol(self,
                                  symbol_id,
                                  query_parameters=dict()):
        request = TradesLatestDataSymbolRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def trades_historical_data(self,
                               symbol_id,
                               query_parameters=dict()):
        request = TradesHistoricalDataRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def quotes_current_data_all(self):
        request = QuotesCurrentDataAllRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def quotes_current_data_symbol(self,
                                   symbol_id):
        request = QuotesCurrentDataSymbolRequest(symbol_id)
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def quotes_latest_data_all(self,
                               query_parameters=dict()):
        request = QuotesLatestDataAllRequest(query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def quotes_latest_data_symbol(self,
                                  symbol_id,
                                  query_parameters=dict()):
        request = QuotesLatestDataSymbolRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def quotes_historical_data(self,
                               symbol_id,
                               query_parameters=dict()):
        request = QuotesHistoricalData(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def orderbooks_current_data_all(self):
        request = OrderbooksCurrentDataAllRequest()
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def orderbooks_current_data_symbol(self,
                                       symbol_id):
        request = OrderbooksCurrentDataSymbolRequest(symbol_id)
        client = self.client_class(request.endpoint(), self.headers)
        return client.perform()

    def orderbooks_latest_data(self,
                               symbol_id,
                               query_parameters=dict()):
        request = OrderbooksLatestDataRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()

    def orderbooks_historical_data(self,
                                   symbol_id,
                                   query_parameters=dict()):
        request = OrderbooksHistoricalDataRequest(symbol_id, query_parameters)
        client = self.client_class(request.endpoint(),
                                   self.headers,
                                   request.query_parameters)
        return client.perform()


def init_path():
    args['--path'] = os.path.join(args['--path'], args['--source'] + '_' + datetime.now().strftime("%Y%m%d-%H%M%S"))
    os.makedirs(args['--path'], exist_ok=True)
    with open(os.path.join(args['--path'], 'args.json'), "w") as f:
        json.dump(args, f)


def save_df(df, filename, columns=None, header=True):
    file_path = os.path.join(args['--path'], filename + '.' + args['--filetype'])
    if args['--filetype'] == 'csv':
        df.to_csv(file_path, index=False,
                  columns=columns,
                  header=header)
    elif args['--filetype'] == 'json':
        df.to_json(file_path, orient='records')


if __name__ == '__main__':
    args = parse_args()
    print(args, end='\n' * 5)
    keys = readKeys()
    timeout = args['--timeout']
    proxy_type = args['--proxy_type']

    if proxy_type == 'fresh':
        find_proxy(args['--find_n_proxy'])
        read_proxies()
    elif proxy_type == 'list':
        read_proxies()
    elif proxy_type == 'rotate':
        read_rproxies()

    if args['--generate_keys']:
        generate_keys(args['--generate_keys'])

    init_path()
    symbols = getSymbols()
    print(symbols, end='\n' * 2)
    if args['--source'] == 'ohlcv':
        getOhlcv(symbols)
    else:
        if args['--source'] == 'trades':
            getTrades(symbols)
        elif args['--source'] == 'quotes':
            getQuotes(symbols)
        elif args['--source'] == 'order':
            getOrder(symbols)

    print('DONE')
