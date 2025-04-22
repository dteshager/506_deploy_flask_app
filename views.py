from flask import Blueprint
import datetime
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>This is the home page!</h1>"
@views.route('/dereje')
def name():
    return "<h1>Hello from Dereje!</h1>"

@views.route('/datetime')
def time():
    now = datetime.datetime.now()
    return f"<h1>Current Date and Time: {now}</h1>"