import streamlit as st
import re  # Import the regular expressions library

# Function to parse and aggressively clean the HTML content from the file
def parse_html_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    parts = content.split('<h1>')  # Split the content based on known restaurant headers
    html_content = {}
    for part in parts[1:]:  # Skip the first split as it will be empty
        title_end = part.find('Review Summary</h1>')
        title = part[:title_end].strip()
        # Aggressively remove all types of whitespace characters, including newlines
        cleaned_html = re.sub(r'\\n', ' ', part)  # Ensure to escape the backslash in the regex
        cleaned_html = re.sub(r'\s+', ' ', cleaned_html).strip()  # Replace all whitespace sequences with a single space
        html_content[title] = f"<h1>{cleaned_html}"
    return html_content


# Streamlit layout
def main():
    st.title("Restaurant Reviews")
    
    # Path to the HTML text file
    file_path = 'Restaurants summary_HTML.txt'

    # Parse the HTML content from the file
    html_content = parse_html_content(file_path)
    
    # Create a dropdown menu to select a restaurant
    restaurant = st.selectbox('Select a Restaurant', options=list(html_content.keys()))
    
    # Display the HTML content for the selected restaurant
    st.markdown(html_content[restaurant], unsafe_allow_html=True)

if __name__ == "__main__":
    main()
