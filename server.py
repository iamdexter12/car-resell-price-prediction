from logging import debug
from os import name
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import util


app = Flask(__name__)
CORS(app)

@app.route('/get_column_names')
def get_column_names():
    response = {'Columns': util.column_names()}
    return response

@app.route('/predict_car_price',methods=['POST'])
def predict_car_price():
    year = float(request.form['YEAR'])
    kilometers_driven= float(request.form['KILOMETERS_DRIVEN'])
    mileage= float(request.form['MILEAGE'])
    engine = float(request.form['ENGINE'])
    power = float(request.form['POWER'])
    seats = float(request.form['SEATS'])
    company = request.form['COMPANY']
    name = request.form['NAME'] 
    location = request.form['LOCATION']
    fuel_type= request.form['FUEL_TYPE']
    transmission = request.form['TRANSMISSION']
    owner_type = request.form['OWNER_TYPE'] 
    
    response = jsonify({'estimated_price': util.get_predict_price(year, kilometers_driven, mileage, engine, power, seats, company, name, location, fuel_type, transmission, owner_type)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run(host='127.0.0.1', port=5001)
