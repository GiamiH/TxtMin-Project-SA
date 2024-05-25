# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:00:52 2024

@author: marma
"""

import json
import re
import csv

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


#Pattern for names with numbers
numbers = r'\d'


# Removes any review w/ Amz Cus and names with 1 & 2 char
data = []
for r in og:
    s = r["profile_name"]
    if (s != "Amazon customer" and s!= "" and s!="amazonUser" and
            s != "Amazon Customer" and not re.search(numbers,s) and len(s) > 2):
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
# Mr -> male
mr1 = r'\bMr\b'
mr2 = r'\bMR\b'
# Ms -> female
ms = r'\bMiss\s\b'
# Dr -> remove doctor & apply corpus
dr1 = r'\bDr\.\b'
dr2 = r'\bDr\.\s\b'
dr3 = r'\bDR\s\b'
dr4 = r'\bdr\.\s\s\s\b'
# Pattern for @
at = r'/@'

## TEsting new erxpression for miss and mr
# dr.   rachna 
names_w = ["Mr . ANUP KUMAR MISHRA", "Dr.Reddee", "DR SIDDHARTH SAXENA", "Miss Preet", 
               "Dr. Sampat  Kumar R"," Dr.Indrani Debnath"," MR Dhilip",
               "dr.   rachna " ]

for i in names_w:
    if re.search(mr1,i) or re.search(mr2,i):
      #  print("male")
    elif re.search(ms, i) :
       # print("female")
    elif  re.search(dr1, i):
        n = re.sub(dr1, '', i)
        n3 = re.sub(p3, ' ', n).strip()
       # print("WAS A DOC " + n3)
    elif re.search(dr2, i) :
        n = re.sub(dr2, '', i)
        n3 = re.sub(p3, ' ', n).strip()
       # print("WAS A DOC " + n3)
    elif re.search(dr3, i) :
        n = re.sub(dr3, '', i)
        n3 = re.sub(p3, ' ', n).strip()
      #  print("WAS A DOC " + n3)
    elif re.search(dr4, i):
        n = re.sub(dr4, '', i)
        n3 = re.sub(p3, ' ', n).strip()
       # print("WAS A DOC " + n3)
    else:
        #general
        print("not an option")
        




"""
# Apply first name get func to main data and lowercase
# Opens male name csv
file_male = "Indian-Male-Names.csv"
male_n = []
"""
"""
with open(file_male, mode = 'r', newline = '', encoding='latin1') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        full_n = row["name"].split()
        # checks if empty
        if full_n:   
            first_n = full_n[0]
            male_n.append(first_n)
"""

# classifies gender with ms/mr

for r in data:
    prof_name = r["profile_name"]
    if re.search(mr1,prof_name) or re.search(mr2,prof_name):
        r["gender"] = "male"

    elif re.search(ms, prof_name) :
        r["gender"] = "female"
       # print("female")
    elif  re.search(dr1, prof_name):
        n = re.sub(dr1, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
       # print("WAS A DOC " + n3)
    elif re.search(dr2, prof_name) :
        n = re.sub(dr2, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
       # print("WAS A DOC " + n3)
    elif re.search(dr3, prof_name) :
        n = re.sub(dr3, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
      #  print("WAS A DOC " + n3)
    elif re.search(dr4, prof_name):
        n = re.sub(dr4, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
       # print("WAS A DOC " + n3)
    else:
        r["gender"] = "unknown"
        n1 = re.sub(p1, '', prof_name)
        n2 = re.sub(p2, '', n1)
        n3 = re.sub(p3, ' ', n2).strip()
        r["profile_name"] = n3
    
      #  Corpus found is in c so we have to see if there is an adaptable 
       # version of it for python


#First Names
names_list = []
for l in data:
    full = l["profile_name"].split()
    if full:
        name_prof = full[0]
        names_list.append(name_prof)




# Created this file in order to check that all the filtering is done correctly    
file_names = "names.txt"

with open(file_names, 'w', encoding = 'utf-8') as f:
    for l in data:
        p = l["profile_name"]
        f.write(p + "\n")
##############################################################################
# May need to insert this above

"""
per_space = r'\.'
res = re.sub(per_space, ' ', n3 )
print(res)
"""
