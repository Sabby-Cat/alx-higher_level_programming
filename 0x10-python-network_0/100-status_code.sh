#!/bin/bash
# status Code get
curl -sL -w "%{http_code}" "$1" -o /dev/null
