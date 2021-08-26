import re
from app import app
from flask import render_template, request
from models.event import *
from models.event_app import events, add_new_event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events = events)

@app.route('/events', methods = ['POST'])
def add_event():
    event_date = request.form['date']
    event = request.form['event']
    guest_number = request.form['guest_number']
    room_location = request.form['room_location']
    description = request.form['description']
    new_event = Event(event_date, event, guest_number, room_location, description)
    add_new_event(new_event)
    return render_template('index.html', title="Home", events=events)