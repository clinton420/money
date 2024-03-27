
# A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello from Flask!'

from flask import Flask, jsonify, request

app = Flask(__name__)

# Route 1: Welcome message
@app.route('/')
def index():
    return jsonify({'message': 'My name is Clinton and my Student:200584976!'})

# Route 2: Sample data
@app.route('/data')
def get_data():
    data = {'message': 'My name is Yash and my Student:200579052!'}
    return jsonify(data)

# Route 3: Dynamic route with parameter
@app.route('/user/<username>')
def get_user(username):
    return jsonify({'username': username})


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.json
        # Extract query text
        query_text = data.get('queryResult', {}).get('queryText', 'No query text provided')
        # Extract fulfillment text
        fulfillment_text = data.get('queryResult', {}).get('fulfillmentText', 'No fulfillment text provided')
        # Return the query and fulfillment text in the response
        response_data = {
            'query_text': query_text,
            'fulfillment_text': fulfillment_text
        }
        return jsonify(response_data)
    else:
        return jsonify({'error': 'Request must be in JSON format'}), 400



if __name__ == '__main__':
    app.run(debug=True)
