from flask import Flask, jsonify, request
import util
from flask_cors import CORS, cross_origin
app = Flask( __name__ )
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/get_location_names')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/predict_home_price', methods = ['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response

if __name__ == "__main__":
    util.load_save_artifcats()
    print('Starting python Flask server........')
    app.run()