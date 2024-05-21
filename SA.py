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
    if (s != "Amazon customer" and s!= "" and s!="amazonUser" and
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
# Mr -> male
mr = r'\bMr\.\b'
# Ms -> female
ms = r'\bMs\.\b'
# Mrs -> female
mrs = r'\bMrs\.\b'
# Dr -> remove doctor & apply corpus
dr = r'\bDr\.\b'


# classifies gender with ms/mr
for r in data:
    prof_name = r["profile_name"]
    
    if re.search(mr,prof_name):
        gender = "male"
    elif re.search(ms, prof_name) or re.search(mrs, prof_name):
        gender = "female"
    else:
        n = re.sub(dr, '', prof_name)
        r["profile_name"] = n
    
        n1 = re.sub(p1, '', n)
        n2 = re.sub(p2, '', n1)
        n3 = re.sub(p3, ' ', n2).strip()



#First Names
for l in data:
    full_n = l["profile_name"]
    w = full_n.split()
    name = w[0]
    l["profile_name"] = name




# Created this file in order to check that all the filtering is done correctly    
file_names = "names.txt"

with open(file_names, 'w', encoding = 'utf-8') as f:
    for r in data:
        p = r["profile_name"]
        f.write(p + "\n")
##############################################################################
# Differentiate Dr. Mr. Ms. Mrs. w/regexp
# After lunch apply it to names above

# Replace any periods with a space
per_space = r'\.'
res = re.sub(per_space, ' ', n3 )
print(res)



##############################################################################

# Sample dataset



data = [
    {"profile_name": "Mr.asd"},
    {"profile_name": "Mrs.fda"},
    {"profile_name": "Ms.fad"},
    {"profile_name": "fda"},
    {"profile_name": "Ms.hither"},
    {"profile_name": "Mr.lol"}
]

# Process each profile name and add a new column for gender
for r in data:
    prof_name = r["profile_name"]
    
    
    # Determine the gender based on the cleaned profile name
    if re.search(mr, prof_name):
        gender = "male"
    elif re.search(ms, prof_name) or re.search(mrs, prof_name):
        gender = "female"
    else:
        # Apply the substitutions
        n1 = re.sub(p1, '', prof_name)
        n2 = re.sub(p2, '', n1)
        n3 = re.sub(p3, ' ', n2).strip()
        
        gender = "none"
        r["profile_name"] = n3
    
    # Add the gender to the dictionary
    r["gender"] = gender
    

# Print the updated dataset
for r in data:
    print(r)

