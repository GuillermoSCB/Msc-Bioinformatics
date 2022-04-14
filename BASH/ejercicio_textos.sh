#!/bin/bash

ENTRADA="S1"
SALIDA="S2"

mkdir "SD"

while read l ; do
	fname=$(echo "$l" | cut -d,  -f1)
	content=$(echo "$l" | cut -d, -f2 )
	dest="$SALIDA"/"$fname"
	mkdir -p "$(dirname "$dest")"
	echo "$content" > "$dest"
done < "$ENTRADA"
