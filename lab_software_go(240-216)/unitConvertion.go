package main

import (
	"fmt"
)

func main() {
	var inp string
	var unitInp string

	fmt.Print("Enter value in mm, cm, and m: ")
	fmt.Scan(&inp)

	fmt.Print("Enter unit to convert in mm, cm, m: ")
	fmt.Scan(&unitInp)

	var value float64
	var unit string

	if inp[len(inp)-2:] == "cm" {
		value = parseValue(inp[:len(inp)-2])
		unit = "cm"
	} else if inp[len(inp)-2:] == "mm" {
		value = parseValue(inp[:len(inp)-2])
		unit = "mm"
	} else if inp[len(inp)-1:] == "m" {
		value = parseValue(inp[:len(inp)-1])
		unit = "m"
	} else {
		return
	}

	if unit == "cm" {
		if unitInp == "mm" {
			fmt.Printf("Value after unit conversion is %.1fmm\n", value*10)
		} else if unitInp == "m" {
			fmt.Printf("Value after unit conversion is %.1fm\n", value/100)
		}
	} else if unit == "mm" {
		if unitInp == "cm" {
			fmt.Printf("Value after unit conversion is %.1fcm\n", value/10)
		} else if unitInp == "m" {
			fmt.Printf("Value after unit conversion is %.1fm\n", value/1000)
		}
	} else if unit == "m" {
		if unitInp == "cm" {
			fmt.Printf("Value after unit conversion is %.1fcm\n", value*100)
		} else if unitInp == "mm" {
			fmt.Printf("Value after unit conversion is %.1fmm\n", value*1000)
		}
	}
}

func parseValue(valueStr string) float64 {
	var value float64
	fmt.Sscanf(valueStr, "%f", &value)
	return value
}
