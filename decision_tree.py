#-------------------------------------------------------------------------
# AUTHOR: Ryan Phan
# FILENAME: decision_tree.py
# SPECIFICATION: Makes a decision tree for a given csv file
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         #print(row)

X = [row[:] for row in db]
Y = [row[-1] for row in db]

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
length = len(X)
for i in range(length):
    for j in range(4):
        if db[i][j] == 'Young':
            X[i][j] = 1
        elif db[i][j] == 'Prepresbyopic':
            X[i][j] = 2
        elif db[i][j] == 'Presbyopic':
            X[i][j] = 3
        elif db[i][j] == 'Myope':
            X[i][j] = 1
        elif db[i][j] == 'Hypermetrope':
            X[i][j] = 2
        elif db[i][j] == 'No':
            X[i][j] = 1
        elif db[i][j] == 'Yes':
            X[i][j] = 2
        elif db[i][j] == 'Reduced':
            X[i][j] = 1
        elif db[i][j] == 'Normal':
            X[i][j] = 2
for i in X:
    del i[-1]

# X = [[1, 1, 1, 1], [3, 1, 1, 2], [2, 1, 1, 1], [2, 1, 1, 2], [3, 1, 2, 2], [1, 1, 2, 2], [1, 2, 1, 1], [2, 1, 2, 1], [3, 2, 1, 1], [1, 1, 2, 1]]

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
length = len(Y)
for i in range(length):
    if Y[i] == 'No':
        Y[i] = 1
    else:
        Y[i] = 2

# Y = [1, 1, 1, 2, 2, 2, 1, 1, 1, 2]

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()