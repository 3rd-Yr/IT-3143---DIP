#!/usr/bin/env python
# coding: utf-8

# In[1]:


movies=["dragon","insidious","warrior","gijoe"]
print('first: ',movies[0])
print('last: ',movies[-1])


# In[2]:


marks=60

if marks>90:
    print("v good")
elif marks>50:
    print("good")
else:
    print("not good")


# In[5]:


marks2=[22,32,45,35,67,89,76]


# In[19]:


def max(a,b,c):
    largest=a
    
    if b>largest:
        largest=b
        
    if c>largest:
        largest=c
        
    return largest
print(max(3,4,5))
print(max(33,44,75))       


# In[9]:


marks2 = [22, 32, 45, 35, 67, 89, 76]

for value in marks2:
    if value > 90:
        print("v good")
    elif value > 50:
        print("good")
    else:
        print("not good")


# In[14]:


for i in range(1,11):
    print("9x",i,"=",9*i)


# In[ ]:




