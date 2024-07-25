import streamlit as st

if st.button("호출"):
    if "text" in st.session_state:
        st.write(st.session_state.text)
        st.write(st.session_state.list)
    else :
        st.write("Error")