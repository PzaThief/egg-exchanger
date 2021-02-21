##krw가 제공하는 주식정보
import os, json
import sys
import datetime
from pathlib import Path
import requests
import mariadb
from pykrx import stock

BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, "secrets.json")  # secrets.json 파일 위치를 명시
with open(secret_file) as f:
    secrets = json.loads(f.read())
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
cur.execute("select update_time from cryptocurrency_from_bithumb")

today = stock.get_nearest_business_day_in_a_week()
