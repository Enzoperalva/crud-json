import constants as const, json

def adding_student_to_json(local_file: str, new_student:dict) -> str:
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
    
def file_is_empty(local_file: str) -> str:
    with open(local_file, 'r', encoding='utf-8') as arq:
        content = arq.read()
        if not content:
            return const.ERRORS[0]["no_students_added"]
        return content


def reading_file(local_file: str) -> list:
    try:    
        with open(local_file, 'r', encoding='utf-8') as arq:
            content = file_is_empty(local_file)
            
            data = json.loads(content)
            return  data
    except FileNotFoundError:
        return const.ERRORS[0]["no_students_added"]
        

def updating_student_in_json(local_file: str, new_student: dict, opc_id: int) -> str:
    try:
        with open(local_file, 'r', encoding='utf-8') as arq:
            content = arq.read()
            if not content:
                return const.ERRORS[0]["no_students_added"]
            
            data = json.loads(content)
            len_data = len(data) 
            
            if opc_id > len_data:
                return const.ERRORS[1]["id_not_found"]
            
            opc_id = opc_id - 1

            data[opc_id] = new_student
        with open(local_file, 'w', encoding='utf-8') as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False)
        
        return const.SUCCESS[1]["updated_student"]

    except FileNotFoundError:
        return const.ERRORS[0]["no_students_added"]
    

def deleting_student(local_file, opc_id):
    try:
        with open(local_file, 'r', encoding='utf-8') as arq:
            data = json.load(arq)
            len_data = len(data) 

            if opc_id > len_data:
                return const.ERRORS[1]["id_not_found"]
            
            opc_id = opc_id - 1
        
        with open(local_file, 'w', encoding='utf-8') as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False)

        return const.SUCCESS[2]["deleted_student"] 
            
    except FileNotFoundError:
        return const.ERRORS[0]["no_students_added"]


def create_file(local_file: str) -> json:
    with open(local_file, 'w') as arq:
        pass


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
