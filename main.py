import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

stackoverflow_url = f'https://stackoverflow.com/jobs?r=true&q='
weworkremotely_url = f'https://weworkremotely.com/remote-jobs/search?term='
remoteok_url = f'https://remoteok.io/remote-dev+'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""


app = Flask('SuperRemoteJobScrapper')

@app.route('/search')
def search():
  term = request.args.get('term')
  stackoverflow_search_url = stackoverflow_url+term
  weworkremotely_search_url = weworkremotely_url+term
  remoteok_search_url = remoteok_url+f'{term}-jobs'
  print(stackoverflow_search_url)
  print(weworkremotely_search_url)
  print(remoteok_search_url)

  return render_template('search.html',term = term)

@app.route('/')
def home():
  return render_template('home.html')

app.run(host='0.0.0.0')