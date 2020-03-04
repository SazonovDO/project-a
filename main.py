from flask import Flask, render_template, request, redirect
from waitress import serve
import argparse
import datetime
from flask_login import LoginManager,current_user,login_required,login_user,logout_user
import models

all_clients = {}
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kndgkakjdjaclk9dlsknknl'
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/who_are_you')
@login_required
def wau_page():
    info = request.user_agent
    addr = request.remote_addr
    clients = []
    for key_client in all_clients:
        clients.append(all_clients[key_client])
    return render_template('who_are_u.html', info=info, addr=addr, clients=clients)

@app.route('/information')
def inf_page():
    return render_template('information.html')

@login_manager.user_loader
def load_user(user_id):
    user = models.User(user_id)
    return user


@app.route('/registration')
def reg_page():
    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def log_page():
    message = ''
    if request.method == 'POST':
        user_name = request.form.get('login')
        user_pass = request.form.get('password')
        if user_name == 'admin' and user_pass == '123':
            user = models.User(1)
            login_user(user)
            return redirect('/')
        else:
            message = 'not correct password'
    return render_template('login.html', message=message)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


def register_new_user(ip, info):
    global all_clients
    last_visit = datetime.datetime.today().strftime('%Y-%m-%d  %H:%M')
    new_key = '{}-{}'.format(ip, info)
    values = {'ip': ip, 'info': info, 'last_visit': last_visit}
    all_clients.update({new_key: values})

@app.route('/')
def index_page():
    ip = request.remote_addr
    info = request.user_agent
    register_new_user(ip, info)
    return render_template('index.html')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--prod', help='Use waitress WSGI instead flask server', action='store_true')
    args = parser.parse_args()

    if args.prod:
        serve(app, host='0.0.0.0', port=80)
    else:
        app.run(debug=True)
