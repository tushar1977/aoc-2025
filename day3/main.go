package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func jolts(bank string, nbat int) int {

	s, p := "", 0
	for b := nbat; b > 0; b-- {
		for i := p; i <= len(bank)-b; i++ {
			if bank[i] > bank[p] {
				p = i
			}

		}

		s += string(bank[p])
		p++
	}
	n, _ := strconv.Atoi(s)
	return n

}

func main() {
	file, _ := os.ReadFile("t.txt")

	part1, part2 := 0, 0

	for s := range strings.FieldsSeq(string(file)) {
		part1 += jolts(s, 2)
		part2 += jolts(s, 12)

	}

	fmt.Println(part1)
	fmt.Println(part2)

}
