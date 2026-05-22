import constants as const, json, msg

def adding_student_to_json(local_file: str, new_student:dict) -> str:
    with open(local_file, 'r', encoding='utf-8') as arq:
        content = arq.read()
        registered_student = []
        if content:
            registered_student = json.loads(content)

    registered_student.append(new_student)    
    
    with open(local_file, 'w+') as arq:
        json.dump(registered_student, arq, indent=4, ensure_ascii=False)

    return const.SUCCESS[0]["student_added"]
    



def reading_file(local_file: str) -> list | str:
    content = evalueted_content_file(local_file)
    
    if not content:
        return const.ERRORS[0]["no_students_added"]
    
    data = json.loads(content)
    return  data
        

def updating_student_in_json(local_file: str, new_student: dict, opc_id: int) -> str:
    content = evalueted_content_file(local_file)
    if not content:
        return const.ERRORS[0]["no_students_added"]
    
    data = json.loads(content)
    len_data = len(data) 
    
    if opc_id > len_data:
        return const.ERRORS[1]["id_not_found"]
    
    indice = opc_id - 1
    data[indice] = new_student
    
    with open(local_file, 'w', encoding='utf-8') as arq:
        json.dump(data, arq, indent=4, ensure_ascii=False)
    
    return const.SUCCESS[1]["updated_student"]

    

def deleting_student(local_file: str, opc_id: int) -> str:
    content = evalueted_content_file(local_file)
    if not content:
        return const.ERRORS[0]["no_students_added"]
    
    data = json.loads(content)
    len_data = len(data) 

    if opc_id > len_data:
        return const.ERRORS[1]["id_not_found"]
    
    indice = opc_id - 1
    log_data = data.pop(indice)

    with open(local_file, 'w', encoding='utf-8') as arq:
        json.dump(data, arq, indent=4, ensure_ascii=False)

    return const.SUCCESS[2]["deleted_student"]            


def evalueted_content_file(local_file: str) -> str | bool:
    with open(local_file, 'r', encoding='utf-8') as arq:
        content = arq.read()
        if not content:
            return False
        return content


def create_file(local_file: str) -> None:
    with open(local_file, 'w') as arq:
        pass


def print_error(txt):
    erro = msg.msg_erro(txt)
    msg.print_formatted(erro)