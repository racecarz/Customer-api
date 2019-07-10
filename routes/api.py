#!/usr/bin/env python3
import flask
from flask_wtf import FlaskForm
from database.model import Customers
from helpers import object_sanitizer
from flask_mail import Message


api = flask.Blueprint('customer_api', __name__)


@api.route("/")
def index():
    return flask.jsonify({'text':'hello'})

@api.route("/email")
def email():
    usr_data = Customers.query.order_by(Customers.username).all()
    usr_data_str = ''
    for c in usr_data:
        usr_data_str.join(c.__str__())
    msg = Message(usr_data, sender="carson.zachary@heb.com")
    msg.add_recipient("carson.zachary@heb.com")
    mail.send(msg)

    Customers.update_time()

    return object_sanitizer(msg)

@api.route("/view/<id>")
def return_customer(id):
    cust = Customers.query.filter_by(id=id).first()
    cust_dict = object_sanitizer(cust )
    return flask.jsonify(cust_dict)

@api.route("/view")
def customers():
    cust = Customers.query.all()
    print(cust)
    cust_dict = {}
    for c in cust:
        cust_dict[c.id] = object_sanitizer(c)
    return flask.jsonify(cust_dict)
