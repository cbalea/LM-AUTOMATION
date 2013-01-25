#!/bin/sh
SUITES_SET=$1

VE_DIR="ve" # path to the virtual env directory
rm -rf $VE_DIR # remove the old ve
virtualenv $VE_DIR --no-site-packages

set +o nounset
source $VE_DIR/bin/activate
set -o nounset

##### REQUIREMENTS##########
pip install nose==1.1.2
pip install selenium==2.28.0
pip freeze
firefox --version

killall firefox
sleep 5
killall python
sleep 5
killall nosetests
sleep 5
killall lettuce
sleep 5
killall firefox
sleep 5

python run_suites.py $SUITES_SET
