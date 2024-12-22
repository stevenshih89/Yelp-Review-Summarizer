import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_csv("restaurant_data.csv")
    return data

def display_summary(restaurant_data):
    st.subheader("Restaurant Summary")
    st.write(f"**Restaurant Name:** {restaurant_data['Restaurant Name']}")
    st.write(f"**Positive Reviews (%):** {restaurant_data['Positive Reviews (%)']}")
    st.write(f"**Negative Reviews (%):** {restaurant_data['Negative Reviews (%)']}")
    st.write(f"**Categories:** {restaurant_data['Categories']}")
    st.write(f"**Themes:** {restaurant_data['Themes']}")
    st.write(f"**Descriptions:** {restaurant_data['Descriptions']}")


def main():
    # Title
    st.title("Yelp Restaurant Review Summarizer")
    
    # Load data
    data = load_data()

    # Dropdown for restaurant selection
    restaurant_list = data['Restaurant Name'].unique()
    selected_restaurant = st.selectbox("Select a Restaurant", restaurant_list)

    # Filter data for the selected restaurant
    restaurant_data = data[data['Restaurant Name'] == selected_restaurant].iloc[0]

    # Display summary
    display_summary(restaurant_data)

if __name__ == "__main__":
    main()
