import os, json
import sys
import datetime
from pathlib import Path
import mariadb
import requests
import datetime
import xmltodict


def getbusinessday(today=datetime.datetime.now()):
    if not isinstance(today, datetime.date):
        today = datetime.datetime.strptime(today, "%Y%m%d")
    while isbusinessday(today):
        today -= datetime.timedelta(days=1)
    return today


def isbusinessday(day):
    ans = False
    if day.weekday() > 4:
        ans = True
    else:
        base_url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo"
        params = {"serviceKey": mysecretskey()["DATAgokr_key"], "solYear": day.year, "_type": "json", "numOfRows": 20}
        res = requests.get(base_url, params=params)
        restday = []
        for item in res.json()["response"]["body"]["items"]["item"]:
            restday.append(str(item["locdate"]))
        if day.strftime("%Y%m%d") in restday:
            ans = True
    return ans


def mysecretskey():
    BASE_DIR = Path(__file__).resolve().parent.parent
    secret_file = os.path.join(BASE_DIR, "secrets.json")  # secrets.json 파일 위치를 명시

    with open(secret_file) as f:
        secrets = json.loads(f.read())
    return secrets


def mydbconnect():
    secrets = mysecretskey()
    try:
        conn = mariadb.connect(
            host="127.0.0.1",
            user=secrets["mariadb_username"],
            password=secrets["mariadb_password"],
            port=secrets["mariadb_port"],
            database="egg_exchanger",
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
    return conn