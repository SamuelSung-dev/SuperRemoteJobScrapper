import csv

def save_to_file(term, jobs):
  with open(f'{term}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',)
    writer.writerow(jobs[0].keys())
    for job in jobs:
      writer.writerow(job.values())