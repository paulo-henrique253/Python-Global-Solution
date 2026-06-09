from enum import Enum

#classe empresa
class Empresa:
    def __init__(self, nome: str, pais: str,) -> Empresa:
        self.nome = nome
        self.pais = pais
        self.satelites = list()
        self.score = 50


class AcaoPontuada(Enum):
    #metodo contrutor para criar as penalidades e as bonificacoes com descricao e pontos
    def __init__ (self, descricao: str, pontos: int):
        self.descricao = descricao
        self.pontos = pontos


#enum para penalidades aplicadas nas empresas
class Penalidade(AcaoPontuada):
    ALTO_RISCO_COLISAO = (
        "Alto risco de colisão",
        -15
    )

    GERACAO_LIXO_ESPACIAL = (
        "Geração de lixo espacial",
        -15
    )

    SATELITE_SEM_DESORBITACAO = (
        "Satélite sem plano de desorbitação",
        -15
    )

    REGISTRO_ORBITAL_IRREGULAR = (
        "Registro orbital irregular",
        -20
    )

    FALTA_TRANSPARENCIA = (
        "Falta de transparência",
        -25
    )

    GERACAO_FRAGMENTOS_ORBITAIS = (
        "Geração de fragmentos orbitais",
        -20
    )

    DESCUMPRIMENTO_REGULATORIO = (
        "Descumprimento regulatório",
        -40
    )

    USO_SUSPEITO_INFRAESTRUTURA = (
        "Uso suspeito da infraestrutura espacial",
        -40
    )

    SATELITE_INATIVO = (
        "Satélite inativo em órbita",
        -10
    )

    

#enum para bonificações aplicadas nas empresas
class Bonificacao(AcaoPontuada):
    DESORBITACAO_RESPONSAVEL = (
        "Desorbitação responsável",
        20
    )

    BAIXO_RISCO_COLISAO = (
        "Baixo risco de colisão",
        15
    )

    SATELITE_ATIVO_REGULARIZADO = (
        "Satélite ativo e regularizado",
        10
    )

    PLANO_MITIGACAO_APROVADO = (
        "Plano de mitigação aprovado",
        25
    )

    BAIXA_GERACAO_LIXO_ESPACIAL = (
        "Baixa geração de lixo espacial",
        20
    )

    REGISTRO_ORBITAL_REGULAR = (
        "Registro orbital regular",
        10
    )

    TRANSPARENCIA_DADOS = (
        "Transparência de dados",
        15
    )

    INICIATIVA_SUSTENTAVEL = (
        "Participação em iniciativa sustentável",
        30
    )

    CONFORMIDADE_REGULATORIA = (
        "Conformidade regulatória",
        10
    )