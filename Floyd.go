package main

import "fmt"

func main() {
	var n int
	var pathNum int
	var adjMatrix [][]int
	const INF = 100000000
	
	fmt.Scanln(&n)
	adjMatrix = make([][]int, n, n)
	
	for i:=0; i<n; i++ {
		adjMatrix[i] = make([]int, n, n)
		for j:=0; j<n; j++ {
			if i==j {
				adjMatrix[i][j] = 0
			} else {
				adjMatrix[i][j] = INF
			}
		}
	}
	
	fmt.Scanln(&pathNum)
	for i:=0; i<pathNum; i++ {
		var a, b, weight int
		
		fmt.Scanln(&a, &b, &weight)
		a--
		b--
		if weight < adjMatrix[a][b] {
			adjMatrix[a][b] = weight
		}
	}
	
	for k:=0; k<n; k++ {
		for j:=0; j<n; j++ {
			if adjMatrix[k][j] == INF {
				continue
			}
			for i:=0; i<n; i++ {
				if adjMatrix[i][j] > adjMatrix[i][k] + adjMatrix[k][j] {
					adjMatrix[i][j] = adjMatrix[i][k] + adjMatrix[k][j]
				}
			}
		}
	}
	
	for i:=0; i<n; i++ {
		for j:=0; j<n; j++ {
			if adjMatrix[i][j] == INF {
				adjMatrix[i][j] = 0
			}
			fmt.Printf("%d ", adjMatrix[i][j])
		}
		fmt.Println()
	}
}