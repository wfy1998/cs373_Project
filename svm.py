import csv
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score

filename = "data.csv"
fields = []
X = []
y = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        X.append(row[0:-2])
        y.append(int(row[3]))
y = np.array([y]).T

positive_count = np.sum(y==1)
negative_count = np.sum(y==-1)
positive_samples = list(np.where(y==1)[0])
negative_samples = list(np.where(y==-1)[0])
print positive_count, negative_count

samples = []
X_train = []
y_train = []
X_test = []
y_test = []
accuracy = np.zeros(10)
for i in range(2,11):
    samples_in_fold = []
    count1 = 0
    count2 = 0
    for j in range(i-1):
        samples = positive_samples[count1: (count1 + positive_count/i)] \
                + negative_samples[count2: (count2 + negative_count/i)]
        samples_in_fold.append(samples)
        count1 = count1 + positive_count/i
        count2 = count2 + negative_count/i
    samples = positive_samples[count1:] \
              + negative_samples[count2:]
    samples_in_fold.append(samples)

    for k in range(i):
        for n in range(i):
            if n != k:
                for m in samples_in_fold[n]:
                    X_train.append(X[m])
                    y_train.append(y[m])
        for m in samples_in_fold[k]:
            X_test.append(X[m])
            y_test.append(y[m])
        clf = svm.SVC(gamma='scale')
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy[i-1] = accuracy[i-1] + accuracy_score(y_pred, y_test)
        # print accuracy[i-1]
    accuracy[i-1] = accuracy[i-1]/i
    print accuracy[i-1]

