import streamlit as st
import pandas as pd
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="DevOps Enterprise System", layout="wide")

# الهيدر
st.title("🏢 نظام إدارة الموارد الذكي (Live Demo)")
st.markdown("---")

# القائمة الجانبية (Sidebar)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/9438/9438069.png", width=100)
st.sidebar.title("إعدادات النظام")
status = st.sidebar.radio("حالة السيرفر:", ["تشغيل (Online)", "صيانة (Maintenance)"])

# الجزء الأول: بطاقات إحصائية (Metrics)
col1, col2, col3 = st.columns(3)
col1.metric("عدد المستخدمين", "1,250", "+12%")
col2.metric("كفاءة النظام", "98.5%", "0.5%")
col3.metric("الطلبات النشطة", "432", "-5%")

st.markdown("---")

# الجزء الثاني: رسم بياني تفاعلي
st.subheader("📈 تحليل أداء العمليات (Real-time)")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['الإنتاج', 'المبيعات', 'الأرباح']
)
st.line_chart(chart_data)

# الجزء الثالث: إضافة بيانات يدوية (الشيء الملموس)
st.subheader("✍️ تسجيل دخول موظف جديد")
with st.form("employee_form"):
    name = st.text_input("اسم الموظف:")
    dept = st.selectbox("القسم:", ["IT", "HR", "DevOps", "Finance"])
    date = st.date_input("تاريخ البدء:")
    submit = st.form_submit_button("إضافة للملحقات")
    
    if submit:
        st.success(f"تم تسجيل {name} في قسم {dept} بنجاح عبر الـ Pipeline!")

# تذييل الصفحة
st.info(f"حالة النظام الحالية: {status} | تم النشر بواسطة GitHub Actions")