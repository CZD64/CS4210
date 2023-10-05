# -------------------------------------------------------------------------
# AUTHOR: Ryan Phan
# FILENAME: decision_tree_2.py
# SPECIFICATION: Train with three different sets of data to test with one
# FOR: CS 4210- Assignment #2
# TIME SPENT: :(
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import csv

dbTest = []
data = []

with open('contact_lens_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for c, row in enumerate(reader):
        if c > 0:  # skipping the header
            dbTest.append(row)

# data = [row[:] for row in dbTest]
# print (data)
length = len(dbTest)
for a in range(length):
    for b in range(4):
        if dbTest[a][b] == 'Young':
            dbTest[a][b] = 1
        elif dbTest[a][b] == 'Prepresbyopic':
            dbTest[a][b] = 2
        elif dbTest[a][b] == 'Presbyopic':
            dbTest[a][b] = 3
        elif dbTest[a][b] == 'Myope':
            dbTest[a][b] = 1
        elif dbTest[a][b] == 'Hypermetrope':
            dbTest[a][b] = 2
        elif dbTest[a][b] == 'No':
            dbTest[a][b] = 1
        elif dbTest[a][b] == 'Yes':
            dbTest[a][b] = 2
        elif dbTest[a][b] == 'Reduced':
            dbTest[a][b] = 1
        elif dbTest[a][b] == 'Normal':
            dbTest[a][b] = 2

for i in range(length):
    if dbTest[i][-1] == 'No':
        dbTest[i][-1] = 1
    else:
        dbTest[i][-1] = 2

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    error = 0

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    X = [row[:] for row in dbTraining]
    Y = [row[-1] for row in dbTraining]

    # transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    length = len(X)
    for i in range(length):
        for j in range(4):
            if dbTraining[i][j] == 'Young':
                X[i][j] = 1
            elif dbTraining[i][j] == 'Prepresbyopic':
                X[i][j] = 2
            elif dbTraining[i][j] == 'Presbyopic':
                X[i][j] = 3
            elif dbTraining[i][j] == 'Myope':
                X[i][j] = 1
            elif dbTraining[i][j] == 'Hypermetrope':
                X[i][j] = 2
            elif dbTraining[i][j] == 'No':
                X[i][j] = 1
            elif dbTraining[i][j] == 'Yes':
                X[i][j] = 2
            elif dbTraining[i][j] == 'Reduced':
                X[i][j] = 1
            elif dbTraining[i][j] == 'Normal':
                X[i][j] = 2
    for i in X:
        del i[-1]
    # print(X)
    # X =

    # transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    length = len(Y)
    for i in range(length):
        if Y[i] == 'No':
            Y[i] = 1
        else:
            Y[i] = 2
    # print (Y)
    # Y =

    # loop your training and test tasks 10 times here
    for i in range(10):
        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        # dbTest =

        # print(data)

        for data in dbTest:

            # transform the features of the test instances to numbers following the same strategy done during training,
            # and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            # where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            # --> add your Python code here+

            for k in X:
                class_predicted = clf.predict([k])[0]

            #print(class_predicted)

            # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            # --> add your Python code here
            if class_predicted != data[4]:
                error += 1

    # find the average of this model during the 10 runs (training and test set)
    # --> add your Python code here
    # print(len(X))
    # print (error)

    average = len(X) / error

    # print the average accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    # --> add your Python code here
    print("The final accuracy for", ds, "is", average)
