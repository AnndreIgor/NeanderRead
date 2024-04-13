import numpy as np
import os

instruction_set = {
    'NOP':  0,
    'STA': 16,
    'LDA': 32,
    'ADD': 48,
    'OR':  64,
    'AND': 80,
    'NOT': 96,
    'JMP': 128,
    'JN':  144,
    'JZ':  160,
    'HLT': 240
}

variables = {
    'MENOS_UM': 255,
    'AUX_A2': 137,
    'AUX_A': 136,
    'AUX_N': 135,
    'ZERO': 254,
    'UM': 253,
    'R1': 132,
    'R2': 133,
    'N2': 131,
    'A': 128,
    'N': 129,
    'X': 134,
    'B': 130,
    'R': 138
}

def txt_to_mem(text_file: str, instruction_set: dict, variables: dict):
    with open(text_file, 'r') as f:
        text = f.read()

    text = replace_intructions(text, instruction_set)
    text = replace_intructions(text, variables)

    result = format_mem_file(text)
    save_mem_file(result, text_file)

    return result

def replace_intructions(text: str, instruction_set: dict) -> str:
    for key, value in instruction_set.items():
        text = text.replace(key, str(value))

    return text

def replace_variables(text: str, variables: dict) -> str:
    for key, value in variables.items():
        text = text.replace(key, str(value))

    return text

def format_mem_file(text: str):
    instructions = text.split()

    mem = np.zeros(516)

    # carregar as instruções default do neander
    instructions_neander_default = ['3', '78', '68', '82']
    for index, instruction in enumerate(instructions_neander_default):
        mem[index] = instruction

    i = 4
    for instruction in instructions:
        mem[i] = instruction
        i += 2

    return mem.astype('uint8')


def save_mem_file(array: np.array, text_file: str):
    output_name, _ = os.path.splitext(text_file)
    array.tofile(output_name + '.mem')


if __name__ == '__main__':
    meu = txt_to_mem('trabalho.txt', instruction_set, variables)
    print(meu)
