import streamlit as st
import pandas as pd
from datetime import datetime
import uuid

# Function to save data to Excel file
def save_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel('patient_records.xlsx', index=False)

# Function to generate unique patient ID
def generate_patient_id():
    return str(uuid.uuid4())

# Streamlit app
def main():
    st.title("Patient Records Application")

    # Load existing data from Excel file (if any)
    try:
        existing_data = pd.read_excel('patient_records.xlsx')
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    # Initialize data dictionary to store current patient data
    data = {
        'Patient ID': [],
        'First Name': [],
        'Last Name': [],
        'Age': [],
        'Treatment': [],
        'Problem': [],
        'Date of Treatment': [],
        'Date of Visit': []
    }

    # User input section
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    age = st.number_input("Age", min_value=0, max_value=150)
    treatment = st.text_input("Treatment")
    problem = st.text_area("Problem")
    date_of_treatment = st.date_input("Date of Treatment", datetime.now())
    date_of_visit = st.date_input("Date of Visit", datetime.now())

    # Check if the patient already exists in records
    existing_patient = existing_data[
        (existing_data['First Name'] == first_name) &
        (existing_data['Last Name'] == last_name) &
        (existing_data['Age'] == age)
    ]

    if st.button("Submit"):
        if existing_patient.empty:
            patient_id = generate_patient_id()
        else:
            patient_id = existing_patient.iloc[0]['Patient ID']

        # Update data dictionary
        data['Patient ID'].append(patient_id)
        data['First Name'].append(first_name)
        data['Last Name'].append(last_name)
        data['Age'].append(age)
        data['Treatment'].append(treatment)
        data['Problem'].append(problem)
        data['Date of Treatment'].append(date_of_treatment)
        data['Date of Visit'].append(date_of_visit)

        # Save to Excel file
        save_to_excel(data)

        st.success("Patient information saved successfully!")

if __name__ == "__main__":
    main()
