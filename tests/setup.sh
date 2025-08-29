#!/usr/bin/env bash
set -euo pipefail
ROOT="$(dirname "$0")/.."
cd "$ROOT"
python3 tests/generate.py --all
gcc -std=c11 -O2 -Wall -Wextra -Wpedantic main.c -o prog
