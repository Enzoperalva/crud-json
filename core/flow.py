from time import sleep
import service, msg, constants as const

def sending_new_student(local_file:str) -> bool:
    new_student = register_student()
    if new_student == "Usuário digitou um nome inválido.":
        msg.feedback_for_user(new_student, "error")
        return False
    
    student_json = service.adding_student_to_json(local_file, new_student)
    if student_json == "Aluno cadastrado!":
        msg.feedback_for_user(student_json, "success")
        return True
    
    msg.feedback_for_user(student_json, "error")
    return False


def list_student(local_file: str) -> bool:
    data = service.reading_file(local_file)
    if data == "Você não adicionou nenhum aluno.":
        msg.feedback_for_user(data, "error")
        return False
    
    cont = 0
    print('ID - NOME - IDADE')
    for item in data:
        cont +=1
        print(f'{cont} - {item['name']} - {item['age']}')
    print()
    sleep(1)
    return True


def update_student(local_file: str) -> bool:
    list_student(local_file)

    opc_id = register_id_student()
    new_student = register_student()
    
    if not new_student:
        msg.feedback_for_user("Usuário digitou um nome inválido.", "error")
        return False
    
    content = service.updating_student_in_json(local_file, new_student, opc_id)
    if content == "Você não adicionou nenhum aluno.":
        msg.feedback_for_user(content, "error")
        return False
    
    elif content == "Id não encontrado.":
        msg.feedback_for_user(content, "error")
        return False

    msg.feedback_for_user(content, "success")
    return True


def delete_student(local_file: str) -> bool:
    list_student(local_file)
    opc_id = register_id_student()
    
    if opc_id == "Usuário digitou um valor inválido.":
        msg.feedback_for_user(opc_id, "error")
        return False
    
    content = service.deleting_student(local_file, opc_id)
    if content == "Você não adicionou nenhum aluno.":
        msg.feedback_for_user(content, "error")
        return False
    
    elif content == "Id não encontrado.":
        msg.feedback_for_user(content, "error")
        return False
    
    msg.feedback_for_user(content, "success")
    return True
    




def register_student() -> dict | str:
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
