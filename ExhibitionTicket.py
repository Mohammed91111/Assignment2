#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import the Ticket class
from Ticket import Ticket

class ExhibitionTicket(Ticket):
    def __init__(self, duration, price, category, location, date):
        """
        Initializes an ExhibitionTicket object with the given attributes.

        """
        super().__init__(price, category, location, date)
        self.duration = duration

    def getDuration(self):
        """
        Gets the duration of the exhibition ticket.

       
        """
        return self.duration

    def setDuration(self, duration):
        """
        Sets the duration of the exhibition ticket.

        
        """
        self.duration = duration

# Create an instance of the ExhibitionTicket class
exhibition_ticket = ExhibitionTicket("3 hours", 50.0, "Regular", "Museum of Modern Art", "2024-07-15")

# Print the information of the exhibition ticket
print("Exhibition Ticket Information:")
print("Duration:", exhibition_ticket.getDuration())
print("Price:", exhibition_ticket.getPrice())
print("Category:", exhibition_ticket.getCategory())
print("Location:", exhibition_ticket.getLocation())
print("Date:", exhibition_ticket.getDate())


# In[ ]:




