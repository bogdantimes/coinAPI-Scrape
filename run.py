""" Coinapi key generator and data downloader

Example, try:
python run.py --symbol=BITSTAMP_SPOT_LTC_USD  --source=ohlcv --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --timeout=20
python run.py --exchange=BITSTAMP  --source=ohlcv --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --limit=100000
python run.py --exchange=BITSTAMP  --source=trades --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --limit=100000
python run.py --symbol=BINANCE_SPOT_BTC_USDT,BINANCE_SPOT_ETH_USDT,BINANCE_SPOT_EOS_USDT,BINANCE_SPOT_ETH_BTC,BINANCE_SPOT_ONT_USDT,BINANCE_SPOT_BCC_USDT,BINANCE_SPOT_EOS_BTC,BINANCE_SPOT_ETC_USDT,BINANCE_SPOT_ONT_BTC,BINANCE_SPOT_NANO_BTC,BINANCE_SPOT_TRX_USDT,BINANCE_SPOT_BCC_BTC,BINANCE_SPOT_XRP_BTC,BINANCE_SPOT_ETC_BTC,BINANCE_SPOT_XRP_USDT,BINANCE_SPOT_VET_USDT,BINANCE_SPOT_TRX_BTC,BINANCE_SPOT_ADA_USDT,BINANCE_SPOT_NEO_USDT,BINANCE_SPOT_XLM_BTC,BINANCE_SPOT_CMT_BTC,BINANCE_SPOT_VET_BTC,BINANCE_SPOT_NEO_BTC,BINANCE_SPOT_ADA_BTC,BINANCE_SPOT_LTC_USDT,BINANCE_SPOT_THETA_BTC,BINANCE_SPOT_LTC_BTC,BINANCE_SPOT_IOTA_USDT,BINANCE_SPOT_BNB_BTC,BINANCE_SPOT_BNB_USDT,BINANCE_SPOT_XLM_USDT,BINANCE_SPOT_TUSD_USDT,BINANCE_SPOT_ICX_USDT,BINANCE_SPOT_IOTA_BTC,BINANCE_SPOT_ZRX_BTC,BINANCE_SPOT_ICX_BTC,BINANCE_SPOT_WTC_BTC,BINANCE_SPOT_XMR_BTC,BINANCE_SPOT_ARN_BTC,BINANCE_SPOT_TUSD_BTC,BINANCE_SPOT_LSK_BTC,BINANCE_SPOT_ZIL_BTC,BINANCE_SPOT_QKC_BTC,BINANCE_SPOT_DASH_BTC,BINANCE_SPOT_IOTX_BTC,BINANCE_SPOT_NANO_ETH,BINANCE_SPOT_DOCK_BTC,BINANCE_SPOT_NPXS_BTC,BINANCE_SPOT_NAS_BTC,BINANCE_SPOT_CMT_ETH,BINANCE_SPOT_YOYO_BTC,BINANCE_SPOT_EOS_ETH,BINANCE_SPOT_QTUM_USDT,BINANCE_SPOT_LINK_BTC,BINANCE_SPOT_GAS_BTC,BINANCE_SPOT_ELF_BTC,BINANCE_SPOT_IOST_BTC,BINANCE_SPOT_LOOM_BTC,BINANCE_SPOT_NCASH_BTC,BINANCE_SPOT_VET_ETH,BINANCE_SPOT_NULS_BTC,BINANCE_SPOT_WAN_BTC,BINANCE_SPOT_REP_BTC,BINANCE_SPOT_GTO_BTC,BINANCE_SPOT_KEY_BTC,BINANCE_SPOT_BNB_ETH,BINANCE_SPOT_CVC_BTC,BINANCE_SPOT_ADA_ETH,BINANCE_SPOT_DENT_BTC,BINANCE_SPOT_THETA_ETH,BINANCE_SPOT_XVG_BTC,BINANCE_SPOT_MDA_BTC,BINANCE_SPOT_POA_BTC,BINANCE_SPOT_IOST_ETH,BINANCE_SPOT_TRX_ETH,BINANCE_SPOT_BAT_BTC,BINANCE_SPOT_MFT_BTC,BINANCE_SPOT_ENG_BTC,BINANCE_SPOT_XRP_ETH,BINANCE_SPOT_XEM_BTC,BINANCE_SPOT_BQX_BTC,BINANCE_SPOT_NEO_ETH,BINANCE_SPOT_SNT_BTC,BINANCE_SPOT_NAS_ETH,BINANCE_SPOT_NULS_USDT,BINANCE_SPOT_ONT_ETH,BINANCE_SPOT_PPT_BTC,BINANCE_SPOT_AION_BTC,BINANCE_SPOT_SUB_BTC,BINANCE_SPOT_ADX_BTC,BINANCE_SPOT_QTUM_BTC,BINANCE_SPOT_LOOM_ETH,BINANCE_SPOT_ZRX_ETH,BINANCE_SPOT_ICX_ETH,BINANCE_SPOT_BCD_BTC,BINANCE_SPOT_STORM_BTC,BINANCE_SPOT_OMG_BTC,BINANCE_SPOT_BCC_ETH,BINANCE_SPOT_MTL_BTC,BINANCE_SPOT_ZEC_BTC --source=ohlcv --from=2018-08-23 --to=2018-08-24 --proxy_type=list --period=1HRS --filetype=csv --limit=100000 --timeout=10
python run.py --exchange=BINANCE --quote=USDT,BTC,ETH --base=BTC,ETH,EOS,ONT,BCC,ETC,NANO,TRX,XRP,VET,ADA,NEO,XLM,CMT,LTC,THETA,IOTA,BNB,TUSD,ICX,ZRX,WTC,XMR,ARN,LSK,ZIL,QKC,DASH,IOTX,DOCK,NPXS,NAS,YOYO,QTUM,LINK,GAS,ELF,IOST,LOOM,NCASH,NULS,WAN,REP,GTO,KEY,CVC,DENT,XVG,MDA,POA,BAT,MFT,ENG,XEM,BQX,SNT,PPT,AION,SUB,ADX,BCD,STORM,OMG,MTL,ZEC --source=ohlcv --from=2018-08-23 --to=2018-08-24 --proxy_type=list --period=1HRS --filetype=csv --limit=100000 --timeout=10

to run in the background on linux:
    nohup my_command > my.log 2>&1 &
    echo $! > save_pid.txt
to stop it:
    kill -9 `cat save_pid.txt`
    rm save_pid.txt


top 100 coins on linux:
nohup /root/anaconda3/bin/python run.py --symbol=BINANCE_SPOT_BTC_USDT,BINANCE_SPOT_ETH_USDT,BINANCE_SPOT_EOS_USDT,BINANCE_SPOT_ETH_BTC,BINANCE_SPOT_ONT_USDT,BINANCE_SPOT_BCC_USDT,BINANCE_SPOT_EOS_BTC,BINANCE_SPOT_ETC_USDT,BINANCE_SPOT_ONT_BTC,BINANCE_SPOT_NANO_BTC,BINANCE_SPOT_TRX_USDT,BINANCE_SPOT_BCC_BTC,BINANCE_SPOT_XRP_BTC,BINANCE_SPOT_ETC_BTC,BINANCE_SPOT_XRP_USDT,BINANCE_SPOT_VET_USDT,BINANCE_SPOT_TRX_BTC,BINANCE_SPOT_ADA_USDT,BINANCE_SPOT_NEO_USDT,BINANCE_SPOT_XLM_BTC,BINANCE_SPOT_CMT_BTC,BINANCE_SPOT_VET_BTC,BINANCE_SPOT_NEO_BTC,BINANCE_SPOT_ADA_BTC,BINANCE_SPOT_LTC_USDT,BINANCE_SPOT_THETA_BTC,BINANCE_SPOT_LTC_BTC,BINANCE_SPOT_IOTA_USDT,BINANCE_SPOT_BNB_BTC,BINANCE_SPOT_BNB_USDT,BINANCE_SPOT_XLM_USDT,BINANCE_SPOT_TUSD_USDT,BINANCE_SPOT_ICX_USDT,BINANCE_SPOT_IOTA_BTC,BINANCE_SPOT_ZRX_BTC,BINANCE_SPOT_ICX_BTC,BINANCE_SPOT_WTC_BTC,BINANCE_SPOT_XMR_BTC,BINANCE_SPOT_ARN_BTC,BINANCE_SPOT_TUSD_BTC,BINANCE_SPOT_LSK_BTC,BINANCE_SPOT_ZIL_BTC,BINANCE_SPOT_QKC_BTC,BINANCE_SPOT_DASH_BTC,BINANCE_SPOT_IOTX_BTC,BINANCE_SPOT_NANO_ETH,BINANCE_SPOT_DOCK_BTC,BINANCE_SPOT_NPXS_BTC,BINANCE_SPOT_NAS_BTC,BINANCE_SPOT_CMT_ETH,BINANCE_SPOT_YOYO_BTC,BINANCE_SPOT_EOS_ETH,BINANCE_SPOT_QTUM_USDT,BINANCE_SPOT_LINK_BTC,BINANCE_SPOT_GAS_BTC,BINANCE_SPOT_ELF_BTC,BINANCE_SPOT_IOST_BTC,BINANCE_SPOT_LOOM_BTC,BINANCE_SPOT_NCASH_BTC,BINANCE_SPOT_VET_ETH,BINANCE_SPOT_NULS_BTC,BINANCE_SPOT_WAN_BTC,BINANCE_SPOT_REP_BTC,BINANCE_SPOT_GTO_BTC,BINANCE_SPOT_KEY_BTC,BINANCE_SPOT_BNB_ETH,BINANCE_SPOT_CVC_BTC,BINANCE_SPOT_ADA_ETH,BINANCE_SPOT_DENT_BTC,BINANCE_SPOT_THETA_ETH,BINANCE_SPOT_XVG_BTC,BINANCE_SPOT_MDA_BTC,BINANCE_SPOT_POA_BTC,BINANCE_SPOT_IOST_ETH,BINANCE_SPOT_TRX_ETH,BINANCE_SPOT_BAT_BTC,BINANCE_SPOT_MFT_BTC,BINANCE_SPOT_ENG_BTC,BINANCE_SPOT_XRP_ETH,BINANCE_SPOT_XEM_BTC,BINANCE_SPOT_BQX_BTC,BINANCE_SPOT_NEO_ETH,BINANCE_SPOT_SNT_BTC,BINANCE_SPOT_NAS_ETH,BINANCE_SPOT_NULS_USDT,BINANCE_SPOT_ONT_ETH,BINANCE_SPOT_PPT_BTC,BINANCE_SPOT_AION_BTC,BINANCE_SPOT_SUB_BTC,BINANCE_SPOT_ADX_BTC,BINANCE_SPOT_QTUM_BTC,BINANCE_SPOT_LOOM_ETH,BINANCE_SPOT_ZRX_ETH,BINANCE_SPOT_ICX_ETH,BINANCE_SPOT_BCD_BTC,BINANCE_SPOT_STORM_BTC,BINANCE_SPOT_OMG_BTC,BINANCE_SPOT_BCC_ETH,BINANCE_SPOT_MTL_BTC,BINANCE_SPOT_ZEC_BTC --source=ohlcv --from=2016-08-20 --to=2018-08-20 --period=1MIN --proxy_type=fresh --find_n_proxy=500 --limit=100000 > my.log 2>&1 &

echo $! > save_pid.txt


cron task:
crontab -e

MAILTO="ahmedengu@gmail.com"
0 0 * * * /root/anaconda3/bin/python /root/task/run.py --symbol=BINANCE_SPOT_BTC_USDT,BINANCE_SPOT_ETH_USDT,BINANCE_SPOT_EOS_USDT,BINANCE_SPOT_ETH_BTC,BINANCE_SPOT_ONT_USDT,BINANCE_SPOT_BCC_USDT,BINANCE_SPOT_EOS_BTC,BINANCE_SPOT_ETC_USDT,BINANCE_SPOT_ONT_BTC,BINANCE_SPOT_NANO_BTC,BINANCE_SPOT_TRX_USDT,BINANCE_SPOT_BCC_BTC,BINANCE_SPOT_XRP_BTC,BINANCE_SPOT_ETC_BTC,BINANCE_SPOT_XRP_USDT,BINANCE_SPOT_VET_USDT,BINANCE_SPOT_TRX_BTC,BINANCE_SPOT_ADA_USDT,BINANCE_SPOT_NEO_USDT,BINANCE_SPOT_XLM_BTC,BINANCE_SPOT_CMT_BTC,BINANCE_SPOT_VET_BTC,BINANCE_SPOT_NEO_BTC,BINANCE_SPOT_ADA_BTC,BINANCE_SPOT_LTC_USDT,BINANCE_SPOT_THETA_BTC,BINANCE_SPOT_LTC_BTC,BINANCE_SPOT_IOTA_USDT,BINANCE_SPOT_BNB_BTC,BINANCE_SPOT_BNB_USDT,BINANCE_SPOT_XLM_USDT,BINANCE_SPOT_TUSD_USDT,BINANCE_SPOT_ICX_USDT,BINANCE_SPOT_IOTA_BTC,BINANCE_SPOT_ZRX_BTC,BINANCE_SPOT_ICX_BTC,BINANCE_SPOT_WTC_BTC,BINANCE_SPOT_XMR_BTC,BINANCE_SPOT_ARN_BTC,BINANCE_SPOT_TUSD_BTC,BINANCE_SPOT_LSK_BTC,BINANCE_SPOT_ZIL_BTC,BINANCE_SPOT_QKC_BTC,BINANCE_SPOT_DASH_BTC,BINANCE_SPOT_IOTX_BTC,BINANCE_SPOT_NANO_ETH,BINANCE_SPOT_DOCK_BTC,BINANCE_SPOT_NPXS_BTC,BINANCE_SPOT_NAS_BTC,BINANCE_SPOT_CMT_ETH,BINANCE_SPOT_YOYO_BTC,BINANCE_SPOT_EOS_ETH,BINANCE_SPOT_QTUM_USDT,BINANCE_SPOT_LINK_BTC,BINANCE_SPOT_GAS_BTC,BINANCE_SPOT_ELF_BTC,BINANCE_SPOT_IOST_BTC,BINANCE_SPOT_LOOM_BTC,BINANCE_SPOT_NCASH_BTC,BINANCE_SPOT_VET_ETH,BINANCE_SPOT_NULS_BTC,BINANCE_SPOT_WAN_BTC,BINANCE_SPOT_REP_BTC,BINANCE_SPOT_GTO_BTC,BINANCE_SPOT_KEY_BTC,BINANCE_SPOT_BNB_ETH,BINANCE_SPOT_CVC_BTC,BINANCE_SPOT_ADA_ETH,BINANCE_SPOT_DENT_BTC,BINANCE_SPOT_THETA_ETH,BINANCE_SPOT_XVG_BTC,BINANCE_SPOT_MDA_BTC,BINANCE_SPOT_POA_BTC,BINANCE_SPOT_IOST_ETH,BINANCE_SPOT_TRX_ETH,BINANCE_SPOT_BAT_BTC,BINANCE_SPOT_MFT_BTC,BINANCE_SPOT_ENG_BTC,BINANCE_SPOT_XRP_ETH,BINANCE_SPOT_XEM_BTC,BINANCE_SPOT_BQX_BTC,BINANCE_SPOT_NEO_ETH,BINANCE_SPOT_SNT_BTC,BINANCE_SPOT_NAS_ETH,BINANCE_SPOT_NULS_USDT,BINANCE_SPOT_ONT_ETH,BINANCE_SPOT_PPT_BTC,BINANCE_SPOT_AION_BTC,BINANCE_SPOT_SUB_BTC,BINANCE_SPOT_ADX_BTC,BINANCE_SPOT_QTUM_BTC,BINANCE_SPOT_LOOM_ETH,BINANCE_SPOT_ZRX_ETH,BINANCE_SPOT_ICX_ETH,BINANCE_SPOT_BCD_BTC,BINANCE_SPOT_STORM_BTC,BINANCE_SPOT_OMG_BTC,BINANCE_SPOT_BCC_ETH,BINANCE_SPOT_MTL_BTC,BINANCE_SPOT_ZEC_BTC --source=ohlcv --from=$(date --date=' 1 days ago' '+%Y-%m-%d') --to=$(date '+%Y-%m-%d') --period=1MIN --proxy_type=fresh --find_n_proxy=500 --limit=100000 --timeout=5 >/dev/null 2>&1


Usage:
  run.py (--symbol=<string> | [--exchange=<string>] [--base=<string>] [--quote=<string>] [--type=<string>]) [--source=<string>] (--from=<date>|--from=<date> --track_from) [--to=<date>] [--period=<string>]  [--limit=<int>]  [--levels=<int>]  [--path=<path>] [--filetype=<string>] [--proxy_type=<string>] [--timeout=<int>] [--generate_keys=<int>] [--find_n_proxy=<int>] [--proxy_dnsbl] [--proxy_strict] [--log_to=<filename>] [--dropbox_key=<string>] [--dropbox [keep | --delete_period=<string>]] [--dropbox_dir=<path>]
  run.py --continue [--path=<path>]
  run.py --convert=<path> --period=<string> [--path=<path>] [--dropbox_key=<string>] [--dropbox [keep | --delete_period=<string>]] [--dropbox_dir=<path>] [--source=<string>] [--filetype=<string>]
  run.py (-h | --help)

Arguments:
  --symbol=<string>     Symbol id for requested timeseries, comma separated, check https://docs.coinapi.io/#list-all-symbols
  --exchange=<string>     identifier of the exchange where symbol is traded, comma separated, check https://docs.coinapi.io/#list-all-symbols
  --base=<string>     FX Spot base asset identifier, for derivatives it’s contact underlying (e.g. BTC for BTC/USD), comma separated, check https://docs.coinapi.io/#list-all-symbols
  --quote=<string>     FX Spot quote asset identifier, for derivatives it’s contract underlying (e.g. USD for BTC/USD), comma separated, check https://docs.coinapi.io/#list-all-symbols
  --type=<string>     Type of symbol (possible values are: SPOT, FUTURES or OPTION), comma separated
  --from=<date>     starting date.
  --source=<string>     the data to be downloaded (ohlcv, trades, quotes, order) [default: ohlcv].
  --convert=<path>     a path to a directory that contains csv files to be converted.
  --continue  continue the last run [default: False].

Options:
  -h --help     Show this screen.
  --path=<path>  a directory to save data to [default: out].
  --filetype=<string>  the saved data file type (json, csv) [default: csv].
  --to=<date>  ending date.
  --period=<string>  supported time periods available for requesting OHLCV timeseries data OR to convert data to,comma separated, check https://docs.coinapi.io/#list-all-periods.
  --limit=<int>  Amount of items to return , minimum is 1, maximum is 100000 [default: 10000].
  --levels=<int>  Maximum amount of levels from each side of the book to include in response, max 20 [default: 20].
  --timeout=<int>  request timeout [default: 120].
  --generate_keys=<int>  generate N new coinapi keys.
  --find_n_proxy=<int>  number of proxies to find at a time [default: 100].
  --proxy_type=<string>  type of proxy (None, fresh, list, rotate) [default: None].
  --proxy_dnsbl  Check proxy in spam databases (DNSBL) [default: False].
  --proxy_strict  strict proxy search [default: False].
  --dropbox  to enable moving files to dropbox [default: false].
  --dropbox_key=<string>  dropbox access key [default: IAO3blUBPSAAAAAAAAAAGdXfH_dwns1tIWEpBT4ExVi4agvtKLlfZjgiDiFT1Y-6].
  --dropbox_dir=<path>  dropbox directory to upload to, the script gonna create a multiple subfolders containing the exchange name,period,coin then the csv ex. (/OHLCV_data/BITSTAMP/2HRS_OHLCV/BITSTAMP_SPOT_LTC_USD/2HRS_2018-08-30.csv) [default: /OHLCV_data].
  keep  to keep files after copying them to dropbox [default: false].
  --log_to=<filename>  specify a file name to save all the output to.
  --track_from  to keep track of the last from to ensure that the script starts from the last time it ran gonna use --from if the last from not found [default: false].
  --delete_period=<string>  comma separated periods to get deleted from the server after uploading to dropbox.


"""

