import streamlit as st
st.image('images/10003.jpg', caption='cola')
text = st.text_input("입력")
if st.button("Save"):
    st.session_state.text = text
    st.session_state.list = [1, 2, 3, 4, 5]
#st.session_state는 키와 값으로 나뉨
#st.session_state.key  or
#st.session_state["key"]
