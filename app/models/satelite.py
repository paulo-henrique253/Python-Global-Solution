from enum import Enum

class Satelite:
    def __init__(self, nome: str, empresa: str, orbita: TipoOrbita, status: StatusOperacao) -> Satelite:
        self.nome = nome
        self.empresa = empresa
        self.orbita = orbita
        self.status = status
    
class TipoOrbita(Enum):
    ALTA = "alta"
    MEDIA = "media"
    BAIXA = "baixa"
    GEOESTACIONARIA = "geoestacionaria"

class StatusOperacao(Enum):
    ATIVO = "ativo"
    INATIVO = "inativo"