import asyncio
import json
import logging
import os
import random
import re
import shutil
import urllib
import urllib.parse
import urllib.request
import warnings
from datetime import datetime, timedelta
from json import JSONDecoder, JSONEncoder
from time import sleep

import dateutil.parser
import requests
import urllib3

try:
    from docopt import docopt
    from schema import Schema, And, Or, Use, SchemaError, Regex
    import names
    from guerrillamail import GuerrillaMailSession, GuerrillaMailException
    from fake_useragent import UserAgent
    from proxybroker import Broker
    from proxybroker.resolver import Resolver
    import pandas as pd
    import dropbox
except ImportError:
    pass
    exit('One or more of the required libraries is missing\n'
         'Use the following commands to install them:\n'
         'pip install schema\n'
         'pip install docopt\n'
         'pip install names\n'
         'pip install python-guerrillamail\n'
         'pip install fake-useragent\n'
         'pip install proxybroker\n'
         'pip install pandas\n'
         'pip install dropbox\n'
         '\n\nOr run:\n'
         'pip install -r requirements.txt\n'
         '\n')

periods = ["1SEC", "2SEC", "3SEC", "4SEC", "5SEC", "6SEC", "10SEC", "15SEC", "20SEC", "30SEC", "1MIN", "2MIN", "3MIN",
           "4MIN", "5MIN", "6MIN", "10MIN", "15MIN", "20MIN", "30MIN", "1HRS", "2HRS", "3HRS", "4HRS", "6HRS", "8HRS",
           "12HRS", "1DAY", "2DAY", "3DAY", "5DAY", "7DAY", "10DAY", "1MTH", "2MTH", "3MTH", "4MTH", "6MTH", "1YRS",
           "2YRS", "3YRS", "4YRS", "5YRS"]

