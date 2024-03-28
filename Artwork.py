#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Artwork:
    def __init__(self, id, title, artist, dateOfCreation, historicalSignificance, location):
        """
        Initializes an Artwork object with the given attributes. """
        self.id = id
        self.title = title
        self.artist = artist
        self.dateOfCreation = dateOfCreation
        self.historicalSignificance = historicalSignificance
        self.location = location

    def getTitle(self):
        """Gets the title of the artwork."""
        return self.title

    def setTitle(self, title):
        """Sets the title of the artwork."""
        self.title = title

    def getArtist(self):
        """Gets the artist of the artwork."""
        return self.artist

    def setArtist(self, artist):
        """Sets the artist of the artwork."""
        self.artist = artist

    def getDateOfCreation(self):
        """Gets the date of creation of the artwork."""
        return self.dateOfCreation

    def setDateOfCreation(self, dateOfCreation):
        """Sets the date of creation of the artwork."""
        self.dateOfCreation = dateOfCreation

    def getHistoricalSignificance(self):
        """Gets the historical significance of the artwork."""
        return self.historicalSignificance

    def setHistoricalSignificance(self, historicalSignificance):
        """Sets the historical significance of the artwork."""
        self.historicalSignificance = historicalSignificance

    def getLocation(self):
        """Gets the location of the artwork."""
        return self.location

    def setLocation(self, location):
        """Sets the location of the artwork."""
        self.location = location

# Create an instance of the Artwork class
artwork = Artwork(1, "Artwork", "Mohammad", "2024", "Post-Impressionist painting", "Museum of Modern Art")

# Print the information of the artwork instance
print("Artwork Information:")
print("ID:", artwork.id)
print("Title:", artwork.title)
print("Artist:", artwork.artist)
print("Date of Creation:", artwork.dateOfCreation)
print("Historical Significance:", artwork.historicalSignificance)
print("Location:", artwork.location)



# In[ ]:




