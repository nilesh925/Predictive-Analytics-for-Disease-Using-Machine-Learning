import pickle  # pre trained model loading
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Prediction of Disease Outbreaks", layout="wide", page_icon="doctor"
)
diabetes_model = pickle.load(
    open(
        r"C:\Users\NILESH\OneDrive\Desktop\AICTE INTERNSHIP\Prediction Of Disease Outbreak\saved_models\diabetes_model.sav",
        "rb",
    )
)
heart_disease_model = pickle.load(
    open(
        r"C:\Users\NILESH\OneDrive\Desktop\AICTE INTERNSHIP\Prediction Of Disease Outbreak\saved_models\heart_model.sav",
        "rb",
    )
)
parkinsons_model = pickle.load(
    open(
        r"C:\Users\NILESH\OneDrive\Desktop\AICTE INTERNSHIP\Prediction Of Disease Outbreak\saved_models\parkinsons_model.sav",
        "rb",
    )
)

with st.sidebar:
    selected = option_menu(
        "Prediction of disease outbreak system",
        ["Diabetes Prediction", "Heart Diseases Prediction", "Parkinsons Prediction"],
        menu_icon="hospital-fill",
        icons=["activity", "heart", "person"],
        default_index=0,
    )

if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number Of Pregnacies")
    with col2:
        Glucose = st.text_input("Glucose level")
    with col3:
        Bloodpressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
    with col2:
        Insulin = st.text_input("Insulin level")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    with col2:
        Age = st.text_input("Age of the person")

    # Predict Button for Diabetes
    diab_diagnosis = ""
    if st.button("Diabetes Test Result"):
        user_input = [
            Pregnancies,
            Glucose,
            Bloodpressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age,
        ]

        if "" in user_input:
            st.error("Please fill all fields")
        else:
            try:
                user_input = [float(x) for x in user_input]

                diab_prediction = diabetes_model.predict([user_input])

                if diab_prediction[0] == 1:
                    st.success("The person is diabetic")
                else:
                    st.success("The person is not diabetic")

            except ValueError:
                st.error("Please enter valid numeric values")


if selected == "Heart Diseases Prediction":
    st.title("Heart Diseases Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain types")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholestorl in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar >120 mg/dl")
    with col1:
        restecg = st.text_input("Resting ElectroCardiographic Results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input("ST depression induced by exercise")
    with col2:
        slope = st.text_input("Slope of peak exercise ST segment")
    with col3:
        ca = st.text_input("Major vessels colored by flourosopy")
    with col1:
        thal = st.text_input("thal:0 = normal;1=fixed defect;2= reversable defect")

    # Predict Button for heart
    heart_disease = ""
    if st.button("Heart Disease Test Result"):
        user_input = [
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal,
        ]

        if "" in user_input:
            st.error("Please fill all fields")
        else:
            try:
                user_input = [float(x) for x in user_input]

                heart_prediction = heart_disease_model.predict([user_input])

                if heart_prediction[0] == 1:
                    st.success("The person has Heart Disease")
                else:
                    st.success("The person does not have Heart Disease")

            except ValueError:
                st.error("Please enter valid numeric values")

if selected == "Parkinsons Prediction":
    st.title("Parkinson's Diseases Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        MDVP_Fo_Hz = st.text_input("MDVP(Hz)")
    with col2:
        MDVP_Fhi_Hz = st.text_input("MDVP (Hz)")
    with col3:
        MDVP_Flo_Hz = st.text_input("MDVP  (Hz)")
    with col4:
        MDVP_Jitter = st.text_input("MDVP (%)")
    with col5:
        MDVP_Jitter_Abs = st.text_input("MDVP (Abs)")
    with col1:
        MDVP_RAP = st.text_input(" MDVP")
    with col2:
        MDVP_PPQ = st.text_input("MDVP")
    with col3:
        Jitter_DDP = st.text_input("Jitter")
    with col4:
        MDVP_Shimmer = st.text_input("  MDVP")
    with col5:
        MDVP_Shimmer_dB = st.text_input("MDVP(DB)")
    with col1:
        Shimmer_APQ3 = st.text_input(" Shimmer")
    with col2:
        Shimmer_APQ5 = st.text_input("Shimmer")
    with col3:
        MDVP_APQ = st.text_input(" MDVP ")
    with col4:
        Shimmer_DDA = st.text_input(" Shimmer ")
    with col5:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("Spread1")
    with col5:
        spread2 = st.text_input("Spread2")
    with col1:
        D2 = st.text_input("D2")
    with col2:
        PPE = st.text_input("PPE")

    # Predict Button for Parkinson's
    parkinsons_disease = ""
    if st.button("Parkinson's Test Result"):
        user_input = [
            MDVP_Fo_Hz,
            MDVP_Fhi_Hz,
            MDVP_Flo_Hz,
            MDVP_Jitter,
            MDVP_Jitter_Abs,
            MDVP_RAP,
            MDVP_PPQ,
            Jitter_DDP,
            MDVP_Shimmer,
            MDVP_Shimmer_dB,
            Shimmer_APQ3,
            Shimmer_APQ5,
            MDVP_APQ,
            Shimmer_DDA,
            NHR,
            HNR,
            RPDE,
            DFA,
            spread1,
            spread2,
            D2,
            PPE,
        ]

        if "" in user_input:
            st.error("Please fill all fields")
        else:
            try:

                user_input = [float(x) for x in user_input]

                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    st.success("The person has Parkinson's Disease")
                else:
                    st.success("The person does not have Parkinson's Disease")

            except ValueError:
                st.error("Please enter valid numeric values")
