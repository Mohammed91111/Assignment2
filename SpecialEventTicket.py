#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the Ticket class
from Ticket import Ticket

class SpecialEventTicket(Ticket):
    def __init__(self, eventName, duration, price, category, location, date):
        """
        Initializes a SpecialEventTicket object with the given attributes.

       
        """
        super().__init__(price, category, location, date)
        self.eventName = eventName
        self.duration = duration

    def getEventName(self):
        """
        Gets the name of the special event.

    
        """
        return self.eventName

    def setEventName(self, eventName):
        """
        Sets the name of the special event.

      
        """
        self.eventName = eventName

    def getDuration(self):
        """
        Gets the duration of the special event.

       
        """
        return self.duration

# Create an instance of the SpecialEventTicket class
special_event_ticket = SpecialEventTicket("Concert", "3 hours", 100.0, "VIP", "City Hall", "2024-09-15")

# Print the information of the special event ticket
print("Special Event Ticket Information:")
print("Event Name:", special_event_ticket.getEventName())
print("Duration:", special_event_ticket.getDuration())
print("Price:", special_event_ticket.getPrice())
print("Category:", special_event_ticket.getCategory())
print("Location:", special_event_ticket.getLocation())
print("Date:", special_event_ticket.getDate())


# In[ ]:




