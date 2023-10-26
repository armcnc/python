"""
******************************************************************************
* @author  ARMCNC site:www.armcnc.net github:armcnc.github.io
******************************************************************************
"""

class Machine:

    def __init__(self, framework):
        self.framework = framework
        self.user = "armcnc"
        self.coordinates = []
        self.is_alive = False
        self.info = None
