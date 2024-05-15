# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:00:52 2024

@author: marma
"""

import json
import re

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

# Filters names

# Single char with dot
p1 = r'\b[a-zA-Z]\.\s?'
# Single chars
p2 = r'\b[a-zA-Z]\b'
# Many spaces
p3 = r'\s+'
for r in data:
    prof_name = r["profile_name"]
    print(prof_name)
    n1 = re.sub(p1, '', prof_name)
    n2 = re.sub(p2, '', n1)
    n3 = re.sub(p3, ' ', n2).strip()
    r["profile_name"] = n3
    print(r["profile_name"])

##############################################################################
# Differentiate Dr. Mr. Ms. Mrs. w/regexp
t = "J.musthafa"
mr = r'\bMr\.\b'
ms = r'\bMs\.\b'
mrs = r'\bMrs\.\b'

if re.search(mr, t):
    t = "male"
if re.search(ms, t):
    t = "female"
if re.search(mrs, t):
    t = "female"

# Replace any periods with a space
per_space = r'\.'
res = re.sub(per_space, ' ', t)
print(res)

#Doctor
dr = r'\bDr\.\b'



per_space = r'\.'
res = re.sub(per_space, ' ', t)
print(res)
##############################################################################


"""
# Testing with strings to identify names via 
split_4= list("sam a.asdam.")
print(split_4)   

c = 0
pre = ""
p=0

for i in split_4:
        if i == " ":
            c=0
            pre=""
        elif i.isalpha():
            c +=1
            pre+=i
        elif i == ".":
            p +=1
        elif c==2:
            for indx in range(0,c+p):
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
         


"""
