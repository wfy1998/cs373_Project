from sklearn import svm
import csv
import numpy as np

X = [[0, 0], [1, 1]]
y = [0, 1]
def run(X, y):
    filename = "data.csv"
    fields = []
    rows = []
    lable = []
    dataRow = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            dataRow.append(float(row[0]))
            dataRow.append(float(row[1]))
            dataRow.append(float(row[2]))
            row[3] = float(row[3])
            rows.append(dataRow)
            lable.append(row[3])

    clf = svm.SVC(gamma='scale')
    print clf.fit(rows, lable)
    print clf.predict(rows)




run(X, y)
