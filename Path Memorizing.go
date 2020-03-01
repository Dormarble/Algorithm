package main


import (
	"fmt"
    "sort"
)

func main() {
	tickets := [][]string{{"ICN", "COO"}, {"ICN", "BOO"}, {"COO", "ICN"}, {"BOO", "DOO"}}
	d := solution(tickets)

	fmt.Print(d)
}
//최종 경로를 저장할 변수를 전역변수로 선언
var answerInt []int
var adjList [][]int
var isUsed [][]bool
var totalNum int

func solution(tickets [][]string) []string {
    answerInt = make([]int, len(tickets)+1, len(tickets)+1)
    s := map[string]int{}
    for _, ticket := range tickets {
        s[ticket[0]] = 0
        s[ticket[1]] = 0
    }

    cities := make([]string, len(s), len(s))
    tmp := 0
    for ss, _ := range s {
        cities[tmp] = ss
        tmp++
    }
    sort.Slice(cities, func(i, j int) bool {
        return cities[i] < cities[j]
    })
    cityToIdx := map[string]int{}
    for i, city := range cities {
        cityToIdx[city] = i
    }
    adjList = *createAdjList(tickets, cityToIdx)
    isUsed = make([][]bool, len(cityToIdx), len(cityToIdx))
    for i, aaa := range adjList {
        isUsed[i] = make([]bool, len(aaa), len(aaa))
    }
	totalNum = len(tickets)
	dfs(cityToIdx["ICN"], []int{cityToIdx["ICN"]}, 0)

    answer := make([]string, len(tickets)+1, len(tickets)+1)
    for i, p := range answerInt {
        answer[i] = cities[p]
    }

    return answer
}

func dfs(city int, path []int, depth int) {
	
// 각각의 dfs의 끝에서 깊이를 확인하고 끝에 다다른 경로를 최종 경로 변수에 저장
// 이 if문 안에 조건을 더 넣어서 어떤 경로를 최종 경로로 지정할 것인지 결정할 수 있음
    if depth == totalNum {
		copy(answerInt, path)
		return
    }

    for i, dest := range adjList[city] {
        if isUsed[city][i] == false {
            isUsed[city][i] = true

            path = append(path, dest)
            dfs(dest, path, depth+1)
            isUsed[city][i] = false
			path = path[:len(path)-1]
        }
    }
    return
}

func createAdjList(tickets [][]string, cityToIdx map[string]int) *[][]int {
    length := len(cityToIdx)
    adjList := make([][]int, length, length)

    for _, ticket := range tickets {
        start := cityToIdx[ticket[0]]
        desti := cityToIdx[ticket[1]]

        adjList[start] = append(adjList[start], desti)
    }
    for i:=0; i<len(adjList); i++ {
        sort.Slice(adjList[i], func (a, b int) bool {
            return adjList[i][a] < adjList[i][b]
        })
    }
    return &adjList
}