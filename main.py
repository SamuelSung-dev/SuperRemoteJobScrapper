from flask import Flask, render_template, request, redirect
from jobscrapper import get_jobs

app = Flask('SuperRemoteJobScrapper')

db = {}

@app.route('/search')
def search():
  term = request.args.get('term')
  if term == '':
    return redirect('/')
  else:
    if term not in db.keys():
      db[term] = get_jobs(term)

  return render_template('search.html',term = term, job_list=db[term])

@app.route('/')
def home():
  return render_template('home.html')

app.run(host='0.0.0.0')