import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("image/photos.jpg", width=400)

with col2:
    st.title("Sanket Dhonde")
    content ="""Hi , I am Sanket Dhonde I am a Programmer . I am pursuing a B.E in artifical intelligence and data science in Mumbai University.
     As these domians continue to shape the future of technology ,I am at forefront of innovation , exploring the intersection of data-driven insights and intelligent systems . 
     So i am in studying mode for seeking more skills in data analysis and artificial intellgence.
     """
    st.info(content)


content2 = """
Below you can find some of my work done on python . Feel free to Contact me
"""

st.subheader(content2)


col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep = ";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/" + row["image"])
        st.write(f"[Source code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/" + row["image"])
        st.write(f"[Source code]({row['url']})")



