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
        self.task = threading.Thread(name="status_task", target=self.task)
        self.task.daemon = True
        self.task.start()

    def task(self):
        while True:
            if self.framework.machine.is_alive:
                try:
                    self.api.poll()
                except linuxcnc.error as detail:
                    self.framework.utils.service.service_write({"command": "launch:error", "message": detail, "data": False})

                self.framework.utils.json.dumps(self.api)
                # for x in dir(self.api):
                #     if not x.startswith("_"):
                #         print(x, getattr(self.api, x))

            self.framework.utils.set_sleep(5)
