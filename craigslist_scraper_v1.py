#!/usr/bin/env python
# coding: utf-8

# In[9]:


#This code checks job postings on Bay Area Craigslist for several key terms, with an input option to add more.
# benjamingibbs.net        github.com/benjaminagibbs


# In[10]:


from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[11]:


#here are the keywords and optional additional input
keywords = ['lab assistant','graduate','associate engineer']
if input("Want to add any search terms? (y/n) ") == 'y':
        keywords.append(input("Cool, which ones? "))


# In[12]:


#here's the scrape
page = requests.get("https://sfbay.craigslist.org/d/jobs/search/jjj")
soup = BeautifulSoup(page.content, 'html.parser')
sortable_results = soup.find(id="sortable-results")
rows = sortable_results.find_all(class_= "rows")

jobs = rows[0]

#uncomment the following line for HTML reference 
#print(jobs.prettify())


# In[13]:


time = jobs.find_all("time",class_="result-date")
titles = jobs.find_all(class_="result-title hdrlnk")


# In[14]:


#here's a complete list of all postings for troubleshooting, just uncomment 'skinny'
datetime = []
post_title = []
post_link = []

for date in time:
   datetime.append(date.get("title"))

for title in titles:
    post_title.append(title.text)
    post_link.append(title.get("href"))


# In[15]:


skinny = pd.DataFrame({
    "When":datetime,
    "Title":post_title,
    "link":post_link,
})
#skinny


# In[29]:


#Here's the parse and check
goodjob_name = []
goodjob_time = []
goodjob_link = []

i = 0

for title in titles:
    if any(part in title.text for part in keywords):
        goodjob_name.append(title.text)
        goodjob_time.append(datetime[i])
        #the link is pulled here but not yet included in the final output.
        goodjob_link.append(title.get("href"))
    i=i+1
    
good_jobs = pd.DataFrame({
            "title":goodjob_name,
            "date":goodjob_time,
             })

pd.reset_option('display.max_columns')
print(good_jobs)


# In[21]:





# In[ ]:




