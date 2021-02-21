##krw가 제공하는 금융상품 정보
import os, json
import sys
import datetime
from pathlib import Path
import requests
import mariadb
import myutil
from contextlib import closing

today = datetime.datetime.now()
if datetime.datetime.now().hour < 9:
    today = today - datetime.timedelta(
        hours=15 + today.hour, minutes=today.minute, seconds=today.second, microseconds=today.microsecond
    )
today = getbusinessday(today)

with closing(myutil.mydbconnect()) as conn:
    with conn.cursor() as cur:
        cur.execute("select update_time from cryptocurrency_from_bithumb")


base_bidurl = "dbms/MDC/STAT/standard/"
bids = {
    "stock": "MDCSTAT01501",
    "etf": "MDCSTAT04301",
    "etn": "MDCSTAT06401",
    "elw": "MDCSTAT08301",
    "bond": "MDCSTAT09801",
    "derivative": "MDCSTAT12501",
}

params = {"bld": "dbms/MDC/STAT/standard/MDCSTAT01501", "mktId": "ALL", "trdDd": "20200831"}
url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"
stock_data = requests.post(url, data=params).json()
