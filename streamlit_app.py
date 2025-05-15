import streamlit as st
import requests

# Set your FastAPI endpoint
API_URL = "http://localhost:8001/score_headlines"  # Replace with your API port

st.set_page_config(page_title="Headline Sentiment Scorer", layout="wide")
st.title("📰 Headline Sentiment Analyzer")

# Input headline management
if "headlines" not in st.session_state:
    st.session_state.headlines = [""]

def add_headline():
    st.session_state.headlines.append("")

def remove_headline(index):
    st.session_state.headlines.pop(index)

# UI for headline input
st.subheader("✏️ Enter Headlines")
for i, headline in enumerate(st.session_state.headlines):
    col1, col2 = st.columns([6, 1])
    with col1:
        st.session_state.headlines[i] = st.text_input(f"Headline {i+1}", value=headline, key=f"headline_{i}")
    with col2:
        if st.button("🗑️", key=f"remove_{i}"):
            remove_headline(i)
            st.experimental_rerun()

st.button("➕ Add Headline", on_click=add_headline)

# Submit to backend
if st.button("🚀 Analyze Sentiment"):
    valid_headlines = [h for h in st.session_state.headlines if h.strip()]
    if not valid_headlines:
        st.warning("Please enter at least one headline.")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(API_URL, json={"headlines": valid_headlines})
                result = response.json()
                st.success("Analysis Complete!")
                for h, l in zip(valid_headlines, result["labels"]):
                    st.write(f"**{h}** ➡️ _{l}_")
            except Exception as e:
                st.error(f"API Error: {e}")
