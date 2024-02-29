#!/bin/bash
# status Code get
curl -so /dev/null -w '%{http_code}' $1i
