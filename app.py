import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

# إعداد الصفحة
st.set_page_config(page_title="Global Data Center Ops", layout="wide", page_icon="☁️")

# دالة لجلب الطقس الحقيقي
def get_live_weather(city):
    try:
        # جلب البيانات من API عالمي مفتوح
        url = f"https://wttr.in/{city}?format=%t+%h+%w"
        response = requests.get(url)
        data = response.text.split()
        return {
            "temp": data[0],     # درجة الحرارة
            "humidity": data[1], # الرطوبة
            "wind": data[2]      # سرعة الرياح
        }
    except:
        return {"temp": "N/A", "humidity": "N/A", "wind": "N/A"}

st.title("☁️ Global Infrastructure Weather Monitor")
st.markdown("---")

# --- الصف الأول: بيانات حقيقية من مدن عالمية ---
st.subheader("🌐 حالة الطقس في مراكز البيانات الرئيسية")
col1, col2, col3 = st.columns(3)

cities = {"بغداد": "Baghdad", "دبي": "Dubai", "لندن": "London"}
cols = [col1, col2, col3]

for (name_ar, name_en), col in zip(cities.items(), cols):
    weather = get_live_weather(name_en)
    with col:
        st.metric(f"مركز بيانات {name_ar}", weather["temp"], f"الرطوبة: {weather['humidity']}")
        st.caption(f"الرياح: {weather['wind']}")

st.divider()

# --- الصف الثاني: التحليل التلقائي والـ Pipeline ---
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📈 حمل الشبكة المتوقع (بناءً على الظروف الجوية)")
    # رسم بياني متحرك بسيط
    chart_data = pd.DataFrame(np.random.randn(15, 1), columns=['Network Load'])
    st.line_chart(chart_data)

with right_col:
    st.subheader("🚨 الإجراءات التلقائية")
    temp_val = int(get_live_weather("Baghdad")["temp"].replace('°C', '').replace('+', ''))
    
    if temp_val > 35:
        st.error("⚠️ تحذير: حرارة عالية! تفعيل نظام التبريد الإضافي.")
    else:
        st.success("✅ الحرارة مستقرة: الأنظمة تعمل بكفاءة طبيعية.")

    st.info(f"آخر فحص آلي للـ Pipeline: {time.strftime('%H:%M:%S')}")