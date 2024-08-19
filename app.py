from flask import Flask, request, jsonify, redirect
from quickSort import quickSort

app = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.json
    array = data.get('array')
    reverse = data.get('reverse', False)
    
    if array is None:
        return jsonify({'error': 'Array is required'}), 400
    
    sorted_array = quickSort(array, reverse=reverse)
    return jsonify({'sorted_array': sorted_array})

if __name__ == '__main__':
    app.run(debug=True)
