#!/bin/bash
# show all methods possible
curl -sI -X OPTIONS $1 | grep 'Allow:' | cut -d ' ' -f2-
