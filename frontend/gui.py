import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog

class TimerApp(QWidget):
    def __init__(self, start_callback, stop_callback):
        """
        传入回调函数，前端不直接处理计时逻辑，而是调用后端函数
        :param start_callback: 计时开始的回调
        :param stop_callback: 计时结束的回调
        """
        super().__init__()
        self.start_callback = start_callback
        self.stop_callback = stop_callback

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("计时未开始", self)
        layout.addWidget(self.label)

        self.start_btn = QPushButton("开始计时", self)
        self.start_btn.clicked.connect(self.start_timer)
        layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("结束计时", self)
        self.stop_btn.clicked.connect(self.stop_timer)
        layout.addWidget(self.stop_btn)

        self.setLayout(layout)

    def start_timer(self):
        """调用外部 start_callback 来开始计时"""
        self.start_callback()
        self.label.setText("计时中...")

    def stop_timer(self):
        """调用外部 stop_callback 来结束计时，并弹出输入框"""
        elapsed_time = self.stop_callback()
        if elapsed_time:
            task, ok1 = QInputDialog.getText(self, "记录工作内容", "请输入你刚才的工作内容：")
            if ok1:
                category, ok2 = QInputDialog.getText(self, "分类", "请输入分类标签（如：编程、学习）：")
                if ok2:
                    return elapsed_time, task, category
        return None
