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

st.title('Contributors')
st.divider()
st.image('jc.jpg')
