#Please Master These 10 Python Functions…
#https://www.youtube.com/watch?v=kGcUtckifXc
age=23
name="Tim"

'''
## Function-01:
##       Using extra parameter in "print" function
#print ("My name is", name, "and I am", age, "years old.")
#print ("My name is", name, "and I am", age, "years old.", sep="|")
#print ("My name is", name, "and I am", age, "years old.", sep=",")
'''

'''
##       Print 2 lines a seperate lines & in same line
#print ("My name is Prasanna")
#print ("I am a Smart Person")

#print ("My name is Prasanna", end=" & ")
#print ("I am a Smart Person")

#print ("My name is Prasanna", end=" | ")
#print ("I am a Smart Person")


### Function-02: 
###       Basic help() function
#help(print)

#def add_function(a, b):
    #"""
    #a = a + 2
    #b = b + 3
    #"""
    #return a + b

#help(add_function)
'''

'''
## Function-03: RANGE Function
rng = range(10)
print (rng)           #range(0, 10)
print (list(rng))     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

rng = range(2,10)
print (rng)           #range(2, 10)
print (list(rng))     #[2, 3, 4, 5, 6, 7, 8, 9]


rng = range(2,10,2)
print (rng)           #range(2, 10, 2)
print (list(rng))     #[2, 4, 6, 8]

rng = range(2,10,3)
print (rng)           #range(2, 10, 3)
print (list(rng))     #[2, 5, 8]


rng = range(10,-10,-2)
print (rng)           #range(10,-10,-2)
print (list(rng))     #[10, 8, 6, 4, 2, 0, -2, -4, -6, -8]
'''

'''
## Function-04: MAP Function
print ("\nPrint all strings in array")
strings = ['Apple', 'Mango', 'Grapes', "CustardApple", "WaterMelon"]
print (strings)         #['Apple', 'Mango', 'Grapes', "CustardApple", "WaterMelon"]

print ("\nGetting Getting lengths of each value in the array")
lengths = list(map(len, strings)) # Getting lengths of each value in the array
print (lengths)         #[5, 5, 6, 12, 10]

print ("\nUsing LAMBDA function")
lengths = map(lambda x: "Fruit: " + x, strings)
print (list(lengths))   #['Fruit: Apple', 'Fruit: Mango', 'Fruit: Grapes', 'Fruit: CustardApple', 'Fruit: WaterMelon']


print ("\nUsing user-defined function: add_test_FruitColon")
def add_test_FruitColon (string):
    return  "Fruit: " + string

lengths = map(add_test_FruitColon, strings)
print (list(lengths))   #['Fruit: Apple', 'Fruit: Mango', 'Fruit: Grapes', 'Fruit: CustardApple', 'Fruit: WaterMelon']
'''

'''
## Function-05: FILTER Function
strings = ['Apple', 'Mango', 'Grapes', "CustardApple", "WaterMelon"]
def longer_than_5_characters (string):
    return  len(string) > 5

#filtered = filter(lambda x: "a" in x, strings)  #remove the letter 'a'
filtered = filter(longer_than_5_characters, strings)
print ("")
print (list(strings))   #['Apple', 'Mango', 'Grapes', 'CustardApple', 'WaterMelon']
print (list(filtered))  #['Grapes', 'CustardApple', 'WaterMelon']

filtered = filter(lambda x: len(x) > 5, strings)
print ("")
print (list(strings))   #['Apple', 'Mango', 'Grapes', 'CustardApple', 'WaterMelon']
print (list(filtered))  #['Grapes', 'CustardApple', 'WaterMelon']
'''

'''
## Function-06: SUM Function
numbers = [1, 3, 23, 7, 16, 11]
print ("")
print (sum(numbers))        #61
print (sum(numbers, 10))    #71 (10 is initial value)
print (sum(numbers, -13))   #48 (-30 is initial value)

numbers = [1, 3, 23, 7, 16, 21.34, 11]
print ("")
print (sum(numbers))        #82.34
print (sum(numbers, 10))    #92.34 (10 is initial value)
print (sum(numbers, -6))    #76.34 (-6 is initial value)
'''

