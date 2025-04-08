import streamlit as st
import pyshorteners as pyst
import pyperclip as pc
st.markdown("<h1 style='text-align:center;'>URL SHORTNER</h1>",unsafe_allow_html=True)

#To copy tiny url to clipboard
def copying():
    pc.copy(short_url)    

#using with will give errors
form=st.form("url")
url=form.text_input("URL to be shortened")
state=form.form_submit_button("SHORTEN")

#shortener class allows to shorten url
shortner=pyst.Shortener()
if state:
    short_url=shortner.tinyurl.short(url)
    st.markdown("<h4 style='text-align:center;'>SHORT URL</h4>",unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align:center;'>{short_url}</h6>",unsafe_allow_html=True)
    state1=st.button("COPY",on_click=copying)
    
