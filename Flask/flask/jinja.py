### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask, render_template, request, redirect, url_for

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/success/<int:score>")
def success(score):
    res = "PASSED" if score >= 50 else "FAILED"
    return render_template("result.html", results=res)


@app.route("/successres/<int:score>")
def successres(score):
    res = "PASSED" if score >= 50 else "FAILED"
    data = {"score": score, "res": res}
    return render_template("result1.html", results=data)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["c"])
        datascience = float(request.form["datascience"])

        total_score = int((science + maths + c + datascience) / 4)

        return redirect(url_for("successres", score=total_score))

    return render_template("getresult.html")


if __name__ == "__main__":
    app.run(debug=True)
