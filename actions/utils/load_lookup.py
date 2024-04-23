import csv 
from typing import Any, Text, Dict, List


def load_lookup_table(path)->Dict[Text,Any]:
    lookup_table = {}
    with open(path,mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lookup_table[row['item'].lower().strip()] = row['price']
        
    return lookup_table


# lookup_table = load_lookup_table("../Foods.csv")
# print (lookup_table)
# item = "chilly momo"

# if item in lookup_table:
#     price = lookup_table[item]

#     print (f"The price of {item} is {price}")
# else:
#     print (f"Sorry, we do not have the price of {item}")