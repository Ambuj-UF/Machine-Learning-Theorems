from sklearn import tree
from sklearn import neighbors
from sklearn.datasets import load_iris

fdata = open("data.csv", "r").readlines()



def decision_tree(accuracy, init, end):
    target = list()
    data = list()

    target_test = list()
    data_test = list()
    for i, line in enumerate(fdata):
        if i != 0:
            sline = [float(x) for x in line.strip().split(",")]
            if i > init and i <= end:
                target.append(sline[-1])
                data.append(sline[:-1])
            else:
                target_test.append(sline[-1])
                data_test.append(sline[:-1])


    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(data, target)

    output = clf.predict(data_test)

    count = 0

    tn = 0; tp = 0; fp = 0
    for x, y in zip(output, target_test):
        if float(x) == float(y):
            count = count + 1
            if float(x) == 1.0:
                tp = tp + 1
            if float(x) == 0.0:
                tn = tn + 1
        else:
            if float(x) == 1.0:
                fp = fp + 1

    return float(count)/67, float(tn)/(fp+tn), float(tp)/(tp+fp)

save_best_values = list()
accuracy = 0
store_acc = 0
for num in range(267):
    """Perform decision tree crossvalidation"""
    
    init = num
    end = init + 199
    if end > 267:
        break
    accuracy, specificity, precision = decision_tree(accuracy, init, end)

    if accuracy > store_acc:
        store_acc = accuracy
        save_best_values = [init, end, accuracy, specificity, precision]




print "Best training data range after cross validation->", save_best_values[0], "-", save_best_values[1]
print "Decision Tree Accuracy->", save_best_values[2]
print "Decision Tree Specificity->", save_best_values[3]
print "Decision Tree Precision->", save_best_values[4]



def knn_run(accuracy, init, end):
    target = list()
    data = list()
    
    target_test = list()
    data_test = list()
    for i, line in enumerate(fdata):
        if i != 0:
            sline = [float(x) for x in line.strip().split(",")]
            if i > init and i <= end:
                target.append(sline[-1])
                data.append(sline[:-1])
            else:
                target_test.append(sline[-1])
                data_test.append(sline[:-1])

    knn = neighbors.KNeighborsClassifier(n_neighbors=1)
    knn.fit(data, target)

    output_knn = knn.predict(data_test)

    count = 0
    tn = 0; tp = 0; fp = 0
    for x, y in zip(output_knn, target_test):
        if float(x) == float(y):
            count = count + 1
            if float(x) == 1.0:
                tp = tp + 1
            if float(x) == 0.0:
                tn = tn + 1
        else:
            if float(x) == 1.0:
                fp = fp + 1

    return float(count)/67, float(tn)/(fp+tn), float(tp)/(tp+fp)


save_best_values = list()
accuracy = 0
store_acc = 0
for num in range(267):
    """Perform knn tree crossvalidation"""
    
    init = num
    end = init + 199
    if end > 267:
        break
    accuracy, specificity, precision = knn_run(accuracy, init, end)
    if accuracy > store_acc:
        store_acc = accuracy
        save_best_values = [init, end, accuracy, specificity, precision]




print "Best training data range after cross validation->", save_best_values[0], "-", save_best_values[1]
print "KNN Accuracy->", save_best_values[2]
print "KNN Specificity->", save_best_values[3]
print "KNN Precision->", save_best_values[4]



