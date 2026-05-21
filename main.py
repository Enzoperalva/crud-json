from rich import print
from time import sleep
import core, msg, os, service

FILE_LOG_STUDENT = 'alunos.json'

if not os.path.isfile(FILE_LOG_STUDENT):
    service.create_file(FILE_LOG_STUDENT)

while True:
    print('[blue]1 -[/] [purple]Criar usuário[/] \n'
        '[blue]2 -[/] [purple]Listar usuários[/] \n'
        '[blue]3 -[/] [purple]Atualizar usuários[/]\n'
        '[blue]4 -[/] [purple]Deletar usuário[/] \n'
        '[blue]5 -[/] [purple]Sar[/]'
    )

    try:
        option = int(input('Opção: '))
        print()
    except KeyboardInterrupt:   
        erro = msg.msg_erro('\nUsuário forçou saida!')
        msg.print_formatted(erro)
        os.system('clear')
        break
    except ValueError:
        erro = msg.msg_erro('ERRO! Usuário digitou um valor inválido.')
        msg.print_formatted(erro)
        continue
    options = {
        1: lambda: core.add_student(FILE_LOG_STUDENT),
        2: lambda: core.list_student(FILE_LOG_STUDENT),
        3: lambda: core.update_student(FILE_LOG_STUDENT),
        4: lambda: core.delete_student(FILE_LOG_STUDENT)
    }

    if option not in (1, 2, 3, 4, 5):
        erro = msg.msg_erro('ERRO! Usuário selecionou índice inválido.')
        msg.print_formatted(erro)
        continue
    
    data = options.get(option)
    if data:
        data()
    else:
        print('[cyan]Obrigado por usar nosso pograma<3[/]')
        sleep(1)
        os.system('clear')
        break