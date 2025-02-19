# Coinapi key generator and data downloader

## Installation:
* Python installation:
```
mkdir /temp
cd /temp

wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
bash Anaconda3-5.2.0-Linux-x86_64.sh
# wizard ****
```
* Libraries installation:
```
pip install -r requirements.txt
```

```bash
python run.py --symbol=BINANCE_SPOT_BTC_USDT --from=2023-01-01 --generate_keys=100
```

## Example, try:
```
python run.py --symbol=BITSTAMP_SPOT_LTC_USD  --source=ohlcv --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --timeout=20
python run.py --exchange=BITSTAMP  --source=ohlcv --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --limit=100000
python run.py --exchange=BITSTAMP  --source=trades --from=2018-08-23 --proxy_type=rotate --period=1HRS --filetype=csv --limit=100000
python run.py --symbol=BINANCE_SPOT_BTC_USDT,BINANCE_SPOT_ETH_USDT,BINANCE_SPOT_EOS_USDT,BINANCE_SPOT_ETH_BTC,BINANCE_SPOT_ONT_USDT,BINANCE_SPOT_BCC_USDT,BINANCE_SPOT_EOS_BTC,BINANCE_SPOT_ETC_USDT,BINANCE_SPOT_ONT_BTC,BINANCE_SPOT_NANO_BTC,BINANCE_SPOT_TRX_USDT,BINANCE_SPOT_BCC_BTC,BINANCE_SPOT_XRP_BTC,BINANCE_SPOT_ETC_BTC,BINANCE_SPOT_XRP_USDT,BINANCE_SPOT_VET_USDT,BINANCE_SPOT_TRX_BTC,BINANCE_SPOT_ADA_USDT,BINANCE_SPOT_NEO_USDT,BINANCE_SPOT_XLM_BTC,BINANCE_SPOT_CMT_BTC,BINANCE_SPOT_VET_BTC,BINANCE_SPOT_NEO_BTC,BINANCE_SPOT_ADA_BTC,BINANCE_SPOT_LTC_USDT,BINANCE_SPOT_THETA_BTC,BINANCE_SPOT_LTC_BTC,BINANCE_SPOT_IOTA_USDT,BINANCE_SPOT_BNB_BTC,BINANCE_SPOT_BNB_USDT,BINANCE_SPOT_XLM_USDT,BINANCE_SPOT_TUSD_USDT,BINANCE_SPOT_ICX_USDT,BINANCE_SPOT_IOTA_BTC,BINANCE_SPOT_ZRX_BTC,BINANCE_SPOT_ICX_BTC,BINANCE_SPOT_WTC_BTC,BINANCE_SPOT_XMR_BTC,BINANCE_SPOT_ARN_BTC,BINANCE_SPOT_TUSD_BTC,BINANCE_SPOT_LSK_BTC,BINANCE_SPOT_ZIL_BTC,BINANCE_SPOT_QKC_BTC,BINANCE_SPOT_DASH_BTC,BINANCE_SPOT_IOTX_BTC,BINANCE_SPOT_NANO_ETH,BINANCE_SPOT_DOCK_BTC,BINANCE_SPOT_NPXS_BTC,BINANCE_SPOT_NAS_BTC,BINANCE_SPOT_CMT_ETH,BINANCE_SPOT_YOYO_BTC,BINANCE_SPOT_EOS_ETH,BINANCE_SPOT_QTUM_USDT,BINANCE_SPOT_LINK_BTC,BINANCE_SPOT_GAS_BTC,BINANCE_SPOT_ELF_BTC,BINANCE_SPOT_IOST_BTC,BINANCE_SPOT_LOOM_BTC,BINANCE_SPOT_NCASH_BTC,BINANCE_SPOT_VET_ETH,BINANCE_SPOT_NULS_BTC,BINANCE_SPOT_WAN_BTC,BINANCE_SPOT_REP_BTC,BINANCE_SPOT_GTO_BTC,BINANCE_SPOT_KEY_BTC,BINANCE_SPOT_BNB_ETH,BINANCE_SPOT_CVC_BTC,BINANCE_SPOT_ADA_ETH,BINANCE_SPOT_DENT_BTC,BINANCE_SPOT_THETA_ETH,BINANCE_SPOT_XVG_BTC,BINANCE_SPOT_MDA_BTC,BINANCE_SPOT_POA_BTC,BINANCE_SPOT_IOST_ETH,BINANCE_SPOT_TRX_ETH,BINANCE_SPOT_BAT_BTC,BINANCE_SPOT_MFT_BTC,BINANCE_SPOT_ENG_BTC,BINANCE_SPOT_XRP_ETH,BINANCE_SPOT_XEM_BTC,BINANCE_SPOT_BQX_BTC,BINANCE_SPOT_NEO_ETH,BINANCE_SPOT_SNT_BTC,BINANCE_SPOT_NAS_ETH,BINANCE_SPOT_NULS_USDT,BINANCE_SPOT_ONT_ETH,BINANCE_SPOT_PPT_BTC,BINANCE_SPOT_AION_BTC,BINANCE_SPOT_SUB_BTC,BINANCE_SPOT_ADX_BTC,BINANCE_SPOT_QTUM_BTC,BINANCE_SPOT_LOOM_ETH,BINANCE_SPOT_ZRX_ETH,BINANCE_SPOT_ICX_ETH,BINANCE_SPOT_BCD_BTC,BINANCE_SPOT_STORM_BTC,BINANCE_SPOT_OMG_BTC,BINANCE_SPOT_BCC_ETH,BINANCE_SPOT_MTL_BTC,BINANCE_SPOT_ZEC_BTC --source=ohlcv --from=2018-08-23 --to=2018-08-24 --proxy_type=list --period=1HRS --filetype=csv --limit=100000 --timeout=10
python run.py --exchange=BINANCE --quote=USDT,BTC,ETH --base=BTC,ETH,EOS,ONT,BCC,ETC,NANO,TRX,XRP,VET,ADA,NEO,XLM,CMT,LTC,THETA,IOTA,BNB,TUSD,ICX,ZRX,WTC,XMR,ARN,LSK,ZIL,QKC,DASH,IOTX,DOCK,NPXS,NAS,YOYO,QTUM,LINK,GAS,ELF,IOST,LOOM,NCASH,NULS,WAN,REP,GTO,KEY,CVC,DENT,XVG,MDA,POA,BAT,MFT,ENG,XEM,BQX,SNT,PPT,AION,SUB,ADX,BCD,STORM,OMG,MTL,ZEC --source=ohlcv --from=2018-08-23 --to=2018-08-24 --proxy_type=list --period=1HRS --filetype=csv --limit=100000 --timeout=10
```
## To run in the background on linux:
```
    nohup my_command > my.log 2>&1 &
    echo $! > save_pid.txt
```
## To stop it:
```
    kill -9 `cat save_pid.txt`
    rm save_pid.txt
```

