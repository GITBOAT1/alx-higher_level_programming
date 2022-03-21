#!/bin/bash
# that URL, and displays the size of the body of the response
curl -sI $1 | grep 'Content-Length' | cut -f2 -d ':'
