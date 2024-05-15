from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/power/<int:x>/<int:y>')
def power(x, y):
    result = x ** y
    print("today is 10-5-2024 V3")
    return jsonify(result=result)  # Return a JSON response with the result

@app.route('/health_V2')
def health_check():
    # Check if application components are healthy
    # Return a JSON response indicating health status
    return jsonify(status='ok')

if __name__ == "__main__":
    app.run()