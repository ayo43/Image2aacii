#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!pip install pywhatkit


# In[15]:


from PIL import Image
import pywhatkit


# In[31]:


Image.open(r"C:\Users\ayok4\OneDrive\Pictures\ScreenSaver\402897.jpg")


# In[29]:


pywhatkit.image_to_ascii_art(r'C:\Users\ayok4\OneDrive\Pictures\ScreenSaver\402897.jpg', 'myTxt')


# In[32]:


file = open('myTxt.txt', 'r')
print(file.read())


# In[ ]:




