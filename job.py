from bs4 import BeautifulSoup
# scrapes latest published job advertisement from a specific website and returns the job title and the link to the job
import requests
import time
import datetime
import smtplib
from email.message import EmailMessage
import os

# the url of the website to be scraped
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=usa').text
print(html_text)
