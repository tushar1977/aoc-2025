package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.ReadFile("t.txt")
	var ranges [][2]int
	ans1 := 0
	var queries []int
	for s := range strings.FieldsSeq(string(file)) {
		if strings.Contains(s, "-") {
			parts := strings.Split(s, "-")
			if len(parts) == 2 {
				a, _ := strconv.Atoi(parts[0])
				b, _ := strconv.Atoi(parts[1])

				ranges = append(ranges, [2]int{a, b})

			}

		} else {
			v, _ := strconv.Atoi(s)
			queries = append(queries, v)
		}

	}

	//NEVER WORKS
	//mp := make(map[int]int)
	//
	// for _, q := range ranges {
	// 	for i := q[0]; i <= q[1]; i++ {
	// 		if _, exists := mp[i]; !exists {
	// 			mp[i] = 1
	// 		}
	// 	}
	// }
	//
	// for _, q := range queries {
	// 	if _, e := mp[q]; e {
	// 		fmt.Println(e)
	// 		ans1++
	// 	}
	// }

	for _, q := range queries {
		for _, r := range ranges {
			l, rr := r[0], r[1]
			if q >= l && q <= rr {
				ans1++
				break
			}
		}

	}

	fmt.Println(ans1)

	sort.Slice(ranges, func(i, j int) bool {

		return ranges[i][0] < ranges[j][0]
	})
	merged := make([][2]int, 0)

	for _, q := range ranges {
		l, r := q[0], q[1]
		if len(merged) == 0 || l > merged[len(merged)-1][1]+1 {

			merged = append(merged, [2]int{l, r})

		}

		if r > merged[len(merged)-1][1] {
			merged[len(merged)-1][1] = r
		}
	}

	fmt.Println(merged)
	fmt.Println(len(merged))

}
