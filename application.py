from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hogyi bhai deploy app benstalk se siddharth got it"

@app.route('/about')
def about():
    return "This is a sample Flask app deployed on Beanstalk."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

