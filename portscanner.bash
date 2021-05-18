#! /bin/bash

# script designed to target and find hosts with permission with MYSQL installed.. executed via kali linux 

nmap -sT 192.168.1.1/24 -p 3306 >/dev/null -oG MySQLscan # example 

cat MySQLscan | grep open > MySQLscan2 

cat MySQLscan2 

# ez lol