package main

import (
	"fmt"
)

func main() {
	var b float32
	var h float32
	fmt.Print("Base: ")
	fmt.Scan(&b)
	fmt.Print("Height: ")
	fmt.Scan(&h)
	fmt.Printf("Area: %.4f", b*h*0.5)

}
