package main

import "fmt"

type Checkpoint struct {
	Name   string
	Status string
	Detail string
}

func describe(checkpoint Checkpoint) string {
	return fmt.Sprintf("%s: %s (%s)", checkpoint.Name, checkpoint.Status, checkpoint.Detail)
}

func main() {
	checkpoints := []Checkpoint{
		{Name: "ingest", Status: "ok", Detail: "rows normalized"},
		{Name: "review", Status: "hold", Detail: "extraction fixture marker: shared code sample"},
		{Name: "publish", Status: "ok", Detail: "index refreshed"},
	}

	for _, checkpoint := range checkpoints {
		fmt.Println(describe(checkpoint))
	}
}
