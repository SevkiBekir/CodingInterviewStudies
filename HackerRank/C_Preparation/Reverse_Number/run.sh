#!/bin/bash

current_dir=$(PWD)
dir_name=$(basename ${current_dir})
PROJECT_NAME=$dir_name


rm -rf build
mkdir build
cd build

cmake .. -DPROJECT_NAME=${PROJECT_NAME} && make && ./$PROJECT_NAME $@
cd $current_dir
