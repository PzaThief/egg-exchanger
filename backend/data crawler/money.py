##한국수출입은행이 제공하는 환율정보
import os, json
import sys
import datetime
from pathlib import Path
import requests
import mariadb

BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, "secrets.json")  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())
my_key = secrets["koreaexim_key"]

today = datetime.date.today()
today += datetime.timedelta(min(-today.weekday() + 4, 0))

base_url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?"
params = {"data": "AP01", "authkey": my_key, "searchdate": today.strftime("%Y%m%d")}
response = requests.post(base_url, verify=False, data=params)

try:
    conn = mariadb.connect(
        host="127.0.0.1",
        user=secrets["mariadb_username"],
        password=secrets["mariadb_password"],
        port=3306,
        database="egg_exchanger",
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")

cur = conn.cursor()
placeholder = ", ".join(["%s"] * len(response.json()[0]))
stmt = "insert into `{table}` ({columns}) values ({values});".format(
    table="money_exchange_from_koreaexim", columns=",".join(response.json()[0].keys()), values=placeholder
)
cur.execute("TRUNCATE TABLE " + "money_exchange_from_koreaexim")
for i in response.json():
    cur.execute(stmt, tuple(i.values()))
conn.commit()
cur.close()
conn.close()