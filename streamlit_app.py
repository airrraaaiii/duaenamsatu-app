import streamlit as st

st.title("aiirraaaa")
st.write(
    "Let's start building! For wowww apa ini to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("IMG_3576.jpeg")
st.write("\n")
st.subheader("aira paskib keren mantap")
st.write(
    "lagi sering dispen gara gara paskib"
)
st.write(
    """
    - sayang ale
    - sayang keifa
    - sayang rin
    - sayang tari
    - sayang maudi
    """
)
st.header("ngecheck nilai ganjil genap")
angka = st.number_input("kasih angka:", value=0, step=1)

if(angka % 2) == 0:
    st.write(f"{angka} adalah genap")
else:
    st.write(f"{angka} adalah ganjil")
