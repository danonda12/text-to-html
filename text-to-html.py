import streamlit as st
import base64
from bs4 import BeautifulSoup

def text_to_html(text):
    # Add a custom stylesheet link to the head of the HTML content
    custom_css = '<link rel="stylesheet" href="data:text/css;base64,' + base64.b64encode(STYLESHEET.encode()).decode() + '">'
    html_content = f'{custom_css}\n{str(BeautifulSoup(text, "html.parser"))}'
    return html_content

# Define your custom stylesheet
STYLESHEET = '''
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        line-height: 1.6;
        margin: 20px;
        padding: 20px;
        background-color: #f5f5f5;
        color: #333;
    }

    h1 {
        color: #4285f4;
    }

    h2 {
        color: #333;
    }

    p {
        color: #555;
    }

    a {
        color: #4285f4;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    code {
        background-color: #f8f8f8;
        border: 1px solid #ddd;
        border-radius: 4px;
        padding: 2px 4px;
    }

    blockquote {
        border-left: 4px solid #4285f4;
        padding: 10px;
        margin: 10px 0;
        background-color: #f9f9f9;
    }
'''

def main():
    st.title("Text to HTML Converter")

    # User input
    text_input = st.text_area("Enter your text:", placeholder="Type here...", height=150)

    # Convert button
    if text_input:
        # Convert text to HTML
        html_output = text_to_html(text_input)

        # Display HTML output with improved styling
        # st.markdown(
        #     f'<div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">{html_output}</div>',
        #     unsafe_allow_html=True
        # )

        # Download button
        download_link = get_download_link(html_output)
        st.markdown(download_link, unsafe_allow_html=True)

    # Instructions and tips
    st.sidebar.header("Instructions")
    st.sidebar.markdown("1. Enter your text in the text area.")
    st.sidebar.markdown("2. Click the 'Convert to HTML' button.")
    st.sidebar.markdown("3. Download the generated HTML if needed.")

def get_download_link(html_content):
    # Function to create a download link for the generated HTML content
    encoded_html = base64.b64encode(html_content.encode()).decode()
    href = f'data:text/html;base64,{encoded_html}'
    download_button = f'<a class="download-button" href="{href}" download="generated_page.html">Download HTML</a>'
    return download_button

if __name__ == "__main__":
    main()
