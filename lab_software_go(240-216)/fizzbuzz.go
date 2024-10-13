package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Print("Enter number: ")
	fmt.Scan(&n)
	fmt.Printf("The number is %d\n", n)

	if n%3 == 0 && n%5 == 0 {
		fmt.Println("FizzBuzz")
	} else if n%3 == 0 {
		fmt.Println("Fizz")
	} else if n%5 == 0 {
		fmt.Println("Buzz")
	}
}
