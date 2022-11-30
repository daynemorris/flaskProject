from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/convert_celsius_to_fahrenheit')
@app.route('/convert_celsius_to_fahrenheit/<celsius>')
def page_to_convert_celsius(celsius=0.0):
    fahrenheit = convert_celsius_to_fahrenheit(float(celsius))
    return f"{fahrenheit}"


@app.route('/convert_fahrenheit_to_celsius')
@app.route('/convert_fahrenheit_to_celsius/<fahrenheit>')
def page_to_convert_celsius(fahrenheit=0.0):
    celsius = convert_celsius_to_fahrenheit(float(fahrenheit))
    return f"{celsius}"


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


if __name__ == '__main__':
    app.run()
