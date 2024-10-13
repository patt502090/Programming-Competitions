package main

import (
	"fmt"
)

func main() {
	var lines int
	fmt.Print("Line: ")
	fmt.Scan(&lines)

	if lines <= 0 || lines >= 10 {
		fmt.Println("Out of Range")
		return
	}

	for i := 1; i <= lines; i++ {

		for j := 1; j <= i; j++ {
			fmt.Print(j)
		}

		for j := i - 1; j >= 1; j-- {
			fmt.Print(j)
		}

		fmt.Println()

	}
}
