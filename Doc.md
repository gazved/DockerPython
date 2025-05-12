# Documentação - Desafio Técnico — Integrações

## Informações Pessoais
- Nome: Gabriel Azevedo Alvarenga
- CPF: 11143456602
- Email: gazevedoalvarenga@gmail.com
- Número: 31984757777

## Como Utilizar o App

### Pré-requisitos
- Instale o [Docker](https://www.docker.com/get-started) e o [Docker Compose](https://docs.docker.com/compose/install/) em sua máquina.
- Certifique-se de ter uma conexão com a internet para acessar a API externa.

### Passos para Iniciar
1. Clone o repositório para sua máquina:
   
   git clone https://github.com/gazved/DockerPython
   cd DockerPython
2. Inicie os serviços Docker:
   docker-compose up --build
   Acesse a aplicação no navegador em:
   Frontend/Backend Integrado: http://localhost:3000

### Funcionalidades
   - Visualização de Corridas Agendadas: Exibe as próximas corridas agendadas para o email padrão (john.doe@gmail.com)
   -Histórico de Corridas: Clique em "Mostrar Histórico" para visualizar o histórico completo de corridas passadas.

   - Funções Disponíveis
    -src/api/client.py
       AutomyClient.authenticate():
         Descrição: Autentica na API externa (https://appsaccess.automy.com.br/login) usando as credenciais fornecidas (username: fldoaogopdege, password: ygalepsm) e obtém um token JWT válido por 15 minutos.
         Retorno: O token JWT armazenado em self.token.
       AutomyClient.get_races(email):
         Descrição: Faz uma requisição à API para buscar corridas associadas ao email fornecido, usando uma query SQL (SELECT * FROM desafio.cadastro_baterias_desafio WHERE email = '<email>').
         Parâmetro: email (string) - Email do cliente (padrão: john.doe@gmail.com).
         Retorno: Lista de dicionários com dados das corridas (ex.: [{"data_agendamento": "20/04/2025", ...}, ...]).
    -src/services/filter_service.py
       filter_races_by_date(races_data):
         Descrição: Filtra os dados das corridas com base na data atual, separando em corridas passadas e futuras.
         Parâmetro: races_data (lista) - Dados brutos retornados pela API.
         Retorno: Tupla (past_races, upcoming_races) - Listas de corridas passadas e futuras.
    -src/services/message_service.py
       format_races_message(upcoming_races, past_races):
         Descrição: Formata mensagens de texto para exibir corridas (não usado diretamente no frontend atual, substituído por Jinja2).
         Parâmetros: upcoming_races e past_races (listas).
         Retorno: String formatada com mensagens.
       show_full_history(past_races):
         Descrição: Formata o histórico completo de corridas passadas (não usado diretamente no frontend atual).
         Parâmetro: past_races (lista).
         Retorno: String formatada com o histórico.
    -src/main.py
       Rotas:
         / (GET/POST):
         Descrição: Rota principal que busca corridas, filtra os dados e renderiza o template index.html.
         Parâmetro (POST): email (opcional, via formulário).
         Retorno: HTML renderizado com corridas e histórico (se ativado).
         /toggle-history (GET):
         Descrição: Alterna a exibição do histórico completo de corridas passadas.
         Retorno: HTML renderizado com show_history=True.
### Processo de Build e Deploy
- Build
  Certifique-se de que o requirements.txt contém as dependências necessárias:

  flask
  requests
- Execute o build dos containers:

  docker-compose build
  Isso usa o Dockerfile para criar a imagem baseada em python:3.11-slim, instala dependências e copia os arquivos do projeto.
- Deploy
  Inicie os serviços com:
  docker-compose up
  O container escuta na porta 3000 do host, mapeada para a porta 3000 do container.
  Para parar os serviços:
  docker-compose down
- Observações sobre Portas
  A porta padrão é 3000. Não houve alterações na configuração padrão de portas no Docker.
  Observações Adicionais
  Token JWT: O token expira a cada 15 minutos. A aplicação renova automaticamente o token quando necessário.
  API Externa: A aplicação depende da API em https://appsaccess.automy.com.br. Se a API estiver fora do ar, uma mensagem de erro será exibida.
  Remoção de Arquivos: O arquivo original README.md foi removido, conforme instruções do desafio.
  Frontend: A interface é estática e renderizada pelo Flask com Jinja2. Não há suporte a formulário de entrada de email no momento.
