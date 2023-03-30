#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install opencv-python')


# In[14]:



import cv2

from matplotlib import pyplot as plt


img = cv2.imread('Image.jpg',0)


histr = cv2.calcHist([img],[0],None,[256],[0,256])


plt.plot(histr)
plt.show()


# In[12]:


import cv2

from matplotlib import pyplot as plot

image = cv2.imread('Image.jpg')

plot.hist(image.ravel(),256)
plot.show()


# In[ ]:




