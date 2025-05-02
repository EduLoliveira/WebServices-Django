*** Apresentação Pessoal e Profissional ***
Boa noite, Sou Eduardo Lucio, 
Desenvolvedor Fullstack, responsavel por esse Projeto_django!

Estou buscando uma oportunidade para crescimento na carreira Profissional, nunca atuei como desenvolvedor. Mas dê 2021 (2º Ano do colegial) sou Estudante de Desenvolvimento web, e sempre em movimento, buscando ser um profissional em T.
---------------------------------------------------------------------------------------------------------------

*** 0. Guia de Inicialização do Projeto Django ***
Este projeto é uma aplicação web desenvolvida com Django, um framework em Python;

A aplicação fornece uma interface de usuário web (frontend), para interagir com os dados.
As principais funcionalidades incluem operações básicas de CRUD (criar, ler, atualizar, excluir) em diversos modelos de dados, seguindo o padrão arquitetural MVT (Model-View-Template) do Django​.

*** Tecnologias Usadas ***
Python3 – Linguagem de programação usada pelo Django, versão 3.12.10

Django – Framework web em Python (versão 4.0)
    .
SQLite – Banco de dados no Django para desenvolvimento local. 
    .
HTML, CSS, JavaScript – Tecnologias para o frontend 
.
Git & GitHub – Hospedagem do código-fonte
.
pip – Gerenciador de pacotes Python para instalar as dependências
.
Visual Studio Code (ou similar) – Ambiente de desenvolvimento recomendado. 
Configurar o interpretador Python do projeto no editor e a extensão Python para facilitar o desenvolvimento.

*** Processos Instalação Windows ***
-- pip install -r requirements.txt

Recomendado: 
-- Instalar o "Python3" nas extensões do VScode. 
-- Instalar "SQLite viewer" nas extensões do VScode, visualiza os dados e sua estrutura SQL.

	Quando acessar o projeto, abrir o terminal:
	-- CTRL + J

	Iremos usar o comando PWD para ver onde estamos, dentro do arquivo.
	-- PWD 
	Caso estiver no local, onde se encontra  um arquivo manage.py, ok.
	
	-- python manage.py makemigrations
	-- python manage.py migrate

	Agora basta apenas executar esse comando.
	E acessar o localhost que será exibido no Terminal.
	-- Python manage.py runserver


1. Começando a preparar o ambiente, iremos usar o Visual studio Code:

	Iremos ate o topo na esquerda. File, depois OpenFolder,
	Abriremos o arquivo do projeto, no local que deixamos. 
	-- Ex: /home/usuario/Downloads/projeto_entrega
	

2. Usaremos o Terminal do Vscode, ou CMD:

	Realizaremos a instalação dos pacotes basicos, primeiro:
	-- sudo apt update
	-- sudo apt install python3 python3-pip

	Instalação dos pacotes, de execução.
	-- pip install -r requirements.txt

 	Caso queira verificar a versão instalada: python3 –version
	Caso queira verificar a versão instalada: python3 -m django --version
	/ou/ django-admin --version

	Recomendado: 
	-- Instalar SQLite viewer nas extensões do VScode, para visualizar os dados em estrutura SQL.


3. Após realizar o download das dependencias.
Iremos executar o mesmo no Vscode.

	Quando acessar o projeto, abrir o terminal:
	-- CTRL + J

	Iremos usar o comando PWD para ver onde estamos, dentro do arquivo.
	-- PWD 
	Caso estiver no local, onde se encontra  um arquivo manage.py, ok.
	
	-- python manage.py makemigrations
	-- python manage.py migrate

	Se não:
	-- LS 
	Acessar a pasta que é exibida:
	-- cd Projeto_django


4. Após esses processos, iremos utilizar o seguinte comando para rodar a aplicação.
	
	Agora basta apenas executar esse comando.
	E acessar o localhost que será exibido no Terminal.
	-- Python manage.py runserver

---------------------------------------------------------------------------------------------------------------
OBS:
	Um detalhe que foi observado, seria da aplicação contar os ID de registros passados, mesmo após serem apagados.
	Para apagar todos dados já incluido no banco e iniciar uma nova contagem, fazemos o seguinte processo!

	Acessando o banco
	-- sqlite3 db.sqlite3
	Visualiza todas as tabelas
	-- .tables
	
	Utilize esses comandos na sequencia. 
	
	Rodar esses comandos na sequencia .
	-- DELETE FROM app_empresa_empresa;
	-- DELETE FROM app_empresa_endereco

	E agora apagamos os dados seguindo a sequencia de ‘app_empresa_empresa’
	-- DELETE FROM sqlite_sequence WHERE name=’app_empresa_empresa’
	-- DELETE FROM sqlite_sequence WHERE name='app_empresa_endereco';
	
-------------------------------------------------------------------------------------------------------------
*** Responsabilidade dos pacotes no Projeto_django ***
MODELS e FORMS,
	Models tem a função de estruturas oque iremos receber dos dados.
	Já o Forms e responsavel pelo direcionamento dos dados ate o Model, e armazenamento no ambiente do "django.db".

VIEWS, 
	Temos todos controles de Fluxos e processamento de dados e de API's, introduzidas no "Template/home.html".
	Primeira pagina '' é onde terá um Layout basico, e o proprio Formulario. 

URLS,
	Responsavel por todo processo de navegação entre as paginas, e importação das validações. 

SETTINGS,
	Usado para configurar o ambiente, INSTALLED_APP, TEMPLATES, STATIC_URL, STATICFILES_DIRS.

STATIC,
	Possui as funções herdadas de toda aplicação, como mascaras do Formulario (telefone, CNPJ, CEP). 
	Até funções de validação das API, possui iteração de cor, caso Validado ou caso Validação negada! 

---------------------------------------------------------------------------------------------------------------