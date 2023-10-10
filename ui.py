import streamlit as st

from naive import naive_string_match
from robinkarp import rabin_karp_string_match

st.title("String Matching Algorithms")

text = st.text_input("Enter the text:")
pattern = st.text_input("Enter the pattern to search:")

algorithm = st.radio("Choose Algorithm:", ("Naive", "Rabin-Karp"))

def display_results():
    if algorithm == "Naive":
        matches = naive_string_match(text, pattern)
    else:
        matches = rabin_karp_string_match(text, pattern)
    
    if matches:
        st.write(f"Pattern found at positions: {matches}")
    else:
        st.write("Pattern not found in the text.")

if st.button("Search"):
    if text and pattern:
        display_results()
    else:
        st.warning("Please enter both text and pattern.")

st.sidebar.markdown("### Instructions")
st.sidebar.markdown("1. Enter the text in the 'Enter the text' field.")
st.sidebar.markdown("2. Enter the pattern to search in the 'Enter the pattern to search' field.")
st.sidebar.markdown("3. Choose the algorithm (Naive or Rabin-Karp).")
st.sidebar.markdown("4. Click the 'Search' button to find the pattern in the text.")