## Top 100 coins on linux:
```
nohup /root/anaconda3/bin/python run.py --symbol=BINANCE_SPOT_BTC_USDT,BINANCE_SPOT_ETH_USDT,BINANCE_SPOT_EOS_USDT,BINANCE_SPOT_ETH_BTC,BINANCE_SPOT_ONT_USDT,BINANCE_SPOT_BCC_USDT,BINANCE_SPOT_EOS_BTC,BINANCE_SPOT_ETC_USDT,BINANCE_SPOT_ONT_BTC,BINANCE_SPOT_NANO_BTC,BINANCE_SPOT_TRX_USDT,BINANCE_SPOT_BCC_BTC,BINANCE_SPOT_XRP_BTC,BINANCE_SPOT_ETC_BTC,BINANCE_SPOT_XRP_USDT,BINANCE_SPOT_VET_USDT,BINANCE_SPOT_TRX_BTC,BINANCE_SPOT_ADA_USDT,BINANCE_SPOT_NEO_USDT,BINANCE_SPOT_XLM_BTC,BINANCE_SPOT_CMT_BTC,BINANCE_SPOT_VET_BTC,BINANCE_SPOT_NEO_BTC,BINANCE_SPOT_ADA_BTC,BINANCE_SPOT_LTC_USDT,BINANCE_SPOT_THETA_BTC,BINANCE_SPOT_LTC_BTC,BINANCE_SPOT_IOTA_USDT,BINANCE_SPOT_BNB_BTC,BINANCE_SPOT_BNB_USDT,BINANCE_SPOT_XLM_USDT,BINANCE_SPOT_TUSD_USDT,BINANCE_SPOT_ICX_USDT,BINANCE_SPOT_IOTA_BTC,BINANCE_SPOT_ZRX_BTC,BINANCE_SPOT_ICX_BTC,BINANCE_SPOT_WTC_BTC,BINANCE_SPOT_XMR_BTC,BINANCE_SPOT_ARN_BTC,BINANCE_SPOT_TUSD_BTC,BINANCE_SPOT_LSK_BTC,BINANCE_SPOT_ZIL_BTC,BINANCE_SPOT_QKC_BTC,BINANCE_SPOT_DASH_BTC,BINANCE_SPOT_IOTX_BTC,BINANCE_SPOT_NANO_ETH,BINANCE_SPOT_DOCK_BTC,BINANCE_SPOT_NPXS_BTC,BINANCE_SPOT_NAS_BTC,BINANCE_SPOT_CMT_ETH,BINANCE_SPOT_YOYO_BTC,BINANCE_SPOT_EOS_ETH,BINANCE_SPOT_QTUM_USDT,BINANCE_SPOT_LINK_BTC,BINANCE_SPOT_GAS_BTC,BINANCE_SPOT_ELF_BTC,BINANCE_SPOT_IOST_BTC,BINANCE_SPOT_LOOM_BTC,BINANCE_SPOT_NCASH_BTC,BINANCE_SPOT_VET_ETH,BINANCE_SPOT_NULS_BTC,BINANCE_SPOT_WAN_BTC,BINANCE_SPOT_REP_BTC,BINANCE_SPOT_GTO_BTC,BINANCE_SPOT_KEY_BTC,BINANCE_SPOT_BNB_ETH,BINANCE_SPOT_CVC_BTC,BINANCE_SPOT_ADA_ETH,BINANCE_SPOT_DENT_BTC,BINANCE_SPOT_THETA_ETH,BINANCE_SPOT_XVG_BTC,BINANCE_SPOT_MDA_BTC,BINANCE_SPOT_POA_BTC,BINANCE_SPOT_IOST_ETH,BINANCE_SPOT_TRX_ETH,BINANCE_SPOT_BAT_BTC,BINANCE_SPOT_MFT_BTC,BINANCE_SPOT_ENG_BTC,BINANCE_SPOT_XRP_ETH,BINANCE_SPOT_XEM_BTC,BINANCE_SPOT_BQX_BTC,BINANCE_SPOT_NEO_ETH,BINANCE_SPOT_SNT_BTC,BINANCE_SPOT_NAS_ETH,BINANCE_SPOT_NULS_USDT,BINANCE_SPOT_ONT_ETH,BINANCE_SPOT_PPT_BTC,BINANCE_SPOT_AION_BTC,BINANCE_SPOT_SUB_BTC,BINANCE_SPOT_ADX_BTC,BINANCE_SPOT_QTUM_BTC,BINANCE_SPOT_LOOM_ETH,BINANCE_SPOT_ZRX_ETH,BINANCE_SPOT_ICX_ETH,BINANCE_SPOT_BCD_BTC,BINANCE_SPOT_STORM_BTC,BINANCE_SPOT_OMG_BTC,BINANCE_SPOT_BCC_ETH,BINANCE_SPOT_MTL_BTC,BINANCE_SPOT_ZEC_BTC --source=ohlcv --from=2016-08-20 --to=2018-08-20 --period=1MIN --proxy_type=fresh --find_n_proxy=500 --limit=100000 > my.log 2>&1 &

echo $! > save_pid.txt
```

