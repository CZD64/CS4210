# -------------------------------------------------------------------------
# AUTHOR: Ryan Phan
# FILENAME: knn.py
# SPECIFICATION: Reads from binary file and outputs LOO-CV error rate for 1nn
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

from sklearn.metrics import accuracy_score

db = []

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            # print(row)

col = len(db[0])

X = []
Y = []
testSample = []
temp = []
errorCounter = 0
iteration = 0
predict = []

# loop your data to allow each instance to be your test set
for i in db:
    # print (i) add the training features to the 2D array X removing the instance that will be used for testing in
    # this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to float to avoid warning
    # messages --> add your Python code here db[i]= float(db[i])
    for j in range(col - 1):
        i[j] = (float(i[j]))
    X.append(i[:-1])
    # print (X)

    # X = [[2, 1], [4, 1], [3, 2], [0, 3], [3, 3], [4, 3], [1, 4], [2, 4], [4, 4], [0, 5]]

    # transform the original training classes to numbers and add to the vector Y removing the instance that will be
    # used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each feature value to float to
    # avoid warning messages --> add your Python code here
    if i[-1] == '+':
        i[-1] = 1.0
    else:
        i[-1] = 2.0
    Y.append(i[-1])
    # print (Y)

    # Y = [2, 2, 1, 2, 1, 1, 2, 1, 1, 2]

    # store the test sample of this iteration in the vector testSample
    # --> add your Python code here
    testSample = X
    #print (testSample)
    #print (X)
    # testSample =

    # fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    # use your test sample in this iteration to make the class prediction. For instance:
    class_predicted = clf.predict([testSample])[0]
    # --> add your Python code here

    # compare the prediction with the true label of the test instance to start calculating the error rate.
    # --> add your Python code here
    print (class_predicted)
    iteration+=1

# print the error rate
# --> add your Python code here
#accuracy = accuracy_score(Y,predict)
#print(accuracy)
