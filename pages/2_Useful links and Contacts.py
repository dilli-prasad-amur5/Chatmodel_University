import streamlit as st

st.write("## Useful Links and Contact details")
st.markdown("")
st.markdown("""
This page contains a collection of useful links that can provide you with additional information and resources. Click on the expanders below to view links related to different topics.""")

def load_css():
    with open("css/faq-styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

load_css()

with st.expander("###### University Timetable/Schedule"):
    st.markdown("""
    - Timetables for summer semester 2024 can be founs at [Stundenpläne Hochschule Rosenheim](https://splan.fh-rosenheim.de/splan/mobile?lan=de&acc=true&act=tt&sel=pg&pu=33&sd=true&dfc=2023-04-13&loc=3&sa=false&cb=o)
    - University schedule for summer semester 2024 can be found at [Terminplan Sommersemester 2024](https://www.th-rosenheim.de/fileadmin/formalia/Dokumente_und_Merkblaette/Terminplaene_Kalender/Terminplan_20241_EuD.pdf)
    """)

with st.expander("###### Enrollment certificate/ Immatriculation"):
    st.markdown("""
    you can Register for exams & Internship, Grade sheets/Transcript of Records  and download your enrollment certificate from the [online student service center](https://cm.th-rosenheim.de/qisserver/pages/cs/sys/portal/hisinoneStartPage.faces).
    - **Enrollment certificate:** First login to your account using your student login credentails. After you login, you select 'My Studies' in Menubar and  ***Mystudies > Student service > Requested Reports / Reports***  and here you can download your certificate both in English and German.
    - **Registration for examinations:** To view the subjects you registered for exams visit ***Mystudies > My registrations for an examination / internship*** here you can view all the subjects you registered for the cuurent semester.
    - **Registration for examinations:** You can download your Grade sheet/Transcripts at ***Mystudies > My achievements*** page and at the bottom of the page you can find Transcripts of Records PDF documents.
    """)

with st.expander("###### Student Administration"):
    st.markdown("""
    The Student Administration department is responsible for managing a variety of essential services and procedures for students such as processing of name changes, recognizing foreign school-leaving certificates, managing leave of absence requests, handling university applications, overseeing the process of exmatriculation, accommodating visiting students, conducting matriculation or enrolment, issuing Student Cards, managing tuition fees, and overseeing admission processes.
    """)
    st.markdown("""
    To communicate with the Student Administration at TH Rosenheim, individuals can reach out through telephone numbers available: +49 (0) 8031 805 2162 and +49 (0) 8031 805 2163. Additionally, inquiries can be sent via email to studienamt@th-rosenheim.de. The administration office is located on the Rosenheim Campus, in Building B, Room B 1.36.
    """)
    st.markdown("""
    The office is open to visitors at specific times during the week and the hours of operation are on Monday and Thursday from 09:00 to 12:00 hrs, and on Wednesday from 13:00 to 15:00 hrs.
    """)

with st.expander("###### Examinations Office "):
    st.markdown("""
    The Examinations Office deals with the following matters:  Degree certificate, recognition of previous study, Grade certificate with seal, Examinations: Organisation, registration and deregistration, sickness notification.
    """)
    st.markdown("""
    **Examination Office Rosenheim contact details:** Loacted in Rosenheim in Building B Room 1.35. Non-technical degree programmes: Irena Walter (Head of Department), Phone: +49 8031 805 2150, Hannah Tüllmann, Phone: +49 8031 805 2356, Anne Klopfer, Phone: +49 8031 805 2352. Technical degree programmes: Sandra Fischer, Phone: +49 8031 805 2153, Angela Voit, Phone: +49 8031 805 2152, Julie Bufler, Phone +49 8031 805 2353, Johanna Feller-Wagner, +49 8031 805 2151. pruefungsamt@th-rosenheim.de. 
    """)
    st.markdown("""
    **Contact Burghausen Campus and Mühldorf am Inn Campus:** Werner Thar (Head of Department), Phone +49 8031 805 4025, werner.thar@th-rosenheim.de. Fabian Dalhoff (Campus Mühldorf am Inn only), Phone +49 8031 805 4523, fabian.dalhoff@th-rosenheim.de.
    """)

with st.expander("###### Internship Office"):
    st.markdown("""
    The Internship Office deals with the following concerns: Internship abroad, Internships, Company contacts.
    """)
    st.markdown("""
    **Rosenheim campus contact details:** Susanne Armbruster-Brück, Phone +49 8031 805 2158. Silvia Kroneck, Phone +49 8031 805 2326, Building B Room 1.28a , praktikantenamt@th-rosenheim.de. Attention! Special opening hours: Tue-Thu: 9:00-12:00 hrs, Tue only: 13:00 - 15:00 hrs.
    """)
    st.markdown("""
    **Contact details for Burghausen Campus and Mühldorf am Inn Campus:** Werner Thar (Head of Department), Phone +49 8031 805 4025, werner.thar@th-rosenheim.de. Fabian Dalhoff (Campus Mühldorf am Inn only), Phone +49 8031 805 4523, fabian.dalhoff@th-rosenheim.de. 
    """)

with st.expander("###### International Office"):
    st.markdown("""
    The International Office of Rosenheim Technical University of Applied Sciences (TH Rosenheim) is in charge of mobility programmes and helps students plan and apply for their stay abroad.
    """)
    st.markdown("""
    **Address and contact details:** R 2.22 (Building R, 2nd Floor) in Rosenheim campus. Contact persons are Academic Director- Prof. Dr. Carolin Fleischmann, carolin.fleischmann@th-rosenheim.de,  +49 (0)8031 / 805 – 2460. 
    
    Sibylle Möbius leads as the Head of the International Office and International University Partnerships, available at +49 (0)8031 / 805 – 2117, or via email at sibylle.moebius@th-rosenheim.de. 
    
    Tamara Hormaier serves as the Erasmus+ Institutional Coordinator, focusing on outgoing students and staff, reachable at +49 (0)8031 / 805 - 2118 or tamara.hormaier@th-rosenheim.de. 
    
    Tina Kaffl oversees Erasmus+ Internships, short-term programmes, staff mobility, and worldwide scholarships, contactable at +49 (0)8031 / 805 - 2782 or tina.kaffl@th-rosenheim.de. 
    
    Andschana Mendes is the coordinator for incoming exchange students, available at +49 (0)8031 / 805 - 2566 or andschana.mendes@th-rosenheim.de. 
    
    Maria Heinrich focuses on international marketing, with her contact details being +49 (0)8031 / 805 - 2993 and maria.heinrich@th-rosenheim.de. 
    
    Tatjana Erlewein-Paulsen is involved with the Projekt Internationalisierung 2.0, reachable at +49 (0)8031 / 805 - 2789 or tatjana.erlewein-paulsen@th-rosenheim.de. 
    
    Florian Thoma coordinates the HAW.International (Module B) project, with his contact information at +49 (0)8031 / 805 - 2683 or florian.thoma@th-rosenheim.de. 
    
    Lastly, Franziska Wohlfart supports the HAW.International (Module B) project, available at +49 (0)8031 / 805 - 2843 or franziska.wohlfart@th-rosenheim.de. This team ensures the smooth operation and development of international activities and partnerships at the university.
    """)
    st.markdown("""
    
    """)