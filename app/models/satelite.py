from enum import Enum

#classe para o satélite
class Satelite:
    def __init__(self, nome: str, empresa: str, orbita: TipoOrbita, status: StatusOperacao) -> Satelite:
        self.nome = nome
        self.empresa = empresa
        self.orbita = orbita
        self.status = status

#enum para o tipo de orbita
class TipoOrbita(Enum):
    ALTA = "alta"
    MEDIA = "media"
    BAIXA = "baixa"
    GEOESTACIONARIA = "geoestacionaria"

#enum para o status de operação do satélite
class StatusOperacao(Enum):
    ATIVO = "ativo"
    INATIVO = "inativo"