# Function-07: SORTED Function
'''
numbers = [4, 5, 2, 3, -1, 0, 9]
print ("")
print (sorted(numbers))                  #[-1, 0, 2, 3, 4, 5, 9]
print (sorted(numbers,reverse=True))     #[9, 5, 4, 3, 2, 0, -1]

people =[
    {"Name": "Tim",      "Age": 23},
    {"Name": "John",     "Age": 43},
    {"Name": "John",     "Age": 27},
    {"Name": "Preston",  "Age": 12},
    {"Name": "Dony",     "Age": 36},
    {"Name": "Mark",     "Age": 18}
]
print ("")
print ("Sort array based on [Age] Ascending & then Descending")
sorted_people = sorted(people, key=lambda person: person['Age'])
print (sorted_people)  
sorted_people = sorted(people, key=lambda person: person['Age'],reverse=True)
print (sorted_people)  


print ("")
print ("Sort array based on [Name] Ascending & then Descending")
sorted_people = sorted(people, key=lambda person: person['Name'])
print (sorted_people)  
sorted_people = sorted(people, key=lambda person: person['Name'],reverse=True)
print (sorted_people)  
'''


'''
## Function-08: ENUMERATE Function
fruits = ['Apple', 'Mango', 'Grapes', "CustardApple", "WaterMelon"]
print ("")
print ("Show as Key Value line-items")
for index, fruit in enumerate(fruits):
    print (f"{index+1}", fruit)

print ("")
print ("Show as Tuple")
print (list(enumerate(fruits)))
'''


## Function-09: ZIP Function
'''
print ("")
print ("There is 1-to-1 mapping available between 2 arrays")
fruits = ['Apple', 'Mango', 'Grapes', "CustardApple", "WaterMelon"]
prices = [ 17,      13,      4,        14,             3] 
for idx, fruit in enumerate(zip(fruits, prices)):
    print (f"{idx+1}", fruit)
     # There is 1-to-1 mapping available between 2 arrays
     # 1 ('Apple', 17)
     # 2 ('Mango', 13)
     # 3 ('Grapes', 4)
     # 4 ('CustardApple', 14)
     # 5 ('WaterMelon', 3)


print ("")
print ("There is NO 1-to-1 mapping available in ""prices"" array")
fruits = ['Apple', 'Mango', 'Grapes', "CustardApple", "WaterMelon"]
prices = [ 17,      13,      4,        3] 
for idx, fruit in enumerate(zip(fruits, prices)):
    print (f"{idx+1}", fruit)
     # There is NO 1-to-1 mapping available in prices array
     # 1 ('Apple', 17)
     # 2 ('Mango', 13)
     # 3 ('Grapes', 4)
     # 4 ('CustardApple', 3)



print ("")
print ("There is NO 1-to-1 mapping available in ""fruits"" array")
fruits = ['Apple', 'Grapes', "CustardApple", "WaterMelon"]
prices = [ 17,      13,       4,              3, 11] 
for idx, fruit in enumerate(zip(fruits, prices)):
    print (f"{idx+1}", fruit)
     # There is NO 1-to-1 mapping available in fruits array
     # 1 ('Apple', 17)
     # 2 ('Grapes', 13)
     # 3 ('CustardApple', 4)
     # 4 ('WaterMelon', 3)
'''

## Function-10: OPEN Function
'''
'''
filename = "LearnPython_Test-15Oct2025.txt"
print ("")
print ("Writing to a file - 1st Method")
#file = open("LearnPython_Test-15Oct2025.txt", "w")  # Create & Open file in write-mode
file = open(filename, "w")  # Create & Open file in write-mode
file.write("File Name: LearnPython_Test-15Oct2025.txt")
file.write("This is my first line.\n")
file.write("This is my second line.\n")
file.write("This is my third line.\n")  


print ("")
print ("Writing to a file - 1st Method (all content in single write)")
file.write("This is my 1st line.\n This is my 2nd line.\n This is my 3rd line.")
file.close()  # Close the file


print ("")
print ("Writing to a file - 2nd Method")
#with open("LearnPython_Test-15Oct2025.txt", "a") as file:  # Create & Open file in append-mode
with open(filename, "a") as file:  # Create & Open file in append-mode
    file.write("File Name: LearnPython_Test-16Oct2025.txt\n")
    file.write("This is my first line.\n")
    file.write("This is my second line.\n")
    file.write("This is my third line.\n")  
    file.write("This is my 1st line.\n This is my 2nd line.\n This is my 3rd line.")


print ("")
print ("Reading file content")
#with open("LearnPython_Test-15Oct2025.txt", "r") as file:  # Open file in READ-mode
with open(filename, "r") as file:  # Open file in READ-mode
    text = file.read()
    print (text)