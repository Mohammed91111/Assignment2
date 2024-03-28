#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Ticket:
    def __init__(self, price, category, location, date):
        """
        Initializes a Ticket object with the given attributes.

       
        """
        self.price = price
        self.category = category
        self.location = location
        self.date = date

    def getPrice(self):
        """
        Gets the price of the ticket.

        Returns:
            float: The price of the ticket.
        """
        return self.price

    def setPrice(self, price):
        """
        Sets the price of the ticket.

        
        """
        self.price = price

    def getCategory(self):
        """
        Gets the category of the ticket.

    
        """
        return self.category

    def setCategory(self, category):
        """
        Sets the category of the ticket.

        
        """
        self.category = category

    def getLocation(self):
        """
        Gets the location of the ticket.


        """
        return self.location

    def setLocation(self, location):
        """
        Sets the location of the ticket.

      
        """
        self.location = location

    def getDate(self):
        """
        Gets the date of the ticket.

        """
        return self.date

    def setDate(self, date):
        """
        Sets the date of the ticket.

    
        """
        self.date = date

# Create an instance of the Ticket class
ticket = Ticket(50.00, "Regular", "Museum of Modern Art", "2024-05-01")

# Print the information of the ticket
print("Ticket Information:")
print("Price:", ticket.getPrice())
print("Category:", ticket.getCategory())
print("Location:", ticket.getLocation())
print("Date:", ticket.getDate())


# In[ ]:




