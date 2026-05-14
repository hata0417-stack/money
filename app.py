import streamlit as st

# 1. 頁面基本設定
st.set_page_config(page_title="三步前佈局監控", layout="centered")

# 2. 自定義深色風格與進度條顏色
st.markdown("""
    <style>
    .stApp { background-color: #0f1117; color: white; }
    .card {
        background-color: #1e212b;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
        margin-bottom: 15px;
    }
    .step-label { font-size: 0.85em; color: #888; margin-bottom: 5px; }
    .quote { font-style: italic; color: #f9d71c; border-left: 3px solid #f9d71c; padding-left: 10px; margin: 15px 0; }
    /* 自定義進度條顏色 */
    .stProgress > div > div > div > div { background-color: #00d4ff; }
    </style>
""", unsafe_allow_html=True)

# 3. 核心佈局邏輯：定義三步階段
# 這裡以你提到的均豪 (5443) 為範例樣本
target_stock = "5443 均豪"
current_step = 2  # 模擬目前處於第二步：等待驗證
step_titles = {
    1: "第一步：訊息萌芽 (研究期)",
    2: "第二步：認知擴散 (等待期)",
    3: "第三步：資金湧入 (佈局期)"
}

# 4. 頂部標題與金句
st.markdown(f"<h2 style='color: #ff4b4b; margin-bottom:0;'>{target_stock}</h2>", unsafe_allow_html=True)
st.markdown(f"<div class='quote'>「別人研究我等待，別人等待我已佈局」</div>", unsafe_allow_html=True)

# 5. 三步前進度視覺化
st.write(f"**目前階段：{step_titles[current_step]}**")
progress_val = (current_step / 3)
st.progress(progress_val)

col1, col2, col3 = st.columns(3)
col1.caption("1. 訊息蒐集" if current_step > 1 else "👉 研究中")
col2.caption("2. 認知驗證" if current_step > 2 else ("👉 等待中" if current_step == 2 else "2. 等待期"))
col3.caption("3. 資金動能" if current_step == 3 else "3. 佈局期")

st.divider()

# 6. 實戰監控細節 (結合你對 5443 的觀察)
st.markdown("### 🔍 關鍵驗證清單")

# 模擬三層全中的邏輯判斷
st.markdown(f'''
<div class="card" style="border-left: 5px solid #00d4ff;">
    <div style="display: flex; justify-content: space-between;">
        <span style="color: #00d4ff; font-weight: bold;">戰略目標：FOPLP 核心設備</span>
        <span style="background-color: #333; padding: 2px 8px; border-radius: 5px; font-size: 0.8em;">核心邏輯</span>
    </div>
    <p style="font-size: 0.9em; color: #ccc; margin-top: 10px;">
        目前狀態：訊息已出，認知正從少數人擴散至市場。<br>
        <span style="color: #f9d71c; font-weight: bold;">💡 關鍵動作：等待 3D NIR 通過驗證的那一天。</span>
    </p>
</div>
''', unsafe_allow_html=True)

# 模擬即時行情數據
col_p, col_c = st.columns(2)
col_p.metric("預估入場價", "等待訊號", "-")
col_c.metric("目前市場熱度", "中等", "認知擴散中")

# 7. 底部警語與心法
st.warning("⚠️ 三步前核心：不買訊息，買「驗證後的認知」")
st.error("❗ 人工確認後決定進出場")
