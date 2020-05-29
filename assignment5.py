from flask import Flask, render_template, request, g
import sqlite3

app = Flask (__name__)

# conn = sqlite3.connect('flowers.db')
# c = conn.cursor()

DATABASE = 'flowers.db'
def get_db():
   db = getattr(g, '_database', None)
   if db is None:
       db = g._database = sqlite3.connect(DATABASE)
   return db

@app.teardown_appcontext
def close_connection(exception):
   db = getattr(g, '_database', None)
   if db is not None:
       db.close()

@app.route('/')
def index():
   c = get_db().cursor()
   c.execute('SELECT COMNAME FROM FLOWERS')
   all_flowers = c.fetchall()
   return render_template("index.html", all_flowers=all_flowers)

@app.route('/update')
def update():
   c = get_db().cursor()
   # this just gets the data from the db

   c = get_db().cursor()
   c.execute('SELECT GENUS, SPECIES, COMNAME FROM FLOWERS')
   genus_flowers = c.fetchall()
   return render_template("update.html", genus_flowers=genus_flowers)

@app.route('/insert')
def insert():
   c = get_db().cursor()
   # this just gets the data from the db

   c = get_db().cursor()
   c.execute('SELECT NAME, PERSON, LOCATION, SIGHTED FROM SIGHTINGS')
   sighting_flowers = c.fetchall()
   return render_template("insert.html", sighting_flowers=sighting_flowers)

@app.route('/query')
def query():
   c = get_db().cursor()
   # this just gets the data from the db



   c = get_db().cursor()
   c.execute('SELECT NAME, PERSON, LOCATION, SIGHTED FROM SIGHTINGS ORDER BY SIGHTED DESC')

   #c.execute("'SELECT name, person, location, sighted FROM (select name, person, location sighted, row_number() over (partition by name order by sighted desc) as sight_rank from sightings) ranked where sight_rank <= 10 '")
   #c.execute('SELECT t.NAME, t.sighted FROM SIGHTINGS AS t WHERE t.sighted IN (SELECT sighted FROM SIGHTINGS WHERE SIGHTINGS.NAME = t.NAME ORDER BY SUBSTR(sighted, 7, 2) || - || SUBSTR(sighted, 1, 5) DESC LIMIT 2 ) ORDER BY t.NAME, t.sighted DESC')

   sighting_flowers = c.fetchall()
   return render_template("query.html", sighting_flowers=sighting_flowers)



@app.route('/profile/<name>')
def profile(name):
   return render_template("profile.html", name=name)


if __name__ == "__main__":
   app.run(debug=True)
