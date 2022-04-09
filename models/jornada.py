class JornadaModel:
    def __init__(self, jornada_id, nome, nivel_sla, descricao):
        self.jornada_id = jornada_id
        self.nome = nome
        self.nivel_sla = nivel_sla
        self.descricao = descricao

    def json(self):
        return {
            'jornada_id': self.jornada_id,
            'nome': self.nome,
            'nivel_sla': self.nivel_sla,
            'descricao': self.descricao
        }