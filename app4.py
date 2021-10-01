from flask import Flask, request, render_template,  make_response, session
app = Flask(__name__)
app.secret_key = '0648df38f3da4cba904ba383359c97266bd43bb55d023d9245397d22baea66a9'


@app.route("/")
def session_count():
    counter = 0
    if session.get('visit'):
        counter = session['visit']
    else:
        session['visit'] = 0
    response = make_response((render_template('index.html', visit=counter)))
    session['visit'] += 1
    return response


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return """
        <form action='http://127.0.0.1:5000/login', method='POST'>
            <input name = "username">
            <input type = "submit">
        </form>
        """
    elif request.method == 'POST':
        username = request.form['username']
        response = make_response((render_template('success_authorisation.html', user=username)))
        return response


@app.route("/logout")
def logout():
    visit = "!"
    if 'visit' in session:
        session.pop('visit', None)
        response = make_response((render_template('no_visit.html', visit=visit)))
        return response


if __name__ == 'main':
    app.run(debug=True)
