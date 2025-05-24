import streamlit as st
from PIL import Image
import io
import os
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Image to PDF Converter",
    page_icon="📄",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🖼️ Image to PDF Converter")
st.markdown("Upload your image and convert it to PDF format easily!")

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert button
    if st.button("Convert to PDF"):
        try:
            # Create a PDF file
            pdf_bytes = io.BytesIO()
            image.save(pdf_bytes, format='PDF')
            pdf_bytes.seek(0)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pdf_filename = f"converted_image_{timestamp}.pdf"
            
            # Download button
            st.download_button(
                label="Download PDF",
                data=pdf_bytes,
                file_name=pdf_filename,
                mime="application/pdf"
            )
            
            st.success("PDF created successfully! Click the download button above to save it.")
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Made by ❤️ imran hassan") 