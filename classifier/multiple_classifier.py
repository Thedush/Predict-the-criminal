import csv
import numpy as np
import pickle
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
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

names = ["DecisionTree","AdaBoost"]

classifiers = [
    DecisionTreeClassifier(criterion='entropy',max_depth=6),
    AdaBoostClassifier(DecisionTreeClassifier(max_depth=2),
                          algorithm="SAMME.R",
                           n_estimators=250)
    ]
with open('criminal_train.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	x1=list()
    	for i in range (0,70):
         	#print(row[rowinlist[i]])
         	x1.append(float(row[rowinlist[i]]))
        x.append(x1)
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

for name, clf in zip(names, classifiers):
        print 'Training started:{}'.format(name)
        clf.fit(x, y)
        #score = clf.score(X_test, y_test)
        print "Training completed"
        prid=list()
        for j in range(0,len(test)):
            x1=[]
            x1.append(test[j])
            predict=clf.predict(x1)
            prid.append(predict)


    #     print prid

        writer = csv.writer(open("{}.csv".format(name), 'w'))
        writer.writerow(["PERID","Criminal"])
        for asd in range (0,len(personid)):
             writer.writerow([personid[asd],int(prid[asd])])

# def add_friend(name, phone, address, birthday):
#     friend = [name, phone, address, birthday]
    

#     writer = csv.writer(open("friends.csv", "ab"), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(friend)
#     return True


