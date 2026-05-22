from rich import print
import os, core.flow as flow, ui.msg as msg, core.service as service

FILE_LOG_STUDENT = 'alunos.json'

if not os.path.isfile(FILE_LOG_STUDENT):
    service.create_file(FILE_LOG_STUDENT)

while True:
    print('[blue]1 -[/] [purple]Criar usuário[/] \n'
        '[blue]2 -[/] [purple]Listar usuários[/] \n'
        '[blue]3 -[/] [purple]Atualizar usuários[/]\n'
        '[blue]4 -[/] [purple]Deletar usuário[/] \n'
        '[blue]5 -[/] [purple]Sair[/]'
    )

    try:
        option = int(input('Opção: '))
        print()
    except KeyboardInterrupt:
        msg.feedback_for_user('\nUsuário forçou saida!', 'error')
        os.system('clear')
        break
    except ValueError:
        msg.feedback_for_user('ERRO! Usuário digitou um valor inválido.', 'error')
        continue
    options = {
        1: lambda: flow.sending_new_student(FILE_LOG_STUDENT),
        2: lambda: flow.list_student(FILE_LOG_STUDENT),
        3: lambda: flow.update_student(FILE_LOG_STUDENT),
        4: lambda: flow.delete_student(FILE_LOG_STUDENT)
    }

    if option not in (1, 2, 3, 4, 5):
        msg.feedback_for_user('ERRO! Usuário selecionou índice inválido.', 'error')
        continue
    
    data = options.get(option)
    if data:
        data()
    else:
        msg.feedback_for_user("Obrigado por usar o meu script<3", "friendly")
        os.system('clear')
        break