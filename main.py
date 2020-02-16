from flask import Flask, render_template, request, redirect
from waitress import serve
import argparse

app = Flask(__name__)

@app.route('/who_are_you')
def wau_page():
    info = request.user_agent
    addr = request.remote_addr
    return render_template('who_are_u.html', info=info, addr=addr)

@app.route('/information')
def inf_page():
    return render_template('information.html')

@app.route('/registration')
def reg_page():
    return render_template('registration.html')

@app.route('/')
def index_page():
    return render_template('index.html')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--prod', help='Use waitress WSGI instead flask server', action='store_true')
    args = parser.parse_args()

    if args.prod:
        serve(app, host='0.0.0.0', port=80)
    else:
        app.run()
