from flask import *
app=Flask(__name__)
@app.route("/")
def main():
    return render_template("Task4_1_Edgar.html")
app.run()
app.close()