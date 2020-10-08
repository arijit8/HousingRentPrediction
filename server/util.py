import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index = __locations.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0],2)

def load_save_artifcats():
    global __locations, __data_columns, __model

    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_cols']
        __locations = __data_columns[3:]

    with open('./artifacts/bangalore home price model.pickle', 'rb') as f:
        __model = pickle.load(f)


if __name__ == "__main__":
    load_save_artifcats()
    get_location_names()
    print(get_estimated_price('1st Phase JP Nagar',2000,3,2))