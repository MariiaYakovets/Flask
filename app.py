from flask import Flask, render_template, url_for
import random

app = Flask('app.py')

@app.route("/")
def start():
    return render_template('index.html')

@app.route("/cat")
def cat():
    n_cat = random.randint(1,10)
    return render_template('cat.html', n_cat = n_cat)

@app.route("/cat/<number>")
def cat_two(number):
    return render_template("cat_number.html", cat_num = number)