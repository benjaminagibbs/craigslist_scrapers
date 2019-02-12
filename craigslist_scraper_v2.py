#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This code checks job postings on Bay Area Craigslist for several key terms, with an input option to add more.
# benjamingibbs.net        github.com/benjaminagibbs


# In[2]:


from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pyexcel_ods import get_data
from pyexcel_ods import save_data
import os
import csv


# In[3]:


#here are the keywords and optional additional input
keywords = ['lab assistant','graduate','associate engineer']


#if input("Want to add any search terms? (y/n) ") == 'y':
#       keywords.append(input("Cool, which ones? "))


# In[4]:


#here's the scrape
page = requests.get("https://sfbay.craigslist.org/d/jobs/search/jjj")
soup = BeautifulSoup(page.content, 'html.parser')
sortable_results = soup.find(id="sortable-results")
rows = sortable_results.find_all(class_= "rows")

jobs = rows[0]

#uncomment the following line for HTML reference 
#print(jobs.prettify())


# In[5]:


time = jobs.find_all("time",class_="result-date")
titles = jobs.find_all(class_="result-title hdrlnk")


# In[6]:


#here's a complete list of all postings for troubleshooting, just uncomment 'skinny'
datetime = []
post_title = []
post_link = []

for date in time:
   datetime.append(date.get("title"))

for title in titles:
    post_title.append(title.text)
    post_link.append(title.get("href"))


# In[7]:


skinny = pd.DataFrame({
    "When":datetime,
    "Title":post_title,
    "link":post_link,
})
#skinny


# In[8]:


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
            "link":goodjob_link
             })


print(good_jobs)


# In[9]:


#here we check the existing .ods file, remove duplicates from good_jobs, then append what's left
ospath = os.path.join(os.path.expanduser('~'),"Desktop","scraper-results.csv")


if good_jobs.shape[0] > 0:
    n = 0
    with open(ospath,'r') as csvfile:
        previous = csv.reader(csvfile, delimiter=',')
        if not any(good_jobs['title'].tolist() for row in previous):
            with open(ospath,'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([goodjob_time[n],goodjob_name[n],goodjob_link[n]])
        n = n + 1
    csvfile.close()
#new_set = previous.append(good_jobs)


# In[10]:


print("found",len(good_jobs['title'].tolist()),"jobs!")


# In[ ]:





# In[ ]:




