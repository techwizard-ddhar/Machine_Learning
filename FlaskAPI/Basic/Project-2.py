from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = '8ee2792af814a884dac39ac88815f5db'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'London')
    weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    
    response = requests.get(weather_api_url)
    
    if response.ok:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'message': 'Weather data not available for the specified city.'}), 404

if __name__ == '__main__':
    app.run(debug=True)


