import streamlit as st
import joblib
import pandas as pd



model = joblib.load('salary_prediction_model.pkl')

def Predict_salary(CompanySize, Industry, Experience, Title, City): #'Company Size', 'Industry', 'Experience', 'Title', 'City'

    input_data = pd.DataFrame({
    "Company Size":[CompanySize],
    "Industry":[Industry],
    "Experience":[Experience],
    "Title":[Title],
    "City":[City] })

    prediction = model.predict(input_data)
    return prediction[0]

Cities = ['Halifax', 'Montreal', 'Hamilton–Niagara Peninsula',
       'Kitchener–Waterloo–Barrie', 'Toronto',
       'Vancouver Island and Coast', 'Moncton–Richibucto', 'Calgary',
       'Winnipeg', 'Kingston–Pembroke', 'Edmonton', 'Ottawa', 'Other',
       'London']
Industries = ['IT / Software', 'Manufacturing, Transportation, or Supply Chain',
       'Insurance', 'Advertising Services', 'Wholesale', 'Healthcare',
       'Oil & Gas', 'Financial Services', 'Legal Services',
       'Retail and Consumer Services', 'Higher Education']
Experiences = ['5 to 9 years', '10 or more years', '2 to 4 years', '0 to 1 years']

Titles = ['Data scientist or machine learning specialist',
       'Developer, full-stack', 'Data or business analyst',
       'Developer, front-end', 'Engineer, data', 'Developer, back-end',
       'Developer, game or graphics',
       'Developer, desktop or enterprise applications',
       'DevOps specialist', 'Developer, mobile',
       'Cloud infrastructure engineer', 'Security professional',
       'Scientist', 'System administrator', 'Educator',
       'Research & Development role',
       'Developer, embedded applications or devices', 'Hardware Engineer',
       'Developer, QA or test', 'Academic researcher',
       'Engineering manager', 'Senior Executive (C-Suite, VP, etc.)',
       'Project manager', 'Developer Experience',
       'Database administrator', 'Engineer, site reliability', 'Designer',
       'Product manager']

Companysizes = ['Small (2-19 Employees)', 'Medium (20-499 Employees)',
       'Large (500-9999 Employees)',
       'Very Large (10000 or More Employees)']






st.title(" Welcome to the Canadian Salary Predictor 🍁 ")

st.markdown(
    """
    This app uses machine learning to estimate salary ranges for various technical roles in Canada. By inputting your city, industry, experience level, job title, and company size, you can get a prediction of the expected salary for your profile.

    **Features:**
    - **Company Size:** Choose the size of the company you are interested in, ranging from Small to Very Large.
    - **Industry:** Select the industry you work in or are interested in.
    - **Experience:** Indicate your level of experience in years.
    - **Job Title:** Choose your current or desired job title.
    - **City:** Select the city where you are or where you are seeking employment.

    Simply fill out the details and hit the 'Predict Salary' button to see the estimated salary.

    """,
    unsafe_allow_html=True
)

st.divider()

CompanySize = st.selectbox('**Company Size**',  Companysizes)
Industry = st.selectbox('**Industry**',  Industries)
Experience = st.selectbox('**Experience**',  Experiences)
Title = st.selectbox('**Title**',  Titles)
City = st.selectbox('**City**',  Cities)


if st.button('Predict Salary'):
    if CompanySize and Industry and Experience and Title and City:
        salary = Predict_salary(CompanySize, Industry, Experience, Title, City)
        st.success(f'The predicted salary is: ${salary:,.2f}')

    else:
        st.error('Please fill out all the fields')

st.markdown(""" 
        **Disclaimer:** 
        The predictions are based on a limited dataset and may not fully represent real-world conditions""")

st.image('canadasky.png')  

