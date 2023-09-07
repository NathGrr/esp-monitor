import logging
import sys

import cfclient
import cfclient.ui.tabs
import cfclient.ui.toolboxes
import cflib.crtp
from cfclient.ui.dialogs.about import AboutDialog
from cfclient.ui.dialogs.bootloader import BootloaderDialog
from cfclient.utils.config import Config
from cfclient.utils.config_manager import ConfigManager
from cfclient.utils.input import JoystickReader
from cfclient.utils.logconfigreader import LogConfigReader
from cfclient.utils.zmq_led_driver import ZMQLEDDriver
from cfclient.utils.zmq_param import ZMQParamAccess
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.mem import MemoryElement
from cflib.crtp.udpdriver import UdpDriver
import time

def main():
    cf = Crazyflie(ro_cache=None,rw_cache=cfclient.config_path + "/cache")
    cflib.crtp.init_drivers()
    cf.open_link("udp://192.168.43.42")
    while True:
        time.sleep(1)
        print(cf.packet_received)

if __name__ == '__main__':
    main()