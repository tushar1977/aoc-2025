package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func part2(a int, b int) int {
	ans := 0
	for j := a; j <= b; j++ {
		ns := strconv.Itoa(j)
		for x := 1; x < len(ns); x++ {
			sub := ns[:x]
			if sub == "" {
				continue
			}
			repeatTimes := len(ns) / len(sub)

			built := strings.Repeat(sub, repeatTimes)
			if built == ns {
				val, _ := strconv.Atoi(ns)
				ans += val
			}
		}
	}
	return ans
}

func main() {
	file, _ := os.Open("t.txt")
	scanner := bufio.NewScanner(file)

	total := 0
	ans := 0
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.SplitSeq(line, ",")
		for v := range parts {
			r := strings.Split(v, "-")

			a, _ := strconv.Atoi(r[0])
			b, _ := strconv.Atoi(r[1])
			total += part2(a, b)

			for j := a; j <= b; j++ {
				s := strconv.Itoa(j)
				if len(s)%2 != 0 {
					continue
				}
				mid := len(s) / 2
				news := s[:mid] + s[:mid]

				if news == s {
					ans += j
				}
			}
		}
	}
	fmt.Println(ans)
	fmt.Println(total)
}
