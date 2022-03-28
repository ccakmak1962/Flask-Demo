from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! This is ay üssü alpha.</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# gunicorn --bind 0.0.0.0:5000 wsgi:app
