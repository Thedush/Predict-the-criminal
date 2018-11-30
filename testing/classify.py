import csv
# with open('criminal_test.csv', 'rb') as csvfile:
#      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#      for row in spamreader:
#         print ', '.join(row)
#         break

# with open('criminal_test.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#          print(row['PERID'], row['IFATHER'])





from sklearn.naive_bayes import GaussianNB

with open('criminal_train.csv', 'r') as fp:
    cl = NaiveBayesClassifier(fp)




