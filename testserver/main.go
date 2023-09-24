package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"time"
)

func main() {
	// Create a server on port 8443
	srv := &http.Server{Addr: ":8443", Handler: http.HandlerFunc(handle)}
	// Start the server with TLS.
	log.Printf("Serving on https://0.0.0.0:8443")
	log.Fatal(srv.ListenAndServeTLS("server.crt", "server.key"))
}

// race
var idx = 0

func handle(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path == "/long" {
		time.Sleep(3 * time.Second)
	}

	idx++

	// Log the request protocol
	log.Printf("[idx=%d] Got connection: %s", idx, r.Proto)

	// Log request headers
	log.Println("Got headers:")
	for k, v := range r.Header {
		log.Printf("%s: %v\n", k, v)
	}

	if body, err := io.ReadAll(r.Body); err == nil {
		log.Printf("Got body: %s\n", body)
	}

	// Send a message back to the client
	w.Write([]byte("Hello:" + fmt.Sprintf("[idx=%d] Seconds: %d, Milli: %d", idx, time.Now().Unix(), time.Now().UnixMilli())))
}
