import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/train.csv")

st.title("📊 Sales Analytics Dashboard")

# Show dataset
st.subheader("Dataset Preview")
st.write(data.head())

# Total sales
total_sales = data["Sales"].sum()
st.metric("Total Sales", f"${total_sales:,.2f}")

# Sales by Category
st.subheader("Sales by Category")
category_sales = data.groupby("Category")["Sales"].sum()
st.bar_chart(category_sales)

# Sales by Region
st.subheader("Sales by Region")
region_sales = data.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)

# Top Products
st.subheader("Top 10 Products by Sales")
top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
st.write(top_products)

# Sales Distribution
st.subheader("Sales Distribution")
fig, ax = plt.subplots()
data["Sales"].hist(ax=ax)
st.pyplot(fig)