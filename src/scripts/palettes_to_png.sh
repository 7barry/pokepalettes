#!/usr/bin/env bash
for i in {1..251}; do
  /Applications/Firefox.app/Contents/MacOS/firefox -screenshot \
  ~/Documents/Computers/Repos/pokepalettes/build/png/$i.png \
  file:///Users/Barry/Documents/Computers/Repos/pokepalettes/build/html/$i.html \
  --window-size=1000,1000
done

chmod +x rename.sh
./rename.sh
