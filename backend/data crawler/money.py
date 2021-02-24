##한국수출입은행이 제공하는 환율정보
import os, json
import sys
import datetime
from pathlib import Path
import requests
import mariadb
import myutil
from contextlib import closing

secrets = myutil.mysecretskey()
my_key = secrets["koreaexim_key"]

today = datetime.datetime.now()
if today.hour < 11:
    today = today - datetime.timedelta(
        hours=13 + today.hour, minutes=today.minute, seconds=today.second, microseconds=today.microsecond
    )
today = myutil.getbusinessday(today)

with closing(myutil.mydbconnect()) as conn:
    with conn.cursor() as cur:
        cur.execute("select update_time from money_exchange_from_koreaexim")
        if cur.fetchone() is None or (datetime.datetime.now() - cur.fetchone()[0]).seconds / 3600 > 1:
            base_url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?"
            params = {"data": "AP01", "authkey": my_key, "searchdate": today.strftime("%Y%m%d")}
            response = requests.post(base_url, verify=False, data=params)
            money_data = []
            for i in response.json():
                if i.pop("result") == 1:
                    money_data.append(i)
                else:
                    continue
            if money_data:
                placeholder = ", ".join(["%s"] * (len(money_data[0]) + 1))
                stmt = "insert into `{table}` ({columns}) values ({values});".format(
                    table="money_exchange_from_koreaexim",
                    columns=",".join(money_data[0].keys()) + ",time_fromapi",
                    values=placeholder,
                )
                cur.execute("TRUNCATE TABLE " + "money_exchange_from_koreaexim")
                for i in money_data:
                    cur.execute(stmt, [myutil.if_float_conv(v) for v in i.values()] + [today])
                conn.commit()