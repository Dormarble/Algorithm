package main

import (
	"fmt"
)

const MAX int = 101

var a [][]int
var d [MAX]int
var c [MAX]bool
var node int = 3
var m, s int

func dfs(x int) bool {
	for i := 0; i < len(a[x]); i++ {
		t := a[x][i]

		if c[t] {
			continue
		}
		c[t] = true
		if d[t] == 0 || dfs(d[t]) {
			d[t] = x
			return true
		}
	}
	return false
}

func main() {
	a = make([][]int, node+1, node+1)
	for i := 1; i <= node; i++ {
		a[i] = []int{}
	}
	a[1] = append(a[1], 1)
	a[1] = append(a[1], 2)
	a[1] = append(a[1], 3)
	a[2] = append(a[2], 1)
	a[3] = append(a[3], 2)

	var count int = 0

	for i := 1; i <= node; i++ {
		c = [MAX]bool{}
		if dfs(i) {
			count++
		}
	}
	fmt.Printf("%d개의 매칭이 이루어짐\n", count)
	for i := 1; i <= 100; i++ {
		if d[i] != 0 {
			fmt.Printf("%d -> %d\n", d[i], i)
		}
	}
}
