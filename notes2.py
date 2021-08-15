# Python Structures 
shopping = ["eggs", "bread", "banana"]
print(shopping) 

# for loop to get elements out of the list 
for items in shopping:
    print(items) 

# Most real world data is stored in tabular form which is rows and columns 
# This is called matrice or two dimensional data 

# Using nested list to store data from a matrix 
m = [[1, 2, 3], [4, 5, 6]]
print(m[1][2])

# access each element in a nested list matrix 
for i in range(len(m)): 
    for j in range(len(m[i])): 
        print(m[i][j])

# alternative 
for row in m: 
    for col in row: 
        print(col) 

# Matrix Operations 
# two nested lists 
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

# 3 x 3 matrix 
result = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

# iterate through the rows 
for i in range(len(X)): 
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
print(result) 

# Matrix multiplication Operation 
X = [[1, 2], [4, 5], [3, 6]]
Y = [[1, 2, 3, 4], [5, 6, 7, 8]]

# zero matrix placeholder to store results 
result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# iterate through the row of X 
for i in range(len(X)): 
    # iterate by the column of Y 
    for j in range(len(Y[0])):
        # iterate by the rows of Y 
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
# print the final result 
for r in result:
    print(r) 

# Some common list methods => slice, sort, append, search, insert and remove data. 
# Access elements inside a list 
shopping_List = ["Bread", "Eggs", "Rice"]
print(shopping_List[1])

# replacing an element inside a list 
final_list = shopping_List[1] = "orange"
print(final_list)

# Slicing to get data out 
print(shopping_List[:1]) 

# another way to add items to the list 
print(shopping_List.append("apple")) 

# can add elements at specific indexes using the insert method 
another_list = shopping_List.insert(1, "biscuits")
print(another_list) 

# remove data from the list 
shopping_List.remove("apple")

# DICTIONARY KEYS AND VALUES 
employee = {
    'name': "Jesse Mensah", 
    'age': 32, 
    'department': "sales"
}
print(employee['name'])

# create an empty dictionary from scratch and extend use key value assignment 
movie = {} 
movie['title'] = "Four Runners"
movie["director"] = "Jesse"
movie["year"] = "2025"
movie["rating"] = 9.8
print(movie) 

# using zip method to manipulate dictionaries 
items = ["apple", "rice", "eggs"]
quantity = [5, 3, 2]
orders = zip(items, quantity)
print(list(orders))
# can also turn a zip object into a tuple 
print(tuple(orders))
# also turn a zip object into a dictionary 
print(dict(orders))

# Dictionary methods 
orders = {'apple': 5, 'orange': 3, 'banana': 2}
print(orders.values())
print(list(orders.values()))
print(list(orders.keys()))
# iterate through a dictionary 
for tuple in list(orders.items()):
    print(tuple)

# Tuples => similar to a list but cannot be changed, Immutable. 
daysofweek_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(len(daysofweek_tuple))

shopping_tuple = ("Rice", "Eggs", "Bananas")
print(shopping_tuple + ('apple', 'oranges'))
print(shopping_tuple)


# Sets => ordered collection of unique and immutable objects. 
s1 = set([1, 2, 3, 4, 5, 6])
print(s1) 
s2 = set([1, 2, 2, 3, 4, 4, 5, 6, 6])
print(s2) 
s3 = set([3, 4, 6, 6, 6, 1, 1, 2])
print(s3) 
s4 = {"apple", "orange", "banana"}
print(s4) 
s4.add('pineapple')
print(s4)


# Set Operations 
s5 = {1, 2, 3, 4}
s6 = {3, 4, 5, 6}
# union 
print(s5 | s6) 
print(s5.union(s6))

# intersection 
print(s5 & s6) 
print(s5.intersection(s6))

# difference 
print(s5 - s6) 
print(s5.difference(s6)) 

# subset method 
s7 = {1, 2, 3}
s8 = {1, 2, 3, 4, 5}
print(s7 <= s8)
print(s7.issubset(s8))

# superset method 
print(s8 >= s7) 
print(s8.issuperset(s7))
print(s8 > s7) 
print(s8 > s8)


