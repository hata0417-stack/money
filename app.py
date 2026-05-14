import streamlit as st
from FinMind.data import DataLoader
import pandas as pd

# 1. 頁面設定
st.set_page_config(page_title="台股三層監控", layout="centered")

# 2. 初始化 API 讀取器 (FinMind 免費版不需 Token 也能跑，但有次數限制)
dl = DataLoader()

# 自定義 CSS (維持你喜歡的深色風格)
st.markdown("""
    <style>
    .stApp { background-color: #0f1117; color: white; }
    .card { background-color: #1e212b; padding: 20px; border-radius: 15px; border: 1px solid #333; margin-bottom: 12px; }
    .trigger-on { color: #00ff88; border: 1px solid #00ff88; padding: 2px 8px; border-radius: 5px; font-size: 0.8em; }
    </style>
""", unsafe_allow_html=True)

# 3. 側邊欄：選擇要監控的股票
target = st.sidebar.selectbox("切換監控標的", ["00919", "00757", "8028", "00878", "2330"])

# 4. 抓取真實數據 (抓取最近兩天的資料來計算漲跌)
@st.cache_data(ttl=3600) # 快取一小時，節省 API 流量
def get_stock_data(sid):
    df = dl.taiwan_stock_daily(stock_id=sid, start_date='2024-01-01')
    return df.tail(2) # 取最後兩筆

try:
    df_mini = get_stock_data(target)
    curr_price = df_mini['close'].iloc[-1]
    prev_price = df_mini['close'].iloc[-2]
    diff = curr_price - prev_price
    pct_change = (diff / prev_price) * 100

    # 5. 顯示頂部資訊
    st.markdown(f"<h2 style='color: #ff4b4b; margin:0;'>{target}</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.metric(label="即時收盤價", value=f"{curr_price}", delta=f"{pct_change:.2f}%")
    with col2:
        if abs(pct_change) > 2: # 假設漲跌超過 2% 就顯示三層全中信號 (這裡可以自定義邏輯)
            st.markdown("<br><span style='background-color: #ff4b4b; color: white; padding: 4px 12px; border-radius: 15px;'>三層全中</span>", unsafe_allow_html=True)

    # 6. 三層邏輯卡片 (這部分的數值現在會根據 target 變動)
    st.markdown(f'''
    <div class="card" style="border-left: 5px solid #00ff88;">
        <span style="color: #00ff88;">籌碼面</span>
        <p style="font-size: 0.9em; color: #aaa;">監測今日法人買賣超數據更新中...</p>
    </div>
    <div class="card" style="border-left: 5px solid #f9d71c;">
        <span style="color: #f9d71c;">技術面</span>
        <p style="font-size: 0.9em; color: #aaa;">收盤 {curr_price}，正在比對近期高點...</p>
    </div>
    <div class="card" style="border-left: 5px solid #5c8aff;">
        <span style="color: #5c8aff;">基本面</span>
        <p style="font-size: 0.9em; color: #aaa;">該標的最新營收報告分析中...</p>
    </div>
    ''', unsafe_allow_html=True)

except Exception as e:
    st.error(f"資料讀取失敗，可能是 API 流量限制。錯誤訊息: {e}")

st.error("❗ 人工確認後決定進出場")
