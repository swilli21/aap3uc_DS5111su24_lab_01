find . -type f -exec wc -w {} + | awk '{total += $1} END {print total}'
