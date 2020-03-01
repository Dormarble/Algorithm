package main

import "fmt"

func main() {
	var n, a int
	result := 1
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		fmt.Scan(&a)
		result += a - 1
	}
	fmt.Println(result)
}
