#!/bin/bash
# size body 
curl -sI $1 | grep "Content-Length:" | cut -d' ' -f2
