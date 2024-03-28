#!/usr/bin/env python
# coding: utf-8

# In[4]:


from Artwork import Artwork
from Visitor import Visitor
from Exhibition import Exhibition
class Museum:
    def __init__(self):
        """
        Initializes a Museum object with empty lists for artworks, visitors, and exhibitions.
        """
        self.artworks = []
        self.visitors = []
        self.exhibitions = []

    def getArtworks(self):
        """
        Gets the list of artworks in the museum.

       
        """
        return self.artworks

    def getVisitors(self):
        """
        Gets the list of visitors in the museum.

        """
        return self.visitors

    def getExhibitions(self):
        """
        Gets the list of exhibitions in the museum.

        
        """
        return self.exhibitions

    def addArtwork(self, artwork):
        """
        Adds an artwork to the museum.

        
        """
        self.artworks.append(artwork)

    def addVisitor(self, visitor):
        """
        Adds a visitor to the museum.

       
        """
        self.visitors.append(visitor)

    def addExhibition(self, exhibition):
        """
        Adds an exhibition to the museum.

        Args:
            exhibition (Exhibition): The exhibition to add to the museum.
        """
        self.exhibitions.append(exhibition)

    def sellTicket(self, visitor):
        """
        Simulates selling a ticket for a museum visit.

       
        """
        print(f"Ticket sold to {visitor.getName()}.")

    def organizeTour(self):
        """
        Simulates organizing a tour of the museum.
        """
        print("Tour organized.")


# In[ ]:




