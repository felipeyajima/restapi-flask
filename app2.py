from flask import Flask
from flask_restful import Resource, Api
from prometheus_flask_exporter import RESTfulPrometheusMetrics

app = Flask(__name__)
api = Api(app)

metrics = RESTfulPrometheusMetrics(app, api)

@app.route('/')
def index():
    return 'Olá mundo!'

if __name__ == '__main__':
    app.run()