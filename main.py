# coding:utf-8

from src.web import get_stock_prices
from src.file import write_csv

# 銘柄番号
company = 7201
# 取得日数
days = 0

# DB接続情報
host = "localhost"
port = 15432
dbname = "postgres"
table = "dev_stock"
schema = "nq52"
user = "postgres"
password = "postgres"

######################################################
# 株価の初回取得
# yahoo!financeから株価を取得、DBへ投入
######################################################

if __name__ == "__main__":

    data = get_stock_prices.get_stock_prices(company, 300, "1d")

    # db_access.insert_dev_stock(company, host, port, dbname, table, schema, user, password, data)

    write_csv.write_dev_stock(data)

    print(data)
