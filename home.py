import streamlit as st

st.sidebar.title("Trash Classifier App")
st.page_link("home.py",label="Home")
st.page_link("app.py",label="Application")
st.page_link("contributors.py",label="Contributors")
#st.sidebar.markdown("# [Home](https://emtech-2-final-project-home.streamlit.app/)")
#st.sidebar.markdown("# [Application](https://emtech-2-final-project-application.streamlit.app/)")
#st.sidebar.markdown("# [Contributors](https://emtech-2-final-project-contributors.streamlit.app/)")

page_bg_img = '''
<style>
.main {
background-image: url("https://static.vecteezy.com/system/resources/previews/034/346/838/non_2x/different-colored-recycle-waste-bins-illustration-waste-types-segregation-recycling-vector.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
