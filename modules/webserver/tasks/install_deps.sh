#!/usr/bin/env bash
# install deps for the webserver
apt update
apt install -y curl wget
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
~/.nvm/nvm install 12 && ~/.nvm/nvm alias default node

apt update
apt install -y yarn --no-install-recommends yarn
apt install -y nginx python3 python3-pip git 
yarn global add parcel-bundler




