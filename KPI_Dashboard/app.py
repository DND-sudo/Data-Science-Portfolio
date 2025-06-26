import streamlit as st
import pandas as pd
import plotly.express as px
from utils import compute_kpis, filter_data

st.set_page_config(page_title="KPI Dashboard", layout="wide")

st.sidebar.title("Upload & Filter Data")
uploaded_file = st.sidebar.file_uploader("Upload your CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    categories = df['Category'].unique()
    
    with st.sidebar:
        selected_categories = st.multiselect("Select Category", categories, default=list(categories))
        date_range = st.date_input("Select Date Range", [df['Date'].min(), df['Date'].max()])
    
    filtered_df = filter_data(df, selected_categories, date_range)

    st.title("📊 Business KPI Dashboard")
    kpis = compute_kpis(filtered_df)

    st.metric("Total Revenue", f"${kpis['revenue']:,.2f}")
    st.metric("Total Sales", int(kpis["sales_count"]))
    st.metric("Avg Order Value", f"${kpis['avg_order_value']:,.2f}")

    st.plotly_chart(px.line(filtered_df, x='Date', y='Revenue', title="Monthly Revenue"))
    st.plotly_chart(px.pie(filtered_df, names='Category', values='Revenue', title="Revenue by Category"))
else:
    st.info("Please upload a CSV to begin.")

