# Imports

import streamlit as st
import pandas as pd
import joblib

# Page configration

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Load pipline


pipeline = joblib.load(
    "models/student_performance_pipeline.pkl"
)

# Set title

st.title("🎓 Student Performance Predictor")

st.markdown("""
Predict whether a student is likely to achieve **Satisfactory**
or **Unsatisfactory** academic performance using a Machine Learning model.
""")

st.divider()
# Slidbar

st.sidebar.title("About")

st.sidebar.info("""
This application predicts whether a student is likely to achieve satisfactory academic performance.

Model Used:
- Random Forest Classifier

Tech Stack

🐍 Python

🤖 Scikit-learn

🎨 Streamlit
""")

# Dividing inputs(Student Information) into three different categories

st.header("📝 Student Information")

col1, col2, col3 = st.columns(3)

# Column 1 personal Information

with col1:
    st.subheader("👤 Personal")

    age = st.number_input(
        "Age",
        min_value=12,
        max_value=30,
        value=17
    )

    sex = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    address = st.selectbox(
        "Address",
        ["Urban", "Rural"]
    )

    famsize = st.selectbox(
        "Family Size",
        ["LE3 (3 or less)", "GT3 (Greater than 3)"]
    )

    Pstatus = st.selectbox(
        "Parents Living Together",
        ["Yes", "No"]
    )

# Column 2 Family information

with col2:
    st.subheader("👨‍👩‍👧 Family")

    education_mapping = {
    "No formal education": 0,
    "Primary education": 1,
    "Middle school": 2,
    "Secondary school": 3,
    "Higher education": 4
}

    mother_education = st.selectbox(
    "Mother's Education",
    list(education_mapping.keys())
)

    Medu = education_mapping[mother_education]


    father_education = st.selectbox(
    "Father's Education",
    list(education_mapping.keys())
)

    Fedu = education_mapping[father_education]


    Mjob = st.selectbox(
        "Mother's Job",
        ["teacher","health","services","at_home","other"]
    )

    Fjob = st.selectbox(
        "Father's Job",
        ["teacher","health","services","at_home","other"]
    )

    guardian = st.selectbox(
        "Guardian",
        ["mother","father","other"]
    )

# Column 3 Academic information

with col3:
    st.subheader("📚 Academic")

    school = st.selectbox(
        "School",
        ["GP","MS"]
    )

    studytime = st.selectbox(
        "Study Time",
        [
            "<2 hours/week",
            "2-5 hours/week",
            "5-10 hours/week",
            ">10 hours/week"
        ]
    )

    studytime_mapping = {
    "<2 hours/week": 1,
    "2-5 hours/week": 2,
    "5-10 hours/week": 3,
    ">10 hours/week": 4
}

    studytime = studytime_mapping[studytime]

    travel_mapping = {
    "Less than 15 minutes": 1,
    "15–30 minutes": 2,
    "30–60 minutes": 3,
    "More than 1 hour": 4
}
    
    travel_time = st.selectbox(
    "Travel Time",
    list(travel_mapping.keys())
)

    traveltime = travel_mapping[travel_time]

    failures = st.number_input(
        "Past Class Failures",
        0,
        4,
        0
    )

    absences = st.number_input(
        "Absences",
        0,
        100,
        5
    )

# A divider and 3 more columns for next few caregories
st.divider()

st.header("🏫 School Support & Lifestyle")

col4, col5, col6 = st.columns(3)

#School Support

with col4:
    st.subheader("🏫 School Support")

    schoolsup = st.selectbox(
        "Extra Educational Support",
        ["Yes", "No"]
    )

    famsup = st.selectbox(
        "Family Educational Support",
        ["Yes", "No"]
    )

    paid = st.selectbox(
        "Extra Paid Classes",
        ["Yes", "No"]
    )

    activities = st.selectbox(
        "Extra-curricular Activities",
        ["Yes", "No"]
    )

    nursery = st.selectbox(
        "Attended Nursery School",
        ["Yes", "No"]
    )

