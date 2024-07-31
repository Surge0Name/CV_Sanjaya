import streamlit as st
import base64


def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

base64_image = load_image("Me.jpeg")

st.markdown("""
    <style>
            @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
            .my-image{
                width: 150px;
                height: 150px;
                border-radius: 50%;
                object-fit: cover;
                margin-bottom:20px;
                margin-top: 25px;
                margin-left: 39px;
            }
            .container{
                display:flex;
            }
            .section{
                width:100%;
                
            }
            .profile-header{
                display: flex;
                align-item: center;
                margin-bottom: 20px;
                margin-left: 20px;
            }
            .profile-text{
                margin-left: 50px;
            }
            .header{
                font-size:24px;
                font-weight: bold;
            }
            .subheader{
                font-size: 20px;
                font-weight: bold;
                text-decoration: underline;
            }
            .about-section{
                margin-top: 20px;
                text-align: center;

            }
            .contact-header{
                padding: px;
                border-radius: 5px;
                margin-top: 20px;
                margin-left: 5px;
                display: flex;
                flex-direction: column;
                align-items: center;
                
            }
            .edu-section{
                margin-left:50px;
            }
     </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.5,2.9])

with col1:
    st.markdown(f"""
        <div class = "section">
            <img src ="data:image/jpeg;base64,{base64_image}" class="my-image" alt ="Profile Image">
            <div class = "about-section">
                <h4>About Me</h4>
                <p>I am a fresh graduate from Physic Engineering ITS with main interest in both system engineering and programming. I am familiar with data science & Python</p>
            </div>
        </div>
""", unsafe_allow_html=True)
    st.markdown("""
        <div class="section contact-header">
            <h4>Personal Information</h4>
        </div>
        <p><i class = "fas fa-calendar-alt"></i>  Banjarmasin, 30 Desember 2000</p>
        <p><i class= "fas fa-home"></i> Jln. HKSN Komp. AMD permai Blok A5 RT/RW 025/002 No.198, Banjarmasin, Kalimantan Selatan</p>
        <div class="section contact-header">
            <h4>Contact</h4>
        </div>
            <p><i class = "fas fa-phone"></i>  +62 882 5808 2509</p>
            <p><i class = "fas fa-envelope"></i>  sanjaya12bjm@gmail.com</p>
            <p><i class = "fab fa-linkedin"></i><a href:"https://www.linkedin.com/in/i-gede-sanjaya-putra-vhyasa-2b83b41b6">  LinkedIn</a></p>

""", unsafe_allow_html=True)
    st.markdown("""
    <div class="container">
        <div class="section">
            <h4 class="subheader">Languange</h4>
            <ul>
                <li>Bahasa Indonesia</li>
                <li>English</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)
    st.markdown("""
    <div class="container">
        <div class="section">
            <h4 class="subheader">Skills Summary</h4>
            <ul>
                <li>Python</li>
                <li>Flutter</li>
                <li>ReactJs</li>
                <li>OpenCV</li>
                <li>Data Wrangling</li>
                <li>Tailwind</li>
                <li>Trainer</li>
                <li>Google Spreadsheet and Ms.Excel</li>
                <li>Human Resources</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class = "profile-text">
             <h1> I Gede Sanjaya Putra Vhyasa</h1>
             <h3>Bachelor of Engineering Physic</h3>
        </div>
""", unsafe_allow_html= True)
    # Education and Work Experience
    st.markdown("""
        <div class="edu-section">
            <h4 class="subheader">Education</h4>
            <p>Institut Teknologi Sepuluh November (ITS)</p>
            <p>Physic Engineering, IPK 3.1</p>
            <p>2019 - 2024</p>
        </div>
        <div class="edu-section">
            <h4 class="subheader">Work Experience</h4>
            <h5>Community Service | R&D Staff in Community Service Project</h5>
            <p>September 2021 - December 2021</p>
            <ul>
                <li>Community service titled "IoT Based Pond Water Quality Parameter Monitoring System in Milkfish Pond Cultivation"</li>
                <li>Assembling the electrical circuit according to the diagram that has been provided</li>
                <li>Acquisition part for the electrical part</li>
                <li>Calibrating hardware</li>
            </ul>
            <h5>PT. Elefante Infrajdi Solusi | Internship (Kerja Praktek)</h5>
            <p>July 2022 - August 2022</p>
            <ul>
                <li>Internship for developing a program to scan and extract civilian ID for registration</li>
                <li>Helping staff to develop website by implementing the code I have written</li>
                <li>Writing the program to be able to extract multiple id</li>
                <li>OpenCV and OCR were used in the project with Python</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    # Organization Experience
    st.markdown("""
        <div class="container">
            <div class="edu-section">
                <h4 class="subheader">Organization Experience</h4>
                <h5>Kendo Student Club | President</h5>
                <p>February 2021 - February 2022</p>
                <ul>
                    <li>Planning, assisting, and coordinating my staff in managing the entire courses and events of the organization</li>
                    <li>Overseeing and managing 22 staff in 4 divisions to run 15 work programs throughout the year</li>
                </ul>
                <h5>Embedded and Cyber-Physical System Laboratory | Head of A.I Division</h5>
                <p>May 2021 - December 2023</p>
                <ul>
                    <li>Teaching and upgrading skills of ECS Laboratory staff</li>
                    <li>Spokesperson when high school students visited ECS laboratory</li>
                    <li>Teaching physics engineering students during openlab programs</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)