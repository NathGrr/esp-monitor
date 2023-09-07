#!/bin/bash

git submodule init
git submodule update

cd /workspaces/esp-monitor/crazyflie-lib-python && pip3 install -r requirements.txt && pip3 install -e .
cd /workspaces/esp-monitor/crazyflie-clients-python && pip3 install -e .