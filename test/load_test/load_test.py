from locust import HttpUser, between, task


class LoadTest(HttpUser):
    """
    Configurando um teste de carga com o Locust
    """
    wait_time = between(1, 3)

    @task
    def add_servico(self):
        """ Fazendo a inserção de servicos aleatórios.
        """

        # criando o servico
        servico = {
            'nome': 'Camiseta',
            'categoria': 'Roupas',
            'descricao': 'Uma camiseta confortável e estilosa',
            'marca': 'MarcaX',
            'preco': '29.99'
        }
        # configurando a requisição
        headers = {'Content-Type': 'multipart/form-data'}
        response = self.client.post('servico', data=servico, headers=headers)

        # verificando a resposta
        data_response = response.json()
        if response.status_code == 200:
            print("Servico %s salvo na base" % servico["nome"])
        elif response.status_code == 409:
            print(data_response["mesage"] + servico["nome"])
        else:
            print('Falha na rota de adição de um servico')

    @task
    def listagem(self):
        """ Fazendo uma listagem dos items salvos.
        """
        # configurando a requisição
        response = self.client.get('servicos')
    
        # verificando a resposta
        data = response.json()
        if response.status_code == 200:
            print('Total de items salvos: %d' % len(data["servicos"]))
        else:
            print('Falha na rota /servicos')

    @task
    def get_servico(self):
        """ Fazendo uma busca pelo servico de id 1.
        """
        # configurando a requisição
        response = self.client.get('servico?id=1')
    
        # verificando a resposta
        data = response.json()
        if response.status_code == 200:
            print('Servico visitado: %s' % data["nome"])
        else:
            print('Falha na rota /servico?id=1')

    @task
    def busca_servico(self):
        """ Fazendo uma busca por servicos que no tem o termo "Faxina".
        """
        # configurando a requisição
        response = self.client.get('busca_servico?termo=Faxina')
    
        # verificando a resposta
        data = response.json()
        if response.status_code == 200:
            print('Total de servicos : %d' % len(data["servicos"]))
        else:
            print('Falha na rota /busca_servico')
