# fgmkPackaging
Scripts to help packaging FGMK.

## Snap

    cd snap
    snapcraft stage
    snapcraft snap

### Building dependencies

On a clean Ubuntu 16.04 install, you need to install the following

    sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev snapcraft


### Installing Snap locally

    sudo snap install fgmk_0.1.0_amd64.snap


## Deb

To generate a `.deb` from fgmk source

    git clone https://github.com/ericoporto/fgmk.git
    cd fgmk
    python3 setup.py --command-packages=stdeb.command bdist_deb

The `.deb` file will be in the folder `deb_dist`, with the name `python3-fgmk_1.0.0-1_all.deb`


### Building dependencies

    sudo pip3 install stdeb
    sudo apt install python3-all
