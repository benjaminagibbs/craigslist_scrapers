# craigslist_scrapers

Currently, this repository holds several editions of a job scraper, both in .py and .ipynb formats. Using BeautifulSoup, the html file is pulled from craigslist's jobs page for the San Francisco bay area. The titles of the jobs are checked for keywords, currently "graduate", "lab assistant", and "associate engineer". Hits are returned along with a link and exact time of posting.

version 1 (v1) of the script is a proof of concept that returns a list and includes the option to input keywords whenever the program is run. This script is intended to be run manually, and mostly exists as a troubleshooting tool for the next version of the script, which is considerably more automated.

version 2 (v2) saves results on a .csv file on the desktop of a linux system. The .csv file is checked for repeats before new entries are saved. The additional keyword input feature was removed so that the script can be run without a user. For automation, a bash excecutable is run by chronjob, a program scheduling utility on Linux (http://1selfsolutions.com/scheduling-python-script-linux-cron-job/)
