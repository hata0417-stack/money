import streamlit as st

# 1. 頁面配置：模擬手機 App 窄版顯示
st.set_page_config(page_title="三步前佈局系統", layout="centered")

# 2. 核心 CSS 樣式：強調「時間差」與「層次感」
st.markdown("""
    <style>
    .stApp { background-color: #0f1117; color: white; }
    .status-card {
        background: linear-gradient(145deg, #1e212b, #151821);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #333;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .phase-badge {
        padding: 4px 12px;
        border-radius: 10px;
        font-size: 0.85em;
        font-weight: bold;
        text-transform: uppercase;
    }
    .phase-1 { background-color: #3b3b3b; color: #aaa; border: 1px solid #555; }
    .phase-2 { background-color: #1c3b2d; color: #00ff88; border: 1px solid #00ff88; }
    .phase-3 { background-color: #3b1c1c; color: #ff4b4b; border: 1px solid #ff4b4b; }
    </style>
""", unsafe_allow_html=True)

# 3. 三步前模型核心邏輯定義
# 你可以根據觀察隨時調整這些標的的階段
STOCK_DB = {
    "5443 均豪": {
        "step": 2,
        "msg": "FOPLP 核心設備商",
        "verify": "等待 3D NIR 驗證通過",
        "logic": "別人研究我等待，現在是驗證認知的關鍵點",
        "trend": "認知擴散中"
    },
    "00919 群益台灣精選高息": {
        "step": 1,
        "msg": "累積 20 張長期計畫",
        "verify": "觀察配息穩定度與填息能力",
        "logic": "別人恐慌我研究，領先佈局複利起點",
        "trend": "穩定領息"
    },
    "8028 昇陽半導體": {
        "step": 3,
        "msg": "晶圓薄化規格提升",
        "verify": "營收兌現，資金持續湧入",
        "logic": "別人追高我收割，三層全中邏輯兌現",
        "trend": "佈局完成"
    }
}

# 4. 側邊欄：選擇標的
st.sidebar.title("💎 投資管理")
selected_name = st.sidebar.selectbox("選擇監控標的", list(STOCK_DB.keys()))
data = STOCK_DB[selected_name]

# 5. 主介面顯示
st.markdown(f"<h1 style='margin-bottom:0;'>{selected_name}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='color:#888;'>關鍵訊息：{data['msg']}</p>", unsafe_allow_html=True)

# 顯示「三步前」進度視覺化
st.divider()
step = data['step']
cols = st.columns(3)

# 視覺化三個階段的狀態
for i, col in enumerate(cols, 1):
    status = "✅ 已完成" if i < step else ("🔥 進行中" if i == step else "⏳ 待啟動")
    color = "#00ff88" if i == step else ("#555" if i > step else "#aaa")
    col.markdown(f"<div style='text-align:center; color:{color}; font-weight:bold;'>第 {i} 步</div>", unsafe_allow_html=True)
    col.caption(status)

st.progress(step / 3)

# 6. 詳細邏輯卡片
phase_class = f"phase-{step}"
st.markdown(f'''
<div class="status-card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="phase-badge {phase_class}">
            {"研究期" if step==1 else "等待期" if step==2 else "佈局期"}
        </span>
        <span style="color:#888; font-size:0.9em;">趨勢：{data['trend']}</span>
    </div>
    <div style="margin-top:20px;">
        <h4 style="color:#f9d71c; margin-bottom:5px;">核心邏輯</h4>
        <p style="color:#eee; line-height:1.6;">{data['logic']}</p>
    </div>
    <div style="margin-top:15px; padding-top:15px; border-top: 1px solid #333;">
        <h4 style="color:#00d4ff; margin-bottom:5px;">下一波驗證訊號</h4>
        <p style="color:#00d4ff; font-weight:bold; font-size:1.1em;">{data['verify']}</p>
    </div>
</div>
''', unsafe_allow_html=True)

# 7. 底部警語與心法
st.info("💡 三步前心法：不要買別人的出場成本，要買認知的時間差。")
st.error("❗ 本系統僅供邏輯追蹤，人工確認後方可進出場。")
