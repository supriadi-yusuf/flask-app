from flask import Flask
from configure import configure

app = Flask(__name__)

@app.route( '/', methods=['GET', 'POST'])
def index():
    return 'Welcome'

if __name__ == '__main__':
    configure(app)
    print(app.config['SECRET_KEY'])
    app.run(debug=True) # "debug = True" means if error is detected, app will be restarted