from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculate', methods = ['POST'])
def calculate():
    number = request.form.get('number')
    number = int(number)
    for i in range(2, number):
        if number % i == 0:
            return 'The number is not prime!'
    return 'The number is prime!'

@app.route('/')
def home():
    return render_template('home.html')