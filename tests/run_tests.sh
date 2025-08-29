#!/usr/bin/env bash
set -euo pipefail
ROOT="$(dirname "$0")/.."
cd "$ROOT"
gcc -std=c11 -O2 -Wall -Wextra -Wpedantic main.c -o prog
for f in tests/input_*.txt; do
  i="$(basename "$f" .txt)"
  echo "== Running $i =="
  ./prog < "tests/${i}.txt" > "tests/${i}.out"
  diff -u "tests/${i/input/output}.txt" "tests/${i}.out" && echo "OK"
done
