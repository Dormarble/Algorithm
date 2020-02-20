package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func dfs(lands *[][]int, union *[][]int, paraX int, paraY int) {
	moveX := []int{1, 1, 0, -1, -1, -1, 0, 1}
	moveY := []int{0, 1, 1, 1, 0, -1, -1, -1}

	for i := 0; i < len(moveX); i++ {
		x := paraX + moveX[i]
		y := paraY + moveY[i]

		if 0 <= x && x < len(*union) && 0 <= y && y < len((*union)[0]) {
			if (*union)[x][y] == 0 && (*lands)[x][y] == 1 {
				(*union)[x][y] = 1
				dfs(lands, union, x, y)
			}
		}
	}
}

func main() {
	var w, h int
	output := []int{}
	in := bufio.NewReader(os.Stdin)

	fmt.Scanln(&w, &h)

	for w != 0 && h != 0 {
		lands := make([][]int, h, h)
		union := make([][]int, h, h)
		var count int

		for i := 0; i < h; i++ {
			lands[i] = make([]int, w, w)
			union[i] = make([]int, w, w)
			for j := 0; j < w; j++ {
				union[i][j] = 0
			}
		}
		for i := 0; i < h; i++ {
			lineString, err := in.ReadString('\n')
			if err != nil {
				panic("invalid grid input")
			}
			lineString = lineString[:len(lineString)-1]
			chars := strings.Split(lineString, " ")

			for j := 0; j < w; j++ {
				if chars[j] == "1" {
					lands[i][j] = 1
				} else {
					lands[i][j] = 0
				}
			}
		}
		for i := 0; i < h; i++ {
			for j := 0; j < w; j++ {
				if union[i][j] == 0 && lands[i][j] == 1 {
					union[i][j] = 1
					dfs(&lands, &union, i, j)
					count++
				}
			}
		}
		output = append(output, count)

		fmt.Scanln(&w, &h)
	}

	for i := 0; i < len(output); i++ {
		fmt.Println(output[i])
	}
}
