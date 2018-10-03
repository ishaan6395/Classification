"""
Author: Ishaan Thakker
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import operator
import math
import matplotlib.pyplot as plt

def main():
    speed = []
    want_to = []
    speed_wantTo = {}
    binsize = 1
    wrong_values = []
    threshold_values = []
	#Reading the data form the csv file
    with open('vehicle_data_v2181.csv') as file:
        reader = csv.reader(file, delimiter=',')
        line = 0
        for value in reader:
            if line>0:
		# appending the round value as required
                speed.append(round(float(value[0])))
                want_to.append(round(float(value[4])))
            else:
                line+=1
    ind =0
    best_missclass_rate = math.inf

    min_threshold = math.floor(min(speed))
    max_threshold = math.ceil(max(speed))
	
	#making a list of all possible thresholds
    thresholds = [i for i in range(min_threshold,max_threshold+1)]
    best_threshold = 0

    ind = 0
    falsemin = 0
    truemin = 0
    test = []
    test1 = []
    len1 = 0
    len2 = 0
	
	#this will compute the best threshold out of all the available thresholds in the list
    for i in thresholds:
	#getting the list of false alarms and misses for the respective threshold
        n_miss = [speed[j] for j in range(0,len(speed)) if (speed[j]<i) and want_to[j]==1]
        n_fa = [speed[j] for j in range(0,len(speed)) if (speed[j]>=i) and want_to[j]==0]
	#getting the list of false positives and true positives for respective thresholds  
	      
        falsepositive =[speed[j] for j in range(0,len(speed)) if speed[j]>=i and want_to[j] == 0]
        truepositive = [speed[j] for j in range(0,len(speed)) if speed[j]>=i and want_to[j] == 1]
	
	# COmputing the cost function        
        wrong = len(n_miss) + len(n_fa)*3
        wrong_values.append(wrong)
        threshold_values.append(i)
	
	# appending the true positive rate and false positive rate in a list for ROC curve
        test.append(len(falsepositive)/len([i for i in want_to if i==0]) )
        test1.append(len(truepositive) / len([i for i in want_to if i==1]))
	
	# Condition for getting the best threshold.
        if wrong <= best_missclass_rate:
            len1 = len(n_miss)
            len2 = len(n_fa)
            best_missclass_rate = wrong
            best_threshold = i
            falsemin = len(falsepositive)/len([i for i in want_to if i==0])
            truemin = len(truepositive) / len([i for i in want_to if i==1])

	
    miss_list = len([speed[j] for j in range(0,len(speed)) if (speed[j]<best_threshold) and want_to[j]==1])
    falsealarm_list = len([speed[j] for j in range(0,len(speed)) if (speed[j]>=best_threshold) and want_to[j]==0])

	#print the number of false alarms and number of aggressive drivers not caught
    print("Number of misses: "+str(miss_list))
    print("Number of false alarms: "+str(falsealarm_list))
    print("Minimum Threshold: "+str(best_threshold))
    threshold_values = np.array(threshold_values)
    wrong_values = np.array(wrong_values)
	
	#Plot the ROC Curve
    plt.figure(figsize = [20,10])
    plt.subplot(2,2,1)
    plt.plot(test, test1, marker='o')
    plt.plot(falsemin,truemin,'g*', color='r')
    plt.text(falsemin, truemin, 'Lowest Cost Function = ('+str(round(falsemin,2))+','+str(round(truemin,2))+')', rotation = 45,color='b')
    plt.xlabel('False Positive')
    plt.ylabel('True Positive')
    plt.title('ROC Curve')

	# Plotting threshold values against the cost function(name of the list if wrong_values)
    plt.subplot(2,2,2)
    plt.plot(threshold_values,wrong_values, marker='o')
    plt.xlabel('Threshold Values')
    plt.ylabel('Values of Cost Function')
    plt.title('Plotting threshold values against the cost function')
    plt.show()


if __name__=='__main__':
    main()
