from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Helsingborg, Sweden',
    'salary': 'Kr. 50.000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Malmö, Sweden',
    'salary':'Kr. 60.000'
  },
  {
    'id': 3,
    'title': 'Devops Engineer',
    'location': 'Helsingborg, Sweden',
    'salary': 'Kr. 70.000'
  },
  {
    'id': 4,
    'title': 'Frontend Engineer',
    'location': 'Helsingborg, Sweden',
    'salary': 'Kr. 50.000'
  }
]

@app.route('/')
def hello_Salah():
  return render_template('home.html', jobs=JOBS, company_name='Salah')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)