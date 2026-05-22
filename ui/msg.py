from rich import print
from time import sleep

def msg_erro(msg: str) -> str:
    return f'[red]{msg}[/]'


def msg_success(msg: str) -> str:
    return f'[green]{msg}[/]'


def print_formatted(msg: str, sleep_time: float=1) -> None:
    print(msg)
    sleep(sleep_time)
    print()

def msg_friendly(msg):
    return f'[cyan]{msg}[/]'

def feedback_for_user(msg: str, type_msg: str) -> None:
    type_msg = type_msg.strip().lower()

    if type_msg == 'error':
        erro = msg_erro(msg)
        print_formatted(erro)
    elif type_msg == 'success':
        success = msg_success(msg)
        print_formatted(success)
    elif type_msg == 'friendly':
        friendly = msg_friendly(msg)
        print_formatted(friendly)
    else:
        raise ValueError('Parametros válido para type_msg = "error" | "success" | "friendly"')
    