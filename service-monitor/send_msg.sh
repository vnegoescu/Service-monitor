#!/bin/bash

curl -X POST -d "{\"text\":\"$1\"}" -H'Content-Type: application/json' localhost:6000
