#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Manager():
    name = " "
    age = 0
    languages = set()
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.languages = set()
        
    def addlanguage(self, language):
        self.languages.add(language)


# In[9]:


class Employee():
    name = " "
    age = 0
    languages = set()
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def addlanguage(self, language):
        self.languages.add(language)


# In[17]:


e1 = Employee("David", 28)
e1.addlanguage("French")
e1.addlanguage("English")
print(e1.name + ", " + str(e1.age))
print(e1.languages)

m = Manager("Levi", 45)
m.addlanguage("Japanese")
m.addlanguage("English")
print(m.name + ", " + str(m.age))
print(m.languages)


# In[ ]:




