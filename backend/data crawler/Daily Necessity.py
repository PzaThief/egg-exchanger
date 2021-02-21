##서울시 openapi가 제공하는 생필품가격정보
import os, json
import sys
import datetime
from pathlib import Path
import requests
import mariadb
import myutil
from contextlib import closing

day = myutil.isbusinessday(datetime.datetime.now())
# secrets = myutil.mysecretskey()
# with closing(myutil.mydbconnect()) as conn:
#     with conn.cursor() as cur: