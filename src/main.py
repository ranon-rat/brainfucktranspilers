
import os
import argparse
import sys


my_parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description="this is a simple transpiler for brainfuck", epilog="enjoy the program :)")
my_parser.add_argument("-name",
                       type=str, help='that the file is going to have')
my_parser.add_argument("-file",
                       type=str, required=True, help='the file that the program is going to transpile')


def made_output(input: str) -> str:
    out: str = ""
    for i in input:
        if i == ">":
            out += "ptr++;"
        elif i == "<":
            out += "ptr--;"
        elif i == "+":
            out += "bfvar[ptr]++;"
        elif i == "-":
            out += "bfvar[ptr]--;"
        elif i == ".":
            out += "putchar(bfvar[ptr]);"
        elif i == ",":
            out += "(bfvar[ptr])=getchar();"
        elif i == "[":
            out += "while (bfvar[ptr]) {"
        elif i == "]":
            out += "}"

    return out


def main():
    # input
    args: my_parser.parse_args = my_parser.parse_args()

    brainfuck_file: open = open(os.path.join(os.getcwd(), args.file), "r")
    output_c = "#include <stdio.h>\nint bfvar[3000];unsigned int ptr; int main(){" + made_output(
        brainfuck_file.read()) + "return 0;}"
    
    brainfuck_file.close()
    # output
    name:str
    if args.name is not None:
        name = args.name
    else:
        name="default.c"
    with open(os.path.join(os.getcwd(), name),"w+") as fs:
        fs.write(output_c)
        


if __name__ == "__main__":
    main()
