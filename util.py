import pickle
import json
import numpy as np

_data_columns = None
_model = None

def get_predict_price(year, kilometers_driven, mileage, engine, power, seats, company, name, location, fuel_type, transmission, owner_type):
    input = np.zeros(len(_data_columns))
    input[0] = year
    input[1] = kilometers_driven
    input[2] = mileage
    input[3] = engine
    input[4] = power
    input[5] = seats

    company_index = _data_columns.index(company)
    input[company_index] = 1
    
    name_index = _data_columns.index(name)
    input[name_index] = 1
    
    location_index = _data_columns.index(location)
    input[location_index] = 1
    
    fuel_type_index = _data_columns.index(fuel_type)
    input[fuel_type_index] = 1
    
    transmission_index = _data_columns.index(transmission)
    input[transmission_index] = 1
    
    owner_type_index = _data_columns.index(owner_type)
    input[owner_type_index] = 1

    return _model.predict([input])[0]

def load_artifacts():
    global _data_columns
    global _model
    
    print('Loading Artifacts...')

    with open('./columns.json','r') as f:
        _data_columns = json.load(f)['data_columns']

    with open('./car_resell_prices_model.pickle','rb') as f:
        _model = pickle.load(f)

    print('Artifacts...Loaded')


def column_names():
    return _data_columns

load_artifacts()
print(get_predict_price(10, 5000, 10, 1582, 58.16, 6.0, 'bentley', 'other', 'mumbai', 'diesel', 'automatic', 'second'))
