import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('all_bus_details.csv')
    return df

df = load_data()

# Title
st.title("Bus Services Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

# State filter
states = df['State'].unique()
selected_state = st.sidebar.selectbox("Select State", states)

# Route filter (dynamic)
routes = df[df['State'] == selected_state]['Route Name'].unique()
selected_route = st.sidebar.selectbox("Select Route", routes)

# Filter data based on selections
filtered_data = df[(df['State'] == selected_state) & (df['Route Name'] == selected_route)]

# Total number of buses available for the selected route
total_buses = len(filtered_data)
st.subheader(f"Total number of buses available for the selected route: {total_buses}")

# Sorting button
sort_by = st.selectbox("Sort by", ["Price", "Rating"])

if sort_by == "Price":
    filtered_data = filtered_data.sort_values(by='Price', ascending=True)
elif sort_by == "Rating":
    filtered_data = filtered_data.sort_values(by='Rating', ascending=False)

# Table of bus details
st.subheader("Bus Details")
st.write(filtered_data)
