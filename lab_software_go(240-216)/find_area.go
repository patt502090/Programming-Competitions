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
	area := 0.5 * b * h
	fmt.Printf("Base: %.1f Height: %.1f Area: %.4f\n", b, h, area)
}
