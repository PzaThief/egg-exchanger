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

data = requests.post("https://www.mitemmania.com/_xml/gamemoney_servers.xml.php?gamecode=138")
result = xmltodict.parse(data.text)
dictionay = json.load(json.dump(result))