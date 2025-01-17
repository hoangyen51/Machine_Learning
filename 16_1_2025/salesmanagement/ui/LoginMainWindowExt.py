from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from salesmanagement.ui.LoginMainWindow import Ui_MainWindow
from salesmanagement.ui.MainProgramMainWindowExt import MainProgramMainWindowExt


class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_DangNhap.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        username=self.lineEdit_NhapUserName.text()
        password=self.lineEdit_2_NhapPassword.text()
        # giả lập đăng nhập
        if username=='admin' and password=='123':
            self.MainWindow.hide()
            self.mainwindow = QMainWindow()
            self.myui = MainProgramMainWindowExt()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg=QMessageBox()
            self.msg.setWindowTitle("Login thất bại")
            self.msg.setText("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập.")
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.show()