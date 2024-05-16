from sys import argv
from re import match

fn = argv[1]

with open(fn, "r", encoding="latin-1") as file:
    output = open("tmp", "w", encoding="latin-1")
    index = 1

    for l in file.readlines():
        if match(r"^\d{2}$", l):
            l = f'{index}\n'
            index += 1

        output.write(l)

    output.close()
