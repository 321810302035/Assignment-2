#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if a>b and a>=c:
       print("a is largest")
elif b>=a and b>=c:
       print("b is largest")
else:
        print("c is larger")


# In[6]:


a=str(input("enter a string"))
b=a[::-1]
print("reverse string is:",b)


# In[15]:


n=int(input("enter num"))
temp=n
reverse=1
digit=0
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            print("not prime number")
        break
    else:
            print("prime number")
else:
            print("not prime number")


# In[19]:


try:
    n=int(input("enter a number"))
except:
    print("enter the valid integer type")
else:
    temp=n
    sum=0
    while(n>0):
        digit=n%10
        sum=sum*10+digit
        n=n//10
        if sum==temp:
            print("palindrome")
        else:
            print("not palindrome")
finally:
                print("done")


# In[20]:


n=int(input("enter the value of n"))
t,s=0,0
for i in range(1,n+1):
    s=i*1
    t=t+s
    i=i+1
print("the sum of squares pf first n naural nubers is",t)   


# In[ ]:




