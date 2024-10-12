package main

import (
	"fmt"
)

func main() {
	var a int
	var sym string
	fmt.Print("Enter the number of rows: ")
	fmt.Scan(&a)
	fmt.Print("Enter print symbol: ")
	fmt.Scan(&sym)

	// fmt.Println(a)

	for i := 1; i <= a; i-- {

		for j := 0; j < a-i; j++ {
			fmt.Print(" ")
		}

		for k := 1; k <= (2*i - 1); k++ {
			fmt.Print(sym)
		}
		fmt.Println()
	}
}
