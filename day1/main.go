package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {

	file, _ := os.Open("t.txt")
	scanner := bufio.NewScanner(file)

	ans := 50
	cnt := 0

	for scanner.Scan() {
		line := scanner.Text()
		side := line[0]
		dis, _ := strconv.Atoi(line[1:])
		if side == 'L' {
			for i := dis; i > 0; i-- {
				ans--
				ans %= 100
				if ans == 0 {
					cnt++
				}
			}

		} else {
			for i := dis; i > 0; i-- {
				ans++
				ans %= 100
				if ans == 0 {
					cnt++
				}
			}
		}
	}
	fmt.Println(cnt)

}
