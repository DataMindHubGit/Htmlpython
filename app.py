import streamlit as st

# Function to generate HTML code with Python code
def generate_html_with_code(user_code):
    # Define the HTML structure
    html_code = f"""
    <!-- Include Prism.js CSS for styling --> 
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet"/>
    
    <!-- Include Prism.js Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    
    <!-- Include Prism.js for Python -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
    
    <!-- Custom CSS to modify the background color to dark blue -->
    <style>
        pre[class*="language-"] {{
            background-color: #001f3d !important; /* Dark blue background */
            color: #f0f0f0; /* Light text color for readability */
        }}
    </style>
    
    <!-- Your Python code block with syntax highlighting -->
    <pre><code class="language-python">
{user_code}
    </code></pre>
    """
    return html_code

# Streamlit Interface
st.title("Python Code to HTML Generator")

# Text area for user to input Python code
user_code = st.text_area("Enter your Python code here:", height=200)

# When the user clicks on the 'Generate HTML' button
if st.button("Generate HTML"):
    if user_code:
        # Generate HTML with the Python code
        html_output = generate_html_with_code(user_code)
        # Display the generated HTML code
        st.text_area("Generated HTML (ready to paste in WordPress):", html_output, height=300)
    else:
        st.error("Please enter some Python code to generate the HTML.")
