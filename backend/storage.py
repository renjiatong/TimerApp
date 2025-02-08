import json
import os

class Storage:
    def __init__(self, filename = "work_log.json"):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f)
                
    def save_record(self, time_spend, task, category):
        with open(self.filename, "r") as f:
            data = json.load(f)
        data.append({"time_spend": time_spend, "task": task, "category": category})
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)
            
    def load_records(self):
        with open(self.filename, "r") as f:
            return json.load(f)
        