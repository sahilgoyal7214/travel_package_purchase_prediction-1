import streamlit as st
from PIL import Image
from streamlit.components.v1 import html
def app():
    def open_page(url):
        open_script= """
            <script type="text/javascript">
                window.open('%s', '_blank').focus();
            </script>
        """ % (url)
        html(open_script)
    
    
    st.markdown(
        f"""
        <style>
    
        /* Center the submit button and text */
        .stButton > button {{
            display: block;
            margin: 0 auto;
            background-color: red;
            color: white;
        }}
        
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(f'''   <style>
       .stApp {{
       background-image: url("https://s3-alpha-sig.figma.com/img/5bf3/5bad/ea08dcca7bd9ae6809151988dcd3042a?Expires=1699228800&Signature=mYtGXtk1Mg84IarAqABSF73sTK7NTb7MBppBTSZjTj5grZSaiZJ3-2ccuUY4XIBgKjYtGYA119BDR-cqtdY-E6pR5XaZd39CJPK2KBbDq6e~65~swb7J9KRDb2TKL0sQEbfXwSzGHidcnOlSUNavqI2Zje1Lmhj5GaAPVrXkB77UXC13X0PhasqgA8PNXUEgkkEAWEN1ZLbgoRsaJTuXTwGAks9SXf6GqIrOGuKLVxIWGE~RJQdRMGG1W4Osa8Q2oFe8fhRC7bIAE-R1nDf7BqfrYBfi49DMSgZyKCD8x-r8PXnn2aeJX65448fC1~9WLPfv-6afDJHKj0WI3z2yyg__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4");
       background-attachment: fixed;
        background-size: cover
       }}
       </style> 
        
       ''',   unsafe_allow_html=True)
    
    
    
    
        # Title and subheader
    st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Metal Mania;font-size: 100px;font-style: normal;font-weight: 400;line-height: normal;letter-spacing: -5.6px;'>Travel Package Purchase Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #FFF;font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>This will predict whether the customer will purchase the package or not.</h1>", unsafe_allow_html=True)


        # Define the drop-down options
    col1, col2,col3,col4 = st.columns(4)

        
    with col2:
            
            # Define your 9 drop-down menus for the left column with labels to the left
        age = st.selectbox("", ["Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75 and over"])
        type_of_contact = st.selectbox("", ["company invited", "self-invited"])
        city_tier = st.selectbox("", ["Tier 1", "Tier 2", "Tier 3"])
        occupation = st.selectbox("", ["Free lancer", "Salaried", "Small Business", "Large Business"])
        gender = st.selectbox("", ["Male", "Female"])
        duration_of_pitch = st.selectbox("", ["< 15 minutes", "15-30 minutes", "30-45 minutes", "> 45 minutes"])
        number_of_people = st.selectbox("", list(range(1, 11)))
        product_pitched = st.selectbox("", ["basic", "deluxe", "king", "standard", "super deluxe"])
        number_of_followups = st.selectbox("", list(range(0, 6)))
    with col1:
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Age</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Type of Contact</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>City Tier</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Occupation</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Gender</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Duration of Pitch</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Number of People</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Product Pitched</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Number of Follow-ups</h1>", unsafe_allow_html=True)
            
    with col3:
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Marital Status</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Passport</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Number of Trips</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Designationn</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Pitch Satisfaction Score</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Annual Income</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Number of Children</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Preferred Property Star</h1>", unsafe_allow_html=True)
            st.markdown("<h1 style='text-align: center; color: #FFF; font-family: Montaga;font-size: 40px;font-style: normal;font-weight: 400;line-height: normal;'>Rating by Sales Person</h1>", unsafe_allow_html=True)
    with col4:
            # Define the remaining 9 drop-down menus for the right column with labels to the left
            marital_status = st.selectbox("", ["Single", "Married", "Divorced", "Unmarried"])
            passport = st.selectbox("", ["Yes", "No"])
            number_of_trips = st.selectbox("", list(range(0, 11)))
            designation = st.selectbox("", ["Manager", "AVP", "Executive","VP","Senior Manager"])
            pitch_satisfaction_score = st.selectbox("", list(range(1, 6)))
            annual_income = st.selectbox("", ["< $25,000", "$25,000 - $50,000", "$50,000 - $75,000", "> $75,000"])
            number_of_children = st.selectbox(" ", list(range(0, 6)))
            preferred_property_star = st.selectbox("  ", list(range(1, 6)))
            rating_by_sales_person = st.selectbox("   ", list(range(1, 6)))

        # Submit button
        
    
    
    if st.button("Submit"):
                if rating_by_sales_person > 3:
                    st.success("Customer will buy the product")
                else:
                    st.error("Customer will not buy the product")
                
    st.button('New Customer', on_click=open_page, args=('https://forms.gle/QRZsJbomMPivZYPZ9',))

    if st.button("Contact Us"):
                st.write("Email: example@email.com")
                st.write("Phone: +1-123-456-7890")

  