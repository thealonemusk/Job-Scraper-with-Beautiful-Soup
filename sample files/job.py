from bs4 import BeautifulSoup
# scrapes latest published job advertisement from a specific website and returns the job title and the link to the job
import requests


# the url of the website to be scraped
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                         '=submit&txtKeywords=python&txtLocation=usa').text
# print(html_text)
soup = BeautifulSoup(html_text, 'html.parser')
# print(soup.prettify())
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
# print(jobs)
for job in jobs:
    published_date = job.find('span', class_="sim-posted").span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
        skills = job.find('span', class_="srp-skills").text.replace(' ', '')
        more_info = job.header.h2.a['href']
        print(f'Company Name: {company_name.strip()}')
        print(f'Required Skills: {skills.strip()}')
        print(f'More Info: {more_info}')
        print(f'Published Date: {published_date}')
        # print(f'experience: {experience.strip()}')
        print('')

# export the results to a text file

import os
os.chdir(r'C:\Users\Ashutosh Jha\Desktop')
with open('jobs.txt', 'w') as f:
    f.write(f'Company Name: {company_name.strip()}')
    f.write(f'Required Skills: {skills.strip()}')
    f.write(f'More Info: {more_info}')
    f.write(f'Published Date: {published_date}')
    # f.write(f'experience: {experience.strip()}')
    f.write('')
