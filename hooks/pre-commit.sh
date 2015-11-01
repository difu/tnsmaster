#!/usr/bin/env bash
# Ensure that all unit tests are successful
python3 -m unittest discover tests/
RESULT_UNITTEST=$?
[ $RESULT_UNITTEST -ne 0 ] && exit 1
exit 0
