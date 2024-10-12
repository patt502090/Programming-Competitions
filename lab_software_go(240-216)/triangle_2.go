package main

import (
	"fmt"
)

func main() {
	var a int
	fmt.Print("Enter the number of rows: ")
	fmt.Scan(&a)
	// fmt.Println(a)

	for i := 1; i <= a; i++ {

		for j := 0; j < a-i; j++ {
			fmt.Print(" ")
		}

		for k := 1; k <= i; k++ {
			fmt.Print("*")
		}
		fmt.Println()
	}
}
