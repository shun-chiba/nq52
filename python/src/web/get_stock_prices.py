# -*- coding: utf-8 -*-

import urllib.request
import ssl
import pandas as pd
import datetime

# 指定した期間、銘柄の株価を取得する
# param
# 	銘柄、ティックの長さ、期間、
# return
#   取得したデータ


def get_stock_prices(company_cd, interval_sec, term):

    # urlの設定
    url = "https://www.google.com/finance/getprices?q={0}&x=TYO&i={1}&p={2}&f=d,o,h,l,c,v&df=cpct&auto=1&ts=1489550582260&ei=4rrIWJHoIYya0QS1i4IQ"

    # urlのパラメータに値セット
    url = url.format(str(company_cd), str(interval_sec), term)

    # データ取得
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)
    result = str(response.read())

    # データの整形
    result = result.split("\\n")
    columns = result[4].split("=")[1].split(",")
    data = []
    for row in result[8:-1]:
        data.append(row.split(","))

    # pandasにデータ格納
    df = pd.DataFrame(data)
    df.columns = columns

    # UNIX時間の変換
    base_date = datetime.datetime.today()

    for i in range(len(df["DATE"])):
        if "a" in df["DATE"][i]:
            base_date = float(df["DATE"][i][1:])
            df["DATE"][i] = datetime.datetime.fromtimestamp(base_date)
        else:
            df["DATE"][i] = datetime.datetime.fromtimestamp(base_date + (interval_sec * float(df["DATE"][i])))

    return df
