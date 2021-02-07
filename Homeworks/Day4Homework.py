#!/usr/bin/env python
# coding: utf-8

# In[19]:


def prime(n):
    for x in range(n + 1):
        m = int(n / 2)
        flag = 0
        for y in range(m):
            if(x % (y + 2) == 0):
                flag += 1
        if(flag == 1 or flag == 0):
            print(x)
            
n = 100
prime(100)


# In[ ]:




