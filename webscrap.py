from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get('https://www.myjobmag.co.ke/').text
soup = BeautifulSoup(html_text,'lxml')
job_info = soup.find_all('li', class_  =  'job-info')
print('JOBS POSTED TODAY')
job_list = []
for job in job_info:
    title = job.find('li',class_ = 'mag-b')
    posted = job.find(id = 'job-date')
    description = job.find('li',class_ = 'job-desc')
    job_item = {
        'Job Title':title.text,
        'Date Posted': posted.text,
        'Job Description': description.text
    }
    job_list.append(job_item)

df = pd.DataFrame(job_list)
df.to_excel('jobs_kenya.xlsx', engine='openpyxl')




