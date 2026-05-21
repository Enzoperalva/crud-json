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