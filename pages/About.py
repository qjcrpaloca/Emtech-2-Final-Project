import streamlit as st

page_bg_img = '''
<style>
.main {
background-image: url("https://static.vecteezy.com/system/resources/previews/034/346/838/non_2x/different-colored-recycle-waste-bins-illustration-waste-types-segregation-recycling-vector.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("About the App")
st.divider()
st.subheader("Introducing EcoSort, the innovative app designed to simplify waste management by classifying images of trash. Using advanced image recognition technology, EcoSort accurately identifies and categorizes items as cardboard, glass, metal, paper, plastic, or others. Simply snap a photo, and let EcoSort do the sorting for you, ensuring your recyclables end up in the right place. Perfect for both personal and community use, EcoSort promotes environmental responsibility with ease. Transform your waste disposal habits and contribute to a greener planet with EcoSort.")
