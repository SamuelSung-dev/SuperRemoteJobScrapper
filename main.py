from flask import Flask, render_template, request, redirect, send_file
from jobscrapper import get_jobs
from exporter import save_to_file

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
      jobs = get_jobs(term)
      if jobs != []:
        db[term] = jobs
  if term in db.keys():
    return render_template('search.html',term = term, job_list=db[term])
  else:
    return render_template('search.html',term = term, job_list=[])

@app.route('/export')
def export():
  try:
    term=request.args.get('term')
    if not term:
      raise Exception() 
    term = term.lower()
    if term not in db.keys():
      raise Exception()
    save_to_file(term, db[term])
    return send_file(f'{term}.csv', mimetype='text/csv', attachment_filename=f'{term}.csv', as_attachment=True)
  except:
    return redirect('/')
  pass

@app.route('/')
def home():
  return render_template('home.html')

app.run(host='0.0.0.0')