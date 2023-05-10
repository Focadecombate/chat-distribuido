from termcolor import colored

def print_commands():
    commands = """Comandos disponíveis:
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
         """

    print(colored(commands, "blue"))
