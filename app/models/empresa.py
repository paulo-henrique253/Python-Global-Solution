#classe empresa
class Empresa:
    def __init__(self, nome: str, pais: str,) -> Empresa:
        self.nome = nome
        self.pais = pais
        self.satelites = list()
        self.score = 50