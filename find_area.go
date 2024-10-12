package main

import (
	"fmt"
)

func main() {

	var b float64
	var h float64
	fmt.Print("Base: ")
	fmt.Scan(&b)
	fmt.Print("Height: ")
	fmt.Scan(&h)
	fmt.Printf("Area: %.4f\n", 0.5*b*h)
}
