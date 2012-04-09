# -*- coding: utf-8 -*-  
'''
Windows例程
@author: sanli
'''
from pywinauto import application
from subprocess import Popen

class JAVApp:
    def __init__(self, apppath = 'C:\\HHQ\\JAV\\IPCClient\\JAVClient.exe' , cwd = 'C:\\HHQ\\JAV\\IPCClient' ,
                  user = 'admin' , password = 'admin' ):
        self.apppath = apppath
        self.cwd = cwd
        self.user = user
        self.password = password
        self.isstarted = False
        
    def start_auto_login(self):
        if not self.isstarted:
            if not hasattr(self, 'proc'):
                self.proc = Popen([self.apppath], cwd=self.cwd)
                
            if not hasattr(self , 'app'):
                self.app = application.Application()
                
            self.app.connect_( process = self.proc.pid )
            self.logindia = logindia = self.app.top_window_()
            # for print the indentifiers
            #logindia.print_control_identifiers()
            logindia['Edit1'].SetEditText(self.user)
            logindia['Edit2'].SetEditText(self.password)
            logindia['Button1'].Click()
            self.isstarted = True
        else:
            #已经启动了
            pass
    
    
    def stop(self):
        self.proc.kill()
        del(self.proc)
        self.isstarted = False
    
    
    def restart(self):
        if self.isstarted :
            self.stop()
        
        self.start_login()


'''CMDServer开启一个网络端口，为视频转发服务预留
'''
import socket
class CMDServer:
    def __init__(self, host = 'localhost' , port = 38000):
        self.host = host
        self.port = port
        
    '''启动服务，如果端口已经被占用，则抛出异常
    '''
    def start_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((self.host , self.port))
            sock.listen(1)
            conn, addr = sock.accept()
        except socket.error, msg:
            sock.close()
            sock = None
            raise Exception("启动服务失败，另外一个实例可能已经启动了。 ")
        
if __name__ == "__main__":
    app = JAVApp()
    app.start_auto_login()
        