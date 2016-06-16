#!/bin/bash
#Requires git, stdeb, python3
here=`pwd`

mkdir build
cd build
git clone https://github.com/ericoporto/fgmk.git
cd fgmk
cp -f $here/fgmk-map.svg .
cp -f $here/fgmk.desktop .
cp -f $here/fgmk.svg .
cp -f $here/fgmk.xml .
cp -f $here/MANIFEST.in .
cp -f $here/setup.py .

python3 setup.py --command-packages=stdeb.command bdist_deb
