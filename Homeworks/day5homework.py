#!/usr/bin/env python
# coding: utf-8

# In[43]:


class Animals():
    
    color = " "
    name = " "
    
    def __init__(self, color, name):
        self.color = color
        self.name = name    
    def makeNoise(self):
        pass    


# In[53]:


class Cats(Animals):
    def __init__(self, color, name):
        super().__init__(color, name)
    def makeNoise(self):
        return "meow"


# In[54]:


class Dogs(Animals):
    def __init__(self, color, name):
        super().__init__(color, name)
    def makeNoise(self):
        return "bark"


# In[55]:


cat = Cats("white", "tesla")
dog = Dogs("pink", "paws")

print("Cat's name: " + cat.name, " cat's color: " + cat.color)
print("Dog's name: " + dog.name, " dog's color: " + dog.color)
print("Cat says " + cat.makeNoise())
print("Dog says: " + dog.makeNoise())

