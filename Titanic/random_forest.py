#The first thing to do is to import the relevant packages
# that I will need for my script, 
#these include the Numpy (for maths and arrays)
#and csv for reading and writing csv files
#If i want to use something from this I need to call 
#csv.[function] or np.[function] first

import csv as csv 
import numpy as np
# Import the random forest package
from sklearn.ensemble import RandomForestClassifier 


#Open up the csv file in to a Python object
csv_file_object = csv.reader(open('data/train.csv', 'rb')) 
header = csv_file_object.next()  #The next() command just skips the 
                                 #first line which is a header
train_data=[]                          #Create a variable called 'data'
for row in csv_file_object:      #Run through each row in the csv file
    train_data.append(row)             #adding each row to the data variable
train_data = np.array(train_data) 	         #Then convert from a list to an array

#I need to convert all strings to integer classifiers:
#Male = 1, female = 0:
train_data[train_data[0::,4]=='male',4] = 1
train_data[train_data[0::,4]=='female',4] = 0
#embark c=0, s=1, q=2
train_data[train_data[0::,11] =='C',11] = 0
train_data[train_data[0::,11] =='S',11] = 1
train_data[train_data[0::,11] =='Q',11] = 2

#I need to fill in the gaps of the data and make it complete.
#So where there is no price, I will assume price on median of that class
#Where there is no age I will give median of all ages

#All the ages with no data make the median of the data
train_data[train_data[0::,5] == '',5] = np.median(train_data[train_data[0::,5]\
                                           != '',5].astype(np.float))
#All missing ebmbarks just make them embark from most common place
train_data[train_data[0::,11] == '',11] = np.round(np.mean(train_data[train_data[0::,11]\
                                                   != '',11].astype(np.float)))
train_data = np.delete(train_data,[0,3,8,10],1) #remove the name data, cabin and ticket
#I need to do the same with the test data now so that the columns are in the same
#as the training data

# Create the random forest object which will include all the parameters
# for the fit
Forest = RandomForestClassifier(n_estimators = 100)
print "Training ...."
# Fit the training data to the training output and create the decision
# trees
Forest = Forest.fit(train_data[0::,1::],train_data[0::,0])

#Open the test file object
test_file_obect = csv.reader(open('data/test.csv', 'rb'))
header = test_file_obect.next()
test_data = []
ids = []
for row in test_file_obect:
		ids.append(row[0])
		test_data.append(row)
test_data = np.array(test_data)

#I need to convert all strings to integer classifiers:
#Male = 1, female = 0:
test_data[test_data[0::,3]=='male',3] = 1
test_data[test_data[0::,3]=='female',3] = 0
#ebark c=0, s=1, q=2
test_data[test_data[0::,10] =='C',10] = 0 #Note this is not ideal, in more complex 3 is not 3 tmes better than 1 than 2 is 2 times better than 1
test_data[test_data[0::,10] =='S',10] = 1
test_data[test_data[0::,10] =='Q',10] = 2

#All the ages with no data make the median of the data
test_data[test_data[0::,4] == '',4] = np.median(test_data[test_data[0::,4]\
                                           != '',4].astype(np.float))
#All missing ebmbarks just make them embark from most common place
test_data[test_data[0::,10] == '',10] = np.round(np.mean(test_data[test_data[0::,10]\
                                                   != '',10].astype(np.float)))
#All the missing prices assume median of their respectice class
for i in xrange(np.size(test_data[0::,0])):
    if test_data[i,8] == '':
        test_data[i,8] = np.median(test_data[(test_data[0::,8] != '') &\
                                             (test_data[0::,1] == test_data[i,1])\
            ,8].astype(np.float))

test_data = np.delete(test_data,[0,2,7,9],1) #remove the name data, cabin and ticket

print "Predicting ...."
# Take the same decision trees and run on the test data
Output = Forest.predict(test_data)

print str(np.size(Output.astype(np.float))) + " " +  str( np.sum(Output.astype(np.float)))

open_file_object = csv.writer(open("data/randomforest.csv", "wb"))
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, Output))
