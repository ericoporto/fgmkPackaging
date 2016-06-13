#!/bin/bash
here=`pwd`

mkdir build
cd build
git clone https://github.com/ericoporto/fgmk.git
cd fgmk
cp "$here/ubuntu-related/*" .
python3 setup.py --command-packages=stdeb.command bdist_deb
