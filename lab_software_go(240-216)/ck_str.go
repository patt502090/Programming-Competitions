package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter text: ")
	input, _ := reader.ReadString('\n') // Read the entire line
	input = strings.TrimSpace(input)    // Remove any trailing newline

	fmt.Print(input) // Print the full input
}
