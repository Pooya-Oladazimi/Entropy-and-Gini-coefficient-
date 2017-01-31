# -*- coding: utf-8 -*-
#! /usr/bin/python3

import matplotlib.pyplot as plt
import random
import numpy as np
import math


def Gini_coefficient(tables,guests):
    
    S = len(tables)
    table_shared = {} #{table:table-shared value}

    for table in tables:
        table_shared[table] = tables[table] / guests
    
    denom = 0        
    for table in table_shared:
        denom += table_shared[table]
    
    denom = denom / S
    denom = 2 * denom
    
    tmp = 0
    Gini_coe = 0        
    for i in table_shared:
        for j in table_shared:
           tmp += abs(table_shared[i] - table_shared[j])
    
    tmp = tmp / (math.pow(S,2))
    Gini_coe = tmp / denom
    
    return Gini_coe
    

#end***************************************************************************

def draw_Gini(List1,List2,List3,List4,List5):
    
    x = len(List1) * [0]
    for i in range(0,len(x)):
        x[i] = i+1
        

    plt.xticks(np.arange(0,1001,100))
    plt.ylim(0,1)
    plt.title("Gini Coeficient plot")
    plt.xlabel("Subjects")
    plt.ylabel("Gini Coefficient")

    plt.plot(x,List1,label='simulation1',color="b")
    plt.plot(x,List2,label='simulation2',color="r")
    plt.plot(x,List3,label='simulation3',color="g")
    plt.plot(x,List4,label='simulation4',color="y")
    plt.plot(x,List5,label='simulation5',color="k")
    plt.legend(loc=0,fontsize='small')
    plt.show()


#end***************************************************************************

def sitting_at_tables(Customers_num):
    
    tables = {} #{table:number of guests}    
    All_Gini_coe = 1000 * [0]
    tables[1] = 1        
    Number_of_tables = 1
    Number_of_all_guests = 1    
    re = Gini_coefficient(tables,Number_of_all_guests)    
    All_Gini_coe[Number_of_all_guests-1] = re
    
    for i in range(2,Customers_num+1):
        
        Number_of_all_guests += 1
        found = 0
        rand = random.random()            
        for table in tables:
            
            prob = tables[table] / Number_of_all_guests
            if rand < prob:
                tables[table] += 1
                found = 1
                re = Gini_coefficient(tables,Number_of_all_guests)
                All_Gini_coe[Number_of_all_guests-1] = re
                break
            
        if found == 0:
            Number_of_tables += 1
            tables[Number_of_tables] = 1
            re = Gini_coefficient(tables,Number_of_all_guests)
            All_Gini_coe[Number_of_all_guests-1] = re
        
                            
    return All_Gini_coe

#end***************************************************************************

#start

Customers_num = 1000

print("Simulating1... ")
All_Gini_coes1 = sitting_at_tables(Customers_num)
print("Simulating2... ")
All_Gini_coes2 = sitting_at_tables(Customers_num)
print("Simulating3... ")
All_Gini_coes3 = sitting_at_tables(Customers_num)
print("Simulating4... ")
All_Gini_coes4 = sitting_at_tables(Customers_num)
print("Simulating5... ")
All_Gini_coes5 = sitting_at_tables(Customers_num)

draw_Gini(All_Gini_coes1,All_Gini_coes2,All_Gini_coes3,All_Gini_coes4,All_Gini_coes5)

