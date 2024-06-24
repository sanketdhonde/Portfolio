import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("image/photos.jpg")

with col2:
    st.title("Sanket Dhonde")
    content ="""Hi , I am Sanket Dhonde I am a Programmer . I am pursuing a B.E in artifical intelligence and data science in Mumbai University.
     As these domians continue to shape the future of technology ,I am at forefront of innovation , exploring the intersection of data-driven insights and intelligent systems . 
     So i am in studying mode of more language for data analysis and ai. make it perfect
     """
    st.info(content)




content2 = """
Below you can find some of my work done on python . Feel free to contact me
"""

st.write(content2)




