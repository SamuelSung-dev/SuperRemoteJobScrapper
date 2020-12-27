from flask import Flask, render_template, request, redirect, send_file, after_this_request
from jobscrapper import get_jobs
from exporter import save_to_file
from os import remove

app = Flask('SuperRemoteJobScrapper')

db = {}

@app.route('/search')
def search():
  term = request.args.get('term')
  if term == '':
    return redirect('/')
  else:
    term = term.lower()
    if term not in db.keys():
      db[term] = get_jobs(term)
  return render_template('search.html',term = term, job_list=db[term])

@app.route('/export')
def export():
  try:
    term=request.args.get('term')
    if not term:
      raise Exception() 
    term = term.lower()
    if term not in db.keys():
      raise Exception()
    if len(db[term]) == 0:
      raise Exception()
    save_to_file(term, db[term])

    @after_this_request
    def cleanup(response):
      remove(f'{term}.csv')
      return response

    return send_file(f'{term}.csv', mimetype='text/csv', attachment_filename=f'{term}.csv', as_attachment=True)
  except:
    return redirect('/')
  pass

@app.route('/')
def home():
  return render_template('home.html')

app.run(host='0.0.0.0')