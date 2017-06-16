import csv


def write_dev_stock(data):

    f = open('output.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')

    i = 0

    while i < len(data.index):
        row = data.iloc[i]
        writer.writerow(row)
        i += 1

    f.close()
