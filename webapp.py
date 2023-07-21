import replicate
import os
import streamlit as st
from PIL import Image
from config import openjourney, kandinsky, stable_diffusion_high_resolution, REPLICATE_API_TOKEN

st.title("Midjourney v4")
#REPLICATE_API_TOKEN申请地址：https://replicate.com/account/api-tokens
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

width = st.selectbox("宽", ("128", "256", "384", "448", "512", "576", "640", "704", "768", "832", "896", "960", "1024"))
height = st.selectbox("高", ("128", "256", "384", "448", "512", "576", "640", "704", "768", "832", "896", "960", "1024"))
scale = st.number_input("规模")
steps = st.number_input("迭代步数",step=1)
st.warning('由于内存限制，最大尺寸为 1024x768 或 768x1024', icon="⚠️")

title = st.chat_input('请输入你的提示')
if title:
    st.write(f"用户已发送以下提示:{title}")

with st.sidebar:
    model = st.selectbox("模型", (openjourney, kandinsky, stable_diffusion_high_resolution))


def huihua():
    if title:  # Execute the function only if the user has provided a prompt
        output = replicate.run(
            model_version=model,
            input={"prompt": title, "width": int(width), "height": int(height),"scale":scale,"steps":steps})
        
        for item in output:
            st.write('你的图片是：', item)
            image = item

            with st.container():
                st.image(image, caption=title)


huihua()
