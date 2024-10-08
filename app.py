import streamlit as st
import google.generativeai as gen_ai
import pyperclip

# Configure Streamlit page settings
st.set_page_config(
    page_title="SEO-Optimized Blog Writer",
    page_icon=":pencil2:",
    layout="wide",
)

# Directly set the API key here (not recommended for production)
GOOGLE_API_KEY = "AIzaSyCO7WIRmXTQUPeiARLTklKLufkZRfjfg4U"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Streamlit app layout
st.title("SEO-Optimized Blog Writer")

# User input
blog_topic = st.text_input("Enter your blog topic")

# Function to generate the blog content
def generate_blog(topic):
    prompt = f"""
    Write a comprehensive, SEO-optimized blog post on the following topic:
    {topic}

    Please follow these guidelines:
    1. Start with an engaging introduction
    2. Use H1 for the main title and H2 for subheadings
    3. Include relevant keywords throughout the content
    4. Write informative and engaging paragraphs under each subheading
    5. Conclude with a strong summary
    6. Add a FAQ section at the end with 3-5 relevant questions and answers

    Format the blog post in Markdown, using # for H1 and ## for H2 headings.
    Ensure the content is well-structured, informative, and optimized for search engines.
    """
    
    response = model.generate_content([prompt])
    return response.text

# Function to copy content to clipboard
def copy_to_clipboard(content):
    pyperclip.copy(content)
    st.success("Blog content copied to clipboard!")

# Generate button
if st.button("Generate Blog"):
    if blog_topic:
        with st.spinner("Generating blog content..."):
            blog_content = generate_blog(blog_topic)
        
        # Display the generated blog content
        st.subheader("Generated Blog Content")
        st.markdown(blog_content)

        # Add a copy to clipboard button
        if st.button("Copy to Clipboard"):
            copy_to_clipboard(blog_content)
    else:
        st.warning("Please enter a blog topic.")

# Add some spacing
st.write("\n\n")

# Additional information or instructions
st.info("This tool uses AI to generate SEO-optimized blog content based on your given topic. The generated blog includes an introduction, conclusion, properly structured headings, and a FAQ section. You can copy the content to your clipboard for further editing.")