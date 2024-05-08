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
    
# simplifies start to a single number (1 - 5)
for r in og:
    s = r["review_rating"]
    r["review_rating"] = s[0]

# Removes any review without a name
data = []
for r in og:
    s = r["profile_name"]
    if (s != "Amazon customer" and
        s != "Amazon Customer" and not s[0].isdigit() and len(s) > 2
        and len(s) !=1 ):
        data.append(r)

l = []
for r in data:
    l.append(r["profile_name"])


    
    
