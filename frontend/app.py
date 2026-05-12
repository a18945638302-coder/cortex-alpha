import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="CortexAlpha", page_icon="🧠", layout="wide")
st.title("🧠 CortexAlpha · 外置前额叶")

page = st.sidebar.radio("功能模块", ["今日复盘", "历史日记"])

if page == "今日复盘":
    st.subheader("写下今天的交易与心理状态")
    style = st.selectbox("导师模式", ["buffett", "livermore", "quant"],
                         format_func=lambda x: {"buffett":"🧓 巴菲特","livermore":"⚡ 利弗莫尔","quant":"🤖 量化冷血"}[x])
    mood = st.selectbox("情绪标签", ["", "极度FOMO", "恐慌清仓", "理性分析", "赌徒心态", "严格按计划"])
    ticker = st.text_input("关联代码（如 TSLA）")
    content = st.text_area("今日感悟", height=200, placeholder="像发朋友圈一样写下今天的操作与心理...")

    if st.button("获取 AI 点评", type="primary"):
        if content:
            with st.spinner("导师思考中..."):
                try:
                    res = requests.post(f"{BACKEND_URL}/feedback", json={
                        "content": content, "style": style,
                        "mood": mood or None, "ticker": ticker or None
                    })
                    data = res.json()
                    st.success("点评完成")
                    st.info(data["feedback"])
                except Exception as e:
                    st.error(f"连接后端失败：{e}")
        else:
            st.warning("请先写下今日感悟")

elif page == "历史日记":
    st.subheader("历史记录")
    try:
        res = requests.get(f"{BACKEND_URL}/journals")
        journals = res.json().get("journals", [])
        if journals:
            for j in journals:
                with st.expander(f"{j['created_at'][:10]} · {j.get('ticker','') or '无代码'} · {j.get('mood','') or '无情绪标签'}"):
                    st.write(j["content"])
                    if j.get("feedback"):
                        st.info(f"**AI点评：** {j['feedback']}")
        else:
            st.info("还没有日记，去写第一篇吧！")
    except Exception as e:
        st.error(f"加载失败：{e}")
