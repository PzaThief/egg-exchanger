##itemmania가 제공하는 게임화폐 정보
import os, json
import sys
import datetime
from pathlib import Path
import requests
import mariadb
import myutil
import xmltodict
from contextlib import closing

dbname="gamemoney_from_itemmania"
res = requests.post("https://www.mitemmania.com/_xml/gamemoney_servers.xml.php?gamecode=138")
result = json.loads(json.dumps(xmltodict.parse(res.text)))['list']
if result.get("@result")=="success":
    with closing(myutil.mydbconnect()) as conn:
        with conn.cursor() as cur:
            cur.execute("select update_time from "+dbname)
            before_update_time=cur.fetchone()
            if before_update_time is None or (datetime.datetime.now() - before_update_time[0]).seconds / 3600 > 1:
                for data in result['data']:
                        cur.execute(
                            "insert into "+dbname+" (gamename, servername, count_unit, unit, price, price_unit, store_date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (
                                "메이플",
                                data["@name"],
                                data["@unit_trade"],
                                data["@denomination"],
                                int(data["@price"])/int(data["@multiple"]),
                                "KRW",
                                datetime.datetime.strptime(result['@store_date'],"%Y.%m.%d"),
                            ),
                        )
            conn.commit()