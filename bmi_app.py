import streamlit as st

st.set_page_config(page_title="BMI计算器", page_icon="⚖️")
st.title("⚖️ 你的专属BMI计算器")
st.markdown("输入身高体重，立刻得到结果。**数据不会保存**，请放心使用。")

name = st.text_input("你的名字（选填）")
height = st.number_input("身高（米）", min_value=0.5, max_value=2.5, step=0.01, format="%.2f")
weight = st.number_input("体重（千克）", min_value=10.0, max_value=200.0, step=0.1, format="%.1f")

if st.button("🚀 计算我的BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            advice = "体重过轻，注意营养"
            color = "blue"
        elif bmi < 24:
            advice = "正常范围，保持健康"
            color = "green"
        elif bmi < 28:
            advice = "超重，适当运动"
            color = "orange"
        else:
            advice = "肥胖，建议咨询医生"
            color = "red"
        
        if name:
            st.success(f"{name}，你的BMI是 **{bmi:.2f}**")
        else:
            st.success(f"你的BMI是 **{bmi:.2f}**")
        st.markdown(f"<span style='color:{color}; font-size:20px;'>{advice}</span>", unsafe_allow_html=True)
    else:
        st.error("身高体重必须大于0")