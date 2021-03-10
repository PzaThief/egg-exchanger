##krw가 제공하는 금융상품 정보
import os, json
import sys
import datetime
from pathlib import Path
import requests
import mariadb
import myutil
import xmltodict
from contextlib import closing

today = datetime.datetime.now()
if datetime.datetime.now().hour < 9:
    today = today - datetime.timedelta(
        hours=15 + today.hour, minutes=today.minute, seconds=today.second, microseconds=today.microsecond
    )
today = myutil.getbusinessday(today)
dbname="cryptocurrency_from_bithumb"

with closing(myutil.mydbconnect()) as conn:
    with conn.cursor() as cur:
        cur.execute("select update_time from "+dbname)

url = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"
base_bidpath = "dbms/MDC/STAT/standard/"
bids = {
    "stock": "MDCSTAT01501",
    "etf": "MDCSTAT04301",
    "etn": "MDCSTAT06401",
    "elw": "MDCSTAT08301",
    "bond": "MDCSTAT09801",
    "derivative": "MDCSTAT12501",
}

for bid_key, bid_value in bids.items():
    params = {"bld": base_bidpath + bid_value, "trdDd": today.strftime("%Y%m%d")}
    if bid_key == "stock":
        params["mktId"] = "ALL"
        output = "OutBlock_1"
    else:
        output = "output"
    data = requests.post(url, data=params).json()
    datefromapi = datetime.datetime.strptime(data["CURRENT_DATETIME"], "%Y.%m.%d %p %I:%M:%S")
    data = data[output]
    data_keys = list(set(data[0].keys()).intersection(set(["ISU_SRT_CD", "ISU_ABBRV", "TDD_CLSPRC", "NAV"])))
