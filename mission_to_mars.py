#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Scrape Mars Data: The News
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time
from IPython.display import Image, display


# In[2]:


#This is the path to the executable file we'll be using to automate our browser. This line isn't vital to our code
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # NASA Mars News

# In[3]:


# Visit the red planet science site
url = "https://redplanetscience.com/"
browser.visit(url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, "lxml")


# In[5]:


news = soup.find("div", {"id": "news"})


# In[6]:


rows = (news.find_all("div", {"class", "row"}))
first_row = rows[0]

# Retrieve article title and preview paragraph
news_title = first_row.find("div", {"class", "content_title"}).text
news_paragraph = first_row.find("div", {"class": "article_teaser_body"}).text

print(news_title)
print(news_paragraph)


# # JPL Mars Space Images - Featured Image

# In[7]:


# Visit the space images-mars site
url = "https://spaceimages-mars.com/"
browser.visit(url)


# In[8]:


# HTML object
html = browser.html
soup = BeautifulSoup(html, "lxml")


# In[9]:


image = soup.find("img", {"class": "headerimage"})
featured_image_url = url + image["src"]
print(featured_image_url)


# In[10]:


# Display image
display(Image(featured_image_url))


# # Mars Facts

# In[11]:


url = "https://galaxyfacts-mars.com/"
browser.visit(url)


# In[12]:


html = browser.html
dfs = pd.read_html(html)


# In[13]:


len(dfs)


# In[14]:


dfs[0]


# In[15]:


dfs[1]


# In[16]:


facts = dfs[1]
facts = facts.set_index(0).T
facts.columns = [x.strip(":") for x in facts.columns]
facts


# In[17]:


facts_json = json.loads(facts.to_json(orient="records"))
facts_json


# #  Mars Hemispheres

# In[18]:


# Visit the mars hemisphere site
url = "https://marshemispheres.com/"
# Open Website using splinter
browser.visit(url) 


# In[19]:


# HTML object
html = browser.html
soup = BeautifulSoup(html, "lxml")
# Print (soup.prettify())


# In[20]:


# Retrieve all items with hemisphere info
hemis = soup.find_all("div", {"class":"item"})
len(hemis)


# In[21]:


# For Loop Grab the Title and Image Path
hemi_info = []
for hemi in hemis:
    hemi_url = url + hemi.find("a", {"class": "itemLink"})["href"]
    browser.visit(hemi_url)
    time.sleep(1)
    
    html = browser.html
    soup = BeautifulSoup(html, "lxml")
    
    link = url + soup.find("img", {"class", "wide-image"})["src"]
    title = soup.find("h2", {"class", "title"}).text
    
    data = {
        "img_url": link,
        "title": title
    }
    
    hemi_info.append(data)


# In[22]:


# Hemisphere Information
hemi_info


# In[23]:


# Closing Browser
browser.quit()


# In[24]:


news_title = first_row.find("div", {"class", "content_title"}).text
news_paragraph = first_row.find("div", {"class": "article_teaser_body"}).text


# In[25]:


mars_data = { 
    "news_title": news_title,
    "news_paragraph": news_paragraph,
    "hemi_info": hemi_info
    }


# In[26]:


mars_data['hemi_info'][0]['img_url']


# # Combine

# In[27]:


final_data = {
    "news_title": news_title,
    "news_paragraph": news_paragraph,
    "featured_image_url": featured_image_url,
    "mars_facts": facts_json,
    "hemispheres": hemi_info
}

print(final_data)


# In[ ]:





# In[ ]:




