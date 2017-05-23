# coding:utf-8
import datetime
import scraping_yahoo
import insert_stock

#銘柄番号
company = 7261
#取得日数
days = 0

#DB接続情報
host = "172.17.0.2"
port = 5432
dbname = "postgres"
schema = "nq52"
user = "postgres"
password = "postgres"

######################################################
#株価の初回取得
#yahoo!financeから株価を取得、DBへ投入
######################################################

if __name__ == "__main__":


	print("test")
	EndDate = datetime.date.today()
	StartDate = EndDate - datetime.timedelta(days)

	data = scraping_yahoo.scraping_yahoo(company, StartDate, EndDate, "d")
	print(data)

	insert_stock.insert_stock(company, host, port, dbname, schema, user, password, data)
