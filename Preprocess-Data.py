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
# Dots
p4 = r'\.'
# Mr -> male
mr1 = r'\bMr\b'
mr2 = r'\bMR\b'
# Ms -> female
ms = r'\bMiss\s\b'
# Dr -> remove doctor & apply corpus
dr1 = r'\bDr\.\b'
dr2 = r'\bDr\.\s\b'
dr3 = r'\bDr\s\b'
dr4 = r'\bdr\.\s\s\s\b'
dr5 = r'\bDR\s\b'
er = r'\bEr\.\s\b'
# Pattern for @
at = r'@'
underscore = r'_'

# Apply first name get func to main data and lowercase
# Opens male name csv
file_male = "Processed_Data/Indian-Male-Names.csv"
male_n = []


with open(file_male, mode = 'r', newline = '', encoding='latin1') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        full_n = row["name"].split()
        # checks if empty
        if full_n:   
            first_n = full_n[0]
            first_name = first_n.capitalize()
            male_n.append(first_name)

# Open Female csv
# Opens male name csv
file_female = "Processed_Data/Indian-Female-Names.csv"
female_n = []

# remove single commas
p5 = r'\,'
with open(file_female, mode = 'r', newline = '', encoding='latin1') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        full_n = row["name"].split()
        # checks if empty
        if full_n:   
            first_n = full_n[0]
            first_name = first_n.capitalize()
            first_f = re.sub(p4, "", first_name)
            first_f1 = re.sub(p5, "", first_name)
            female_n.append(first_f1)


# classifies gender with ms/mr
full_names_filt = []
for r in data:
    prof_name = r["profile_name"]
    if re.search(mr1,prof_name):
        r["gender"] = "male"
        n = re.sub(mr1, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
    elif re.search(mr2,prof_name):
        r["gender"] = "male"
        n = re.sub(mr2, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
    elif re.search(ms, prof_name) :
        r["gender"] = "female"
        n = re.sub(ms, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
    elif  re.search(dr1, prof_name):
        r["gender"] = "unknown"
        n = re.sub(dr1, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
    elif re.search(dr2, prof_name) :
        r["gender"] = "unknown"
        n = re.sub(dr2, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
    elif re.search(dr3, prof_name) :
        r["gender"] = "unknown"
        n = re.sub(dr3, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
    elif re.search(dr4, prof_name):
        r["gender"] = "unknown"
        n = re.sub(dr4, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
    elif re.search(dr5, prof_name):
        r["gender"] = "unknown"
        n = re.sub(dr5, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
    elif re.search(er, prof_name):
        r["gender"] = "unknown"
        n = re.sub(er, '', prof_name)
        n3 = re.sub(p3, ' ', n).strip()
        r["profile_name"] = n3
    else:
        r["gender"] = "unknown"
        n1 = re.sub(p1, '', prof_name)
        n2 = re.sub(p2, '', n1)
        n3 = re.sub(p3, ' ', n2).strip()
        n4 = re.sub(p4, "", n3)
        n5 = re.sub(at, ' ', n4)
        n6 = re.sub(underscore, ' ', n5)
        r["profile_name"] = n6
    full_names_filt.append(r["profile_name"])



# Created this file in order to check that all the filtering is done correctly    
file_names = "DEL.txt"

with open(file_names, 'w', encoding = 'utf-8') as f:
    for per in data:
        nam = per["profile_name"]
        if nam.strip():
            n4 = re.sub(p4, "", nam)
            f.write(n4 + "\n")
        
# Deletes First Names that are null
names_list = []
index = 0
del_empty =[]

for l in data: 
    full = l["profile_name"].split()
    if full:
        name_prof = full[0]
        if name_prof == "Roshitha⚡️":
            name_prof = "Roshitha"
        names_list.append(name_prof)
    else:
        del_empty.append(index)
    
    index +=1

def del_emp():
    indx_del  = sorted(del_empty, reverse=True)
    
    for i in indx_del:
        del data[i]
del_emp()

# final_names
file_names = "FINAL_TEST.txt"
with open(file_names, 'w', encoding = 'utf-8') as f:
    for per in names_list:
        per = per.lower()
        per = per.capitalize()
        per = re.sub(p4, "", per)
        f.write(per + "\n")
  
    
      
###################### GENDER SEPERATION ######################################       
### open txt first unisex, male and female if still unkonn count them
unisex_f = "Name_Dictionary/unisex_names.txt"
male_f = "Name_Dictionary/male_names_2.txt"
female_f = "Name_Dictionary/female_names.txt"
unisex_nam = []
male_nam = []
female_nam = []

# Reads files given
def read_file(path):
    with open(path, 'r') as file:
        for line in file:
            if path == unisex_f:       
                unisex_nam.append(line.strip())
            elif path == male_f:
                male_nam.append(line.strip())
            else:       
                female_nam.append(line.strip())
                
read_file(unisex_f)
read_file(male_f)
read_file(female_f)

data_del = []

# cleans unisex names
def detect_uni(u):
    for name in u:
        indx=0
        for n in names_list:
            if name == n:
                data_del.append(indx)
            indx+=1
        
def del_uni():
    data_del_f = sorted(data_del, reverse=True)
    for i in data_del_f:
        del data[i]
        del names_list[i]


detect_uni(unisex_nam)
del_uni()

    
# Genderfies name
def gen_nam(g_nam):
    for gn in g_nam:
        ind=0
        for n in names_list:
            if gn == n:    
                if g_nam == female_nam or g_nam == female_n:
                    data[ind]["gender"] = "female"
                elif g_nam == male_nam or g_nam == male_n :
                    data[ind]["gender"] = "male"            
                    
            ind+=1



gen_nam(male_nam)
gen_nam(female_nam)
gen_nam(male_n)
gen_nam(female_n)


# Gather the final data
rev_n = set()
final_data_g = []
for r in data:
    rev = r["review_title"]
    if rev not in rev_n:
        g = r["gender"]   
    if g in ["male", "female"]:
        final_data_g.append(r)
        
    rev_n.add(rev)


    
################# Saving Final REVIEW #########################################

csv_f = "Final_Gendered_2.csv"

header_cat = final_data_g[0].keys()

with open(csv_f, mode='w', newline = '', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=header_cat)
    writer.writeheader()
    writer.writerows(final_data_g)

# Filter out entries with unknown gender
data_filtered = [entry for entry in data if entry["gender"] != "unknown"]
removed_entries = len(data) - len(data_filtered)
data = data_filtered