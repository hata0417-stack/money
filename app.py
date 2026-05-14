import streamlit as st

# --- 新增：三步前佈局狀態判斷 ---
def get_layout_stage(stock_id):
    # 這裡可以根據你的研究進度手動設定，或透過邏輯判斷
    # 範例：均豪 (5443) 目前處於「等待驗證」階段
    stages = {
        "5443": {"stage": 2, "desc": "等待 3D NIR 驗證訊號", "logic": "訊息已出，認知擴散中"},
        "8028": {"stage": 3, "desc": "資金湧入，三層全中", "logic": "邏輯兌現，執行佈局"},
        "00919": {"stage": 1, "desc": "研究配息穩定性", "logic": "穩定領息，低位研究"}
    }
    return stages.get(stock_id, {"stage": 1, "desc": "初步研究中", "logic": "訊息蒐集階段"})

# --- 介面呈現 ---
target_stock = "5443" # 假設現在看均豪
info = get_layout_stage(target_stock)

st.markdown(f"### 🚀 三步前佈局進度：第 {info['stage']} 步")

# 建立進度條
progress_map = {1: 33, 2: 66, 3: 100}
st.progress(progress_map[info['stage']])

# 顯示你的核心金句
st.info(f"**目前邏輯：** {info['logic']} \n\n **行動指南：** {info['desc']}")

# --- 強化版卡片設計 ---
st.markdown(f'''
<div class="card" style="border-left: 5px solid #00d4ff;">
    <div style="display: flex; justify-content: space-between;">
        <span style="color: #00d4ff; font-weight: bold;">核心觀點 (三步前)</span>
    </div>
    <p style="font-size: 0.9em; color: #eee; margin-top: 10px;">
        「別人研究我等待，別人等待我已佈局」<br>
        <span style="color: #888;">這不是追高，而是領先認知的兌現。</span>
    </p>
</div>
''', unsafe_allow_html=True)
