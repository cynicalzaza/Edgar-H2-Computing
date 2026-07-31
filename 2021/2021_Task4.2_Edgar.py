import sqlite3
from flask import *
conn=sqlite3.connect("Task4.db")
cursor=conn.cursor()
cursor.execute("""SELECT competitor.name,scores.score
FROM  competitor ,scores
WHERE competitor.id=scores.id and scores.round=1
ORDER BY scores.score DESC""")
score1=cursor.fetchall()
cursor.execute("""SELECT competitor.name,scores.score
FROM  competitor ,scores
WHERE competitor.id=scores.id and scores.round=2
ORDER BY scores.score DESC""")
score2=cursor.fetchall()
cursor.execute("""SELECT competitor.name,scores.score
FROM  competitor ,scores
WHERE competitor.id=scores.id and scores.round=3
ORDER BY scores.score DESC""")
score3=cursor.fetchall()
conn.close()
print(score1)
app=Flask(__name__)
@app.route("/1")
def scores1():
    return render_template("Task4_2_Edgar_1.html",score1=score1)
@app.route("/2")
def scores2():
    return render_template("Task4_2_Edgar_2.html",score2=score2)
@app.route("/3")
def scores3():
    return render_template("Task4_2_Edgar_3.html",score3=score3)
app.run()

