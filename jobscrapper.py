import requests
from bs4 import BeautifulSoup

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

so_url = f'https://stackoverflow.com/jobs?r=true&q='
wwr_url = f'https://weworkremotely.com/remote-jobs/search?term='
ro_url = f'https://remoteok.io/remote-dev+'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

#  stackoverflow_search_url = stackoverflow_url+term
#  weworkremotely_search_url = weworkremotely_url+term
#  remoteok_search_url = remoteok_url+f'{term}-jobs'

def get_so_jobs(term):
  so_search_url = so_url+term
  so_r = requests.get(so_search_url)
  print(f'Scrapping : {so_search_url}')
  so_soup = BeautifulSoup(so_r.text, 'html.parser')
  so_job_total = int(so_soup.find(class_='js-search-title').span.text.split(' ')[0])
  if so_job_total == 0:
    print('No jobs')
    return
  else:
    print(f'Total Jobs: {so_job_total}')
  pagenation = int(so_soup.find(class_='s-pagination').a['title'].split(' ')[-1])
  job_list = []
  for ii in range(pagenation):
    so_job_soup = None
    if ii != 0:
      so_page_r = requests.get(so_search_url+f'&pg={ii+1}')
      so_job_soup = BeautifulSoup(so_page_r.text, 'html.parser')
      pass
    else:
      so_job_soup = so_soup
      pass
    print(f'Page: {ii+1} of {pagenation}')
    so_job_list = so_job_soup.find(class_='js-search-results').find(class_='grid--cell').find_all(class_='js-result')    
    for job in so_job_list:
      title = job.find(class_='fs-body3').a['title']
      href = 'https://stackoverflow.com'+job.find(class_='fs-body3')  .a['href']
      company = job.find(class_='fs-body1').find('span').text
      job_list.append({
        'title':title,
        'company':company,
        'href':href,
      })
  return job_list

def get_jobs(term):
  so_jobs = get_so_jobs(term)
  return so_jobs