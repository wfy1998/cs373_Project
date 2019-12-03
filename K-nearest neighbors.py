from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import csv
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import warnings

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

positive_count = np.sum(y == 1)
negative_count = np.sum(y == -1)
positive_samples = list(np.where(y == 1)[0])
negative_samples = list(np.where(y == -1)[0])
print positive_count, negative_count

samples = []
X_train = []
y_train = []
X_test = []
y_test = []
xlabel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ylabelForPlotTwo = []
samplesNum = [len(X)]
accuracy = np.zeros(10)
for i in range(2, 11):
    samples_in_fold = []
    count1 = 0
    count2 = 0
    for j in range(i - 1):
        samples = positive_samples[count1: (count1 + positive_count / i)] \
                  + negative_samples[count2: (count2 + negative_count / i)]
        samples_in_fold.append(samples)
        count1 = count1 + positive_count / i
        count2 = count2 + negative_count / i
    samples = positive_samples[count1:] \
              + negative_samples[count2:]
    samples_in_fold.append(samples)
    samplesNum.append(len(samples))

    for k in range(i):
        for n in range(i):
            if n != k:
                for m in samples_in_fold[n]:
                    X_train.append(X[m])
                    y_train.append(y[m])
        for m in samples_in_fold[k]:
            X_test.append(X[m])
            y_test.append(y[m])

        neigh = KNeighborsClassifier(n_neighbors=5)
        neigh.fit(X_train, y_train)
        y_pred = neigh.predict(X_test)
        acc = 0
        for z in range(len(y_test)):
            if y_test[z] == y_pred[z]:
                acc = acc + 1
        acc = acc * 1.0 / len(y_test) * 1.0
        accuracy[i - 1] = accuracy[i - 1] + acc
    accuracy[i - 1] = accuracy[i - 1] / i
    # print accuracy[i - 1]
    if i == 4:
        for n in range(1, 11):
            neigh = KNeighborsClassifier(n_neighbors=n)
            neigh.fit(X_train, y_train)
            y_pred = neigh.predict(X_test)
            acc = 0
            for z in range(len(y_test)):
                if y_test[z] == y_pred[z]:
                    acc = acc + 1
            acc = acc * 1.0 / len(y_test) * 1.0
            ylabelForPlotTwo.append(acc)
            print acc

warnings.filterwarnings("ignore")

plt.figure(figsize=(10, 5))
plt.plot(xlabel, ylabelForPlotTwo)
plt.title(' Plot of accuracy vs different value of k in knn.')
plt.xlabel('knn')
plt.ylabel('accuracy')
plt.show()

warnings.filterwarnings("ignore")

plt.figure(figsize=(10, 5))
plt.plot(samplesNum, accuracy)
plt.title(' Plot of number of samples versus accuracy')
plt.xlabel('samples')
plt.ylabel('accuracy')
plt.xlim(-0.5, 500)
plt.ylim(0.9, 0.98)
plt.show()
