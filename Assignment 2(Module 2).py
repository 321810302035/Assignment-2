#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
def area(r):
    a=math.pi*r*r
    print('area:',a)
area(int(input("radius:")))


# In[6]:


from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)


# In[18]:


import math
pi=3.14159
def area_of_segment(radius,angle):
    area_of_sector = pi * (radius * radius) * (angle / 360)
    area_of_traingle=1 /2 *(radius * radius) *math.sin((angle * pi) / 180)
    return area_of_sector - area_of_traingle;
radius=10.0
angle=90.0
print("area of minor segment=",area_of_segment(radius,angle))
print("area of major segment=",area_of_segment(radius,(360-angle)))


# In[13]:


import random
l1=[100,1,2,3,30,'hai','hello']
print("the given list:",l1)
random.shuffle(l1)
print("the shuffled list is:",(l1))


# In[19]:


import random
print("random no of list is:")
print(random.choice(range(1,10000)))
print("random no from range is:")
print(random.randrange(1,10000,50))


# In[24]:


import math
print("sin60:",math.sin(60))
print("cos(pi):",math.pi)
print("tan90:",math.tan(90))
print("angle of 0.8660:",math.degrees(math.sin(0.8660254837844386)))
print("5^B:",math.pow(5,8))
print("square root if 400 is:",math.sqrt(400))
print("the value of 5^e:",math.pow(5,math.e))
print("the value of log(1204).base 2:",math.log2(1024))
print("the value of log(1024).base 10:",math.log10(1024))
print("the floor value of 23.56:",math.floor(23.56))
print("the ceiling value of 23.56:",math.ceil(23.56))


# In[ ]:





# In[ ]:




