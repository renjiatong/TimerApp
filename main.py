import sys
from PyQt6.QtWidgets import QApplication
from backend.timer import Timer
from backend.storage import Storage
from frontend.gui import TimerApp

class MainController:
    """管理前后端的交互"""
    def __init__(self):
        self.timer = Timer()
        self.storage = Storage()

    def start_timer(self):
        """开始计时"""
        self.timer.start()

    def stop_timer(self):
        """结束计时，返回已用时间"""
        elapsed_time = self.timer.stop()
        return elapsed_time  # 让 GUI 获取时间并询问用户

    def save_record(self, elapsed_time, task, category):
        """存储记录"""
        self.storage.save_record(elapsed_time, task, category)

def main():
    app = QApplication(sys.argv)
    controller = MainController()

    # 创建 GUI 实例，传递回调函数
    window = TimerApp(controller.start_timer, controller.stop_timer)

    # 连接 GUI 的 stop_timer 返回值到 save_record
    window.stop_btn.clicked.connect(lambda: (
        lambda data: controller.save_record(*data) if data else None
    )(window.stop_timer()))

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
