#!/usr/bin/env bash
# setup mysql
# mysql -u root -p
# CREATE user 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
# GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost';
# CREATE DATABASE tyrell_corp
# CREATE TABLE nexus6( id int PRIMARY KEY, name VARCHAR(20))
# CHANGE REPLICATION SOURCE TO SOURCE_HOST='34.74.72.161', SOURCE_USER='replica_user', SOURCE_LOG_FILE='mysql-bin.000001', SOURCE_LOG_POS=899;
sudo apt update
sudo apt install mysql-server