"""
******************************************************************************
* @author  ARMCNC site:www.armcnc.net github:armcnc.github.io
******************************************************************************
"""

import linuxcnc

class ErrorChannel:

    def __init__(self):
        self.linuxcnc = linuxcnc
        self.api = self.linuxcnc.error_channel()