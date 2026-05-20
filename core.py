from rich import print
from time import sleep
import service, msg

def register_student() -> dict:
    name = input('Nome aluno: ').strip().capitalize()
    if len(name) < 2:
        return False
    try:
        age = int(input('Idade aluno:'))
        new_student = {
            "name": name,
            "age": age
        }
        return new_student
    except ValueError:
        erro = msg.msg_erro('ERRO! Usuário digitou um valor inválido.')
        msg.print_formatted(erro)
        return False

def register_id_student() -> int:
    try:
        opc_id = int(input('Escolha o id. [ 0 ] para o último: '))
        return opc_id
    except ValueError:
        erro = msg.msg_erro('ERRO! Usuário digitou um valor inválido.')
        msg.print_formatted(erro)
        return False


def add_student(local_file:str) -> bool:
    new_student = register_student()
    if not new_student:
        erro = msg.msg_erro('ERRO! Usuário digitou um nome inválido.')
        msg.print_formatted(erro)
        return False
    
    student_json = service.file_push_json(local_file, new_student)
    if student_json == "Aluno cadastrado!":
        ok = msg.msg_success(student_json)
        msg.print_formatted(ok)
        return True
    
    erro = msg.msg_erro(student_json)
    msg.print_formatted(erro)
    return False


def list_student(local_file: str) -> bool:
    data = service.file_push_list(local_file)
    if data:
        cont = 0
        print('ID - NOME - IDADE')
        for item in data:
            cont +=1
            print(f'{cont} - {item['name']} - {item['age']}')
        print()
        sleep(1)
        return True
    
    erro = msg.msg_erro('ERRO! Você não adicionou nenhum aluno.')
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
    
    service.push_for_update_student(local_file, new_student, opc_id)
    return True


def delete_student(local_file: str) -> bool:
    list_student(local_file)
    opc_id = register_id_student()
    service.push_for_delete_student(local_file, opc_id)
