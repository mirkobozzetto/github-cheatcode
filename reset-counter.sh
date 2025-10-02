#!/bin/bash
# Reset counter to 0 to restart daily commits
echo "0" > counter.txt
git add counter.txt
git commit -m "Reset counter for daily automation"
git push origin main
