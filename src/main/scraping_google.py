import pandas
import psycopg2

# 指定した期間、銘柄の株価をyahoo financeから取得する
# param
# 	銘柄、ティックの長さ、期間、
# return
#	取得したデータ

def scraping_google(companyCd, intervalSec, term):

	base = "https://www.google.com/finance/getprices?q={0}&x=TYO&i={1}&p={2}&f=d,c,v,o,h,l&df=cpct&auto=1&ts=1489550582260&ei=4rrIWJHoIYya0QS1i4IQ"
	print(base)
	companyCd = str(companyCd)
	intervalSec = str(intervalSec)
	
	result = []
	while True:
		url = base.format(companyCd, intervalSec,term)
		df = pandas.read_html(url, header=0)
		if len(df[1]) == 0:
			break

		result.append(df[1])
	result = pandas.concat(result)
	print(result)
	result.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']

	return result