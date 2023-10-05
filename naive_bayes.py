# -------------------------------------------------------------------------
# AUTHOR: Ryan Phan
# FILENAME: naive_bayes.py
# SPECIFICATION: output classification of each test instance from weather_test if conf > 0.75
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

# reading the training data in a csv file
# --> add your Python code here
training = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for c, row in enumerate(reader):
        if c > 0:  # skipping the header
            training.append(row)

# transform the original training features to numbers and add them to the 4D array X.
# For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
X = [row[:] for row in training]
length = len(X)
for i in range(length):
    for j in range(5):
        if training[i][j] == 'Sunny':
            X[i][j] = 1.0
        elif training[i][j] == 'Overcast':
            X[i][j] = 2.0
        elif training[i][j] == 'Rain':
            X[i][j] = 3.0
        elif training[i][j] == 'Hot':
            X[i][j] = 1.0
        elif training[i][j] == 'Mild':
            X[i][j] = 2.0
        elif training[i][j] == 'Cool':
            X[i][j] = 3.0
        elif training[i][j] == 'High':
            X[i][j] = 1.0
        elif training[i][j] == 'Normal':
            X[i][j] = 2.0
        elif training[i][j] == 'Strong':
            X[i][j] = 1.0
        elif training[i][j] == 'Weak':
            X[i][j] = 2.0
for i in X:
    del i[-1]
    del i[0]

#print (X)
# X = [[1, 1, 1, 2], [1, 1, 1, 1], [2, 1, 1, 2], [3, 2, 1, 2], [3, 3, 2, 2], [3, 3, 2, 1], [2, 3, 2, 1], [1, 2, 1, 2], [1, 3, 2, 2], [3, 2, 2, 2], [1, 2, 2, 1], [2, 2, 1, 1], [2, 1, 2, 2], [3, 2, 1, 1]]

# transform the original training classes to numbers and add them to the vector Y.
# For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
Y = [row[-1] for row in training]
length = len(Y)
for i in range(length):
    if Y[i] == 'No':
        Y[i] = 1.0
    else:
        Y[i] = 2.0

# print (Y)
# Y = [1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1]

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the test data in a csv file
# --> add your Python code here

test = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for c, row in enumerate(reader):
        if c > 0:  # skipping the header
            test.append(row)
for i in test:
    del i[0]
    del i[-1]
length = len(test)
for i in range(length):
    for j in range(4):
        if test[i][j] == 'Sunny':
            test[i][j] = 1.0
        elif test[i][j] == 'Overcast':
            test[i][j] = 2.0
        elif test[i][j] == 'Rain':
            test[i][j] = 3.0
        elif test[i][j] == 'Hot':
            test[i][j] = 1.0
        elif test[i][j] == 'Mild':
            test[i][j] = 2.0
        elif test[i][j] == 'Cool':
            test[i][j] = 3.0
        elif test[i][j] == 'High':
            test[i][j] = 1.0
        elif test[i][j] == 'Normal':
            test[i][j] = 2.0
        elif test[i][j] == 'Strong':
            test[i][j] = 1.0
        elif test[i][j] == 'Weak':
            test[i][j] = 2.0
#print (test)
# printing the header os the solution
# --> add your Python code here
result = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    print(reader.__next__())

# use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
# --> add your Python code here
dayIndex = []
for a in test:
    prob = clf.predict_proba([a])[0]

    if prob[0] >= 0.75:
        result.append(prob[0])
        dayIndex.append(a)
    elif prob[1] >= 0.75:
        result.append(prob[1])
        dayIndex.append(a)

for i in test:
    pred = clf.predict([i])[0]
    i.append(pred)

counter = 0
temp = []
for x in dayIndex:
    x.append(result[counter])
    counter+=1
    temp.append(x)

print (*temp, sep= "\n")

