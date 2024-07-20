from flask import Flask, render_template, redirect, request, make_response

# создаем приложение
app = Flask('Application')

# создаем путь по ссылке /login и разрешаем принимать гет и пост запросы
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == 'GET':
        # по ссылке возвращаем шаблон html 
        return render_template('login.html')
    # если пост запрос
    if request.method == 'POST':
        print(request.json)
        # по окончанию обработки - дать ответ, 200 код
        return make_response('success', 200)
    
    
# создаем путь по ссылке / и делаем с него автоматическую переадрессовку на ссылку /login
@app.route("/")
def main():
    return redirect("/login")

# при возникновении ошибки, возвращаем шаблон html 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('unknown_page.html')