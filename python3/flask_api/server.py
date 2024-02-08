from flask import Flask, jsonify, request

app = Flask(__name__)

key_values = {'k1': 'v1',
              'k2': 'v2'}

# get all key values
@app.route('/api/v1/key_values', methods=['GET'])
def get_key_values():
    return jsonify(data), 400

# get a key's value
@app.route('/api/v1/key_values/<key>', methods=['GET'])
def get_value(key):
    if key not in data:
        return jsonify({'error': "Key not found"}), 404
    return jsonify(data[key])

# create new key_value pair
@app.route('/api/v1/key_values', methods=['POST'])
def create_key_value():
    if not request.json or not 'key' in request.json or not 'value' in request.json:
        return jsonify({'error': 'Key and value are required'}), 400
    key_values[request.json['key']] = request.json['value']
    return jsonify({request.json['key']: request.json['value']}), 201  # success, new resource created

# update an existing key
@app.route('/api/v1/key_values/<key>', methods=['PUT'])
def update_key_value(key):
    if key not in key_values:
        return jsonify({'error': 'Key not found'}), 404
    if not request.json or not 'value' in request.json:
        return jsonify({'error': 'No value provided'}), 400
    key_values[key] = request.json['value']
    return jsonify({key: request.json['value']})

# delete a key_value pair
@app.route('/api/v1/key_values/<key>', methods=['DELETE'])
def delete_key_value(key):
    if key not in key_values:
        return jsonify({'error': 'Key not found'}), 404
    del(key_values[key])
    return jsonify({'result': True}), 200


if __name__ == '__main__':
    app.run(debug=True)

