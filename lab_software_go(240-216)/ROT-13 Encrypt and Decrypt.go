package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func rot13(r rune) rune {
	if r >= 'a' && r <= 'z' {
		return (r-'a'+13)%26 + 'a'
	}
	if r >= 'A' && r <= 'Z' {
		return (r-'A'+13)%26 + 'A'
	}
	return r
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Select 2 options")
	fmt.Println(" - 1 encrypt with ROT 13")
	fmt.Println(" - 2 decrypt with ROT 13\n")
	var option int
	fmt.Print("Choose option:")
	fmt.Scanf("%d\n", &option)

	fmt.Println("Enter text:")
	text, _ := reader.ReadString('\n')
	text = strings.TrimSpace(text)

	result := ""
	for _, char := range text {
		result += string(rot13(char))
	}

	if option == 1 {
		fmt.Printf("Ciphertext is \"%s\"\n", result)
	} else if option == 2 {
		fmt.Printf("Plaintext is \"%s\"\n", result)
	} else {
		fmt.Println("Invalid option selected")
	}
}
