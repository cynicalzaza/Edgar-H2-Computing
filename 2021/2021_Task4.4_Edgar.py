import sqlite3
from flask import *
conn=sqlite3.connect("Task4.db")
cursor=conn.cursor()
cursor.execute("""SELECT  competitor.name , SUM(scores.score) 
FROM competitor,scores 
WHERE competitor.id=scores.id 
GROUP BY competitor.name""")
results=cursor.fetchall()
app=Flask(__name__)
@app.route("/Q")
def qualified():
    return render_template("Task4_4_Edgar.html",results=results)
app.run()