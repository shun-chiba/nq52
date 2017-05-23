import psycopg2
import datetime

######################################################
#
# DBへ株価投入
#
######################################################

def insert_stock(company, host, port, dbname, schema, user, password, data):

	connection = psycopg2.connect("host="+host+" port="+str(port)+" dbname="+dbname+" user="+user+" password="+password)
	connection.get_backend_pid()
	
	cur = connection.cursor()

	cur.execute("delete from "+ schema +".dev_stock where campany_cd = "+str(company))

	data_array = data.values

	for row in data_array:
		d = datetime.datetime.strptime(row[0], '%Y年%m月%d日')
		cur.execute("insert into "+ schema +".dev_stock values("+str(company)+", '"+d.strftime('%Y%m%d')+"', "+str(row[1])+", "+str(row[2])+", "+str(row[3])+", "+str(row[4])+" ,"+str(row[5])+", "+str(row[6])+", "+str((row[2]+row[3])//2.0)+")")

	connection.commit()
	
	cur.close()
	connection.close()
