from flask import Flask
from flask_restful import Resource, Api
from resources.jornada import Jornadas, Jornada
from prometheus_flask_exporter import RESTfulPrometheusMetrics

from logging import debug, info, warning, critical, error, basicConfig
from logging import INFO
from logging import FileHandler, StreamHandler # são os objetos q gerenciam os exporters, por exemplo, handler que envia para arquivo, para stdout

#Começando a informar a partir do nivel INFO
basicConfig(
    level=INFO,
    filemode="a",
    encoding="utf-8",
    format='%(levelname)s:%(asctime)s:%(message)s',
    #handlers=[StreamHandler()]
)

app = Flask(__name__)
api = Api(app)

metrics = RESTfulPrometheusMetrics(app, api)
metrics.info('first_app', 'This is my first app', version='0.0.1')
api.add_resource(Jornadas, '/jornadas')
api.add_resource(Jornada, '/jornada/<string:jornada_id>')

debug("debugando")
info("info")
error("erro!")

if __name__ == '__main__':
    app.run()