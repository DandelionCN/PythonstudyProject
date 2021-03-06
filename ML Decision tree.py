#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sn

# Read the data.
data = np.asarray(pd.read_csv(r'D:\system study\py\data.csv', header=None))
# Assign the features to the variable X, and the labels to the variable y. 

x = data[:,0:2]
y = data[:,2]

#random split the samples into training data set and testing data set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.13, random_state=99)

# TODO: Create the decision tree model and assign it to the variable model.
# You won't need to, but if you'd like, play with hyperparameters such
# as max_depth and min_samples_leaf and see what they do to the decision
# boundary.
model = DecisionTreeClassifier(max_depth=9,min_samples_leaf=4,min_samples_split=7)
model.fit(x_train,y_train)

# TODO: Fit the model.

# TODO: Make predictions. Store them in the variable y_pred.
y_train_pred = model.predict(x_train)
y_test_pred = model.predict(x_test)
    
# TODO: Calculate the accuracy and assign it to the variable acc.
acc_ytrain_ytrainpred = accuracy_score(y_train,y_train_pred)

acc_ytest_ytestpred = accuracy_score(y_test,y_test_pred)

print('acc_ytrain_ytrainpred is: {:.5f}'.format(acc_ytrain_ytrainpred))
print('acc_ytest_ytestpred is: {:.5f}'.format(acc_ytest_ytestpred))

print('acc_ytrain_ytrainpred is: {:.3%}'.format(acc_ytrain_ytrainpred))
print('acc_ytest_ytestpred is: {:.3%}'.format(acc_ytest_ytestpred))

diff=["acc_ytrain_ytrainpred","acc_ytest_ytestpred"]
acc=[acc_ytrain_ytrainpred*100,acc_ytest_ytestpred*100]


plt.bar(diff,acc,width=0.3, align='center')
plt.show()


print("-----------------------------------------------------------------")


"""Count words."""

def count_words(s, n):   
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    s_list=list(s.split(" "))
    s_count={a:s_list.count(a) for a in s_list}
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    s_sorted=sorted(s_count.items(),key = lambda x:x[1],reverse = True)
    # TODO: Return the top n most frequent words.
    top_n=s_sorted[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    inputstring="Please input a sentence with the blank space as the splitation"
    print ("The top{} Frequency words in the sentence are:\n {}".format(4,count_words(inputstring, 4)))
    print("The total income on the year is:{}".format(12500*12+85000))
    
    
if __name__== "__main__"  :
    test_run()

