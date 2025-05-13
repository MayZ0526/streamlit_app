import streamlit as st

welcome_page = st.Page("pages/welcome.py")
test_page1 = st.Page("pages/test_page1.py")
test_page2 = st.Page("pages/test_page2.py")

pg = st.navigation([welcome_page, test_page1, test_page2])
pg.run()