# Sorting a List of Dictionaries in Python — Clean & Production-Ready!
#https://www.facebook.com/datadriveninsights.corp/posts/pfbid0gzrm6PBsPqMkWUfT65ZcsEtswa4BWYhEzdMrbujLkfT3SWuEJf4EMoYmrdCEGsaMl

#Sorting a list of dictionaries is a common task in real-world Python projects - from processing API responses to organizing user data.
#Here are two clean, production-ready approaches:
#Sort by numerical fields (like age) using sorted() with a lambda
#Sort by string fields (like name) using operator.itengetter for cleaner, faster lookups Both methods avoid modifying the original list and follow Python's best practices (PEP 8, readability, immutability),
#Perfect for anyone working with structured data, JSON records, or API payloads

from operator import itemgetter
people = [{"Name": "James", "Age": 20}, {"Name": "May",   "Age": 14}, {"Name": "Katy",  "Age": 23}]

#1) Sort by age (ascending) using sorted - lambda
people_by_age = sorted(people, key=lambda person: person["Age"])

#2) Sort by name (ascending) using operator.itemgetter
people_by_name = sorted(people, key=itemgetter("Name"))

#Example: print results
if __name__ == "__main__":
     print("Sorted by age: ") 
     for p in people_by_age: print(p)

     print("\nSorted by name:") 
     for p in people_by_name: print(p)
