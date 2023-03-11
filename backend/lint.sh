#!/usr/bin/env bash

# red=$(tput setaf 1)
green=$(tput setaf 2)
reset=$(tput sgr0)

set -x
flake8
