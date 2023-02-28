from flask import Flask, render_template, request, redirect, session , flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *
app = Flask(__name__)
from app import app
from unittest import TestCase

class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home(self):
        with app.test_clinet() as client:
            res=client.get('/')
            html=res.get_data(as_test=True)

            self.assertEqual(res.status_code, 200)
            self.assertIN('<h1 id="title">Forex Converter</h1>', html)
    def test_post(self):
        with app.test_client() as client:
            res=client.post('/result', data=({'c1': 'USD'},{'c2':'USD' }, {'amount': Decimal(10)}))
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1 id="result"> The result is $ 10 </h1>')