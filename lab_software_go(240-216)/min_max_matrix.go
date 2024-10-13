package main

import (
	"fmt"
	"math"
)

func main() {

	var arr []int
	var n int
	var mn int = math.MaxInt
	var mx int = math.MinInt

	for i := 1; i <= 3; i++ {
		for j := 1; j <= 2; j++ {
			if i == 3 && j == 2 {
				fmt.Printf("M[%d][%d]: \n", i, j)
			} else {
				fmt.Printf("M[%d][%d]: ", i, j)
			}
			fmt.Scan(&n)
			if n < mn {
				mn = n
			}
			if n > mx {
				mx = n
			}

			arr = append(arr, n)

		}
	}
	// fmt.Print(arr)
	fmt.Print("Matrix\n")
	fmt.Printf("%d\t%d\t\n", arr[0], arr[1])
	fmt.Printf("%d\t%d\t\n", arr[2], arr[3])
	fmt.Printf("%d\t%d\t\n\n", arr[4], arr[5])
	fmt.Printf("Min = %d\n", mn)
	fmt.Printf("Max = %d", mx)
}
