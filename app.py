from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def random_number():
    number = random.randint(1, 6)
    return f'<h1>Ваше випадкове число: {number}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
