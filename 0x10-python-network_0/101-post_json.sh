#!/bin/bash
# give JSON data
curl -s -d "@$2" -X POST -H 'Content-Type: application/json' $1
