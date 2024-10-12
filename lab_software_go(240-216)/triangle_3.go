package main

import (
	"fmt"
)

func main() {
	var a int
	fmt.Print("Enter the number of rows: ")
	fmt.Scan(&a)
	// fmt.Println(a)

	for i := a; i >= 1; i-- {
		for j := 1; j <= i; j++ {
			fmt.Print("*")
		}
		fmt.Println()
	}
}
