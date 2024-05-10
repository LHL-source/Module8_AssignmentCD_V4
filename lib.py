from flask import Flask
#from werkzeug.urls import url_quote

app = Flask(__name__)

@app.route('/power/<int:x>/<int:y>')
def power(x, y):
    result = x ** y
    print("today is 10-5-2024 V3")
    return result
    #return f"<p>Power of {x} and {y} is {result}</p>"

if __name__ == "__main__":
    app.run()