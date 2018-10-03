In this program what we are trying to figure out is the drivers who are trying to speed.

In order to do this we are trying to minimize the false alarms and false negatives. 
Now as we do not want to cause inconvenience to the drivers we are penalizing false alarms so the cost function we use is 3*false_alarms + false_negatives.

Using this cost function we can find the best threshold value of the speed which we can set as a limit above which we consider the drivers to be speeding.

Now also in order to evaluate the classifier an ROC curve(true positive rate vs false positive rate) is also plotted.

In the plot we can see the best cost function values

