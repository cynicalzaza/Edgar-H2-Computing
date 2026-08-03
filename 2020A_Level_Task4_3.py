
from flask import *
app=Flask(__name__)
people_name=[]
with open("people.txt","r") as file:#automatically closes the file
    for line in file:
        newline=line.split(",")
        people_name.append(newline)

@app.route("/")
def main():
            return render_template("2020_Task4_3.html")
@app.route("/name")
def full_name():
            return render_template("2020_Task4_3_1.html",name=people_name)

app.run()