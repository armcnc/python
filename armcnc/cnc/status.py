"""
******************************************************************************
* @author  ARMCNC site:www.armcnc.net github:armcnc.github.io
******************************************************************************
"""

import threading
import linuxcnc

class Status:

    def __init__(self, framework):
        self.framework = framework
        self.linuxcnc = linuxcnc
        self.api = linuxcnc.stat()
        self.data = None
        self.task = threading.Thread(name="status_task", target=self.task)
        self.task.daemon = True
        self.task.start()

    def task(self):
        while True:
            if self.framework.machine.is_alive:
                try:
                    self.data = self.api.poll()
                except linuxcnc.error as detail:
                    self.framework.utils.service.service_write({"command": "launch:error", "message": detail, "data": False})

                print(self.data)

            self.framework.utils.set_sleep(10)
