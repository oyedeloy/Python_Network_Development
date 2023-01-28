from random import choice
from pprint import pprint
from operator import itemgetter
from tabulate import tabulate

def matching_stuff():
    
    matching = dict()      
    matching["country"] = choice(["Nigeria", "England", "United states"])
    matching["trans"] = choice(["Land", "Air", "Water"])
    matching["payment_method"] = choice(["cash", "debit", "credit", "cash"])
    matching["reciept"] = choice(["yes", "no", "optional"])
    return matching
    
#print(matching_stuff())   

def matched_stuff(num):
    matched = list()
    for stuff in range(num):
        done = matching_stuff()
        if done not in matched:
            matched.append(done)
    return matched
done_matching = matched_stuff(5)

#USING PRINT
print("\n\n----------USING PRINT----------\n")
print(done_matching)

#USING PPRINT
print("\n\n----------USING PPRINT----------\n")
pprint(done_matching)

print('\n_____FORMATTED USING F-STRINGS AND FOR LOOPS_____')
for i, list_item in enumerate[done_matching]:
    for key, value in list_item.items():
        print(f"{key:>16s} :{value}")

# WE WILL PRINT A TABLE OF OBJECTS USING THE TABULATE MODULE
print("\n----- SORTED OBJECTS IN TABULAR FORMAT -------------")
print(tabulate(sorted(done_matching, key=itemgetter("country", "payment_method")), headers="keys"))
#print(tabulate(sorted(devices, key=itemgetter("vendor")), headers="keys"))
print(done_matching[0])    
    