# -*- coding: utf-8 -*-  
'''
JAV控制器主（JAVShell）要用来控制JAV Client的运行，包括一下主要功能：
1. 开机自动运行JAVShell
2. 可以设置安装的Host机器自动登陆，可以设置登陆用的用户名，密码
3. 修改JAV程序的用户界面，包括启动画面，图标文件
4. 可以在JAVShell中启动或停止JAVClient程序
5. 启动JAVClient之后自动输入用户名，密码，打开到JAVClient的主界面
6. 提供界面，配置JAVClient的文件存储路径（下载，照片，日志，录像）
7. 提供新的安装程序，一键安装JAVShell和JAVClient，安装时，在D：创建存储路径
8. JAVShell程序运行时常驻内存，监控JAVClient的运行，如果异常JAVClient异常退出或者是被关闭，就重新启动。运行时在系统托盘上有个小图标，单击弹出JAVShell窗口

补充说明：
1. JAVShell是个独立的程序，用pyQT开发
2. 只能修改JAVClient中的图片和资源，不能修改JAVClient的逻辑。
3. 重新打包后的安装程序可能会比较大（需要保函Python和QT的Runtime Lib，不多于80M

@author: sanli
'''

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSlot
from PyQt4.QtGui import QApplication, QDialog
from winutils import JAVApp, CMDServer
from ui_dialog import Ui_MainDialog
from ui_about import Ui_About



class MainDialog(QDialog):
    '''主对话框窗口
    '''
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_MainDialog()
        self.ui.setupUi(self) 
        self.icon = QtGui.QIcon(':/img/images2.jpg')
        self.setWindowIcon(self.icon)
        self.setIcon()
        self.about_dialog = None
        #绑定信号处理器
        self.bind_handler()      

    def setIcon(self):
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.ui.action_start)
        self.trayIconMenu.addAction(self.ui.action_stop)
        self.trayIconMenu.addAction(self.ui.action_restart)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.ui.action_config)
        self.trayIconMenu.addAction(self.ui.action_about)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.ui.action_exit)
        
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setIcon(self.icon)
        self.trayIcon.show()
        self.trayIcon.setContextMenu(self.trayIconMenu)

    
    def closeEvent(self, event):
        if self.trayIcon.isVisible():
#            QtGui.QMessageBox.information(self, "JAVShell",
#                   QtGui.QApplication.translate("MainDialog", "自动登录JAV", None, QtGui.QApplication.UnicodeUTF8))
            self.hide()
            event.ignore()
            
    '''显示Dailog，在这个函数中读取所有的配置，并显示到界面上
    '''
    def show_dialog(self):
        #TODO
        pass
    
    
    def bind_handler(self):
        self.ui.action_about.triggered.connect(self.about)
        self.ui.action_exit.triggered.connect(self.quit)
        self.ui.action_start.triggered.connect(self.start_jav)
        self.ui.action_stop.triggered.connect(self.stop_jav)
#        self.ui.action_restart.triggered.connect(self)
        self.trayIcon.activated.connect(self.show_dialog)

    @pyqtSlot()        
    def about(self):
        if self.about_dialog == None :
            self.about_dialog = AboutDialog()
        self.about_dialog.show()
        
        
    @pyqtSlot()
    def quit(self):
        self.trayIcon.hide()
        QtGui.QApplication.quit()
    
    @pyqtSlot()
    def start_jav(self):
        if not hasattr(self, 'javapp'):
            self.javapp = JAVApp() 
        self.javapp.start_auto_login()
    
    @pyqtSlot()
    def stop_jav(self):
        if not hasattr(self, 'javapp'):
            self.javapp = JAVApp()
        self.javapp.stop()
        
    '''保存状态改变内容
    '''
    def save_state(self):
        pass
    
    
    def done(self, *args, **kwargs):
        #return QDialog.done(self, *args, **kwargs)
        #检查状态，决定操作
        if args == QDialog.Accepted :
            # TODO: 提醒用户状态改变，需要重启JavClient
            pass
            self.save_state()
            # TODO: 重启
            
        self.hide()
        pass
    
    

        
        
class AboutDialog(QDialog):
    '''关于对话框
    '''
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_About()
        self.ui.setupUi(self)
    

if __name__ == "__main__":
    locale = QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China) 
    QtCore.QLocale.setDefault(locale)
    
    server = CMDServer()
    try:
        server.start_server()
    except Exception, msg:
        print msg
        exit(0)
        
    app = QtGui.QApplication(sys.argv)
    main = MainDialog() 
    #main.show()
    sys.exit(app.exec_())
