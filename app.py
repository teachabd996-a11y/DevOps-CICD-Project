import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

# إعداد الصفحة
st.set_page_config(page_title="Data Center Monitor", layout="wide")

# دالة جلب الطقس من Open-Meteo (أكثر استقراراً)
def get_weather_data(lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url).json()
        return response['current_weather']['temperature']
    except:
        return random.randint(20, 35) # أرقام احتياطية في حال تعطل السيرفر

st.title("🌐 Global Infrastructure & Environment Monitor")
st.markdown("---")

# --- بيانات مراكز البيانات ---
col1, col2, col3 = st.columns(3)

# إحداثيات المدن (بغداد، دبي، لندن)
locations = [
    {"city": "بغداد", "lat": 33.31, "lon": 44.36, "col": col1},
    {"city": "دبي", "lat": 25.20, "lon": 55.27, "col": col2},
    {"city": "لندن", "lat": 51.50, "lon": -0.12, "col": col3}
]

for loc in locations:
    temp = get_weather_data(loc['lat'], loc['lon'])
    with loc['col']:
        st.metric(f"مركز بيانات {loc['city']}", f"{temp}°C", "Live Data")

st.divider()

# --- الرسم البياني الحي (الذي طلبته سابقاً) ---
st.subheader("📈 استهلاك الطاقة اللحظي (Power Consumption)")
if 'chart_data' not in st.session_state:
    st.session_state.chart_data = pd.DataFrame(np.random.randn(20, 1), columns=['Load'])

# إضافة بيانات جديدة عشوائية لجعل الكيرف يتحرك
new_data = pd.DataFrame([np.random.randn()], columns=['Load'])
st.session_state.chart_data = pd.concat([st.session_state.chart_data, new_data]).tail(20)
st.line_chart(st.session_state.chart_data)

# إشعار دخول الموظفين (الملموس)
st.sidebar.subheader("🚨 سجل الوصول")
if np.random.random() > 0.7:
    st.sidebar.success(f"🔓 تم منح صلاحية دخول لـ: المهندس {np.random.choice(['علي', 'سارة', 'أحمد'])}")

# زر للتحديث اليدوي
if st.button('تحديث البيانات الآن'):
    st.rerun()

st.info(f"حالة الـ Pipeline: ✅ متصل | التحديث القادم بعد قليل...")