## Cron task:
```
crontab -e

MAILTO="ahmedengu@gmail.com"
0 0 * * * /root/anaconda3/bin/python /root/task/run.py --symbol=BINANCE_SPOT_BTC_USDT,BINANCE_SPOT_ETH_USDT,BINANCE_SPOT_EOS_USDT,BINANCE_SPOT_ETH_BTC,BINANCE_SPOT_ONT_USDT,BINANCE_SPOT_BCC_USDT,BINANCE_SPOT_EOS_BTC,BINANCE_SPOT_ETC_USDT,BINANCE_SPOT_ONT_BTC,BINANCE_SPOT_NANO_BTC,BINANCE_SPOT_TRX_USDT,BINANCE_SPOT_BCC_BTC,BINANCE_SPOT_XRP_BTC,BINANCE_SPOT_ETC_BTC,BINANCE_SPOT_XRP_USDT,BINANCE_SPOT_VET_USDT,BINANCE_SPOT_TRX_BTC,BINANCE_SPOT_ADA_USDT,BINANCE_SPOT_NEO_USDT,BINANCE_SPOT_XLM_BTC,BINANCE_SPOT_CMT_BTC,BINANCE_SPOT_VET_BTC,BINANCE_SPOT_NEO_BTC,BINANCE_SPOT_ADA_BTC,BINANCE_SPOT_LTC_USDT,BINANCE_SPOT_THETA_BTC,BINANCE_SPOT_LTC_BTC,BINANCE_SPOT_IOTA_USDT,BINANCE_SPOT_BNB_BTC,BINANCE_SPOT_BNB_USDT,BINANCE_SPOT_XLM_USDT,BINANCE_SPOT_TUSD_USDT,BINANCE_SPOT_ICX_USDT,BINANCE_SPOT_IOTA_BTC,BINANCE_SPOT_ZRX_BTC,BINANCE_SPOT_ICX_BTC,BINANCE_SPOT_WTC_BTC,BINANCE_SPOT_XMR_BTC,BINANCE_SPOT_ARN_BTC,BINANCE_SPOT_TUSD_BTC,BINANCE_SPOT_LSK_BTC,BINANCE_SPOT_ZIL_BTC,BINANCE_SPOT_QKC_BTC,BINANCE_SPOT_DASH_BTC,BINANCE_SPOT_IOTX_BTC,BINANCE_SPOT_NANO_ETH,BINANCE_SPOT_DOCK_BTC,BINANCE_SPOT_NPXS_BTC,BINANCE_SPOT_NAS_BTC,BINANCE_SPOT_CMT_ETH,BINANCE_SPOT_YOYO_BTC,BINANCE_SPOT_EOS_ETH,BINANCE_SPOT_QTUM_USDT,BINANCE_SPOT_LINK_BTC,BINANCE_SPOT_GAS_BTC,BINANCE_SPOT_ELF_BTC,BINANCE_SPOT_IOST_BTC,BINANCE_SPOT_LOOM_BTC,BINANCE_SPOT_NCASH_BTC,BINANCE_SPOT_VET_ETH,BINANCE_SPOT_NULS_BTC,BINANCE_SPOT_WAN_BTC,BINANCE_SPOT_REP_BTC,BINANCE_SPOT_GTO_BTC,BINANCE_SPOT_KEY_BTC,BINANCE_SPOT_BNB_ETH,BINANCE_SPOT_CVC_BTC,BINANCE_SPOT_ADA_ETH,BINANCE_SPOT_DENT_BTC,BINANCE_SPOT_THETA_ETH,BINANCE_SPOT_XVG_BTC,BINANCE_SPOT_MDA_BTC,BINANCE_SPOT_POA_BTC,BINANCE_SPOT_IOST_ETH,BINANCE_SPOT_TRX_ETH,BINANCE_SPOT_BAT_BTC,BINANCE_SPOT_MFT_BTC,BINANCE_SPOT_ENG_BTC,BINANCE_SPOT_XRP_ETH,BINANCE_SPOT_XEM_BTC,BINANCE_SPOT_BQX_BTC,BINANCE_SPOT_NEO_ETH,BINANCE_SPOT_SNT_BTC,BINANCE_SPOT_NAS_ETH,BINANCE_SPOT_NULS_USDT,BINANCE_SPOT_ONT_ETH,BINANCE_SPOT_PPT_BTC,BINANCE_SPOT_AION_BTC,BINANCE_SPOT_SUB_BTC,BINANCE_SPOT_ADX_BTC,BINANCE_SPOT_QTUM_BTC,BINANCE_SPOT_LOOM_ETH,BINANCE_SPOT_ZRX_ETH,BINANCE_SPOT_ICX_ETH,BINANCE_SPOT_BCD_BTC,BINANCE_SPOT_STORM_BTC,BINANCE_SPOT_OMG_BTC,BINANCE_SPOT_BCC_ETH,BINANCE_SPOT_MTL_BTC,BINANCE_SPOT_ZEC_BTC --source=ohlcv --from=$(date --date=' 1 days ago' '+%Y-%m-%d') --to=$(date '+%Y-%m-%d') --period=1MIN --proxy_type=fresh --find_n_proxy=500 --limit=100000 --timeout=5 >/dev/null 2>&1
```

