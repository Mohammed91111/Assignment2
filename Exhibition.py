#!/usr/bin/env python
# coding: utf-8

# In[5]:


from Artwork import Artwork

class Exhibition(Artwork):
    def __init__(self, id, title, artist, dateOfCreation, historicalSignificance, location, startDate, endDate):
        """
        Initializes an Exhibition object with the given attributes.

       
           
        """
        super().__init__(id, title, artist, dateOfCreation, historicalSignificance, location)
        self.startDate = startDate
        self.endDate = endDate

    def getStartDate(self):
        """
        Gets the start date of the exhibition.

       
        """
        return self.startDate

    def setStartDate(self, startDate):
        """
        Sets the start date of the exhibition.

        """
        self.startDate = startDate

    def getEndDate(self):
        """
        Gets the end date of the exhibition.

        
        """
        return self.endDate

    def setEndDate(self, endDate):
        """
        Sets the end date of the exhibition.

    
        """
        self.endDate = endDate

# Create an instance of the Exhibition class
exhibition = Exhibition(1, "Artwork", "Mohammad", "2024", "Post-Impressionist painting", "Museum of Modern Art", "2024-05-01", "2024-06-15")

# Print the information of the exhibition
print("Exhibition Information:")
print("ID:", exhibition.id)
print("Title:", exhibition.title)
print("Artist:", exhibition.artist)
print("Date of Creation:", exhibition.dateOfCreation)
print("Historical Significance:", exhibition.historicalSignificance)
print("Location:", exhibition.location)
print("Start Date:", exhibition.getStartDate())
print("End Date:", exhibition.getEndDate())


# In[ ]:




