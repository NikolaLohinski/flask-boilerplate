// -*- coding: utf-8 -*-
//
// Golang (very) simple static files server
// @author: NikolaLohinski (https://github.com/NikolaLohinski)
// @date: 09/02/09
//

package main


import (
  "net/http"
  "path"
)

func main() {
  http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    file := path.Join("static", r.URL.Path[1:])
    http.ServeFile(w, r, file)
  })
  if err := http.ListenAndServe(":8765", nil); err != nil {
    panic(err)
  }
}