import streamlit as st
import pandas as pd 
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# Read the excel file data
df = pd.read_excel("Adidas.xlsx")
st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
image = Image.open('adidas-logo.jpg')

col1, col2 = st.columns([0.1,0.9])
with col1:
    st.image(image,width=100)
    
html_title = """
    <style>
    .title.test{
    font-weight: bold;
    padding: 5px;
    border-radius: 6px    
    }
    </style>
    <center><h1 class="title-test">Adidas Interactive Sales Dashboard</h1></center>"""
with col2:
    st.markdown(html_title, unsafe_allow_html=True)
    
col3, col4, col5 = st.columns([0.1, 0.45, 0.45])
with col3:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last updated by:  \n {box_date}")
    
with col4:
    fig = px.bar(df, x = "Retailer", y = "TotalSales", labels={"TotalSales" : "Total Sales {$}"}, 
                 title = "Total Sales by Retailer", hover_data=["TotalSales"],
                 template="gridon", height=500)
    st.plotly_chart(fig, use_container_width=True)