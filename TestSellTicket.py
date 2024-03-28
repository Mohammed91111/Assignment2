#!/usr/bin/env python
# coding: utf-8

# In[10]:


from Museum import Museum
from Visitor import Visitor
from Exhibition import Exhibition

class TestMuseum:
    def setUp(self):
        self.museum = Museum()  # Initialize the museum object
        self.visitor = Visitor("Ali", 30, "1234567890")  # Create a visitor object

    def test_sell_ticket(self):
        # Add the visitor to the museum
        self.museum.addVisitor(self.visitor)

        # Sell a ticket to the visitor
        self.museum.sellTicket(self.visitor)

        # Check if the ticket is sold successfully by verifying if the visitor is in the list of visitors
        assert self.visitor in self.museum.getVisitors()
        print("Ticket sold successfully.")

if __name__ == '__main__':
    test = TestMuseum()
    test.setUp()
    test.test_sell_ticket()


# In[ ]:




