#!/bin/bash

find . -type f -name ".DS_Store" -size 0 -print0 -exec rm {} \;

