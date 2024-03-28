#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Museum import Museum
from Artwork import Artwork

class TestMuseum:
    def setUp(self):
        self.museum = Museum()
        self.artwork1 = Artwork(1, "Mona Lisa", "Leonardo da Vinci", "1503", "Renaissance masterpiece", "Louvre Museum")
        self.artwork2 = Artwork(2, "The Starry Night", "Vincent van Gogh", "1889", "Post-Impressionist painting", "Museum of Modern Art")

    def test_add_artwork(self):
        self._assert_equal(len(self.museum.getArtworks()), 0)  # Initially, no artworks should be in the museum
        self.museum.addArtwork(self.artwork1)  # Add artwork1 to the museum
        self._assert_equal(len(self.museum.getArtworks()), 1)  # After adding artwork1, there should be 1 artwork in the museum
        self._assert_in(self.artwork1, self.museum.getArtworks())  # Artwork1 should be in the list of artworks in the museum
        self.museum.addArtwork(self.artwork2)  # Add artwork2 to the museum
        self._assert_equal(len(self.museum.getArtworks()), 2)  # After adding artwork2, there should be 2 artworks in the museum
        self._assert_in(self.artwork2, self.museum.getArtworks())  # Artwork2 should be in the list of artworks in the museum

    def _assert_equal(self, value1, value2):
        assert value1 == value2, f"Expected {value1} to be equal to {value2}"

    def _assert_in(self, item, container):
        assert item in container, f"Expected {item} to be in {container}"

if __name__ == '__main__':
    test = TestMuseum()
    test.setUp()
    test.test_add_artwork()


# In[ ]:




