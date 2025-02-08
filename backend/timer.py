import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time:
            self.elapsed_time = round(time.time() - self.start_time, 2)
            self.start_time = None
            return self.elapsed_time
        return 0
