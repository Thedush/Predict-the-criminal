from sklearn import svm
from sklearn import tree
import csv
import numpy as np
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
import math
rowinlist=['IFATHER','NRCH17_2','IRHHSIZ2','IIHHSIZ2','IRKI17_2','IIKI17_2','IRHH65_2','IIHH65_2','PRXRETRY','PRXYDATA','MEDICARE','CAIDCHIP',
			'CHAMPUS','PRVHLTIN','GRPHLTIN','HLTINNOS','HLCNOTYR','HLCNOTMO','HLCLAST','HLLOSRSN','HLNVCOST','HLNVOFFR','HLNVREF',
			'HLNVNEED','HLNVSOR','IRMCDCHP','IIMCDCHP','IRMEDICR','IIMEDICR','IRCHMPUS','IICHMPUS','IRPRVHLT','IIPRVHLT','IROTHHLT',
			'IIOTHHLT','HLCALLFG','HLCALL99','ANYHLTI2','IRINSUR4','IIINSUR4','OTHINS','CELLNOTCL','CELLWRKNG',
			'IRFAMSOC','IIFAMSOC','IRFAMSSI','IIFAMSSI','IRFSTAMP','IIFSTAMP','IRFAMPMT','IIFAMPMT','IRFAMSVC',
			'IIFAMSVC','IRWELMOS','IIWELMOS','IRPINC3','IRFAMIN3','IIPINC3','IIFAMIN3','GOVTPROG','POVERTY3',
			'TOOLONG','TROUBUND','PDEN10','COUTYP2','MAIIN102','AIIND102','ANALWT_C','VESTR','VEREP']


x=[]
y=[]
# j=0
with open('criminal_train.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	x1=list()
    	for i in range (0,70):
         	#print(row[rowinlist[i]])
         	x1.append(float(row[rowinlist[i]]))
        x.append(x1)
        y.append(row['Criminal'])
print "Decision tree Training started"          
        
#clf = RandomForestClassifier(max_depth=2, random_state=0)
# clf =AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
#                          algorithm="SAMME",
#                           n_estimators=200)
clf = KNeighborsClassifier(n_neighbors=2)
#clf = tree.DecisionTreeClassifier()

clf.fit(x, y)

print "Training completed"
'''
# model_save_path='trained_criminal_tree_model.clf'
# if model_save_path is not None:
#         with open(model_save_path, 'wb') as f:
#             pickle.dump(clf, f)

# from sklearn import neighbors
# n_neighbors = int(round(math.sqrt(len(x))))
# print("Chose n_neighbors automatically:", n_neighbors)
# knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm='ball_tree', weights='distance')
# knn_clf.fit(x, y)
# print "Training completed"
# model_save_path='trained_criminal_knn_model.clf'
# if model_save_path is not None:
#         with open(model_save_path, 'wb') as f:
#             pickle.dump(knn_clf, f)

naive=pickle.load(open('trained_criminal_bayes_model.clf', 'rb'))
svm=pickle.load(open('trained_criminal_svm_model.clf', 'rb'))
decision_tree=pickle.load(open('trained_criminal_tree_model.clf', 'rb'))
knn=pickle.load(open('trained_criminal_knn_model.clf', 'rb'))
'''
x=[]

with open('criminal_test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

    	x1=list()
    	for i in range (0,70):
         	#print(row[rowinlist[i]])
         	x1.append(float(row[rowinlist[i]]))
        x.append(x1)
print "pridiction start"
prid=list()
for j in range(0,len(x)):
    x1=[]
    x1.append(x[j])
    predict=clf.predict(x1)
    prid.append(predict)


    #     print prid
writer = csv.writer(open("RandomForestClassifier.csv", 'w'))
for row in prid:
     writer.writerow(row)

# with open('criminal_test.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#     	x=[]
    	
#     	for i in range (0,71):
#          	#print(row[rowinlist[i]])
#          	x.append(row[rowinlist[i]])
#         pridict=clf.predict(x)
#         print predict

        
