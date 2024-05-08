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
    if r["profile_name"] != "Amazon customer" and r["profile_name"] != "Amazon Customer":
        data.append(r)
        
        
    
    
