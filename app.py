import streamlit as st
from FinMind.data import DataLoader
import pandas as pd

# 1. 頁面基本設定
st.set_page_config(page_title="台股監控 App", layout="centered")

# 自定義 CSS (保持深色質感)
st.markdown("""
    <style>
    .stApp { background-color: #0f1117; color: white; }
    .card { background-color: #1e212b; padding: 20px; border-radius: 15px; border: 1px solid #333; margin-bottom: 12px; }
    </style>
""", unsafe_allow_html=True)

# 2. 修改資料抓取邏輯：不要把 DataLoader 放進 Cache，只 Cache 輸出的結果
@st.cache_data(ttl=600) # 快取 10 分鐘就好，避免過期太久
def get_realtime_data(sid):
    # 每次執行時才建立 DataLoader 實例，避免弱引用錯誤
    dl = DataLoader()
    # 抓取最新資料 (改抓近一個月確保一定有兩筆資料可計算漲跌)
    df = dl.taiwan_stock_daily(stock_id=sid, start_date='2024-04-01')
    return df.tail(2)

# 3. 側邊欄選單
target = st.sidebar.selectbox("切換標的", ["00919", "00757", "8028", "00878", "2330"])

# 4. 主畫面顯示
try:
    df_mini = get_realtime_data(target)
    
    if not df_mini.empty and len(df_mini) >= 2:
        curr_price = df_mini['close'].iloc[-1]
        prev_price = df_mini['close'].iloc[-2]
        pct_change = ((curr_price - prev_price) / prev_price) * 100

        st.markdown(f"<h2 style='color: #ff4b4b; margin:0;'>{target}</h2>", unsafe_allow_html=True)
        st.metric(label="最新股價", value=f"{curr_price}", delta=f"{pct_change:.2f}%")

        # 這裡可以加入你原本的「三層全中」卡片內容...
        st.markdown(f'''
        <div class="card" style="border-left: 5px solid #00ff88;">
            <span style="color: #00ff88; font-weight: bold;">數據狀態</span>
            <p style="font-size: 0.9em; color: #aaa; margin-top: 10px;">
                目前選定：{target}<br>
                資料時間：{df_mini['date'].iloc[-1]}
            </p>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.warning("暫時抓不到足夠的歷史資料，請稍後再試。")

except Exception as e:
    st.error(f"連線異常：{e}")

st.info("💡 貼心提醒：FinMind 免費版 API 有每日限制，若頻繁刷新網頁可能會暫時失效。")
