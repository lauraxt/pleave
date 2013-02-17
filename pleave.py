# all the imports
from __future__ import with_statement
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing



from flask import Flask
app = Flask(__name__)
app.config.from_envvar('PLEAVE_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route("/")
def show_companies():
    cur = g.db.execute('select name, leave_policy from company_and_policy order by id desc')
    companies = [dict(name=row[0], leave_policy=row[1]) for row in cur.fetchall()]
    return render_template('show_companies.html', companies=companies)

@app.route('/add', methods=['POST'])
def add_company():
    g.db.execute('insert into company_and_policy (name, parent, leave_policy, number_of_women_employees, number_of_employees, full_pay_days_off, applies_equally) values(?, ?, ?, ?, ?, ?, ?)',
                  [request.form['name'], request.form['parent'], request.form['leave_policy'],
                   request.form['number_of_women_employees'], request.form['number_of_employees'],
                   request.form['full_pay_days_off'], request.form['applies_equally']])
    g.db.commit()
    flash('New company was successfully posted')
    return redirect(url_for('show_companies'))

def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
