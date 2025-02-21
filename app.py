import streamlit as st

st.set_page_config(page_title="🌱 Growth Mindset App", page_icon="💡", layout="wide")
st.title("🚀 Growth Mindset App")

st.header("🌟 Unlock Your Potential")
st.write("💪 Embrace the power of a growth mindset! Your abilities are not fixed—you can improve, learn, and grow through dedication and effort. This app provides daily prompts and reflections to help you build resilience and achieve your goals. 🌿")

# Daily Prompt Section
st.header("✨ Today's Growth Challenge")
st.write("💡 What small step can you take today to get closer to your goals?")

# User Challenge Input
st.header("🔥 Set Your Challenge for Today")
user_input = st.text_input("🎯 Describe the challenge you're facing today:")

if user_input:
    st.success(f"👏 You're tackling: {user_input}. Keep going—progress is made one step at a time! 💪")
else:
    st.warning("⚡ Challenge yourself! Enter a goal to start growing.")

# Reflection Section
st.header("🤔 Reflect on Your Journey")
reflection = st.text_input("📝 What lesson did you learn from today's challenge?")

if reflection:
    st.success(f"🎯 Insight gained: {reflection}. Every challenge is a learning opportunity! 🚀") 
else:
    st.info("🧐 Take a moment to reflect. Learning from experiences makes you stronger!")

# Achievement Section
st.header("🏆 Celebrate Your Wins") 
achievement = st.text_input("🎉 What achievement made you proud today?")
if achievement:
    st.success(f"🌟 Well done! {achievement}. Keep pushing forward and celebrating your growth! 🎊")
else:
    st.info("💖 Acknowledging small wins keeps you motivated! Share yours.")

# Footer (Centered)
st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <p style="font-size: 18px;">🌈 Believe in yourself, stay consistent, and keep moving forward! 🚀</p>
        <p style="font-size: 16px;">© 2025 Created by Kulsum Shaikh ✨</p>
    </div>
""", unsafe_allow_html=True)
