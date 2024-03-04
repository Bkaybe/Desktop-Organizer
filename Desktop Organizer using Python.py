#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil


# In[2]:


desktop_path = os.path.expanduser("~/Desktop")
desktop_path


# In[3]:


os.listdir(desktop_path)


# In[5]:


# Define Desktop Path

desktop_path = os.path.expanduser("~/Desktop")
desktop_path

# Create a dictionary to store the file paths by file extension

files_by_extension = {}

#loop through all the files on the desktop

for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)
    
    #check if its a file 
    if os.path.isfile(file_path):
        
        #get the file extension
        file_extension = os.path.splitext(filename)[1]
        
        #add file extension and file path to directory
        
        if file_extension not in files_by_extension:
            files_by_extension[file_extension]=[]
        
        files_by_extension[file_extension].append(file_path)


# In[6]:


files_by_extension


# In[14]:


#create a folder for each file extension and move the files to respective folder

for file_extension,file_paths in files_by_extension.items():
    folder_name = f"{file_extension[1:].upper()}files"
    folder_path = os.path.join(desktop_path,folder_name)
    
    #create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    #moving the files to respective folders
    for file_path in file_paths:
        shutil.move(file_path,folder_path)


# In[ ]:




