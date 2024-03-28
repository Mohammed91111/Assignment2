#!/usr/bin/env python
# coding: utf-8

# In[4]:


from Museum import Museum
from Exhibition import Exhibition

class TestMuseum:
    def setUp(self):
        self.museum = Museum()  # Initialize the museum object
        self.exhibition = Exhibition(1, "Artwork", "Mohammad", "2024", "Post-Impressionist painting", "Museum of Modern Art", "2024-05-01", "2024-06-15")

    def test_add_exhibition(self):
        # Add the exhibition to the museum
        self.museum.addExhibition(self.exhibition)

        # Check if the exhibition is added successfully by verifying if the exhibition is in the list of exhibitions
        assert self.exhibition in self.museum.getExhibitions()
        print("Exhibition added successfully.")

        # Print the information of the added exhibition
        print("Exhibition Information:")
        print("Title:", self.exhibition.getTitle())
        print("Artist:", self.exhibition.getArtist())
        print("Date of Creation:", self.exhibition.getDateOfCreation())
        print("Historical Significance:", self.exhibition.getHistoricalSignificance())
        print("Location:", self.exhibition.getLocation())
        print("Start Date:", self.exhibition.getStartDate())
        print("End Date:", self.exhibition.getEndDate())

if __name__ == '__main__':
    test = TestMuseum()
    test.setUp()
    test.test_add_exhibition()


# In[ ]:




