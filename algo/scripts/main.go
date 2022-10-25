package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)

// Sort the list in ascending order and return them.
func quicksort(list []int) []int {
	if len(list) < 2 {
		return list
	}

	var left []int
	var right []int

	p := len(list) - 1
	v := list[p]

	list = append(list[:p])

	for i := 0; i < len(list); i++ {
		if list[i] < v {
			left = append(left, list[i])
		} else {
			right = append(right, list[i])
		}
	}

	left = quicksort(left)
	right = quicksort(right)

	return append(append(left, []int{v}...), right...)
}

// Sort the list in ascending order and return them.
func bubble_sort(list []int) []int {
	arr_size := len(list)
	for i := 0; i < arr_size; i++ {
		for j := arr_size - 1; j != i; j-- {
			if list[j] < list[j-1] {
				list[j], list[j-1] = list[j-1], list[j]
			}
		}
	}
	return list
}

// Sort the list in ascending order and return them.
func insertion_sort(list []int) []int {
	for j := 1; j < len(list); j++ {
		key := list[j]
		i := j - 1
		for i >= 0 && (list[i] > key) {
			list[i+1] = list[i]
			i--
		}
		list[i+1] = key
	}
	return list
}

// Returns the difference between the past timestamp and the present.
func get_result_time(_time time.Time) float64 {
	t := time.Now()
	result_time := t.Sub(_time)
	return result_time.Seconds()
}

// Read data from file.
func read_data(f_name string) []int {
	r, err := os.Open(f_name)
	if err != nil {
	}
	defer r.Close()
	var arr []int
	s := bufio.NewScanner(r)
	for s.Scan() {
		text := s.Text()

		i, err := strconv.Atoi(text)
		if err != nil {
			continue
		}

		arr = append(arr, i)
	}
	return arr
}

func main() {
	f, err := os.OpenFile("../results/res.csv", os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}
	newLine := ""
	for i := 20_000; i <= 100_000; i += 20_000 {
		start_time := time.Now()

		quicksort(read_data(fmt.Sprintf("../data/%d.txt", i)))

		newLine = fmt.Sprintf("Go,quick_sort,%d,%f", i, get_result_time(start_time))

		_, err = fmt.Fprintln(f, newLine)
		if err != nil {
			fmt.Println(err)
		}

		start_time = time.Now()

		insertion_sort(read_data(fmt.Sprintf("../data/%d.txt", i)))

		newLine = fmt.Sprintf("Go,insertion_sort,%d,%f", i, get_result_time(start_time))

		_, err = fmt.Fprintln(f, newLine)
		if err != nil {
			fmt.Println(err)
		}

		start_time = time.Now()

		bubble_sort(read_data(fmt.Sprintf("../data/%d.txt", i)))

		newLine = fmt.Sprintf("Go,bubble_sort,%d,%f", i, get_result_time(start_time))

		_, err = fmt.Fprintln(f, newLine)
		if err != nil {
			fmt.Println(err)
		}
	}

}
