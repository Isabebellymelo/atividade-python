import streamlit as st

x = st.slider("Selecione um valor")
st.write(x, "o quadrado é", x * x)
