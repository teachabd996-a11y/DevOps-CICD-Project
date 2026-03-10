import streamlit as st

st.set_page_config(page_title="DevOps Live Demo", page_icon="🚀")

st.title("🚀 DevOps CI/CD Live Dashboard")
st.write("هذا الموقع تم نشره تلقائياً باستخدام Pipeline احترافي!")

# إضافة تفاعل
name = st.text_input("ما هو اسمك؟")
if name:
    st.success(f"أهلاً بك يا {name}! أنت الآن تشاهد قوة الأتمتة.")

st.sidebar.header("System Status")
st.sidebar.info("Pipeline Status: ✅ Healthy")
st.sidebar.info("Environment: Production (Cloud)")

# إضافة آلة حاسبة بسيطة كمثال ملموس
st.subheader("Calculator Service")
num1 = st.number_input("الرقم الأول", value=0)
num2 = st.number_input("الرقم الثاني", value=0)
if st.button("احسب المجموع"):
    st.write(f"النتيجة هي: {num1 + num2}")