pd_offset = ["1S", "2S", "3S", "4S", "5S", "6S", "10S", "15S", "20S", "30S", "60S", "120S", "180S", "240S", "300S",
             "360S", "600S", "900S", "1200S", "1800S", "3600S", "7200S", "10800S", "14400S", "21600S", "28800S",
             "43200S", "86400S", "172800S", "259200S", "432000S", "604800S", "864000S", "1M", "2M", "3M", "4M", "6M",
             "12M", "24M", "36M", "48M", "60M"]

proxies_list = []
proxy_type = 'None'
PRODUCTION_URL = 'https://rest.coinapi.io/v1%s'
keys = []
proxy_types = ['None', 'fresh', 'list', 'rotate']
sources = ["ohlcv", "trades", "quotes", "order"]
filetypes = ["json", "csv"]
timeout = 120.0
args = {}
urllib3.disable_warnings()
warnings.simplefilter(action='ignore', category=FutureWarning)


def generate_keys(num=1):
    logger.info('generate_keys')
    i = 0
    while i < num:
        try:
            sleep(random.randint(3, 8))
            session = GuerrillaMailSession()
            email_address = session.get_session_state()['email_address'].split('@')[0] + '@' + random.choice(
                ['sharklasers.com', 'guerrillamail.info', 'grr.la', 'guerrillamail.biz', 'guerrillamail.com',
                 'guerrillamail.de', 'guerrillamail.net', 'guerrillamail.org', 'guerrillamailblock.com',
                 'spam4.me'])

            logger.info("#" + str(i) + ", " + email_address)

            url = "https://www.coinapi.io/www/freeplan"

            payload = {"email": email_address, "recaptha3token": "03AFY_a8XzG9s_KT_cB-3WH2_20r1_6K62I9HstQqWQX9giVI1hdf26FnhG6CRfeq5zIXAHVaGHwzx6XscjJIND2xAlSh3b2lKnDhovC3c_u3nzlaePQY3CjxmJeAdQfDnWgsKP9j_Z218BoOijHj9jhMRw0QhgEzJU111T6Eo7zkcWkbPlTRXprfK7bLwn9KLyQVnn_NR6u6mB6nP_qmQrUdsQApdoi-hpE7zmBsBzqtXG9X1Ca432rxgoymRsIs8z27h7RhMDFq8IEzKQaRmDhnC17ikfAoVwVayl7Sdjcr01TMOSFq1RrgyuHEG6pFEdRwhRXLKEetTuee4Thyfb2DsAVw4McjVmEFq8TogOsmXfYIn4wbF7DaOxDn6BvUZUF04xr0kHvK94ljby3oD-luqK0NwTBjDuJcbvT3KZSk63HNISnqGB_VdJuJVcczD0WusBcCv8yX4xq4vE0aAcx13GXm3x5r6pO8_CxSmTCn2jwi33WMWJWpatlxgQXGuE1I8XyAdBfw1sW76CyaPj5QmpUYEgtw298_reYXASfAqifa-a3zZ0U6ZQiuA74Hm7V8PIfN8K5N7"}

            r = make_prequest("POST", url, json=payload)
            response = r.text

            if "OK" not in response:
                logger.info(response)
                continue

            wait_start = datetime.now()
            while True:
                try:
                    if (datetime.now() - wait_start).total_seconds() > 300:
                        raise GuerrillaMailException('Waiting for so long...')

                    logger.info('waiting for mail')
                    sleep(random.randint(5, 10))
                    email_list = session.get_email_list()
                    message = email_list[0].excerpt
                    matchObj = re.search(r'API Key: (.*)', message, re.M | re.I)
                    key = matchObj and matchObj.group(1)
                    if (key):
                        break
                except GuerrillaMailException as e:
                    raise Exception(e)
                except Exception as e:
                    logger.error(e)

            i += 1
            logger.info(key)
            tmpKeys = readKeys()
            tmpKeys.append(key)
            keys.append(key)

            with open("keys.json", "w") as f:
                json.dump(tmpKeys, f)
        except  Exception as e:
            logger.error(e)
            logger.info('generate_keys_sleeping...')
            sleep(random.randint(10, 60))


