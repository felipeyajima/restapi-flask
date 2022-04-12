from flask import Flask
from flask_restful import Resource, Api
from resources.jornada import Jornadas, Jornada
from prometheus_flask_exporter import RESTfulPrometheusMetrics

app = Flask(__name__)
api = Api(app)

metrics = RESTfulPrometheusMetrics(app, api)
metrics.info('first_app', 'This is my first app', version='0.0.1')
api.add_resource(Jornadas, '/jornadas')
api.add_resource(Jornada, '/jornada/<string:jornada_id>')


if __name__ == '__main__':
    app.run()