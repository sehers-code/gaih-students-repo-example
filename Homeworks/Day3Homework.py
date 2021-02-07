#!/usr/bin/env python
# coding: utf-8

# In[4]:


d = {}

username = input("Create a new username: ")
password = input("Create a password: ")

d.update({username : password})
print("***************")
loop = True

while loop:
    loop = True
    usr = input("Enter your username to log in: ")
    psw = input("Password: ")
    if(d.get(usr) == psw):
        loop = False
        print("Logged in.")
    

