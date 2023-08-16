import streamlit as st

st.set_page_config(
  page_title="Welcome", page_icon="🎃") # To show this icon press on key ((Windows) + (.))

st.write("# 𝖂𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝕸𝖞 𝕬𝖕𝖕𝖘 ")
st.warning("###(っ◔◡◔)っ ♥ I created this application to practice on the Streamlit library in Python ♥")

st.sidebar.success("Select Demo above.")



# Hide the menu and footer
def hide_menu():
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
            content:'Apps Made by @Saif Malkshahi';
            visibility: visible;
            display: block;
            position: relative;
            #background-color: red;
            padding: 5px;
            top: 2px;
            }
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_menu()



# streamlit run Home.py