import sys
import time
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QCompleter, QLineEdit
import douyu
import main_window
import login_window
import qdarkstyle
import config
from pathlib2 import Path


class CMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_ui()

    def set_ui(self):
        config.ui = self.ui
        config.statusBar = self.statusBar()
        config.progressBar = self.ui.progressBar
        self.ui.pushButton.setEnabled(False)
        self.statusBar().showMessage('软件已准备就绪')
        self.ui.textBrowser.append(
            f"当前用户代理:\n{self.ui.comboBox.currentText()}\n若程序运行缓慢，可点击上方切换用户代理!")
        file_dir = Path.cwd().joinpath('douyu_file')
        if not Path.exists(file_dir):
            Path.mkdir(file_dir)
        self.signal_pbt()

    def closeEvent(self, event):  # 重写关闭事件
        reply = QMessageBox.question(self,
                                     '提示',
                                     "是否要退出程序？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def signal_pbt(self):
        self.ui.lineEdit.textChanged.connect(self.slot_enable)
        self.ui.pushButton.clicked.connect(self.slot_get_page)
        self.ui.comboBox.currentTextChanged.connect(self.slot_get_text)
        self.ui.pushButton_2.clicked.connect(self.slot_open_dir)

    def slot_get_page(self):
        if not config.pages.isdigit():
            QMessageBox.about(self, "温馨提示：", "你输入的不是整数,\n请输入整数后重试!!!")
        elif int(config.pages) > 60:
            QMessageBox.about(self, "温馨提示：", "你输入的页数不能超过60,\n请重新输入!!!")
        else:
            self.ui.textBrowser.append('程序正在运行，请稍等......')
            config.start_time = time.time()  # 程序运行计时
            QApplication.processEvents()  # 实时刷新日志
            config.comboBox_currentText = self.ui.comboBox.currentText()
            douyu.Douyu().run()

    def slot_enable(self):
        config.pages = self.ui.lineEdit.text()
        if config.pages == "":
            self.ui.pushButton.setEnabled(False)
        else:
            self.ui.pushButton.setEnabled(True)

    def slot_get_text(self):
        self.ui.textBrowser.append(f"你切换了用户代理:\n{self.ui.comboBox.currentText()}")

    @staticmethod
    def slot_open_dir():
        os.startfile(Path.cwd().joinpath('douyu_file'))

    # def get_hyper_link(self, url):
    #     # 字体、颜色和大小都可以自定义
    #     # style = "color:#ffb61e;font-size:20px;font-family:Microsoft YaHei"
    #     return f'<a href="{url}" ><b>{url}</b></a>'
    #     self.ui.textBrowser.setOpenExternalLinks(True)


class CLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login_window.Ui_Form()
        self.ui.setupUi(self)
        self.set_ui()

    def set_ui(self):
        self.ui.lineEdit.setPlaceholderText('请输入账号')
        self.ui.lineEdit_2.setPlaceholderText('请输入密码')
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)
        completer = QCompleter(["admin"], self.ui.lineEdit)  # 创建填充器
        self.ui.lineEdit.setCompleter(completer)  # 给 le 设置填充器
        self.signal_login()

    def signal_login(self):
        self.ui.pushButton.clicked.connect(self.slot_login)

    def slot_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        dict_user = {'admin': '284611', 'aaaa': 'zsx123456'}
        if username != '':
            if username in dict_user:
                if password == '':
                    QMessageBox.warning(self, '提示', '请输入密码')
                elif password == dict_user[f'{username}']:
                    QMessageBox.about(self, '提示', '登陆成功...')
                    self.close()
                    main_window.show()
                else:
                    QMessageBox.warning(self, '提示', '密码错误')
            else:
                QMessageBox.warning(self, '提示', '用户名不存在')
        else:
            QMessageBox.warning(self, '登陆失败', '请输入账号')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    login_window = CLoginWindow()
    main_window = CMainWindow()
    login_window.show()
    sys.exit(app.exec_())
