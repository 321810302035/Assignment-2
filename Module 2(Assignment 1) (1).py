#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 1.	Take two inputs from user and check whether they are equal or not
     a=int(input("enter a num"))
     b=int(input("enter b num"))
        if a==b:
            print("a and b are equal")
        else:
            print("a and b are not equal")    


# In[5]:


2.	Take 3 inputs from user and check :
           all are equal
           any of two are equal
           ( use and or )
print("first number")
first=input()
print("second number")
second=input()
print("third number")
third=input()
all=first=second and second=third and third=first
print("all are equal:",all)


# In[ ]:





# In[ ]:





# In[ ]:



def max_of_two( x, y ):

    if x > y:

        return x

    return y

def max_of_three( x, y, z ):
return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

