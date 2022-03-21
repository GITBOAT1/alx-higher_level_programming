#!/bin/bash
# Bash script that takes in a URL, sends a request to
curl -sI $1 | grep 'Allow' | cut -d ' ' -f2-
