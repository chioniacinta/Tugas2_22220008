import streamlit as st
import pandas as pd
import numpy as np

st.title(":blue[Chionia Cinta Mbindi]")
st.write("22220008")

df_sales = pd.read_csv("./sales_data_sample.csv", encoding="iso-8859-1")

# Get unique product lines
product_lines = df_sales["PRODUCTLINE"].unique()

# Create a DataFrame with ORDERDATE as index and product lines as columns
df_productline_sales = df_sales.pivot_table(values='QUANTITYORDERED', index='ORDERDATE', columns='PRODUCTLINE', fill_value=0)

# Print the DataFrame

#
# Area Chart
#
st.title("Area Chart")
st.area_chart(df_productline_sales)
st.markdown("---")
st.title("Bar Chart")
st.bar_chart(df_productline_sales)
st.markdown("---")
st.title("Line Chart")
st.line_chart(df_productline_sales)
st.markdown("---")

# 