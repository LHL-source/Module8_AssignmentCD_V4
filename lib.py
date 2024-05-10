from flask import Flask
from werkzeug.utils import url_quote

app = Flask(__name__)

@app.route('/power/<int:x>/<int:y>')
def power(x, y):
    result = x ** y
    print("today is 8-5-2024 V2")
    return f"<p>Power of {x} and {y} is {result}</p>"

if __name__ == "__main__":
    app.run()