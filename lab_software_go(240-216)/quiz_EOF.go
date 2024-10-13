package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	cnt := make(map[rune]int)
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Print("Enter string: ")
		input, _ := reader.ReadString('\n')

		input = strings.TrimSpace(input)

		if strings.ToLower(input) == "end" {
			break
		}

		for _, char := range strings.ToLower(input) {
			if char >= 'a' && char <= 'z' {
				cnt[char]++
			}
		}
	}

	fmt.Println("******************************")
	fmt.Println("*     Alphabet Counting      *")
	fmt.Println("******************************")

	for char := 'a'; char <= 'z'; char++ {
		if count, exists := cnt[char]; exists {
			fmt.Printf("%c %d\n", char, count)
		}
	}
	fmt.Println("******************************")
}
