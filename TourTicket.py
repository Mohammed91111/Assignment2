#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import the Ticket class
from Ticket import Ticket

class TourTicket(Ticket):
    def __init__(self, guide, groupSize, price, category, location, date):
        """
        Initializes a TourTicket object with the given attributes.

       
        """
        super().__init__(price, category, location, date)
        self.guide = guide
        self.groupSize = groupSize

    def getGuide(self):
        """
        Gets the guide for the tour.

      
        """
        return self.guide

    def setGuide(self, guide):
        """
        Sets the guide for the tour.

       
        """
        self.guide = guide

    def getGroupSize(self):
        """
        Gets the size of the tour group.

       
        """
        return self.groupSize

    def setGroupSize(self, groupSize):
        """
        Sets the size of the tour group.

       
        """
        self.groupSize = groupSize

# Create an instance of the TourTicket class
tour_ticket = TourTicket("Ommer", 10, 30.0, "Regular", "Louvre Museum", "2024-08-20")

# Print the information of the tour ticket
print("Tour Ticket Information:")
print("Guide:", tour_ticket.getGuide())
print("Group Size:", tour_ticket.getGroupSize())
print("Price:", tour_ticket.getPrice())
print("Category:", tour_ticket.getCategory())
print("Location:", tour_ticket.getLocation())
print("Date:", tour_ticket.getDate())


# In[ ]:




