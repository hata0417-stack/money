import streamlit as st

# 1. 頁面基本設定 (模擬手機 App 的窄版佈局)
st.set_page_config(
    page_title="Watchlist Mobile",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 自定義 CSS：還原截圖中的深色背景、霓虹邊框與卡片設計
st.markdown("""
    <style>
    /* 全域背景顏色 */
    .stApp {
        background-color: #0f1117;
        color: white;
    }
    /* 卡片通用樣式 */
    .card {
        background-color: #1e212b;
        padding: 18px;
        border-radius: 15px;
        margin-bottom: 12px;
        border: 1px solid #333;
    }
    /* 標籤樣式 */
    .badge {
        font-size: 0.75em;
        padding: 2px 8px;
        border-radius: 5px;
        font-weight: bold;
    }
    .trigger-on {
        color: #00ff88;
        border: 1px solid #00ff88;
        background-color: rgba(0, 255, 136, 0.1);
    }
    /* 漲跌幅文字 */
    .up-text { color: #00ff88; }
    .down-text { color: #ff4b4b; }
    </style>
""", unsafe_allow_html=True)

# 3. 頂部股票資訊 (以 8028 昇陽半導體為例)
st.markdown("<h2 style='color: #ff4b4b; margin-bottom: 0;'>8028</h2>", unsafe_allow_html=True)
st.caption("昇陽半導體")

col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("<h1 style='font-size: 3.5rem; margin: 0;'>232.0</h1>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='text-align: right; margin-top: 15px;'>", unsafe_allow_html=True)
    st.markdown("<span class='up-text' style='font-size: 1.5rem;'>▲ 2.7%</span>", unsafe_allow_html=True)
    st.markdown("<br><span style='background-color: #ff4b4b; color: white; padding: 2px 10px; border-radius: 12px; font-size: 0.8rem;'>三層全中</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.write("") # 間隔

# 4. 籌碼面卡片
st.markdown('''
<div class="card" style="border-left: 5px solid #00ff88;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="color: #00ff88; font-weight: bold;">籌碼</span>
        <span class="badge trigger-on">✓ 觸發</span>
    </div>
    <p style="font-size: 0.9rem; color: #b0b0b0; margin-top: 10px;">
        外資 +1,240張 / 投信 +180張<br>
        <span style="color: #666;">(法說日大買超)</span>
    </p>
</div>
''', unsafe_allow_html=True)

# 5. 技術面卡片
st.markdown('''
<div class="card" style="border-left: 5px solid #f9d71c;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="color: #f9d71c; font-weight: bold;">技術</span>
        <span class="badge trigger-on" style="color: #f9d71c; border-color: #f9d71c; background-color: rgba(249, 215, 28, 0.1);">✓ 觸發</span>
    </div>
    <p style="font-size: 0.9rem; color: #b0b0b0; margin-top: 10px;">
        收盤 232.0 突破近期高點<br>
        量能持續放大中
    </p>
</div>
''', unsafe_allow_html=True)

# 6. 基本面卡片
st.markdown('''
<div class="card" style="border-left: 5px solid #5c8aff;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="color: #5c8aff; font-weight: bold;">基本面</span>
        <span class="badge trigger-on" style="color: #5c8aff; border-color: #5c8aff; background-color: rgba(92, 138, 255, 0.1);">✓ 觸發</span>
    </div>
    <p style="font-size: 0.9rem; color: #b0b0b0; margin-top: 10px;">
        4月營收 4.65億 年增 +31%<br>
        第1季度法說今日發布
    </p>
</div>
''', unsafe_allow_html=True)

# 7. 底部警語卡片
st.markdown('''
<div class="card" style="background-color: #3b1c1f; border: 1px solid #ff4b4b; text-align: center; padding: 10px;">
    <span style="color: #ff4b4b; font-size: 0.85rem; font-weight: bold;">⚡ 人工確認後決定進出場</span>
</div>
''', unsafe_allow_html=True)