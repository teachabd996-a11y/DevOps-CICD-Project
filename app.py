import streamlit as st
import pandas as pd
import time

# إعدادات احترافية للصفحة
st.set_page_config(page_title="SkyNet DevOps Dashboard", page_icon="🌐", layout="wide")

# تصميم الهيدر مع خلفية لونية (CSS بسيط)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.title("🌐 SkyNet Solutions | Global Operations Center")
st.caption("نظام المراقبة والتحكم الموحد - مدعوم بتقنيات CI/CD")

# --- الصف الأول: مؤشرات حيوية ---
st.markdown("### 📊 حالة الأنظمة العالمية")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="خوادم السحاب", value="🟢 142", delta="Online")
with col2:
    st.metric(label="نسبة استجابة الموقع", value="99.98%", delta="0.02% ↑")
with col3:
    st.metric(label="العمليات المنفذة اليوم", value="45,201", delta="1,200")
with col4:
    st.metric(label="وقت النشر التلقائي", value="1.4 min", delta="تحسن ملحوظ", delta_color="normal")

st.divider()

# --- الصف الثاني: مراقبة الـ Pipeline والبيانات ---
left_column, right_column = st.columns([2, 1])

with left_column:
    st.subheader("🛠️ سجل الـ CI/CD Pipeline الأخير")
    # جدول بيانات واقعي
    df = pd.DataFrame({
        'المرحلة': ['Build', 'Unit Test', 'Security Scan', 'Deploy to Production'],
        'الحالة': ['✅ Successful', '✅ Passed', '✅ Secure', '⏳ Running...'],
        'الوقت المستغرق': ['45s', '120s', '90s', '30s']
    })
    st.table(df)
    
    # رسم بياني لحركة المرور (Traffic)
    st.subheader("📈 مراقبة تدفق البيانات (Real-time Traffic)")
    chart_data = pd.DataFrame(
        [10, 25, 40, 35, 50, 70, 85, 80, 95, 110, 105, 120],
        columns=['Users']
    )
    st.area_chart(chart_data)

with right_column:
    st.subheader("🚨 تنبيهات النظام")
    st.warning("تنبيه: تحديث أمني مطلوب لـ Database Node 4")
    st.error("خطأ: محاولة دخول غير مصرح بها من IP: 192.168.1.1 (تم الحظر)")
    st.success("تم الانتهاء من النسخ الاحتياطي اليومي بنجاح")
    
    # تفاعل ملموس للحضور
    st.subheader("⚙️ التحكم اليدوي")
    if st.button("تحديث قاعدة البيانات الآن"):
        with st.status("جاري التحديث...", expanded=True) as status:
            st.write("فحص الاتصال...")
            time.sleep(1)
            st.write("مزامنة البيانات...")
            time.sleep(1)
            status.update(label="✅ اكتمل التحديث بنجاح!", state="complete", expanded=False)

# تذييل الصفحة
st.markdown("---")
st.sidebar.write(f"Last Commit ID: {time.strftime('%H:%M:%S')}")