## Usage:
```
  run.py (--symbol=<string> | [--exchange=<string>] [--base=<string>] [--quote=<string>] [--type=<string>]) [--source=<string>] (--from=<date>|--from=<date> --track_from) [--to=<date>] [--period=<string>]  [--limit=<int>]  [--levels=<int>]  [--path=<path>] [--filetype=<string>] [--proxy_type=<string>] [--timeout=<int>] [--generate_keys=<int>] [--find_n_proxy=<int>] [--proxy_dnsbl] [--proxy_strict] [--log_to=<filename>] [--dropbox_key=<string>] [--dropbox [keep]] [--dropbox_dir=<path>]
  run.py --continue [--path=<path>]
  run.py --convert=<path> --period=<string> [--path=<path>] [--dropbox_key=<string>] [--dropbox [keep]] [--dropbox_dir=<path>] [--source=<string>] [--filetype=<string>]
  run.py (-h | --help)
```

## Arguments:
```
  --symbol=<string>     Symbol id for requested timeseries, comma separated, check https://docs.coinapi.io/#list-all-symbols
  --exchange=<string>     identifier of the exchange where symbol is traded, comma separated, check https://docs.coinapi.io/#list-all-symbols
  --base=<string>     FX Spot base asset identifier, for derivatives it’s contact underlying (e.g. BTC for BTC/USD), comma separated, check https://docs.coinapi.io/#list-all-symbols
  --quote=<string>     FX Spot quote asset identifier, for derivatives it’s contract underlying (e.g. USD for BTC/USD), comma separated, check https://docs.coinapi.io/#list-all-symbols
  --type=<string>     Type of symbol (possible values are: SPOT, FUTURES or OPTION), comma separated
  --from=<date>     starting date.
  --source=<string>     the data to be downloaded (ohlcv, trades, quotes, order) [default: ohlcv].
  --convert=<path>     a path to a directory that contains csv files to be converted.
  --continue  continue the last run [default: False].
```

## Options:
```
  -h --help     Show this screen.
  --path=<path>  a directory to save data to [default: out].
  --filetype=<string>  the saved data file type (json, csv) [default: csv].
  --to=<date>  ending date.
  --period=<string>  supported time periods available for requesting OHLCV timeseries data OR to convert data to, check https://docs.coinapi.io/#list-all-periods.
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
  --dropbox_dir=<path>  dropbox directory to upload to [default: /OHLCV_data/Binance/1Min_OHLCV].
  keep  to keep files after copying them to dropbox [default: false].
  --log_to=<filename>  specify a file name to save all the output to.
  --track_from  to keep track of the last from to ensure that the script starts from the last time it ran gonna use --from if the last from not found [default: false].
  ```
 
