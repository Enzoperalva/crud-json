import json, msg
import constants as const

def adding_student_to_json(local_file: str, new_student:dict) -> bool:
    try:
        with open(local_file, 'r', encoding='utf-8') as arq:
            content = arq.read()
            registered_student = []
            if content:
                registered_student = json.loads(content)

    except FileNotFoundError:
        return const.ERRORS[0]["no_students_added"]
    
    registered_student.append(new_student)    
    
    with open(local_file, 'w+') as arq:
        json.dump(registered_student, arq, indent=4, ensure_ascii=False)

    return const.SUCCESS[0]["student_added"]
    
    
def file_push_list(local_file: str) -> json:
    try:    
        with open(local_file, 'r', encoding='utf-8') as arq:
            content = arq.read()
            if not content:
                return const.ERRORS[0]["no_students_added"]
            
            data = json.loads(content)
            return  data
    except FileNotFoundError:
        return const.ERRORS[0]["no_students_added"]
        

def push_for_update_student(local_file: str, new_student: dict, opc_id: int) -> bool:
     
    try:
        with open(local_file, 'r', encoding='utf-8') as arq:
            data = json.load(arq)
            len_data = len(data) 
            
            if opc_id > len_data:
                return const.ERRORS[1]["id_not_found"]
            
            opc_id = opc_id - 1
                
            data[opc_id]['name'] = new_student['name'] 
            data[opc_id]['age'] = new_student['age']
        with open(local_file, 'w', encoding='utf-8') as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False)
        
        return const.SUCCESS[1]["updated_student"]

    except FileNotFoundError:
        return const.ERRORS[0]["no_students_added"]
    

def push_for_delete_student(local_file, opc_id):
    log_data = None

    try:
        with open(local_file, 'r', encoding='utf-8') as arq:
            data = json.load(arq)
            len_data = len(data) 

            if opc_id > len_data:
                return const.ERRORS[1]["id_not_found"]
            
            opc_id = opc_id - 1
            log_data = data.pop(opc_id)
        
        with open(local_file, 'w', encoding='utf-8') as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False)

        ok = msg.msg_success(f'ALUNO {log_data["name"]} DELETADO')
        msg.print_formatted(ok)

        return const.SUCCESS[2]["deleted_student"] 
            
    except FileNotFoundError:
        return const.ERRORS[0]["no_students_added"]


def create_file(local_file: str) -> json:
    with open(local_file, 'w') as arq:
        pass


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