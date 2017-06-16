import psycopg2


def insert_dev_stock(company, host, port, dbname, table, schema, user, password, data):

    # DBコネクション取得
    connection = psycopg2.connect("host=" + host + " port=" + str(port) + " dbname=" + dbname + " user=" + user + " password=" + password)
    connection.get_backend_pid()

    cur = connection.cursor()

    # データインサート
    i = 0

    while i < len(data.index):
        row = data.iloc[i]
        cur.execute(
            "insert into " + schema + "."+table+" values(" + str(company) + ", '" + str(row["DATE"]) + "', " + str(
                row["OPEN"]) + ", " + str(row["HIGH"]) + ", " + str(row["LOW"]) + ", " + str(row["CLOSE"]) + " ," + str(
                row["VOLUME"]) + ", " + str(row["CLOSE"]) + ", " + str((float(row["HIGH"]) + float(row["LOW"])) // 2.0) + ")")
        i += 1

    # コミット
    connection.commit()

    # コネクションクローズ
    cur.close()
    connection.close()
