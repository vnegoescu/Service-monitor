#!/bin/bash

curl -i -X GET -d '{"name":"writer"}' -H'Content-Type: application/json' localhost:5000/info
