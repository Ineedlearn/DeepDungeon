import streamlit as st
import json
import os

# 确保 library 目录存在
if not os.path.exists("library"):
    os.makedirs("library")

st.title("⚒️ DeepDungeon 剧本创作工坊")

# --- 1. 获取剧本库列表 ---
all_files = [f for f in os.listdir("library") if f.endswith(".json")]
options = ["✨ 新建空白剧本"] + all_files
selected_file = st.sidebar.selectbox("选择要编辑或参考的剧本", options)

# --- 2. 加载选中的数据 ---
current_data = {"title": "", "setting": "", "opening": ""}
if selected_file != "✨ 新建空白剧本":
    with open(f"library/{selected_file}", "r", encoding="utf-8") as f:
        current_data = json.load(f)

# --- 3. 编辑界面 ---
title = st.text_input("剧本标题", value=current_data.get("title", ""))
setting = st.text_area("世界观设定", value=current_data.get("setting", ""), height=150)
opening = st.text_area("开场白描述", value=current_data.get("opening", ""), height=100)

if st.button("💾 保存到剧本库"):
    filename = f"library/{title.replace(' ', '_')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"title": title, "setting": setting, "opening": opening}, f, ensure_ascii=False, indent=4)
    st.success(f"剧本《{title}》已存入创意工坊！")