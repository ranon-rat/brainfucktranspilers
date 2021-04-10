package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
)

var (
	help bool
	name string
	file string
)

func init() {

	flag.BoolVar(&help, "h", false, "help")
	flag.StringVar(&name, "n", "output.go", "name")
	flag.StringVar(&file, "f", "", "file")
	flag.Parse()

}
func main() {
	if help {
		fmt.Printf("-h\tits for get help\n-n\tfor default the program create a file named 'output.go' but you can name it however you want\n-f\tfile that you want to compile\n")
		return
	}

	f, err := ioutil.ReadFile(file)
	if err != nil {
		fmt.Println("file doesnt find")
		return
	}
	if _, err := os.Create(name); err != nil {
		fmt.Println("something bad happend")
		return
	}

	ioutil.WriteFile(name, []byte("package main\nimport \"fmt\"\nvar (\nptr=0\nbfvar=[3000]int{})\nfunc main(){\n"+outputBrainFuck(string(f))+"\n}"), 777)

}

func outputBrainFuck(input string) string {
	out := ""
	for _, i := range input {
		switch i {
		case '>':
			out += "ptr++;\n "
			break
		case '<':
			out += "ptr--; \n"
			break
		case '+':
			out += "bfvar[ptr]++; \n"
			break
		case '-':
			out += "bfvar[ptr]--; \n"
			break
		case '.':
			out += `fmt.Printf("%c",bfvar[ptr]); ` + "\n"
			break
		case ',':
			out += `fmt.Scanf("%c",(bfvar[ptr])); ` + "\n"
			break
		case '[':
			out += "for bfvar[ptr]>0 { \n"
			break
		case ']':
			out += "}\n "
			break
		}
	}
	return out
}
