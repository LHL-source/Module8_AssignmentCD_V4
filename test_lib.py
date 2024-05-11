import lib

def test_power():
    with lib.app.test_request_context():
        # Simulate a request context to access app-specific functions like jsonify
        result = lib.power(2, 2)
        assert result == {'result': 4}  # Assuming jsonify wraps data in a dictionary
    
    
    