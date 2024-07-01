import base64
import streamlit as st

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("faq.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url('data:image/jpeg;base64,{img}');
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}


[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def load_css():
    with open("css/faq-styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

load_css()


st.write("### Frequently Asked Questions")
st.markdown("")

with st.expander("""###### How to change my university login password?"""):
    st.markdown("""You can do this [Here](https://selfservice.th-rosenheim.de). Log in there with your access data (user name and initial access password) and set your new personal password. Now you can log in to the systems and services with your user name and the new password.""")

with st.expander("""###### How to print/Scan/Plot documents in university?"""):
    st.markdown("""
    you can find detailed information about printing & plotting and user guide on [Printing, Plotting & Scanning](https://intranet.th-rosenheim.de/einrichtungen/rechenzentrum/it-services/drucken-plotten-scannen). For this you need to login to intranet to get accesses to the above webpage.
    """)

with st.expander("""###### connect to eduroam/fh-intern wifi networks?."""):
    st.markdown("""
    To connect to "Eduroam" and "fh-intern" wifi netoworks please visit [WIRELESS INTERNET ACCESS](https://intranet.th-rosenheim.de/einrichtungen/rechenzentrum/systemzugang/wlan) which provides detail information on how to connect to these wifi's with step bt step guide for Android and Iphone users. Ypu will also find the information on how to connect to these wifi on windows/ Ios/ Linux opearting systems.
    """)