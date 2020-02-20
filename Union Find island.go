package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type pair struct {
	root int
	size int
}

func createPair(root int, size int) *pair {
	pair := pair{root, size}
	return &pair
}

type land struct {
	location int
	adj      []int
}

func createLand(loc int) *land {
	land := land{}
	land.location = loc
	land.adj = []int{}

	return &land
}
func find_union(union map[int]*pair, loc int) int {
	root := loc
	for union[root].root != -1 {
		root = union[root].root
	}
	set := loc
	for union[set].root != -1 {
		union[set].root = root
		set = union[set].root
	}
	return root
}
func setAdjustList(lands map[int]*land, land *land, loc int, w int, h int) {
	if _, exist := lands[loc-1]; exist {
		if !isLeft(loc, w) {
			land.adj = append(land.adj, loc-1)
		}
	}
	if _, exist := lands[loc+1]; exist {
		if !isRight(loc, w) {
			land.adj = append(land.adj, loc+1)
		}
	}
	if _, exist := lands[loc-w]; exist {
		if !isTop(loc, w) {
			land.adj = append(land.adj, loc-w)
		}
	}
	if _, exist := lands[loc+w]; exist {
		if !isBottom(loc, w, h) {
			land.adj = append(land.adj, loc+w)
		}
	}
	if _, exist := lands[loc+w+1]; exist {
		if !isRight(loc, w) && !isBottom(loc, w, h) {
			land.adj = append(land.adj, loc+w+1)
		}
	}
	if _, exist := lands[loc+w-1]; exist {
		if !isLeft(loc, w) && !isBottom(loc, w, h) {
			land.adj = append(land.adj, loc+w-1)
		}
	}
	if _, exist := lands[loc-w+1]; exist {
		if !isRight(loc, w) && !isTop(loc, w) {
			land.adj = append(land.adj, loc-w+1)
		}
	}
	if _, exist := lands[loc-w-1]; exist {
		if !isLeft(loc, w) && !isTop(loc, w) {
			land.adj = append(land.adj, loc-w-1)
		}
	}
}
func isLeft(loc int, w int) bool {
	return (loc%w == 0)
}
func isRight(loc int, w int) bool {
	return (loc%w == w-1)
}
func isTop(loc int, w int) bool {
	return (loc/w == 0)
}
func isBottom(loc int, w int, h int) bool {
	return (loc/w == h-1)
}

func main() {
	var w, h int
	output := []int{}
	in := bufio.NewReader(os.Stdin)
	fmt.Scanln(&w, &h)

	for w != 0 && h != 0 {
		lands := make(map[int]*land)

		for i := 0; i < h; i++ {
			lineString, err := in.ReadString('\n')
			if err != nil {
				panic(err)
			}
			lineString = lineString[:len(lineString)-1]
			chars := strings.Split(lineString, " ")

			for j := 0; j < w; j++ {
				if chars[j] == "1" {
					lands[w*i+j] = createLand(w*i + j)
				}
			}

		}

		for loc, land := range lands {
			setAdjustList(lands, land, loc, w, h)
		}

		union := make(map[int]*pair)
		for loc, _ := range lands {
			union[loc] = createPair(-1, 1)
		}

		for loc, land := range lands {
			for _, adj := range land.adj {

				groupAdj := find_union(union, adj)
				groupLoc := find_union(union, loc)

				if groupAdj == groupLoc {
					continue
				}

				if union[groupLoc].size >= union[groupAdj].size {
					union[groupAdj].root = groupLoc
					union[groupLoc].size += union[groupAdj].size
				} else {
					union[groupLoc].root = groupAdj
					union[groupAdj].size += union[groupLoc].size
				}
			}
		}
		count := 0
		for _, pair := range union {
			if pair.root == -1 {
				count++
			}
		}
		output = append(output, count)

		fmt.Scanln(&w, &h)
	}
	for i := 0; i < len(output); i++ {
		fmt.Printf("%d\n", output[i])
	}
}
