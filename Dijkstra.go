package main

import (
	"fmt"
)

var found []bool
var distance []int
var weight [][]int

func choose(distance []int, n int, found []bool) int {
	var min, minpos int
	min = 2 << 62 - 1
	minpos = -1
	
	for i:=0; i<n; i++ {
		if distance[i] < min && !found[i] {
			min = distance[i]
			minpos = i
		}
	}
	return minpos	
}

func shortestPath(start int, n int) {
	var u int
	for i:=0; i<n; i++ {
		distance[i] = weight[start][i]
		found[i] = false
	}
	found[start] = true
	distance[start] = 0
	
	for i:=0; i<n-2; i++ {
		u = choose(distance, n, found)
		found[u] = true
		for w:=0; w<n; w++ {
			if !found[w] {
				if(distance[u] + weight[u][w]<distance[w]) {
					distance[w] = distance[u] + weight[u][w]
				}
			}
		}
	}
}

func main() {
	shortestPath(&weight, 0, 7)
	
	fmt.Println(distance)
}
