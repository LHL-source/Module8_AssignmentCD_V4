import lib
import json  # Import the json module

def test_power():
    with lib.app.test_request_context():
        # Simulate a request context to access app-specific functions like jsonify
        response = lib.power(2, 2)  # Get the response object directly
        assert response.get_json() == {'result': 4}  # Assert against the JSON data in the response
    