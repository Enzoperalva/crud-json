from rich import print
from time import sleep
import service, msg, constants as const

def sending_new_student(local_file:str) -> bool:
    new_student = register_student()
    if not new_student:
        error = msg.msg_erro('ERRO! Usuário digitou um nome inválido.')
        msg.print_formatted(error)
        return False
    
    student_json = service.adding_student_to_json(local_file, new_student)
    if student_json == "Aluno cadastrado!":
        ok = msg.msg_success(student_json)
        msg.print_formatted(ok)
        return True
    
    error = msg.msg_erro(student_json)
    msg.print_formatted(error)
    return False


def list_student(local_file: str) -> bool:
    data = service.reading_file(local_file)
    if not data == "Você não adicionou nenhum aluno.":
        cont = 0
        print('ID - NOME - IDADE')
        for item in data:
            cont +=1
            print(f'{cont} - {item['name']} - {item['age']}')
        print()
        sleep(1)
        return True
    
    erro = msg.msg_erro(data)
    msg.print_formatted(erro)
    return False

def update_student(local_file: str) -> bool:
    list_student(local_file)

    opc_id = register_id_student()
    new_student = register_student()
    
    if not new_student:
        erro = msg.msg_erro('ERRO! Usuário digitou um nome inválido.')
        msg.print_formatted(erro)
        return False
    
    content = service.updating_student_in_json(local_file, new_student, opc_id)

    if content == "Aluno atualizado!":
        success = msg.msg_success(content)
        msg.print_formatted(success)

    return True


def delete_student(local_file: str) -> bool:
    list_student(local_file)
    opc_id = register_id_student()
    service.deleting_student(local_file, opc_id)


def register_student() -> dict:
    name = input('Nome aluno: ').strip().capitalize()
    if len(name) < 2:
        return const.ERRORS[3]["invalid_name"]
    try:
        age = int(input('Idade aluno:'))
        new_student = {
            "name": name,
            "age": age
        }
        return new_student
    except ValueError:
        return const.ERRORS[2]["value_error"]

def register_id_student() -> int:
    try:
        opc_id = int(input('Escolha o id. [ 0 ] para o último: '))
        return opc_id
    
    except ValueError:
        return const.ERRORS[2]["value_error"]