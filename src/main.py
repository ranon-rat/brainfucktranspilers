
from os import path, getcwd
from argparse import ArgumentParser


my_parser: ArgumentParser = ArgumentParser(
    description="this is a simple transpiler for brainfuck", epilog="enjoy the program :)")
#some additions
my_parser.add_argument("-name",
                       type=str, help='that the file is going to have')
my_parser.add_argument("-file",
                       type=str, required=True, help='the file that the program is going to transpile')


def made_output(bf_input: str) -> str:
    out: str = ""
    for i in bf_input:
        if i == ">":
            out += "ptr++;"
        elif i == "<":
            out += "ptr--;"
        elif i == "+":
            out += "(*ptr)++;"
        elif i == "-":
            out += "(*ptr)--;"
        elif i == ".":
            out += "putchar(*ptr);"
        elif i == ",":
            out += "(*ptr)=getchar();"
        elif i == "[":
            out += "while (*ptr) {"
        elif i == "]":
            out += "}"
    return out


def main():
    # input
    args: my_parser.parse_args = my_parser.parse_args()
    brainfuck_file: open = open(path.join(getcwd(), args.file), "r")
    #this is the expected output
    output_c: str = "#include <stdio.h>\nchar array[30000] = {0}; char *ptr = &array[0]; int main(){" + made_output(
        brainfuck_file.read()) + "return 0;}"
    brainfuck_file.close()
    # output
    name:str
    if args.name is not None:
        name = args.name
    else:
        name = "default.c"
    # Create the file
    with open(path.join(getcwd(), name), "w+") as fs:
        fs.write(output_c)
        


if __name__ == "__main__":
    main()
