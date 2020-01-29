from computer import Computer
from time import time, sleep
from itertools import combinations

f = open('input.txt')
program = list(map(int, f.readline().strip().split(',')))
com = Computer(program)
buffer = ''

def str_to_ascii(string):
    result = []
    for char in string:
        result.append(ord(char))
    result.append(10)
    return result

def load_outputs():
    global buffer
    while com.outputs:
        c = com.get_output()
        if c > 1000:
            print(c)
        buffer += chr(c)


commands = []
commands += str_to_ascii('west')
commands += str_to_ascii('take hologram')
commands += str_to_ascii('north')
commands += str_to_ascii('take space heater')
commands += str_to_ascii('east')
commands += str_to_ascii('take space law space brochure')
commands += str_to_ascii('east')
commands += str_to_ascii('take tambourine')
commands += str_to_ascii('west')
commands += str_to_ascii('west')
commands += str_to_ascii('south')
commands += str_to_ascii('east')
commands += str_to_ascii('east')
commands += str_to_ascii('take festive hat')
commands += str_to_ascii('east')
commands += str_to_ascii('take food ration')
commands += str_to_ascii('east')
commands += str_to_ascii('take spool of cat6')
commands += str_to_ascii('west')
commands += str_to_ascii('west')
commands += str_to_ascii('south')
commands += str_to_ascii('east')
commands += str_to_ascii('east')
commands += str_to_ascii('east')
items = ['space heater','hologram','space law space brochure','food ration','tambourine','spool of cat6','festive hat']
for item in items:
    commands += str_to_ascii(f'drop {item}')
com.inputs += commands
commands = []

# comb = list(combinations(items,2))
comb = combinations(items,4)
for c in comb:
    for item in c:
        commands += str_to_ascii(f'take {item}')
    commands += str_to_ascii('south')
    for item in c:
        commands += str_to_ascii(f'drop {item}')
    com.inputs += commands
    commands = []
while True:
    while not com.need_input and not com.halted:
        com.execute()
    com.need_input = False
    load_outputs()
    print(buffer)
    buffer = ''
    command = input()
    command = str_to_ascii(command)
    com.inputs += command

# - space heater
# - hologram
# - space law space brochure
# - food ration
# - tambourine
# - spool of cat6
# - festive hat
