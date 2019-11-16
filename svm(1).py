import csv
import numpy as np
from sklearn import svm

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
samples_in_fold1 = positive_samples[0:positive_count/2] + negative_samples[0:negative_count/2]
samples_in_fold2 = positive_samples[positive_count/2:] + negative_samples[negative_count/2:]

print positive_count, negative_count

X_train = []
for i in samples_in_fold1:
    X_train.append(X[i])
y_train = y[samples_in_fold1]
X_pred = []
for i in samples_in_fold2:
    X_pred.append(X[i])
clf = svm.SVC(gamma='scale')

print clf.fit(X_train, y_train)
print clf.predict(X_pred)
