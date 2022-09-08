import streamlit as st 
import pandas as pd 
import numpy as np
import seaborn as sns 

st.title("Marketing KPI - Key Metric Dashboard")

st.subheader ("using Python")

kpi1, kpi2, kpi3 = st.columns(3)

my_dynamic_value =333.33

kpi1.metric(label = "$Avg Time Spent",
            value = 3.5,
            delta = -1.4)

kpi2.metric(label = "$Bounce Rate",
            value = 78,
            delta = -5,
            delta_color = 'inverse')

kpi3.metric(label = "$CLOUD",
            value = "%.2f" %my_dynamic_value)


st.markdown ("### Important Charts")

chart1, chart2 = st.columns(2)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

chart1.bar_chart(chart_data)
chart2.line_chart(chart_data)

st.dataframe(chart_data)
