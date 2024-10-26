import streamlit as st
from PIL import Image
from datetime import datetime

# Set up the page configuration
st.set_page_config(page_title="Happy Birthday Shubhangi!", layout="wide")

# CSS for styling and animations based on Color Hunt palette
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Norican&family=Playfair+Display:wght@500&display=swap');

    .stApp {
        background-color: #E2F1E7;
        padding: 20px;
    }
    .header {
        background-color: #387478;
        padding: 20px;
        text-align: center;
        font-size: 40px;
        font-family: 'Playfair Display', serif;
        color: white;
        border-radius: 15px;
        animation: fadeIn 3s;
    }
    .main-text {
        font-family: 'Norican', cursive;
        color: #243642;
        font-size: 30px;
        text-align: center;
    }
    .age-text {
        font-family: 'Architects Daughter', cursive;
        color: #243642;
        font-size: 24px;
        text-align: center;
    }
    .footer {
        background-color: #387478;
        padding: 10px;
        text-align: center;
        color: white;
        font-family: 'Architects Daughter', cursive;
        border-radius: 15px;
    }
    .quote-box {
        background-color: #629584;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        font-family: 'Norican', cursive;
        font-size: 20px;
        color: #243642;
        animation: fadeInUp 2s;
        text-align: center;
    }
    .photo-grid {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
        margin: 20px 0;
    }
    .photo-card {
        width: 300px;
        height: 200px;
        overflow: hidden;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        transition: transform 0.2s ease-in-out;
    }
    .photo-card:hover {
        transform: scale(1.05);
    }
    .animated-btn {
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        font-size: 16px;
        font-family: 'Architects Daughter', cursive;
        border-radius: 12px;
        background-color: #387478;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.3s;
        margin: 20px 0;
        animation: pulse 2s infinite;
    }
    .animated-btn:hover {
        background-color: #243642;
        transform: scale(1.1);
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown('<div class="header">Happy Birthday, Shubhangi!</div>', unsafe_allow_html=True)

# Display the greeting message
st.markdown('<p class="main-text">The world has been blessed since you were born! 🎂</p>', unsafe_allow_html=True)

# Calculate real-time age
birthday = datetime(2004, 10, 27)  # Shubhangi's birth date
now = datetime.now()
time_diff = now - birthday
days_since_birth = time_diff.days
years = days_since_birth // 365
months = (days_since_birth % 365) // 30
hours, remainder = divmod(time_diff.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Display age dynamically
st.markdown(
    f'<p class="age-text">You\'ve been a blessing for *{years} years, {months} months, {days_since_birth % 30} days, {hours} hours, {minutes} minutes, and {seconds} seconds*!</p>',
    unsafe_allow_html=True
)

# Interactive Photo Gallery
st.markdown('<p class="main-text">Click to Reveal Butki!</p>', unsafe_allow_html=True)
photos = ["./1.jpeg", "./2.jpeg", "./3.jpeg", "./4.jpeg"]  # Add paths of the 4 photos

st.markdown('<div class="photo-grid">', unsafe_allow_html=True)
for i, photo in enumerate(photos):
    with open(photo, "rb") as img_file:
        img = Image.open(img_file)
        st.image(img, caption=f"Memory {i+1}", use_column_width=True, output_format="JPEG")
st.markdown('</div>', unsafe_allow_html=True)

# Motivational Section
st.markdown(
    """
    <div class="quote-box">
    <h2>May your day be as special as you are, Shubhangi!</h2>
    <p>"Your journey has just begun. Keep shining like the star you are!"</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Call to Action Button with Animation
if st.button("Click to Send Your Wishes!", key="wish-btn"):
    st.balloons()

# Footer Section
st.markdown('<div class="footer">Crafted with love and joy using Python and Streamlit</div>', unsafe_allow_html=True)