
import pickle

import csv
# x=pickle.load(open('xdata', 'rb'))
# y=pickle.load(open('ydata', 'rb'))
svm=pickle.load(open('trained_criminal_svm_model.clf', 'rb'))
decision_tree=pickle.load(open('trained_criminal_tree_model.clf', 'rb'))
rowinlist=['PERID','IFATHER','NRCH17_2','IRHHSIZ2','IIHHSIZ2','IRKI17_2','IIKI17_2','IRHH65_2','IIHH65_2','PRXRETRY','PRXYDATA','MEDICARE','CAIDCHIP',
			'CHAMPUS','PRVHLTIN','GRPHLTIN','HLTINNOS','HLCNOTYR','HLCNOTMO','HLCLAST','HLLOSRSN','HLNVCOST','HLNVOFFR','HLNVREF',
			'HLNVNEED','HLNVSOR','IRMCDCHP','IIMCDCHP','IRMEDICR','IIMEDICR','IRCHMPUS','IICHMPUS','IRPRVHLT','IIPRVHLT','IROTHHLT',
			'IIOTHHLT','HLCALLFG','HLCALL99','ANYHLTI2','IRINSUR4','IIINSUR4','OTHINS','CELLNOTCL','CELLWRKNG',
			'IRFAMSOC','IIFAMSOC','IRFAMSSI','IIFAMSSI','IRFSTAMP','IIFSTAMP','IRFAMPMT','IIFAMPMT','IRFAMSVC',
			'IIFAMSVC','IRWELMOS','IIWELMOS','IRPINC3','IRFAMIN3','IIPINC3','IIFAMIN3','GOVTPROG','POVERTY3',
			'TOOLONG','TROUBUND','PDEN10','COUTYP2','MAIIN102','AIIND102','ANALWT_C','VESTR','VEREP']
x=[]
j=0
with open('criminal_test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

    	x1=list()
    	for i in range (0,71):
         	#print(row[rowinlist[i]])
         	x1.append(row[rowinlist[i]])
        x.append(x1)
print "pridiction start"
pridict=svm.predict(x)
print pridict
# for j in range(0,2):
# 	x1=[]
# 	x1.append(x[j])
# 	pridict=svm.predict(x1)
# 	print x[j][0],pridict,x1
#   	      	