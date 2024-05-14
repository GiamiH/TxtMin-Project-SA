# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:00:52 2024

@author: marma
"""

import json

# open file
with open('Iphone11-R.json', 'r') as file:
    og = json.load(file)

# deletes useless col
for r in og:
    del r["product_company"]
    del r["product"]
    del r["review_country"]
    del r["total_comments"]
    del r["reviewed_at"]
    del r["url"]


# simplifies start to a single int (1 - 5)
for r in og:
    s = r["review_rating"]
    r["review_rating"] = int(s[0])


# Removes any review w/ Amz Cus and names with 1 & 2 char
data = []
for r in og:
    s = r["profile_name"]
    if (s != "Amazon customer" and
        s != "Amazon Customer" and not s[0].isdigit() and len(s) > 2):
        data.append(r)

# Helpful Count is an int
for r in data:   
    s = r["helpful_count"]
    if s[0] == "O":
        r["helpful_count"] = 1
    else:
        n = ""
        for d in s:
            if (d.isdigit()):
                n += d
        r["helpful_count"] = int(n)
        
        s = r["helpful_count"]
        
# Take first names (Clear out Mr./Ms. and Dr.)
for r in data:
    prof_name = r["profile_name"]
    split_name = list(prof_name)
    c = 0
    for i in split_name:
        if i.isalpha():
            c +=1
        else:
            break
    
# Testing with strings to identify namesvia prefix
    
split_4= list("Dr.dasdf")
print(split_4)   

c = 1
pre = ""
for i in split_4:
        if i.isalpha():
            c +=1
            pre+=i
        elif c==2:
            for indx in range(0,c):
                del split_4[0]
        elif pre == "Mr":
                print("Male")
        elif pre == "Dr":
            for indx in range(0,c):
                del split_4[0]
            print("delete :(")
        elif(pre == "Ms"):
                print("Female")
        elif(pre == "Mrs"):
                print("Female")
        else:
            print("Its a string of 3 char")
            
                

print(split_4)   
