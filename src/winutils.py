# -*- coding: utf-8 -*-  
'''
Windows例程
@author: sanli
'''
from pywinauto import application
from subprocess import Popen

class JAVApp:
    def __init__(self, app = 'C:\\HHQ\\JAV\\IPCClient\\JAVClient.exe' , cwd = 'C:\\HHQ\\JAV\\IPCClient' ,
                  user = 'admin' , password = 'admin' ):
        self.app = app
        self.cwd = cwd
        self.user = user
        self.password = password
        self.isstarted = False
        
    def start_auto_login(self):
        self.proc = proc = Popen([self.app], cwd=self.cwd)
        self.app = app = application.Application()
        app.connect_( process = proc.pid )
        self.logindia = logindia = app.top_window_()
        # for print the indentifiers
        #logindia.print_control_identifiers()
        logindia['Edit1'].SetEditText(self.user)
        logindia['Edit2'].SetEditText(self.password)
        logindia['Button1'].Click()
        self.isstarted = True
    
    
    def stop(self):
        self.proc.kill()
        self.isstarted = False
    
    
    def restart(self):
        if self.isstarted :
            self.stop()
        
        self.start_login()
        
        
if __name__ == "__main__":
    app = JAVApp()
    app.start_auto_login()
        