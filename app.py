import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# إعداد الصفحة
st.set_page_config(page_title="Live DevOps Operations", layout="wide")

# تصميم CSS لجعل الواجهة تبدو احترافية
st.markdown("""
    <style>
    .stMetric { border: 1px solid #e6e9ef; padding: 10px; border-radius: 5px; background: #fafafa; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 SkyNet Live Operations Dashboard")
st.caption("بيانات حية يتم تحديثها تلقائياً من نظام الـ DevOps")

# --- الجزء الأول: الإشعارات اللحظية (Notifications) ---
placeholder_alert = st.empty() # مكان مخصص للإشعارات المتغيرة

# --- الجزء الثاني: المؤشرات الرقمية (The Metrics) ---
col1, col2, col3, col4 = st.columns(4)

# --- الجزء الثالث: الرسم البياني المتحرك ---
st.subheader("📈 تدفق البيانات المباشر (Network Traffic)")
chart_placeholder = st.empty()

# محاكاة "قاعدة بيانات" للرسم البياني
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(np.random.randn(20, 1), columns=['Traffic'])

# --- حلقة التحديث المستمر (The Live Loop) ---
# هذه الحلقة تجعل الموقع يتحدث تلقائياً كل ثانيتين
for i in range(100): # سيتحدث 100 مرة (يمكنك زيادتها)
    
    # 1. تحديث الأرقام العشوائية (المؤشرات)
    users = 1500 + random.randint(-50, 50)
    cpu_load = random.uniform(30.0, 75.0)
    requests = random.randint(200, 800)
    
    with col1:
        st.metric("المستخدمين الآن", f"{users}", f"{random.randint(-5, 5)}%")
    with col2:
        st.metric("تحميل المعالج (CPU)", f"{cpu_load:.1f}%", f"{random.uniform(-1, 1):.1f}%")
    with col3:
        st.metric("الطلبات/ثانية", f"{requests}", f"{random.randint(-20, 20)}")
    with col4:
        st.metric("حالة الـ Pipeline", "✅ Stable", "Normal")

    # 2. تحديث الرسم البياني (البورصة)
    new_row = pd.DataFrame([[random.uniform(-1, 1) + st.session_state.data.iloc[-1]['Traffic']]], columns=['Traffic'])
    st.session_state.data = pd.concat([st.session_state.data, new_row]).tail(20) # نحتفظ بآخر 20 نقطة فقط
    chart_placeholder.line_chart(st.session_state.data)

    # 3. محاكاة "إشعارات دخول الموظفين"
    if random.random() > 0.8: # احتمالية 20% لظهور إشعار
        names = ["أحمد", "سارة", "علي", "فاطمة"]
        placeholder_alert.success(f"🔔 تم تسجيل دخول موظف جديد: {random.choice(names)}")
    else:
        placeholder_alert.empty()

    time.sleep(2) # انتظر ثانيتين قبل التحديث القادم
    st.rerun() # أعد تشغيل الكود لتحديث الواجهة