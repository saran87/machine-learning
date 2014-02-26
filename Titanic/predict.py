#The first thing to do is to import the relevant packages
# that I will need for my script, 
#these include the Numpy (for maths and arrays)
#and csv for reading and writing csv files
#If i want to use something from this I need to call 
#csv.[function] or np.[function] first

import csv as csv 
import numpy as np

#Open up the csv file in to a Python object
csv_file_object = csv.reader(open('data/train.csv', 'rb')) 
header = csv_file_object.next()  #The next() command just skips the 
                                 #first line which is a header
data=[]                          #Create a variable called 'data'
for row in csv_file_object:      #Run through each row in the csv file
    data.append(row)             #adding each row to the data variable
data = np.array(data) 	         #Then convert from a list to an array
								 #Be aware that each item is currently
                                 #a string in this format
#The size function counts how many elements are in
#in the array and sum (as you would expects) sums up
#the elements in the array.

number_passengers = np.size(data[0::,0].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
print "number of passengers : " + str(number_passengers)
print "number of survived : " + str(number_survived)
proportion_survivors = number_survived / number_passengers
print "survived % : " + str(proportion_survivors)

women_only_stats = data[0::,4] == "female" #This finds where all 
men_only_stats = data[0::,4] != "female"   #This finds where all the 
                                           #elements do not equal 
                                           #female (I.e. male)

#Using the index from above we select the females and males separately
women_onboard = data[women_only_stats,1].astype(np.float)     
men_onboard = data[men_only_stats,1].astype(np.float)

# Then we finds the proportions of them that survived
proportion_women_survived = \
                       np.sum(women_onboard) / np.size(women_onboard)  
proportion_men_survived = \
                       np.sum(men_onboard) / np.size(men_onboard) 

#and then print it out
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived

test_file_obect = csv.reader(open('data/test.csv', 'rb'))
header = test_file_obect.next()

open_file_object = csv.writer(open("data/genderbasedmodelpy.csv", "wb"))

for row in test_file_obect:       #for each row in test.csv
    if row[3] == 'female':             #is it a female, if yes then
        row.insert(0,'1')              #then Insert the prediction
                                       #of survived,'1' at position 0 
        open_file_object.writerow(row) #and write the row to the
    else:                              #new file else
        row.insert(0,'0')        #insert the prediction of did not 
        open_file_object.writerow(row) #survive (0) and write row 