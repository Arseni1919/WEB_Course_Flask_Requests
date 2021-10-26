from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)

@app.route('/catalog', methods=['POST', 'PUT', 'DELETE', 'GET'])
def catalog_func():
    curr_user = {'firstname': "Ariel", 'lastname': "Perchik", 'wok': 'BGU', 'adress': 'Israel'}

    current_method = request.method
    if 'username' in session:
        user_name, last_name = session['username'], session['lastname']
    else:
        if current_method == 'GET':
            if 'username' in request.args:
                user_name = request.args['username']
                last_name = request.args['lastname']
            else:
                user_name, last_name = '', ''
        elif current_method == 'POST':
            if 'username' in request.form:
                user_name = request.form['username']
                last_name = request.form['lastname']
            else:
                user_name, last_name = '', ''
        else:
            user_name, last_name = '', ''
        session['username'] = ''
        session['lastname'] = ''
    return render_template('catalog.html',
                           curr_user=curr_user,
                           user_name=user_name,
                           last_name=last_name,
                           current_method=current_method)


@app.route('/customers', methods=['GET', 'POST', 'DELETE', "PUT"])
def hello_cart():
    # do something
    customer_registrated = False
    if customer_registrated:

        return redirect(url_for('index'))
    else:
        return 'You need to LOGIN'


@app.route('/about')
def hello_about():
    # do something
    return render_template('about.html')


@app.route('/log_out')
def log_out():
    session['username'] = ''
    session['lastname'] = ''
    return redirect(url_for('index'))


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'GET':
        return render_template('log_in.html')
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['lastname'] = request.form['lastname']
    return redirect(url_for('index'))


@app.route('/friends')
def hello_friends():
    # do something
    curr_user = {'firstname': "Ariel", 'lastname': "Perchik", 'wok': 'BGU', 'adress': 'Israel'}
    return render_template('friends.html',
                           curr_user=curr_user,
                           hobbies=['Prog', 'Paint', "IEM", "Swim", "Sleep"],
                           degree=('B.Sc', 'M.Sc')
                           )

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
