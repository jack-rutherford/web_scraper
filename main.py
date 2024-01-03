import time
from bs4 import BeautifulSoup
import requests



# Add it so you can filter multiple skills
print('Put some skill that you are not familiar with.')
print('Separate the skills with a comma (python, django, linux)')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
# unfamiliar_skill = unfamiliar_skill.split(',')
# print(f'Filtering out {*unfamiliar_skill,}')


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text.strip()
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').replace(',', ', ')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()}')
                    f.write(f'Required Skills: {skills.strip()}')
                    f.write(f'More Info: {more_info}')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60) # 10 mins

