# Socket Chat

## Descrição do Projeto

O projeto consiste em um chat utilizando sockets, onde o cliente se conecta ao servidor e pode enviar mensagens para todos os outros clientes conectados diretamente ou a partir de grupos.

## Escolhas Importantes

- Utilizar Json para trafego de informações
- Threads para receber mensagens
- Separar em serviços para simplificar o código

## Como executar

Você vai precisar do [Poetry]("https://python-poetry.org/docs") instalado na sua máquina, para instalar as dependências do projeto. Para isso, execute o seguinte comando:

```bash
poetry install
```

Após isso, você pode executar o servidor e o cliente em terminais diferentes, utilizando o seguinte comando:

```bash
poetry run python3 ./src/server/main.py
```

```bash
poetry run python ./src/client/main.py
```

## Como utilizar

### Servidor

O servidor é responsável por receber as mensagens dos clientes e repassá-las para os outros clientes conectados. Ele também é responsável por gerenciar os grupos criados pelos clientes.

### Cliente

O cliente possui um menu com as seguintes opções:
  (1) listar clients
  (2) msg client
  (3) listar grupos
  (4) criar grupo
  (5) juntar ao grupo
  (6) msg grupo
  (7) sair do grupo
  (8) excluir grupo
  (help) mostrar comandos
  (quit) sair

#### Listar clients

Lista todos os clientes conectados ao servidor.

#### Msg client

Envia uma mensagem para um cliente específico.

#### Listar grupos

Lista todos os grupos criados no servidor.

#### Criar grupo

Cria um grupo no servidor.

#### Juntar ao grupo

Junta o cliente a um grupo existente.

#### Msg grupo

Envia uma mensagem para um grupo específico.

#### Sair do grupo

Remove o cliente de um grupo específico.

#### Excluir grupo

Exclui um grupo específico.

#### Help

Mostra todos os comandos disponíveis.

#### Quit

Sai do cliente.

## Autores

- [Gustavo Santos]("https://github.com/focadecombate")
