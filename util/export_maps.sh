#!/usr/bin/bash

# exporting tiled maps to image files

cd "$(dirname "$0")"/.. || exit
for f in *.json ; do
	f_base=$(basename "$f" .json)
	echo "converting $f to png"
	tiled --export-map tmx "$f" "$f_base.tmx"
	tmxrasterizer "$f_base.tmx" "$f_base.png"
	rm "$f_base.tmx"
done

