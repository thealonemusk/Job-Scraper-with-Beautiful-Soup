from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                         '=submit&txtKeywords=python&txtLocation=usa').text

soup = BeautifulSoup(html_text, 'html.parser')

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    published_date = job.find('span', class_="sim-posted").span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
        skills = job.find('span', class_="srp-skills").text.replace(' ', '')
        more_info = job.header.h2.a['href']
        experience = job.find('ul', class_="top-jd-dtl clearfix").li.text.strip().replace('card_travel', '')  # Extracting experience required
        print(f'Company Name: {company_name.strip()}')
        print(f'Required Skills: {skills.strip()}')
        print(f'Experience Required: {experience}')
        print(f'More Info: {more_info}')
        print(f'Published Date: {published_date}')
        print('')

# Export the results to a text file
import os
os.chdir(r'C:\Users\Ashutosh Jha\OneDrive\Desktop')


with open('jobs.txt', 'w') as f:
    for job in jobs:
        published_date = job.find('span', class_="sim-posted").span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href']
            experience = job.find('ul', class_="top-jd-dtl clearfix").li.text.strip().replace('card_travel', '') # Extracting experience required
            f.write(f'Company Name: {company_name.strip()}\n')
            f.write(f'Required Skills: {skills.strip()}\n')
            f.write(f'Experience Required: {experience}\n')
            f.write(f'More Info: {more_info}\n')
            f.write(f'Published Date: {published_date}\n')
            f.write('\n')
