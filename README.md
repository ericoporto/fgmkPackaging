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
