import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import pyautogui
import time

# Configuring as a Windows service


class MouseMoverService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MouseMoverService"
    _svc_display_name_ = "Mouse Mover Service"
    _svc_description_ = "Moves the mouse every 10 seconds to prevent the computer from going to sleep."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)


def SvcDoRun(self):
    while True:
        pyautogui.moveRel(500, 100)
        time.sleep(10)

        # Check if the stop event has been set
        if win32event.WaitForSingleObject(self.stop_event, 0) == win32event.WAIT_OBJECT_0:
            break


if __name__ == '__main__':

    # Start the service
    win32serviceutil.HandleCommandLine(MouseMoverService)
