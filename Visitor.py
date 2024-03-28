#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Visitor:
    def __init__(self, name, age, nationalId):
        """
        Initializes a Visitor object with the given attributes.

       
        """
        self.name = name
        self.age = age
        self.nationalId = nationalId
        self.ticket = []

    def getName(self):
        """
        Gets the name of the visitor.

      
        """
        return self.name

    def setName(self, name):
        """
        Sets the name of the visitor.

        
        """
        self.name = name

    def getAge(self):
        """
        Gets the age of the visitor.

        """
        return self.age

    def setAge(self, age):
        """
        Sets the age of the visitor.

       
        """
        self.age = age

    def getNationalId(self):
        """
        Gets the national ID of the visitor.

        """
        return self.nationalId

    def setNationalId(self, nationalId):
        """
        Sets the national ID of the visitor."""
        self.nationalId = nationalId

# Create an instance of the Visitor class
visitor = Visitor("Ali", 30, "1234567890")

# Print the information of the visitor
print("Visitor Information:")
print("Name:", visitor.getName())
print("Age:", visitor.getAge())
print("National ID:", visitor.getNationalId())


# In[ ]:




