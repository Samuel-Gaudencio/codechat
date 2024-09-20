# CodeChat 💬

CodeChat é uma aplicação web simples que permite aos usuários enviar mensagens em uma conversa aberta sobre tecnologia. Utiliza FastHTML para renderização de páginas e Supabase para armazenar as mensagens.

## Tecnologias Utilizadas

- **Python**
- **FastHTML**
- **Supabase**
- **HTMX**
- **dotenv** para gerenciamento de variáveis de ambiente

## Funcionalidades

- Envio de mensagens com nome e conteúdo.
- Lista de mensagens exibida em tempo real.
- Interface simples e intuitiva.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o Python e o Supabase configurados. Você também precisará de um arquivo `.env` com as seguintes variáveis:

SUPABASE_URL=<sua_url_supabase> 
SUPABASE_KEY=<sua_chave_supabase>

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu_usuario/codechat.git
   cd codechat
2. Instale as dependências:
  ```bash
   pip install -r requirements.txt
  ```
3. Execute a aplicação:
 ```bash
   python app.py
  ```
4. Acesse a aplicação no navegador em http://localhost:5001.

## Estrutura do Projeto

- app.py: Código principal da aplicação.
- components.py: Módulo para renderização de formulários e mensagens.
- .env: Arquivo de configuração para variáveis sensíveis.

## Contato
Feito por Samuel Siqueira - Sinta-se à vontade para entrar em contato para qualquer dúvida ou sugestão!
