ramit = {'name': 'Ramit',
'email': 'ramit@gmail.com',
'interests': ['movies', 'tennis'],
'friends': [ 
    { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] },
    { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] } 
    ]}

# Write a python expression that gets the email address of Ramit.
print(ramit['email'])

# Write a python expression that gets the first of Ramit's interests.
print(ramit['interests'][0])

# Write a python expression that gets the email address of Jasmine.
print(ramit['friends'][0]['email'])

# Write a python expression that gets the second of Jan's two interests.
print(ramit['friends'][1]['interests'][1])

# In this exercise, are you using dynamic keys or fixed keys?
# Ans: still fixed; no variable names referenced inside the indexes. 
