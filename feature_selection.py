# This code is a part of my Machine learning coursework 

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn import svm

import numpy as np
from sklearn import cross_validation
from math import ceil, floor


fdata = open("data3.csv", "r").readlines()

def execute(fdata):

    data = list()
    target = list()
    storeDict = dict()

    for i, lines in enumerate(fdata):
        sline = lines.split(",")
        target.append(int(sline[0]))
        data.append([float(x) for j, x in enumerate(sline) if j != 0])
        storeDict[i] = [float(x) for j, x in enumerate(sline) if j != 0]

    data = np.array(data)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(data, target, test_size=0.25, random_state=0)
    clf = ExtraTreesClassifier()
    clf = clf.fit(X_train, y_train)
    model = SelectFromModel(clf, prefit=True)
    X_new = model.transform(X_train)

    clfNew = svm.SVC(kernel='linear', C=1).fit(X_new, y_train)

    value_feature = list()
    countDict = dict()
    for key, val in storeDict.items():
        countDict[key] = 0
        for i, inval in enumerate(val):
            if inval in X_new[0]:
                countDict[key] = countDict[key] + 1


    keyName = max(countDict, key=countDict.get)
    posStore = list()
    for val in X_new[0]:
        posStore.append(storeDict[keyName].index(val))

    X_test_new = list()

    for val in X_test:
        inlist = list()
        for i, inval in enumerate(val):
            if i in posStore:
                inlist.append(inval)

        X_test_new.append(inlist)

    X_test_new = np.array(X_test_new)

    return accuracy_score(y_test, clf.predict(X_test)), accuracy_score(y_test, clfNew.predict(X_test_new))



before = list(); after = list()
for i in range(1000):
    print ".",
    try:
        before_val, after_val = execute(fdata)
        before.append(before_val)
        after.append(after_val)
    except ValueError:
        continue


print "\n\nAverage accuracy before feature selection", float(sum(before))/len(before)
print "\nAverage accuracy after feature selection", float(sum(after))/len(after)













#clf = svm.SVC(kernel='linear', C=1).fit(X_new, y_train)#