def readKeys():
    try:
        with open("keys.json", "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(e)
        return []


def parse_args():
    arguments = docopt(__doc__)
    schema = Schema({
        '--from': Or(None, Use(lambda i: datetime.strptime(i, '%Y-%m-%d')),
                     error='--from=date date should be in the format of YYYY-MM-DD '),
        '--to': Or(And(None, Use(lambda i: datetime.now())), Use(lambda i: datetime.strptime(i, '%Y-%m-%d')),
                   error='--to=date date should be in the format of YYYY-MM-DD '),
        '--period': Or(None, And(Use(str), lambda s: set(str(s).split(',')).issubset(periods)),
                       error='--period=string should be a comma separated string in ' + ','.join(periods)),
        '--delete_period': Or(None, And(Use(str), lambda s: set(str(s).split(',')).issubset(periods)),
                              error='--delete_period=string should be a comma separated string in ' + ','.join(
                                  periods)),
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
        '--timeout': Or(None, Use(float)),
        '--find_n_proxy': Or(None, Use(int)),
        '--generate_keys': Or(None, Use(int)),
        '--symbol': Or(None, And(Use(str), lambda s: s.isupper()),
                       error='--symbol=string should upper case '),
        '--exchange': Or(None, And(Use(str), lambda s: s.isupper()),
                         error='--exchange=string should upper case '),
        '--base': Or(None, And(Use(str), lambda s: s.isupper()),
                     error='--base=string should upper case '),
        '--quote': Or(None, And(Use(str), lambda s: s.isupper()),
                      error='--quote=string should upper case '),
        '--type': Or(None, And(Use(str), lambda s: s.isupper()),
                     error='--type=string should upper case '),
        '--dropbox_key': Or(None, Use(str)),
        '--dropbox_dir': Or(None, And(Use(str), Regex(r'(/(.|[\r\n])*)|(ns:[0-9]+(/.*)?)|(id:.*)')),
                            error='--dropbox_dir=<path> path should start with "/"'),
        '--dropbox': Or(None, Use(bool)),
        'keep': Or(None, Use(bool)),
        '--proxy_dnsbl': Or(None, Use(bool)),
        '--proxy_strict': Or(None, Use(bool)),
        '--continue': Or(None, Use(bool)),
        '--track_from': Or(None, Use(bool)),
        '--help': Or(None, Use(bool)),
        '--log_to': Or(None, Use(os.path.realpath)),
        '--convert': Or(None, And(Use(os.path.realpath), os.path.exists),
                        error='--convert=<path> PATH does not exist'),
        '--path': Or(None, And(Use(os.path.realpath),
                               lambda x: os.makedirs(x, exist_ok=True) or os.path.exists(x)),
                     error='--path=<path> PATH is incorrect')
    }, ignore_extra_keys=False)
    try:
        validate = schema.validate(arguments)
        validate['--symbol'] = validate['--symbol'] and validate['--symbol'].split(',') or []
        validate['--exchange'] = validate['--exchange'] and validate['--exchange'].split(',') or []
        validate['--base'] = validate['--base'] and validate['--base'].split(',') or []
        validate['--quote'] = validate['--quote'] and validate['--quote'].split(',') or []
        validate['--type'] = validate['--type'] and validate['--type'].split(',') or []
        validate['--delete_period'] = validate['--delete_period'] and validate['--delete_period'].split(',') or []
        validate['--period'] = validate['--period'] and validate['--period'].split(',') or []
        validate['--period'] = sorted(validate['--period'], key=lambda x: periods.index(x))
        validate['--path'] = [validate['--path']]

        return validate
    except SchemaError as e:
        logger.error(e)
        exit()


def getSymbols(index=1):
    logger.info('getSymbols')
    symbol_ids = []
    symbols = try_keys(lambda api: api.metadata_list_symbols())

    with open(os.path.join(args['--path'][index], 'list_symbols.json'), "w") as f:
        json.dump(symbols, f)

    for symbol in symbols:
        if (len(args['--symbol']) == 0 or symbol['symbol_id'] in args['--symbol']) \
                and (len(args['--exchange']) == 0 or symbol['exchange_id'] in args['--exchange']) \
                and (len(args['--type']) == 0 or symbol['symbol_type'] in args['--type']) \
                and (len(args['--base']) == 0 or symbol['asset_id_base'] in args['--base']) \
                and (len(args['--quote']) == 0 or symbol['asset_id_quote'] in args['--quote']):
            symbol_ids.append(symbol['symbol_id'])

    with open(os.path.join(args['--path'][index], 'symbol_ids.json'), "w") as f:
        json.dump(symbol_ids, f)

    return symbol_ids


def getTrades(symbol):
    logger.info('getTrades')

    logger.info(symbol)
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

    save_df(data_frame, symbol)

    return data_frame


def getOrder(symbol):
    logger.info('getOrder')

    logger.info(symbol)
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
    save_df(data_frame, symbol)

    return data_frame


def getQuotes(symbol):
    logger.info('getQuotes')

    logger.info(symbol)
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
    save_df(data_frame, symbol)

    return data_frame


def getOhlcv(symbol):
    logger.info('getOhlcv')

    logger.info(symbol)
    next_start = args['--from'].isoformat().split('.')[0]
    symbol_list = []
    while dateutil.parser.parse(next_start).date() < args['--to'].date():
        data = try_keys(lambda api: api.ohlcv_historical_data(symbol, {'time_start': next_start,
                                                                       'time_end':
                                                                           args['--to'].isoformat().split('.')[0],
                                                                       'limit': args['--limit'],
                                                                       'period_id': args['--period'][0] or '1MIN'}))
        if len(data) == 0:
            break
        next_start = data[-1]['time_period_end'].split('.')[0]
        symbol_list.extend(data)

    data_frame = pd.DataFrame.from_dict(symbol_list)

    if len(data_frame.index) > 0:
        save_df(data_frame, symbol)
        # save_df(data_frame, symbol,
        #         columns=['time_open', 'price_close', 'volume_traded', 'price_open', 'price_high', 'price_low',
        #                  'trades_count'],
        #         header=['Date', 'Close', 'Volume', 'Open', 'High', 'Low', 'Market Cap'])
    else:
        logger.info('no data to save')

    return data_frame


def try_keys(call):
    logger.info('try_keys')
    index = 0
    while True:
        try:
            if len(keys) == 0:
                generate_keys(args['--generate_keys'] or 5)

            index = random.randint(0, len(keys) - 1)
            api = CoinAPIv1(keys[index])
            response = call(api)
            results = json.loads(response.text)

            if type(results) is list:
                if response.headers.get('X-RateLimit-Remaining', None) == '0' or len(results) == 100000:
                    logger.info("consumed key: " + keys.pop(index))
                    logger.info("remaining keys: " + str(len(keys)))

                logger.info("received records: " + str(len(results)))
                return results
            else:
                logger.info(results)
                if 'many requests'.lower() in response.text.lower() or 'Invalid API key'.lower() in response.text.lower() \
                        or response.headers.get('X-RateLimit-Remaining', None) == '0':
                    logger.info("used key: " + keys.pop(index))
                    logger.info("remaining keys: " + str(len(keys)))
        except Exception as e:
            logger.error(e)
            logger.info("used key: " + keys.pop(index))
            logger.info("remaining keys: " + str(len(keys)))


def make_prequest(method='get',
                  url=None,
                  headers=dict(),
                  data=None,
                  params=None,
                  auth=None,
                  cookies=None,
                  proxies=None,
                  json=None):
    try:
        ua = UserAgent()
        headers.update({'User-Agent': ua.random})
    except Exception as e:
        logger.error(e)

    if proxy_type == 'None':
        while True:
            try:
                r = requests.request(method=method, url=url, headers=headers, data=data, params=params, auth=auth,
                                     cookies=cookies, proxies=proxies, json=json, timeout=timeout, verify=False)
                if r.status_code < 400:
                    return r
                elif 'many requests'.lower() in r.text.lower() or 'Invalid API key'.lower() in r.text.lower() \
                        or r.headers.get('X-RateLimit-Remaining', None) == '0':
                    return r
                else:
                    logger.info(str(r.status_code) + ' ' + r.text)
                    logger.info('make_prequest_sleeping...')
                    sleep(random.randint(3, 15))
            except Exception as e:
                logger.error(e)
                logger.info('make_prequest_sleeping...')
                sleep(random.randint(3, 15))

    index = 0

    while True:
        try:
            if len(proxies_list) == 0 or (type(proxies_list[0]) != str and len(proxies_list) <= 5):
                find_proxy(args['--find_n_proxy'])
                read_proxies()

            index = random.randint(0, len(proxies_list) - 1)
            if type(proxies_list[index]) == str:
                r = requests.request(method=method, url=proxies_list[index] + urllib.parse.quote_plus(url),
                                     headers=headers,
                                     data=data,
                                     params=params, auth=auth,
                                     cookies=cookies, json=json,
                                     timeout=timeout, verify=False)
                if r.status_code == 403 or r.status_code == 429:
                    logger.info(str(r.status_code) + ' ' + r.text)
                    logger.info("used proxy: " + proxies_list.pop(index))
                    logger.info("remaining proxies: " + str(len(proxies_list)))
                else:
                    return r

            else:
                r = requests.request(method=method, url=url, headers=headers, data=data, params=params, auth=auth,
                                     cookies=cookies, proxies=proxies_list[index], json=json,
                                     timeout=timeout, verify=False)
                if r.status_code >= 400:
                    logger.info(str(r.status_code) + ' ' + r.text)
                    logger.info("used proxy: " + proxies_list.pop(index)["http"])
                    logger.info("remaining proxies: " + str(len(proxies_list)))

                    if 'many requests'.lower() in r.text.lower() or 'Invalid API key'.lower() in r.text.lower() \
                            or r.headers.get('X-RateLimit-Remaining', None) == '0':
                        return r
                else:
                    return r
        except Exception as e:
            logger.error(e)
            logger.info("used proxy: " + str(proxies_list.pop(index)))
            logger.info("remaining proxies: " + str(len(proxies_list)))


async def save_proxy(proxies):
    list = []
    while True:
        try:
            proxy = await proxies.get()
            if proxy is None:
                break
            list.append(
                {"http": ("http://%s:%d" % (proxy.host, proxy.port)),
                 "https": ("https://%s:%d" % (proxy.host, proxy.port))})
            logger.info("#" + str(len(list)) + ", " + proxy.host)
        except  Exception as e:
            logger.error(e)
            logger.info('save_proxy_sleeping...')
            sleep(random.randint(3, 15))

    with open("proxies.json", "w") as f:
        json.dump(list, f)


def read_proxies():
    global proxies_list
    try:
        with open("proxies.json", "r") as f:
            proxies_list = json.load(f)
            return proxies_list
    except Exception as e:
        logger.error(e)
        return []


def read_rproxies():
    global proxies_list
    try:
        with open("rproxy.json", "r") as f:
            proxies_list = json.load(f)
            return proxies_list
    except Exception as e:
        logger.error(e)
        return []


def find_proxy(limit=1000):
    while True:
        try:
            logger.info('find_proxy')
            Resolver._ip_hosts = [
                'https://wtfismyip.com/text',
                'https://api.ipify.org/',
                'https://ipinfo.io/ip',
                'https://ipv4.icanhazip.com/',
                'https://myexternalip.com/raw',
                'https://ipinfo.io/ip',
                'https://ifconfig.io/ip'
            ]
            proxies = asyncio.Queue()
            broker = Broker(proxies)

            dnsbl = ['bl.spamcop.net', 'cbl.abuseat.org', 'dnsbl.sorbs.net',
                     'zen.spamhaus.org', 'bl.mcafee.com', 'spam.spamrats.com'] if args['--proxy_dnsbl'] else None

            tasks = asyncio.gather(
                broker.find(types=['HTTP', 'HTTPS'], limit=limit, strict=args['--proxy_strict'], dnsbl=dnsbl),
                save_proxy(proxies))
            loop = asyncio.get_event_loop()
            loop.run_until_complete(tasks)
            break
        except  Exception as e:
            logger.error(e)
            logger.info('find_proxy_sleeping...')
            sleep(random.randint(3, 15))


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

        return make_prequest(url=resource)


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


class DateTimeDecoder(json.JSONDecoder):

    def __init__(self, *args, **kargs):
        JSONDecoder.__init__(self, object_hook=self.dict_to_object,
                             *args, **kargs)

    def dict_to_object(self, d):
        if '__type__' not in d:
            return d

        type = d.pop('__type__')
        try:
            dateobj = datetime(**d)
            return dateobj
        except:
            d['__type__'] = type
            return d


class DateTimeEncoder(JSONEncoder):
    """ Instead of letting the default encoder convert datetime to string,
        convert datetime objects into a dict, which can be decoded by the
        DateTimeDecoder
    """

    def default(self, obj):
        if isinstance(obj, datetime):
            return {
                '__type__': 'datetime',
                'year': obj.year,
                'month': obj.month,
                'day': obj.day,
                'hour': obj.hour,
                'minute': obj.minute,
                'second': obj.second,
                'microsecond': obj.microsecond,
            }
        else:
            return JSONEncoder.default(self, obj)


def init_path(index=0):
    args['--path'].append(os.path.join(args['--path'][0],
                                       ('convert-' + args['--source'] if args['--convert'] else args[
                                           '--source']) + '_' + (
                                           args['--period'][index] + '_' if args['--period'][
                                               index] else '') + datetime.now().strftime(
                                           "%Y%m%d-%H%M%S")))
    os.makedirs(args['--path'][-1], exist_ok=True)
    if index == 0:
        with open(os.path.join(args['--path'][-1], 'args.json'), "w") as f:
            json.dump(args, f, cls=DateTimeEncoder)


def save_df(df, filename, columns=None, header=True, index=1):
    file_path = os.path.join(args['--path'][index], filename + '_' + (
        args['--period'][index - 1] + '_' if args['--period'][index - 1] else '') + str(args['--from'].date()) + '&' + (
                                     'time_period_end' in df and df['time_period_end'][-1].split('T')[
                                 0] or 'time_coinapi' in df and df['time_coinapi'][-1].split('T')[0] or str(
                                 args['--to'].date())) + '.' + args[
                                 '--filetype'])

    if args['--filetype'] == 'csv':
        df.to_csv(file_path, index=False,
                  columns=columns,
                  header=header)
    elif args['--filetype'] == 'json':
        df.to_json(file_path, orient='records')


def loop_symbols(symbols, call, index=1):
    while len(symbols) > 0:
        call(symbols[0])

        with open(os.path.join(args['--path'][index], "remaining_symbols.json"), "w") as f:
            symbols.pop(0)
            json.dump(symbols, f)
            logger.info('remaining symbols: ' + str(len(symbols)))


def convert_period(df):
    logger.info('convert_period')
    if len(df.index) > 0:
        pass
    else:
        logger.info('no data to save')
    return df


def handle_dropbox():
    index = 1
    while index < len(args['--path']):
        try:
            logger.info('uploading a path to dropbox: ' + args['--path'][index])
            dbx = dropbox.Dropbox(args['--dropbox_key'])
            for root, dirs, files in os.walk(args['--path'][index]):
                files = [file for file in files if
                         file not in ['args.json', 'list_symbols.json', 'remaining_symbols.json', 'symbol_ids.json'] and
                         file.split('.')[1] == args['--filetype']]

                if len(files) == 0:
                    logger.info('Nothing to upload')

                for filename in files:
                    local_path = os.path.join(root, filename)

                    relative_path = os.path.relpath(local_path, args['--path'][index])
                    dropbox_path = os.path.normpath(
                        os.path.join(args['--dropbox_dir'], relative_path.split('_')[0],
                                     relative_path.split('_')[4] + '_' + args['--source'].upper(),
                                     '_'.join(relative_path.split('_')[0:4]),
                                     '_'.join(relative_path.split('_')[4:]))).replace('\\', '/')

                    with open(local_path, 'rb') as f:
                        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
                        logger.info('uploaded to: ' + dropbox_path)

            if (not args['keep'] and len(args['--delete_period']) == 0) \
                    or args['--period'][index - 1] in args['--delete_period']:
                logger.info('deleting folder ' + args['--path'][index])
                shutil.rmtree(args['--path'][index])

            index += 1
        except Exception as e:
            logger.error(e)
            logger.info('Failed to upload to dropbox ... sleeping ...')
            sleep(random.randint(10, 60))


def download_source():
    if args['--source'] == 'ohlcv':
        loop_symbols(symbols, lambda symbol: getOhlcv(symbol))
    elif args['--source'] == 'trades':
        loop_symbols(symbols, lambda symbol: convert_period(getTrades(symbol)))
    elif args['--source'] == 'quotes':
        loop_symbols(symbols, lambda symbol: convert_period(getQuotes(symbol)))
    elif args['--source'] == 'order':
        loop_symbols(symbols, lambda symbol: convert_period(getOrder(symbol)))


def handle_proxies():
    global proxy_type
    proxy_type = args['--proxy_type']
    if proxy_type == 'fresh':
        find_proxy(args['--find_n_proxy'])
        read_proxies()
    elif proxy_type == 'list':
        read_proxies()
    elif proxy_type == 'rotate':
        read_rproxies()


def handle_continue():
    global args
    try:
        latest_subdir = max([os.path.join(args['--path'][0], d) for d in os.listdir(args['--path'][0])],
                            key=os.path.getmtime)
    except Exception as e:
        logger.error(e)
        logger.info('cant find the last run, gonna use the specified dir ')
    if (latest_subdir and os.path.isdir(latest_subdir)):
        argsDir = os.path.join(args['--path'][0], latest_subdir, 'args.json')
    else:
        logger.info('no subfolder found, gonna use the specified dir ')
        argsDir = os.path.join(args['--path'][0], 'args.json')

    if os.path.exists(argsDir):
        with open(argsDir, "r") as f:
            args = json.load(f, cls=DateTimeDecoder)
            args['--continue'] = True
    else:
        logger.info('cant find args .. exit')
        exit()


def init_logger():
    global logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter('%(asctime)-15s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    logger.addHandler(ch)


def read_and_convert(index=0):
    logger.info('read_and_convert, ' + args['--period'][index])

    init_path(index)
    logger.info('output to: ' + args['--path'][-1])

    listdir = os.listdir(args['--convert'])
    listdir = [filename for filename in listdir if filename.endswith(args['--filetype'])]
    if args['--source'] == 'ohlcv':
        for filename in listdir:
            logger.info('Converting: ' + filename)

            file_path = os.path.join(args['--convert'], filename)

            if args['--filetype'] == 'csv':
                df = pd.DataFrame.from_csv(file_path, index_col=7)
            else:
                with open(file_path, "r") as f:
                    df = pd.DataFrame.from_dict(json.load(f))

            ohlc_dict = {'price_open': 'first', 'price_high': 'max', 'price_low': 'min', 'price_close': 'last',
                         'volume_traded': 'sum', 'trades_count': 'sum', 'time_close': 'last', 'time_open': 'first',
                         'time_period_end': 'last'}
            df = df.resample(pd_offset[periods.index(args['--period'][index])], how=ohlc_dict)
            args['--from'] = datetime.strptime(filename.split('_')[-1].split('.')[0], '%Y-%m-%d')

            save_df(df, '_'.join(filename.split('_')[0:4]), index=index + 1)


def write_lastrun():
    with open("last_run.json", "w") as f:
        json.dump({','.join(
            args['--symbol'] + args['--exchange'] + args['--base'] + args['--quote'] + args['--type']): args[
            '--to']},
                  f, cls=DateTimeEncoder)


def read_lastrun():
    try:
        with open(os.path.join("last_run.json"), "r") as f:
            last_run = json.load(f, cls=DateTimeDecoder)
            last_run_from = ','.join(
                args['--symbol'] + args['--exchange'] + args['--base'] + args['--quote'] + args['--type'])
            if last_run_from in last_run:
                args['--from'] = last_run[last_run_from]
                logger.info('--from overridden with: ' + str(args['--from']))
    except  Exception as e:
        logger.error(e)


if __name__ == '__main__':
    init_logger()

    start_exec = datetime.now()
    args = parse_args()

    if args['--log_to'] != None:
        fh = logging.FileHandler(args['--log_to'])
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter('%(asctime)-15s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
        logger.addHandler(fh)

    logger.info(args)

    if args['--continue']:
        handle_continue()

    keys = readKeys()
    timeout = (args['--timeout'], args['--timeout'] * 5) if args['--timeout'] != 0 else None

    handle_proxies()

    if args['--generate_keys']:
        generate_keys(args['--generate_keys'])

    if args['--convert']:
        for index in range(len(args['--period'])):
            read_and_convert(index)
    else:
        if args['--continue']:
            with open(os.path.join(args['--path'][1], "remaining_symbols.json"), "r") as f:
                symbols = json.load(f)
        else:
            init_path()
            if args['--track_from']:
                read_lastrun()
            symbols = getSymbols()

        logger.info(symbols)
        if len(symbols) == 0:
            logger.info('No valid/remaining symbols found!')
            exit()

        download_source()

        if len(args['--period']) > 1 and args['--source'] == 'ohlcv':
            args['--convert'] = args['--path'][1]
            logger.info('converting path: ' + args['--convert'])
            for index in range(1, len(args['--period'])):
                read_and_convert(index)

    if (args['--dropbox']):
        handle_dropbox()

    if args['--track_from']:
        write_lastrun()

    logger.info('DONE, Took: ' + str(timedelta(seconds=(datetime.now() - start_exec).total_seconds())))
