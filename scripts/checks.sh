#!/usr/bin/env bash

set -x

ruff --fix .
black . --line-length=120
mypy --check-untyped-defs -p src.app