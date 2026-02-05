import json
import os

class SaveManager:
    def __init__(self, save_path="saves/slot1.json"):
        self.save_path = save_path
        if not os.path.exists("saves"):
            os.makedirs("saves")

    def save_game(self, data):
        with open(self.save_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("--- 进度已保存至位面碎片 (存档成功) ---")

    def load_game(self):
        if os.path.exists(self.save_path):
            with open(self.save_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None