from flask_restful import Resource, reqparse
from models.jornada import JornadaModel

jornadas = [

    {
        'jornada_id': 'm',
        'nome': 'Cartão da Conta',
        'nivel_sla': 'Life Support',
        'descricao': 'Cartao da Conta iti'
    },
    {
        'jornada_id': 'c',
        'nome': 'Recarga',
        'nivel_sla': 'Alta Disponibilidade',
        'descricao': 'Recarga de Celular'
    },
    {
        'jornada_id': 'g',
        'nome': 'Cartão de Credito',
        'nivel_sla': 'Life Support',
        'descricao': 'Cartao de Credito iti'
    }
]





class Jornadas(Resource):
    def get(self):
        return {'jornadas': jornadas}

class Jornada(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('nivel_sla')
    argumentos.add_argument('descricao')

    def find_jornada(jornada_id):
        for jornada in jornadas:
            if jornada['jornada_id'] == jornada_id:
                return jornada
            #return None;

    #def find_jornadass(self, jornada_id):

    def get(self, jornada_id):
        jornada = Jornada.find_jornada(jornada_id)
        if jornada:
            return jornada
        return {'message': 'jornada not found'}, 404


    def post(self, jornada_id):
        dados = Jornada.argumentos.parse_args()
        jornada_objeto = JornadaModel(jornada_id, **dados)
        nova_jornada = jornada_objeto.json()
        jornadas.append(nova_jornada)
        return nova_jornada, 200

    def put(self, jornada_id):
        dados = Jornada.argumentos.parse_args()
        jornada_objeto = JornadaModel(jornada_id, **dados)
        nova_jornada = jornada_objeto.json()
        jornada = Jornada.find_jornada(jornada_id)
        if jornada:
            jornada.update(nova_jornada)
            return nova_jornada, 200
        jornadas.append(nova_jornada)
        return nova_jornada, 201 #created


    def delete(self, jornada_id):
        global jornadas
        jornadas = [jornada for jornada in jornadas if jornada['jornada_id'] != jornada_id]
        return {'message': 'jornada deleted'}