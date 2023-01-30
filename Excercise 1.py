#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
ANSWER: s[0]
# 'o'
ANSWER: s[5]
# 'djan'
ANSWER: s[0:-2]
# 'jan'
ANSWER: s[1:-2]
# 'go'
ANSWER: s[4:]
# Bonus: Use indexing to reverse the string


###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
ANSWER: l[2][2] = "goodbye"

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

ANSWER: d1['simple_key']

d2 = {'k1':{'k2':'hello'}}

ANSWER: d2['k1']['k2']

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

ANSWER: d3['k1'][0]['nest_key'][1][0]

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

ANSWER: set(mylist)

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

ANSWER: print("Hello my dog's name is {} and he is {} years old".format(name,age))