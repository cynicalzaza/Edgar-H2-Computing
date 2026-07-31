import sqlite3
from flask import *
conn=sqlite3.connect("Task4.db")
cursor=conn.cursor()
cursor.execute("""SELECT competitor.name,round(avg(scores.score),2)
FROM competitor,scores
WHERE competitor.id=scores.id
GROUP BY competitor.name""")
result=cursor.fetchall()
conn.close()
app=Flask(__name__)
@app.route("/m")
def mean():
    return render_template("Task4_3_Edgar.html",result=result)
app.run()