find . -type f -exec wc -l {} + | awk '{total += $1} END {print total}'
