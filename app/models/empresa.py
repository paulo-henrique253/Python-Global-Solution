class Empresa:
    def __init__(self, nome: str, pais: str, num_satelites: int, documentacao) -> Empresa:
        self.nome = nome
        self.pais = pais
        self.num_satelites = num_satelites
        self.documentacao = documentacao
        self.satelites = list()
        self.score = 50