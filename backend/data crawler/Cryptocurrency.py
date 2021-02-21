##빗썸이 제공하는 환율정보
import os, json
import sys
import datetime
from pathlib import Path
import requests
import mariadb
import myutil
from contextlib import closing

secrets = myutil.mysecretskey()
with closing(myutil.mydbconnect()) as conn:
    with conn.cursor() as cur:
        cur.execute("select update_time from cryptocurrency_from_bithumb")
        if cur.fetchone() is None or (datetime.datetime.now() - cur.fetchone()[0]).seconds / 60 > 1:
            response = requests.get("https://api.bithumb.com/public/orderbook/ALL_KRW", verify=False)
            data = response.json()["data"]
            tickers = [k for k, v in data.items() if isinstance(v, dict)]

            cur.execute("TRUNCATE TABLE " + "cryptocurrency_from_bithumb")
            for i in tickers:
                for j in range(5):
                    for bids_asks in ("bids", "asks"):
                        cur.execute(
                            "insert into cryptocurrency_from_bithumb (payment_currency, order_currency, bids_asks, price, quantity, time_fromapi) VALUES (?, ?, ?, ?, ?, ?)",
                            (
                                data["payment_currency"],
                                i,
                                bids_asks,
                                float(data[i][bids_asks][j]["price"]),
                                float(data[i][bids_asks][j]["quantity"]),
                                datetime.datetime.fromtimestamp(int(data["timestamp"]) / 1000),
                            ),
                        )
            conn.commit()