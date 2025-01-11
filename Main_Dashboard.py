import streamlit as st
import pandas as pd
from Data_cleaning import clean_data  
from GUI import apply_theme


@st.cache_data
def get_cleaned_data():
    return clean_data()

selected_theme = apply_theme()


data = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Price": [100, 200, 300],
    "Discount": [10, 20, 30],
})

data = get_cleaned_data()
st.title("Flipcart Analysis")
st.header("Analyze and Explore Categories")

# Sidebar Filters
st.sidebar.header("Filters")

# Category filter
categories = data["Category"].unique()
selected_category = st.sidebar.selectbox("Select a Category", categories)

# Price range filter
filtered_data = data[data["Category"] == selected_category]
min_price, max_price = st.sidebar.slider(
    "Price Range",
    int(filtered_data["Price"].min()),
    int(filtered_data["Price"].max()),
    (int(filtered_data["Price"].min()), int(filtered_data["Price"].max())),
)

filtered_data = filtered_data[(filtered_data["Price"] >= min_price) & (filtered_data["Price"] <= max_price)]

# Discount range filter
min_discount, max_discount = st.sidebar.slider(
    "Discount Range (%)",
    int(filtered_data["Discount rates"].min()),
    int(filtered_data["Discount rates"].max()),
    (int(filtered_data["Discount rates"].min()), int(filtered_data["Discount rates"].max())),
)

filtered_data = filtered_data[
    (filtered_data["Discount rates"] >= min_discount) & (filtered_data["Discount rates"] <= max_discount)
]

# Main Content: Display Filtered Data and Visualizations
st.subheader(f"Data for Category: {selected_category}")
st.dataframe(filtered_data)

# Visualization Section
st.subheader("Visualizations")

# Bar Chart: Distribution of Discounts
st.write("### Distribution of Discounts")
discount_distribution = filtered_data["Discount rates"].value_counts().sort_index()
st.bar_chart(discount_distribution)

# Line Chart: Prices Over Products
st.write("### Prices Over Products")
st.line_chart(filtered_data[["Price", "Original Prices"]])

# Top 10 Products by Discount
st.write("### Top 10 Products by Discount")
top_products = filtered_data.sort_values(by="Discount rates", ascending=False).head(10)
st.table(top_products[["Product Name", "Price", "Original Prices", "Discount rates"]])

  