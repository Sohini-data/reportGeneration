# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 10:50:57 2019

@author: LENOVO
"""

import pandas as pd
import numpy as np
import csv
import datetime as dt
import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('ExpenseDemo.csv')

print data.head(10)

sortedData = data.sort_values(['CreateDate'])

def getdaysleft(row):
    commitData = dt.datetime.strptime(row['CommitDate'],'%d-%m-%Y')
    jobstartdate = dt.datetime.strptime(row['JobStartDate'],'%d-%m-%Y')
    dayLeft = commitData - jobstartdate
    return dayLeft.days

sortedData['daysLeft']=sortedData.apply(getdaysleft, axis=1)

def convertstr(row):
    return str(row['ProjectId'])

sortedData['ProjectIdNew']=sortedData.apply(convertstr,axis=1)


t = np.arange(sortedData.shape[0])
sortedData['BudgetAmount']=sortedData.BudgetAmount.astype(int)
sortedData['ExpenseAmount']=sortedData.ExpenseAmount.astype(int)
sortedData['RecievedAmount']=sortedData.RecievedAmount.astype(int)
sortedData['ProjectAmount']=sortedData.ProjectAmount.astype(int)
sortedData['daysLeft']=sortedData.daysLeft.astype(int)


'''
color = 'tab:red'
ax1.set_ylabel('Amount', color=color)
ax1.plot(t,sortedData['BudgetAmount'].tolist())
ax1.plot(t,sortedData['ExpenseAmount'].tolist())
ax1.plot(t,sortedData['RecievedAmount'].tolist())
ax1.plot(t,sortedData['ProjectAmount'].tolist())
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('days left', color=color) 
ax1.plot(t,sortedData['daysLeft'].tolist(),5,50)
ax2.tick_params(axis='y', labelcolor=color)

'''

ax = sortedData.plot(x="ProjectId", y=["ExpenseAmount","RecievedAmount"], legend=False)
#ax = sortedData.plot(x="ProjectId", y="ExpenseAmount", legend=False)
#ax = sortedData.plot(x="ProjectId", y="RecievedAmount", legend=False)
#ax = sortedData.plot(x="ProjectId", y="ProjectAmount", legend=False)
ax2 = ax.twinx()
sortedData.plot(x="ProjectId", y="daysLeft", ax=ax2, legend=False, color="black")
ax.set_ylabel(r"Amount In INR")
ax2.set_ylabel(r"Days left")
ax.legend()
ax2.legend()
plt.show()













