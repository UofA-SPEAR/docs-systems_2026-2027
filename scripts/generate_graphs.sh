#!/bin/sh
# Regenerate images for the given data/ folders (all of data/ if none given).
# Add a line under "case" to support a new file type.
set -e
root=$(git rev-parse --show-toplevel)
cd "$root"
folders=${*:-$(find data -mindepth 1 -type d)}

for src in $folders; do
  out="docs/graphs/${src#data/}"
  mkdir -p "$out"
  echo "Generating $out"
  for f in "$src"/*; do
    case "$f" in
      *.puml) plantuml -tpng -o "$root/$out" "$f" ;;
      *.dot)  dot -Tpng "$f" -o "$out/$(basename "${f%.*}").png" ;;
      *.py)   python3 "$f" "$out" ;;
    esac
  done
done
