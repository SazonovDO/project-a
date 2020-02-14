from flask import Flask, render_template, request, redirect
from waitress import serve
import argparse

app = Flask(__name__)


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
