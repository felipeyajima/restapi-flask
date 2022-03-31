from flask import Flask
from flask_restful import Resource, Api
from resources.jornada import Jornadas, Jornada

app = Flask(__name__)
api = Api(app)



api.add_resource(Jornadas, '/jornadas')
api.add_resource(Jornada, '/jornada/<string:jornada_id>')

if __name__ == '__main__':
    app.run(debug=True)