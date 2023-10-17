"""
******************************************************************************
* @author  ARMCNC site:www.armcnc.net github:armcnc.github.io
******************************************************************************
"""

import sys
import signal
import subprocess
from .utils import Utils
from .cnc import CNC
from .machine import Machine
import launch as launch_file

class Init:

    def __init__(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        self.utils = Utils(self)
        self.machine = Machine(self)
        self.armcnc = CNC(self)
        self.start()

    def start(self):
        if len(sys.argv) != 2:
            self.utils.log.error("Please specify the machine configuration file.")
            sys.exit(1)

        linuxcnc_pid = subprocess.Popen(["pidof", "-x", "linuxcnc"], stdout=subprocess.PIPE)
        linuxcnc_pid_result = linuxcnc_pid.communicate()[0]
        if len(linuxcnc_pid_result) > 0:
            self.utils.log.error("System detected to be running.")
            sys.exit(1)

        armcnc_start = "armcnc_start"
        if armcnc_start in dir(launch_file):
            self.armcnc.start()
            getattr(launch_file, armcnc_start)(self)
        self.signal_handler(False, False)

    def message_handle(self, message):
        if self.armcnc and message["command"]:
            armcnc_message = "armcnc_message"
            if armcnc_message in dir(launch_file):
                getattr(launch_file, armcnc_message)(self, message)

    def signal_handler(self, signum, frame):
        armcnc_exit = "armcnc_exit"
        if armcnc_exit in dir(launch_file):
            getattr(launch_file, armcnc_exit)(self)
        sys.exit()
