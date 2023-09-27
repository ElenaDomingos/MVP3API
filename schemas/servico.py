from pydantic import BaseModel
from typing import Optional, List
from models.servico import Servico


class ServicoSchema(BaseModel):
    """ Define como um novo servico a ser inserido deve ser representado
    """
    nome_usuario: str = 'João Ferreira'
    email: str = 'joao@gmail.com'
    cep: int = 36904108
    logradouro: str = 'Jose Ribeiro Sobrino'
    numero: int = 99
    bairro: str = 'Sao Vicente'
    cidade: str = 'Manhuacu'
    estado: str = 'MG'
    nome_servico: str = "Faxina"
    descricao: str = 'Faxina geral'
    contato: str = "@joaoferreira"


class ServicoViewSchema(BaseModel):
    """ Define como um novo servico a ser inserido deve ser representado
    """
    nome_usuario: str = 'João Ferreira'
    email: str = 'joao@gmail.com'
    cep: int = 36904108
    logradouro: str = 'Jose Ribeiro Sobrino'
    numero: int = 99
    bairro: str = 'Sao Vicente'
    cidade: str = 'Manhuacu'
    estado: str = 'MG'
    nome_servico: str = "Faxina"
    descricao: str = 'Faxina geral'
    contato: str = "@joaoferreira"


class ServicoBuscaPorNomeSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do servico.
    """
    nome_servico: str = "Faxina"


class ServicoBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do servico.
    """
    id: int = 1

class ListagemServicosSchema(BaseModel):
    """ Define como uma listagem de servicos será retornada.
    """
    servicos:List[ServicoViewSchema]

class ServicoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int

def apresenta_servicos(servicos: List[Servico]):
    """ Retorna uma representação do servico seguindo o schema definido em
        ListagemServicosSchema.
    """
    result = []
    for servico in servicos:
        result.append({
            "id": servico.id,
            "nome_usuario": servico.nome_usuario,
            "email": servico.email,
            "cep": servico.cep,        
            "logradouro": servico.logradouro,    
            "numero": servico.numero,
            "bairro": servico.bairro,
            "cidade": servico.cidade,            
            "estado": servico.estado,            
            "nome_servico": servico.nome_servico,
            "descricao": servico.descricao, 
            "contato": servico.contato,           
        })

    return {"servicos": result}

class ServicoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_servico(servico: Servico):
    """ Retorna uma representação do servico seguindo o schema definido em
        ServicoViewSchema.
    """
    return {
        "id": servico.id,
        "nome_usuario": servico.nome,
        "email": servico.email,
        "cep": servico.cep,
        "logradouro": servico.logradouro,  
        "numero": servico.numero,
        "bairro": servico.bairro,
        "cidade": servico.cidade,
        "estado" : servico.estado,
        "nome_servico": servico.nome_servico,
        "descricao": servico.descricao,
        "contato": servico.contato,       
    }