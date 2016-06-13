#!/bin/bash
here=`pwd`

mkdir build
cd build
git clone https://github.com/ericoporto/fgmk.git
cd fgmk
cp -rf $here/ubuntu-related/data .
cp -f $here/ubuntu-related/setup.py .
cp -f $here/ubuntu-related/MANIFEST.in .
python3 setup.py --command-packages=stdeb.command bdist_deb
