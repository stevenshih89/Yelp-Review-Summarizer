import pandas as pd
import streamlit as st

# Load data from the CSV file
df = pd.read_csv('restaurant_data.csv')

# Function to display reviews based on selected restaurant
def display_reviews(restaurant_name):grgr
    # Filter data based on restaurant name
    restaurant_data = df[df['Restaurant Name'] == restaurant_name].iloc[0]
    
    # Output positive and negative reviews
    st.write(f"**Positive Reviews (%):** {restaurant_data['Positive Reviews (%)']}%")
    st.write(f"**Negative Reviews (%):** {restaurant_data['Negative Reviews (%)']}%")

# Streamlit layout
def main():
    st.title("Restaurant Reviews")

    # Dropdown to select a restaurant
    restaurant_name = st.selectbox("Select a Restaurant", df['Restaurant Name'].unique())

    # Display the reviews based on selected restaurant
    display_reviews(restaurant_name)

if __name__ == "__main__":
    main()
