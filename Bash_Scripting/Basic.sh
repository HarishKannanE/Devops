#!/bin/bash

echo "Welcome to bash script."
    # to print welcome to bash script

sudo yum install wget unzip httpd -y > /dev/null
    # redirect output to /dev/null if there is no error, if there is error display the error.

sudo yum install wget unzip httpd -y &> /dev/null
    # redirect output to /dev/null no matter the output