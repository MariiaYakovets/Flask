from flask import Flask, render_template, redirect

app = Flask('Application')

@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template('login.html')

@app.route("/")
def main():
    return redirect("/login")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('unknown_page.html')