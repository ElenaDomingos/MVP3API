from sqlalchemy import Column, String, Integer
from  models import Base

class Servico(Base):

    # Comentário de aula: a tabela no banco pode seguir um menemônico e 
    # ter um nome diferente do que poderia ser "mais apropriado". Aqui 
    # a tabela que vai representar o servico, se chama 'servico_catalog',
    # supondo o cenário em que o sufixo "catalog" é utilizado para 
    # indicar que é uma tabela de catálogo de servicos.
    __tablename__ = 'servico_catalog'

    # O nome de uma coluna também pode ter no banco um nome diferente
    # como é apresentado aqui no caso do Servico.id que no banco será 
    # servico_catalog.pk_prod, o sufixo pk está sendo utilizado para 
    # indicar que é uma chave primária

    id = Column(Integer, primary_key=True)
    nome_usuario = Column(String(140))
    email = Column(String(140))
    cep = Column(Integer)
    logradouro = Column(String(140))
    numero = Column(Integer)
    bairro = Column(String(140))
    cidade = Column(String(140))
    estado = Column(String(140))
    nome_servico = Column(String(140))
    descricao = Column(String(2000))
    contato = Column(String(140))


    def __init__(self, nome_usuario, email, cep, logradouro, numero, bairro, cidade, estado, nome_servico, descricao, contato):
        """
        Cria um Servico

        Arguments:
            nome_usuario: nome do prestador de serviço.
            email: email do autonomo
            cep: CEP do endereço dele
            logradouro: endereço dele
            numero: número da casa dele
            bairro: bairro onde ele mora
            cidade: cidade onde mora o prestador de serviço
            estado: estado onde ele mora e presta o serviço
            nome_servico: nome do serviço  
            descricao: descrição do serviço oferecido
            contato: contato do autônomo             
        """
        self.nome_usuario = nome_usuario
        self.email = email
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado        
        self.nome_servico = nome_servico
        self.descricao = descricao        
        self.contato = contato
        

    def to_dict(self):
        """
        Retorna a representação em dicionário do Objeto Servico.
        """
        return{
            "id": self.id,
            "nome_usuario": self.nome_usuario,
            "email": self.email,
            "cep": self.cep,
            "logradouro": self.logradouro,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "nome_servico": self.nome_servico,
            "descricao": self.descricao,
            "contato": self.contato,
        }

    def __repr__(self):
        """
        Retorna uma representação do Servico em forma de texto.
        """
        return f"Servico(id={self.id}, nome_usuario='{self.nome_usuario}', email={self.email}, cep={self.cep}, logradouro='{self.logradouro}', numero={self.numero}, bairro='{self.bairro}', cidade='{self.cidade}', estado='{self.estado}', nome_servico='{self.nome_servico}',  descricao='{self.descricao}',  contato='{self.contato}')"    
