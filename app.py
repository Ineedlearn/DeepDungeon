import os
import json
import random
from save_manager import SaveManager

class DeepDungeonEngine:
    def __init__(self):
        self.sm = SaveManager()
        self.player_state = self.sm.load_game() or {"hp": 20, "inventory": [], "history": []}
        self.current_story = None

    def load_scenario(self):
        """从创意工坊（library 文件夹）加载剧本"""
        lib_path = "library"
        files = [f for f in os.listdir(lib_path) if f.endswith(".json")]
        
        print("\n=== 📚 欢迎来到创意工坊剧本库 ===")
        for i, f in enumerate(files):
            print(f"[{i}] {f.replace('.json', '')}")
        
        choice = input("\n请选择要开启的冒险编号 > ")
        if choice.isdigit() and int(choice) < len(files):
            with open(os.path.join(lib_path, files[int(choice)]), "r", encoding="utf-8") as f:
                self.current_story = json.load(f)
                print(f"\n✨ 成功加载剧本：《{self.current_story['title']}》")
        else:
            print("❌ 无效选择，载入默认测试剧本。")
            self.current_story = {"opening": "你在黑暗中醒来...", "setting": "基础教学设定"}

    def play(self):
        """核心游玩逻辑"""
        print(f"\n【背景设定】：{self.current_story.get('setting')}")
        print(f"\n【地下城主】：{self.current_story.get('opening')}")
        
        while self.player_state["hp"] > 0:
            action = input("\n你的行动 (输入 'save' 存档，'exit' 退出) > ")
            
            if action == "save":
                self.sm.save_game(self.player_state)
                continue
            if action == "exit": break

            # 模拟 D20 判定
            roll = random.randint(1, 20)
            if roll >= 12:
                print(f"🎲 判定成功 (投骰: {roll})！你的行动奏效了。")
            else:
                self.player_state["hp"] -= 2
                print(f"🎲 判定失败 (投骰: {roll})！你受到了挫折，生命值 -2 (剩余: {self.player_state['hp']})")

if __name__ == "__main__":
    engine = DeepDungeonEngine()
    engine.load_scenario()
    engine.play()