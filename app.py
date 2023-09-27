from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from models import Session, Servico
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
servico_tag = Tag(name="Servico", description="Adição, visualização e remoção de servicos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/servico', tags=[servico_tag],
          responses={"200": ServicoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_servico(form: ServicoViewSchema):
    """Adiciona um novo Servico à base de dados

    Retorna uma representação dos servicos e comentários associados.
    """
    #print(form)
    servico = Servico(
        nome_usuario=form.nome_usuario,
        email=form.email,
        cep=form.cep,
        logradouro=form.logradouro,
        numero=form.numero,
        bairro = form.bairro,
        cidade=form.cidade,
        estado=form.estado,
        nome_servico=form.nome_servico,
        descricao=form.descricao,
        contato=form.contato,       
    )
    logger.info(f"Adicionando servico de nome: '{servico.nome_usuario}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando servico
        session.add(servico)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.info("Adicionado servico: %s"% servico)
        return apresenta_servico(servico), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Servico de mesmo nome e marca já salvo na base :/"
        logger.warning(f"Erro ao adicionar servico '{servico.nome_usuario}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar servico '{servico.nome_usuario}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/servicos', tags=[servico_tag],
         responses={"200": ListagemServicosSchema, "404": ErrorSchema})
def get_servicos():
    """Faz a busca por todos os Servico cadastrados

    Retorna uma representação da listagem de servicos.
    """
    logger.info(f"Coletando servicos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    servicos = session.query(Servico).all()

    if not servicos:
        # se não há servicos cadastrados
        return {"servicos": []}, 200
    else:
        logger.info(f"%d servicos econtrados" % len(servicos))
        # retorna a representação de servico
        return apresenta_servicos(servicos), 200


@app.get('/servico', tags=[servico_tag],
         responses={"200": ServicoViewSchema, "404": ErrorSchema})
def get_servico(query: ServicoBuscaPorIDSchema):
    """Faz a busca por um Servico a partir do id do servico

    Retorna uma representação dos servicos e comentários associados.
    """
    servico_id = query.id
    logger.info(f"Coletando dados sobre servico #{servico_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    servico = session.query(Servico).filter(Servico.id == servico_id).first()

    if not servico:
        # se o servico não foi encontrado
        error_msg = "Servico não encontrado na base :/"
        logger.warning(f"Erro ao buscar servico '{servico_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.info("Servico econtrado: %s" % servico)
        # retorna a representação de servico
        return apresenta_servico(servico), 200


@app.delete('/servico', tags=[servico_tag],
            responses={"200": ServicoDelSchema, "404": ErrorSchema})
def del_servico(query: ServicoBuscaPorIDSchema):
    """Deleta um Servico a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    id = unquote(unquote(query.id))
    logger.info(f"Deletando dados sobre servico #{id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Servico).filter(Servico.id == id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.info(f"Deletado servico #{id}")
        return {"mesage": "Servico removido", "id": id}
    else:
        # se o servico não foi encontrado
        error_msg = "Servico não encontrado na base :/"
        logger.warning(f"Erro ao deletar servico #'{servico_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.get('/busca_servico', tags=[servico_tag],
         responses={"200": ListagemServicosSchema, "404": ErrorSchema})
def busca_servico(query: ServicoBuscaPorNomeSchema):
    """Faz a busca por servicos em que o termo passando  Servico a partir do id do servico

    Retorna uma representação dos servicos e comentários associados.
    """
    termo = unquote(query.termo)
    logger.info(f"Fazendo a busca por nome com o termo: {termo}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    servicos = session.query(Servico).filter(Servico.nome.ilike(f"%{termo}%")).all()
    
    if not servicos:
        # se não há servicos cadastrados
        return {"servicos": []}, 200
    else:
        logger.info(f"%d rodutos econtrados" % len(servicos))
        # retorna a representação de servico
        return apresenta_servicos(servicos), 200
