#!/bin/bash

current_dir=$(PWD)
PROJECT_NAME="print_tokens"


rm -rf build
mkdir build
cd build

cmake .. -DPROJECT_NAME=${PROJECT_NAME} && make && ./$PROJECT_NAME $@
cd $current_dir
