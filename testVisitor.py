#!/usr/bin/env python
# coding: utf-8

# In[3]:


from Museum import Museum
from Visitor import Visitor

class TestMuseum:
    def setUp(self):
        self.museum = Museum()  # Initialize the museum object
        self.visitor = Visitor("Ali", 30, "1234567890")  # Create a visitor object

    def test_add_visitor(self):
        # Add the visitor to the museum
        self.museum.addVisitor(self.visitor)

        # Check if the visitor is added successfully by verifying if the visitor is in the list of visitors
        assert self.visitor in self.museum.getVisitors()

        # Print visitor information
        print("Visitor information:")
        print(f"Name: {self.visitor.getName()}")
        print(f"Age: {self.visitor.getAge()}")
       

        print("Visitor added successfully.")

if __name__ == '__main__':
    test = TestMuseum()
    test.setUp()
    test.test_add_visitor()


# In[ ]:





# In[ ]:




