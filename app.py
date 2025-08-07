from flask import Flask, request, jsonify
from geopy.distance import geodesic
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/check_proximity', methods=['POST'])
def check_proximity():
    data = request.get_json()
    warehouse_coords = tuple(data['warehouse'])  # [lat, lng]
    delivery_coords = tuple(data['delivery'])    # [lat, lng]
    radius = data.get('radius', 250)             # in meters

    distance = geodesic(warehouse_coords, delivery_coords).meters
    is_within_range = distance <= radius

    return jsonify({
        'distance': round(distance, 2),
        'within_range': is_within_range
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))    # Use PORT from Render or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)