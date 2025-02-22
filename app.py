
import streamlit as st
import datetime
import random

# Motivational Quotes
QUOTES = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "With the new day comes new strength and new thoughts.",
    "Do what you can, with what you have, where you are.",
    "Your limitation—it's only your imagination.",
]

# 🚀 Page Configuration
st.set_page_config(page_title="Growth Mindset Tracker", layout="wide")

# 🌿 Custom Styling
st.markdown("""
    <style>
        body { background: linear-gradient(135deg, #f5f7fa, #c3cfe2); }
        .main-container { text-align: center; padding: 20px; }
        .quote-box { background: #ff6b6b; padding: 15px; color: white; border-radius: 10px; font-size: 18px; font-style: italic; text-align: center; }
        .card { background: rgba(255, 255, 255, 0.9); padding: 25px; border-radius: 12px; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2); backdrop-filter: blur(10px); }
        .header { font-size: 30px; font-weight: bold; color: #ff6b6b; text-align: center; margin-bottom: 20px; }
        .button { background: linear-gradient(90deg, #ff6b6b, #ff8e53); color: white; padding: 10px 15px; border-radius: 10px; text-align: center; font-weight: bold; transition: 0.3s; }
        .button:hover { transform: scale(1.05); box-shadow: 0px 4px 10px rgba(255, 107, 107, 0.5); }
    </style>
    """, unsafe_allow_html=True)

def main():
    # 🎨 Sidebar (Dark Mode)
    theme = st.sidebar.radio("🎨 Choose Theme:", ["Light", "Dark"])
    if theme == "Dark":
        st.markdown("""
            <style>
                body { background: #222; color: white; }
                .stTextInput, .stTextArea, .stSlider, .stButton { background-color: #333 !important; color: white !important; }
                .card { background: rgba(40, 40, 40, 0.9); box-shadow: 0px 5px 15px rgba(255, 255, 255, 0.1); }
                .header { color: #ff8e53; }
                .button { background: linear-gradient(90deg, #ff8e53, #ff6b6b); }
            </style>
        """, unsafe_allow_html=True)

    # 🚀 App Title
    st.markdown("<div class='header'>🚀 Growth Mindset Tracker</div>", unsafe_allow_html=True)
    st.subheader("Develop Your Abilities Through Hard Work and Learning")
    st.write("A growth mindset is the belief that intelligence and abilities can be developed through effort, learning, and persistence.")

    # 🌟 Display a Random Motivational Quote
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.success(random.choice(QUOTES))
    st.markdown("</div>", unsafe_allow_html=True)

    # 📌 Learning Goal Section
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📌 Set Your Learning Goals")
    goal = st.text_area("What is your learning goal for this week?")
    deadline = st.date_input("Deadline for this goal:", datetime.date.today())
    if st.button("💾 Save Goal", key="goal"):
        st.success(f"✅ Goal saved: {goal} (Deadline: {deadline})")
    st.markdown("</div>", unsafe_allow_html=True)

    # 📊 Progress Tracker
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📈 Track Your Progress")
    progress = st.slider("How confident do you feel about your progress?", 0, 100, 50)
    st.progress(progress / 100)
    if st.button("🚀 Submit Progress", key="progress"):
        if progress == 100:
            st.balloons()
            st.success("🎉 Congratulations! You've reached 100% progress!")
        else:
            st.info("Keep going! You're making progress.")
    st.markdown("</div>", unsafe_allow_html=True)

    # 📝 Daily Reflection
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📝 Daily Reflection")
    reflection = st.text_area("Write about your learning experience today:")
    if st.button("💾 Save Reflection", key="reflection"):
        st.success("Reflection saved successfully!")
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
