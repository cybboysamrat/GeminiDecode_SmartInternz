from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the API key for google generative AI
genai.configure(api_key=os.getenv("AIzaSyBUcgR1ZpBf2OwU-IgMiAgkChhE8UroCPY"))

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

# Page header
st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

# Text with styling
text = "Utilizing Gemini Pro AI, this project effortlessly extracts vital information from diverse multilingual documents, transcending language barriers with precision."
styled_text = f'<span style="font-family:serif;">{text}</span>'
st.markdown(styled_text, unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])

# Display uploaded image
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Button to submit the image
submit = st.button("Tell me about the document")

# Input prompt for the AI model
input_prompt = """
You are an expert in understanding invoices.
We will upload an image of an invoice, and you will answer any questions based on the uploaded invoice image.
"""

# Function to get a response from the generative model
def get_gemini_response(input_text, image_data, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image_data, prompt])
    return response.text

# If the submit button is clicked
if submit and uploaded_file is not None:
    # Process the image and get the response from the AI model
    image_data = image  # Pass the image as image data (this can be processed further as needed)
    response = get_gemini_response(input_prompt, image_data, image)
    
    # Display the response
    st.subheader("The response is:")
    st.write(response)
