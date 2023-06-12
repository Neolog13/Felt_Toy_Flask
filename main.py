from flask import Flask, render_template, url_for, request

app = Flask(__name__)

#menu = ['Orange', 'Yellow', 'Green'] это не активные ссылки. Вместо этого пропишем список словарей
menu = [{"name": "Toys", "url": "toys"},
        {"name": "Promotional product", "url": "prom-product"},
        {"name": "Feedback", "url": "contact"}]


@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="About store", menu=menu)


@app.route("/profile/<username>")
def profile(username, path):
    return f"User: {username}, {path}"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        print(request.form)
        #print(request.form[username]) можно брать только конкретное поле
    return render_template('contact.html', title = "Feedback", menu=menu)

# Способы описания url (int, float, path(любые допустимые символы URL + символ слэша(/)))
# Конвертеры можно комбинировать.
# @app.route("/url/<variable>")


# искусственное создание контекста запроса без активации веб-сервера(без последних 2х строк)
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username="vladimir"))

if __name__ == '__main__':
    app.run(debug=True)

