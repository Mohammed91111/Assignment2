#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import the Artwork class
from Artwork import Artwork

class SpecialEvent(Artwork):
    def __init__(self, id, title, artist, dateOfCreation, historicalSignificance, location, duration):
        """
        Initializes a SpecialEvent object with the given attributes.

        
           
        """
        super().__init__(id, title, artist, dateOfCreation, historicalSignificance, location)
        self._duration = duration

    def getDuration(self):
        """
        Gets the duration of the special event.

       
        """
        return self._duration

    def setDuration(self, duration):
        """
        Sets the duration of the special event.

        
        """
        self._duration = duration

# Create an instance of the SpecialEvent class
special_event = SpecialEvent(1, "Concert", "Mozart", "1785", "Classical music performance", "Carnegie Hall", "2 hours")

# Print the information of the special event
print("Special Event Information:")
print("Title:", special_event.getTitle())
print("Artist:", special_event.getArtist())
print("Date of Creation:", special_event.getDateOfCreation())
print("Historical Significance:", special_event.getHistoricalSignificance())
print("Location:", special_event.getLocation())
print("Duration:", special_event.getDuration())


# In[ ]:




