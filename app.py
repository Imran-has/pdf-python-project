import streamlit as st
from PIL import Image
import io
from datetime import datetime
import tempfile
import os

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
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Convert button
    if st.button("Convert to PDF"):
        try:
            # Read the image
            image = Image.open(uploaded_file)
            
            # Convert to RGB if image is in RGBA mode
            if image.mode == 'RGBA':
                image = image.convert('RGB')
            
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                # Convert image to PDF
                image.save(tmp_file.name, 'PDF')
                
                # Read the PDF file
                with open(tmp_file.name, 'rb') as pdf_file:
                    pdf_bytes = pdf_file.read()
                
                # Clean up the temporary file
                os.unlink(tmp_file.name)
            
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
st.markdown("Made with ❤️ using Streamlit") 