#Goals

with col5:
    st.subheader("🎯 Future Goals")

    higher = st.selectbox(
        "Wants Higher Education",
        ["Yes", "No"]
    )

    internet = st.selectbox(
        "Internet Access at Home",
        ["Yes", "No"]
    )

    romantic = st.selectbox(
        "Currently in a Relationship",
        ["Yes", "No"]
    )

    reason = st.selectbox(
        "Reason for Choosing School",
        [
            "course",
            "home",
            "reputation",
            "other"
        ]
    )

# Life style

with col6:
    st.subheader("🌱 Lifestyle")

    famrel = st.slider(
        "Family Relationship",
        1, 5, 3
    )

    freetime = st.slider(
        "Free Time",
        1, 5, 3
    )

    goout = st.slider(
        "Going Out with Friends",
        1, 5, 3
    )

    Dalc = st.slider(
        "Workday Alcohol Consumption",
        1, 5, 1
    )

    Walc = st.slider(
        "Weekend Alcohol Consumption",
        1, 5, 2
    )

    health = st.slider(
        "Current Health",
        1, 5, 3
    )

# Converting input data into required form for model

# Convert user-friendly inputs to dataset values

sex = "M" if sex == "Male" else "F"

address = "U" if address == "Urban" else "R"

famsize = "LE3" if famsize == "LE3 (3 or less)" else "GT3"

Pstatus = "T" if Pstatus == "Yes" else "A"

schoolsup = "yes" if schoolsup == "Yes" else "no"

famsup = "yes" if famsup == "Yes" else "no"

paid = "yes" if paid == "Yes" else "no"

activities = "yes" if activities == "Yes" else "no"

nursery = "yes" if nursery == "Yes" else "no"

higher = "yes" if higher == "Yes" else "no"

internet = "yes" if internet == "Yes" else "no"

romantic = "yes" if romantic == "Yes" else "no"

# Convert all inputs into a Data fram to give it to model

input_data = pd.DataFrame({
    "school": [school],
    "sex": [sex],
    "age": [age],
    "address": [address],
    "famsize": [famsize],
    "Pstatus": [Pstatus],
    "Medu": [Medu],
    "Fedu": [Fedu],
    "Mjob": [Mjob],
    "Fjob": [Fjob],
    "reason": [reason],
    "guardian": [guardian],
    "traveltime": [traveltime],
    "studytime": [studytime],
    "failures": [failures],
    "schoolsup": [schoolsup],
    "famsup": [famsup],
    "paid": [paid],
    "activities": [activities],
    "nursery": [nursery],
    "higher": [higher],
    "internet": [internet],
    "romantic": [romantic],
    "famrel": [famrel],
    "freetime": [freetime],
    "goout": [goout],
    "Dalc": [Dalc],
    "Walc": [Walc],
    "health": [health],
    "absences": [absences]
})

# Add confidence score

if st.button("Predict Performance", use_container_width=True):

    prediction = pipeline.predict(input_data)[0]
    probability = pipeline.predict_proba(input_data)[0]

    confidence = max(probability) * 100

    st.divider()

    st.subheader("🎯 Prediction Result")


# add a better message

if prediction == 1:
    st.success("🎉 This student is likely to have **Satisfactory Academic Performance**.")

    st.info(f"**Prediction Confidence:** {confidence:.2f}%")
    st.progress(confidence / 100)
    st.write("""
The model predicts that the student has a good chance of achieving satisfactory academic performance based on the information provided.
""")

else:
    st.error("⚠️ This student is likely to have **Unsatisfactory Academic Performance**.")

    st.info(f"**Prediction Confidence:** {confidence:.2f}%",)
    st.progress(confidence / 100)
    st.write("""
The model predicts that the student may struggle academically. Consider reviewing factors such as study habits, attendance, and academic support.
""")


# Add disclaimer

st.divider()

st.caption(
    "Disclaimer: This prediction is generated by a machine learning model and should be used for educational purposes only. It is not a substitute for professional academic evaluation."
)
