# -*- coding: utf-8 -*-
#! /usr/bin/python3

import numpy as np
import time
import matplotlib.pyplot as plt
import math
import operator




def draw_plot(user_entropy,system_entropy):
    
    i = 0
    x = len(user_entropy) * [0]
    while i < len(x):
        x[i] = i+1
        i += 1
    
    Y1 = len(user_entropy) * [0]
    Y2 = len(system_entropy) * [0]
    
    i = 0
    while i < len(Y1):
        Y1[i] = user_entropy[i][1]
        Y2[i] = system_entropy[i][1]
        i += 1
    
    plt.xticks(np.arange(0,max(x),40))
    plt.yticks(range(0,int(max(Y2)+2)))
    plt.title("Sorted System Entropy and user Entropy (Average) per day")
    plt.xlabel("Days Rank (base on Entropy)")
    plt.ylabel("Entropy")

    plt.scatter(x,Y1,label='User Entropy',color="r")
    plt.scatter(x,Y2,label='System Entropy',color="b") 
    plt.legend(loc=2)
    plt.show()
    



#end***************************************************************************

def users_Entropy(Days,users_total_post):
    Average_entropy_per_day = {} #{day:Average}

    for day in Days:
        Average = 0
        for user in Days[day]:
            Len = users_total_post[day][user]
            S = 0
            for tag in Days[day][user]:
                
                f = Days[day][user][tag] / Len
                tmp = math.log2(f)
                tmp = f * tmp
                S = S + tmp
            S = -1 * S
            Average += (S / len(Days[day]) )
        
        Average_entropy_per_day[day] = Average
    
    
    Average_entropy_per_day = sorted(Average_entropy_per_day.items(), key=operator.itemgetter(1))
    return Average_entropy_per_day




#end***************************************************************************

def system_Entropy(Tag_per_day,Tag_number_per_day):
    
    Entropy_per_day = {} #{day:average}
    
    for day in Tag_per_day:
        S = 0
        for tag in Tag_number_per_day[day]:
            
            N = Tag_per_day[day]
            f = Tags_number_per_day[day][tag] / N
            tmp = math.log2(f)
            tmp = f * tmp
            S += tmp
            
        S = -1 * S
        Entropy_per_day[day] = S        
    
    
    Entropy_per_day = sorted(Entropy_per_day.items(), key=operator.itemgetter(1))

    return Entropy_per_day
#end***************************************************************************


#start
start = time.time()

file = open("onlyhash.data",'r')
Days = {} #{day:user}
User = {} #{user:meme}
Tag = {} #{meme:count}
users_total_post = {} #{day:user:count of posts}
count = {}
Tags_per_day = {} #{day:count}
Tags_number_per_day = {} #{day:tag:count}
Tag_count = {} #{tag:count}

line = file.readline()

while line:
    tmp = line.split()
    username = tmp[0]
    date = tmp[1]
    tag = tmp[2:]

    if date not in Days:
        Tags_per_day[date] = 0
        for t in tag:
            Tag[t] = 1
            Tag_count[t] = 1
            Tags_per_day[date] += 1
            
        User = {username:Tag}
        Days[date] = User
        users_total_post[date] = {username:1}
        Tags_number_per_day[date] = Tag_count
        Tag_count = {}
        Tag = {}
        User = {}
        
    else:
        if username in Days[date]:
            users_total_post[date][username] += 1
            for t in tag:
                Tags_per_day[date] += 1
                if t in Tags_number_per_day[date]:
                    Tags_number_per_day[date][t] += 1
                else:
                    Tags_number_per_day[date][t] = 1
                    
                    
                if t in Days[date][username]:
                    Days[date][username][t] += 1
                else:
                    Days[date][username][t] = 1
        else:
            
            for t in tag:
                Tag[t] = 1
                Tags_per_day[date] += 1
                if t in Tags_number_per_day[date]:
                    Tags_number_per_day[date][t] += 1
                else:
                    Tags_number_per_day[date][t] = 1
                
                
            users_total_post[date][username] = 1
            Days[date][username] = Tag
            Tag = {}
            
    
    line = file.readline()

file.close()

User_Entropy_per_day = users_Entropy(Days,users_total_post)
system_Entropy_per_day = system_Entropy(Tags_per_day,Tags_number_per_day)

draw_plot(User_Entropy_per_day,system_Entropy_per_day)


print("Run time : ",str(time.time()-start))






