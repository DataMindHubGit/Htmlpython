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
    
    <!-- Custom CSS to modify the background color to #102e76 and center the code block -->
    <style>
        /* Centering the code block */
        .code-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Full viewport height */
        }}

        /* Styling the code block */
        pre[class*="language-"] {{
            background-color: #102e76 !important; /* Dark blue background */
            color: #f0f0f0; /* Light text color for readability */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5); /* Subtle shadow */
            width: fit-content;
            max-width: 80%;
        }}
    </style>
    
    <!-- Your Python code block with syntax highlighting -->
    <div class="code-container">
        <pre><code class="language-python">
{user_code}
        </code></pre>
    </div>
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
