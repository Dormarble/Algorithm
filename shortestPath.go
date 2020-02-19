package main

import (
	"fmt"
	"sync"
)

var nextNodeNum int

type queue struct {
	data   []int
	length int
}

func createQueue() *queue {
	queue := queue{}
	queue.data = []int{}
	queue.length = 0
	return &queue
}
func (q *queue) push(n int) {
	q.data = append(q.data, n)
	q.length++
}
func (q *queue) pop() (output int) {
	if q.length > 0 {
		output = q.data[0]
		q.data = q.data[1:]
		q.length--
		return
	} else {
		return -1
	}
}
func (q *queue) isEmpty() bool {
	if q.length == 0 {
		return true
	} else {
		return false
	}
}

type node struct {
	no         int
	adjNodeNum []int
}

func createNode() *node {
	node := node{}
	node.no = nextNodeNum
	node.adjNodeNum = []int{}
	nextNodeNum++

	return &node
}

func main() {
	var n, m, v, x, y int
	wait := new(sync.WaitGroup)
	paths := []int{}
	queue := createQueue()

	fmt.Scanln(&n, &m, &v)

	wait.Add(m)
	nodes := []*node{}
	for i := 0; i <= n; i++ {
		nodes = append(nodes, createNode())
		paths = append(paths, -1)
	}
	for i := 0; i < m; i++ {
		fmt.Scanln(&x, &y)

		go func(x int, y int) {
			nodes[x].adjNodeNum = append(nodes[x].adjNodeNum, y)
			wait.Done()
		}(x, y)
	}
	wait.Wait()
	paths[v] = 0
	queue.push(v)
	for !queue.isEmpty() {
		cur := queue.pop()
		if cur < 0 {
			panic("queue is empty")
		}
		for _, nodeNum := range nodes[cur].adjNodeNum {
			if paths[nodeNum] == -1 {
				queue.push(nodeNum)
				paths[nodeNum] = paths[cur] + 1
			}
		}
	}
	for i := 1; i <= n; i++ {
		fmt.Printf("%d ", paths[i])
	}
}
