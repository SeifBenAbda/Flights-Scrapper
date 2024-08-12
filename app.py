from flask import Flask, render_template, request
from api.routes.scraping_route import scrapping_bp, scrapping_endpoint_bp
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Enable CORS for all routes
app.register_blueprint(scrapping_bp)
app.register_blueprint(scrapping_endpoint_bp)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run(debug=True)
