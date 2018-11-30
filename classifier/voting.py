print(__doc__)

from itertools import product

import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import AdaBoostClassifier


rowinlist=['IFATHER','NRCH17_2','IRHHSIZ2','IIHHSIZ2','IRKI17_2','IIKI17_2','IRHH65_2','IIHH65_2','PRXRETRY','PRXYDATA','MEDICARE','CAIDCHIP',
      'CHAMPUS','PRVHLTIN','GRPHLTIN','HLTINNOS','HLCNOTYR','HLCNOTMO','HLCLAST','HLLOSRSN','HLNVCOST','HLNVOFFR','HLNVREF',
      'HLNVNEED','HLNVSOR','IRMCDCHP','IIMCDCHP','IRMEDICR','IIMEDICR','IRCHMPUS','IICHMPUS','IRPRVHLT','IIPRVHLT','IROTHHLT',
      'IIOTHHLT','HLCALLFG','HLCALL99','ANYHLTI2','IRINSUR4','IIINSUR4','OTHINS','CELLNOTCL','CELLWRKNG',
      'IRFAMSOC','IIFAMSOC','IRFAMSSI','IIFAMSSI','IRFSTAMP','IIFSTAMP','IRFAMPMT','IIFAMPMT','IRFAMSVC',
      'IIFAMSVC','IRWELMOS','IIWELMOS','IRPINC3','IRFAMIN3','IIPINC3','IIFAMIN3','GOVTPROG','POVERTY3',
      'TOOLONG','TROUBUND','PDEN10','COUTYP2','MAIIN102','AIIND102','ANALWT_C','VESTR','VEREP']


X=[]
y=[]
with open('criminal_train.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      x1=list()
      for i in range (0,70):
          #print(row[rowinlist[i]])
          x1.append(float(row[rowinlist[i]]))

      X.append(x1)
      y.append(row['Criminal'])
test=[]
personid=[]
with open('criminal_test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        personid.append(int(row['PERID']))
    

with open('criminal_test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        x1=list()
        for i in range (0,70):
            #print(row[rowinlist[i]])
            x1.append(float(row[rowinlist[i]]))
        test.append(x1)
# Loading some example data
#iris = datasets.load_iris()
#X = iris.data[:, [0, 2]]
#y = iris.target

# Training classifiers
clf1 = DecisionTreeClassifier(max_depth=4)
clf2 = KNeighborsClassifier(n_neighbors=7)
clf3 = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2),
                          algorithm="SAMME.R",
                           n_estimators=250)
eclf = VotingClassifier(estimators=[('dt', clf1), ('knn', clf2),
                                    ('svc', clf3)],
                        voting='soft', weights=[2, 1, 2])

print "Training decision"
clf1.fit(X, y)
print "Training knn"
clf2.fit(X, y)
print "Training AdaBoostClassifier"
clf3.fit(X, y)
print "Training voting"
eclf.fit(X, y)

# Plotting decision regions
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

f, axarr = plt.subplots(2, 2, sharex='col', sharey='row', figsize=(10, 8))

for idx, clf, tt in zip(product([0, 1], [0, 1]),
                        [clf1, clf2, clf3, eclf],
                        ['Decision Tree (depth=4)', 'KNN (k=7)',
                         'Kernel SVM', 'Soft Voting']):

    Z = clf.predict(test)
    Z = Z.reshape(xx.shape)

    axarr[idx[0], idx[1]].contourf(xx, yy, Z, alpha=0.4)
    axarr[idx[0], idx[1]].scatter(X[:, 0], X[:, 1], c=y,
                                  s=20, edgecolor='k')
    axarr[idx[0], idx[1]].set_title(tt)

plt.show()
