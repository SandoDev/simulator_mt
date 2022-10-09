import time
from typing import final


def process_input():
    print("Digite nombre del archivo de entrada:")
    #name_file = input()
    name_file = "input.txt"

    input_mt = []
    with open(name_file, 'r') as f:
        input_mt = f.readlines()

    print("Digite la longitud de espacios vacios para la cinta:")
    #tape_long = int(input())
    tape_long = 5
    blank_line = "_"*tape_long

    print("Digite la entrada de la cinta:")
    #in_tape = input()
    in_tape = "__1________________"
    tape = blank_line + in_tape + blank_line

    transitions_functions = [line.split() for line in input_mt[:]]
    list_tuple_in = [
        [line[0], line[1]]
        for line in transitions_functions
    ]
    list_action_in = [
        [line[2], line[3], line[4]]
        for line in transitions_functions
    ]
    final_out = {
        "tape": tape,
        "tape_long": tape_long,
        "list_tuple_in": list_tuple_in,
        "list_action_in": list_action_in,
    }
    return final_out


def simulator_mt(tape, tape_long, list_tuple_in, list_action_in):
    stop = True
    current_state = "0"
    position = tape_long+5
    list_tape = list(tape)
    while stop:
        current_tuple = [current_state, list_tape[position]]
        if current_tuple in list_tuple_in:
            time.sleep(0.2)
            values = list_action_in[list_tuple_in.index(current_tuple)]
            list_tape[position] = values[0]
            current_state = values[2]
            if values[1] == 'r':
                position += 1
            elif values[1] == 'l':
                position -= 1
            print(list_tape)
        else:
            stop = False


simulator_mt(**process_input())
