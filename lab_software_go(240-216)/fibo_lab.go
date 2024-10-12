package main

import (
	"fmt"
)

func main() {

	var n int
	fmt.Scan(&n)

	n++
	fmt.Print("Input number of Fibonacci number: ")
	a, b := 0, 1

	for i := 0; i < n; i++ {
		fmt.Print(a)
		if i < n-1 {
			fmt.Print(", ")
		}
		a, b = b, a+b
	}
	fmt.Println()
}
