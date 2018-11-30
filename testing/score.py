from sklearn import svm
from sklearn import tree
import csv
import numpy as np
import pickle
from sklearn.naive_bayes import GaussianNB

rowinlist=['IFATHER','NRCH17_2','IRHHSIZ2','IIHHSIZ2','IRKI17_2','IIKI17_2','IRHH65_2','IIHH65_2','PRXRETRY','PRXYDATA','MEDICARE','CAIDCHIP',
			'CHAMPUS','PRVHLTIN','GRPHLTIN','HLTINNOS','HLCNOTYR','HLCNOTMO','HLCLAST','HLLOSRSN','HLNVCOST','HLNVOFFR','HLNVREF',
			'HLNVNEED','HLNVSOR','IRMCDCHP','IIMCDCHP','IRMEDICR','IIMEDICR','IRCHMPUS','IICHMPUS','IRPRVHLT','IIPRVHLT','IROTHHLT',
			'IIOTHHLT','HLCALLFG','HLCALL99','ANYHLTI2','IRINSUR4','IIINSUR4','OTHINS','CELLNOTCL','CELLWRKNG',
			'IRFAMSOC','IIFAMSOC','IRFAMSSI','IIFAMSSI','IRFSTAMP','IIFSTAMP','IRFAMPMT','IIFAMPMT','IRFAMSVC',
			'IIFAMSVC','IRWELMOS','IIWELMOS','IRPINC3','IRFAMIN3','IIPINC3','IIFAMIN3','GOVTPROG','POVERTY3',
			'TOOLONG','TROUBUND','PDEN10','COUTYP2','MAIIN102','AIIND102','ANALWT_C','VESTR','VEREP']

# with open('criminal_test.csv', 'rb') as csvfile:
#      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#      for row in spamreader:
#      	# print row
#       #   print alist.join(row)
        
#       #   print (alist)
#         row1= next(row)
#         print row1
#         break

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
        # j=j+1
        # print j
        # print x
        # print y
        # if j>=2:
        # 	break
# print x[0],x[1],x[2],x[3]
# print y[0],y[1],y[2],y[3]
training_x=x[:42000]
testing_x=x[42000:]
training_y=y[:42000]
testing_y=y[42000:]

# with open('xdata', 'wb') as f:
#         pickle.dump(x, f)  
# with open('ydata', 'wb') as f:
#         pickle.dump(y, f) 

print "Training naive_bayes training started" 
clf = GaussianNB()
clf.fit(training_x, training_y)
print "Training completed"
model_save_path='trained_criminal_bayes_model1.clf'
if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(clf, f)

'''
print "Training svm training started"       	
clf = svm.SVC(kernel='rbf',C=1000)
clf.fit(x, y)
print "Training completed"
model_save_path='trained_criminal_svm_model.clf'
if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(clf, f)
'''
print "Decision tree Training started"       	
clf = tree.DecisionTreeClassifier()
clf.fit(training_x, training_y)
print "Training completed"
model_save_path='trained_criminal_tree_model1.clf'
if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(clf, f)

naive=pickle.load(open('trained_criminal_bayes_model.clf', 'rb'))
#svm=pickle.load(open('trained_criminal_svm_model.clf', 'rb'))
decision_tree=pickle.load(open('trained_criminal_tree_model.clf', 'rb'))


# pridict=naive.predict(testing)
# #pridict=svm.predict(testing)
# pridict=decision_tree.predict(testing)


accuracy =naive.score(testing_x, testing_y)
print accuracy
accuracy =decision_tree.score(testing_x, testing_y)
print accuracy


# x=[]

# with open('criminal_test.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:

#     	x1=list()
#     	for i in range (0,70):
#          	#print(row[rowinlist[i]])
#          	x1.append(float(row[rowinlist[i]]))
#         x.append(x1)
# print "pridiction start"
# prid=list()
# for j in range(0,len(x)):
# 	x1=[]
# 	x1.append(x[j])
# 	pridict=naive.predict(x1)

#     print prid
# writer = csv.writer(open("submit.csv", 'w'))
# for row in pridict:
#     writer.writerow(row)

# with open('criminal_test.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#     	x=[]
    	
#     	for i in range (0,71):
#          	#print(row[rowinlist[i]])
#          	x.append(row[rowinlist[i]])
#         pridict=clf.predict(x)
#         print predict

        
