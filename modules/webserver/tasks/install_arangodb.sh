#!/usr/bin/env bash
# installs Arangodb
curl -OL https://download.arangodb.com/arangodb34/DEBIAN/Release.key
apt-key add - < Release.key


echo 'deb https://download.arangodb.com/arangodb34/DEBIAN/ /' | tee /etc/apt/sources.list.d/arangodb.list
apt-get install apt-transport-https
apt-get update

echo arangodb3 arangodb3/backup boolean false | debconf-set-selections
echo arangodb3 arangodb3/upgrade boolean false | debconf-set-selections
echo arangodb3 arangodb3/password password $PT_password | debconf-set-selections
echo arangodb3 arangodb3/password_again password $PT_password | debconf-set-selections
echo arangodb3 arangodb3/storage_engine select $PT_storage  | debconf-set-selections

apt-get install -y arangodb3=3.4.7-1
# pkill -f arangodb