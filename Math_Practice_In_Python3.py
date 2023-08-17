#!/usr/bin/env python
# coding: utf-8

# ## Math Practice

# In[2]:


#########################################################
### EXECUTE THIS CELL BEFORE YOU  TEST YOUR SOLUTIONS ###
#########################################################

import imp
sol = imp.load_compiled("sol", "./sol.py")
from nose.tools import assert_equal


# ## A note on variable initialization
# 
# Variable initialization refers to the act of declaring a variable (giving it a name) and assigning it a value. A variable's name is declared on the left side of the `=` and its value on the right side. This can be done in a single line of code, like the below. Note that a variable's name may not contain spaces or special characters, with the exception of the underscore `_`.
# 
# ```python
# my_variable = 1
# ```
# 
# Once initialized, referring to `my_variable` in subsequent lines of code will actually refer to `my_variable`'s value, which has been set to `1`. However, as their name implies, variables can have changing values. For example, we might do something like the below:
# 
# ```python
# my_variable = 1
# print(my_variable)     # This will print out the value of my_variable
# # >>> 1
# 
# my_variable = 1 * 2    # We've now changed the value of my_variable to be (1 * 2) = 2
# print(my_variable)
# # >>> 2
# ```
# 
# We can also reference a variable's current value in it's own re-assignment! This can be done if the variable has already been assigned a value previously. For example:
# ```python
# my_variable = my_variable * 3
# print(my_variable)
# # >>> 6
# ```
# What the above line is doing is setting the value of `my_variable` equal to the current value of `my_variable`, which we set to `2`, multiplied by `3`. This ends up being: `my_variable = 2 * 3 = 6`

# Calculate the result of 3.93 multiplied by 4901 and save it in a variable named 'q1', then print it out.

# In[3]:


q1 = 3.93 * 4901

print(q1)


# In[4]:


##########################
### TEST YOUR SOLUTION ###
##########################
# Note: All test cases are read-only

assert_equal(q1, sol.q1)
print("Success!")


# Calculate the result of 215 divided by 6 and save it in a variable named 'q2', then print it out.

# In[5]:


q2 = 215 / 6

print(q2)


# In[6]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q2, sol.q2)
print("Success!")


# Calculate the result of 3 divided by 0.3 and save it in a variable named 'q3', then print it out.

# In[7]:


q3 = 3 / 0.3
print(q3)


# In[8]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q3, sol.q3)
print("Success!")


# Calculate the remainder of 215 divided by 6 and save it in a variable named 'q4', then print it out.

# In[13]:


q4 = 215 % 6
print(q4)


# In[14]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q4, sol.q4)
print("Success!")


# Calculate the value of 9 raised to the 12th power and save it in a variable named 'q5', then print it out.

# In[15]:


q5 = 9**12

print(q5)


# In[16]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q5, sol.q5)
print("Success!")


# Cast 3.5 to an integer and save it in a variable named 'q6', then print it out.

# In[18]:


q6 = int(3.5)

print(q6)


# In[19]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q6, sol.q6)
print("Success!")


# ## Data Types Practice

# Calculate the data type of `"False"` (notice the **quotes** around the word False!) and save it in a variable named 'q7', then print it out.

# In[24]:


q7 = type("False")

print(q7)


# In[25]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q7, sol.q7)
print("Success!")


# Calculate the data type of True and save it in a variable named 'q8', then print it out.

# In[26]:


q8 = type(True)

print(q8)


# In[27]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q8, sol.q8)
print("Success!")


# Calculate the data type of the result of 1000 divided by 10 and save it in a variable named 'q9', then print it out.

# In[28]:


q9 = type(1000 / 10)

print(q9)


# In[29]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q9, sol.q9)
print("Success!")


# Cast the value of 6.3 divided by 3.8 to an integer. Save it in a variable named 'q10', then print it out.

# In[30]:


q10 = int(6.3 / 3.8)

print(q10)


# In[31]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q10, sol.q10)
print("Success!")


# ## String Practice

# Concatenate the strings 'James', 'Brian', and 'Patrick' - store the result in a variable called 'q11', then print it out. Make sure to add a single empty space between the names!

# In[47]:


q11 = ( 'James' + ' Brian' + ' Patrick')
print(q11)


# In[48]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q11, sol.q11)
print("Success!")


# Make the following string correct, storing it in a variable named 'q12':<br />
# `q12 = "4 % 2 = " + (4 % 2))`

# In[83]:


q12 = "4 % 2 = " + str(4 % 2)

print(q12)


# In[84]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q12, sol.q12)
print("Success!")


# Save the following quote, (including the double quotes), in a variable called 'q13', then print it:<br />
# Albert Einstein's best quote is "I have no special talent. I am only passionately curious."

# In[87]:


q13 = 'Albert Einstein\'s best quote is "I have no special talent. I am only passionately curious."'
print(q13)


# In[88]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(q13, sol.q13)
print("Success!")


# In[ ]:




