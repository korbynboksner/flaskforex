from flask import Flask, render_template, request, redirect, session , flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *
app = Flask(__name__)
app.config['SECRET_KEY'] = "s"

cr = CurrencyRates(force_decimal=True)
cc = CurrencyCodes()

possible_curr=['EUR','IDR' , 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']

@app.route("/")
def start():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def set_up():
    c1=request.form['c1']
    c2=request.form['c2']
    a=request.form['amount']
    if possible_curr.count(c1)==0 or possible_curr.count(c2)==0 or a == '' or a <='0':
        if possible_curr.count(c1)==0:
            flash(f"{c1} is not a valid code")
        if possible_curr.count(c2)==0:
            flash(f"{c2} is not a valid code")
        if a <='0':
            flash("Invalid amount")
        return redirect("/")

    rv = cr.convert(c1, c2, Decimal(a))
    rs = cc.get_symbol(c2)

    return render_template("result.html", result_value=rv, result_symbol=rs )








