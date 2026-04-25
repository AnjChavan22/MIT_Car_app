import streamlit as st
import pandas as pd
import pickle

# Load model
try:
    with open('final_model.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('columns.pkl', 'rb') as f:
        cols = pickle.load(f)

except FileNotFoundError:
    st.error("Model files not found. Keep final_model.pkl and columns.pkl in folder.")
    st.stop()

# Dropdown values
d1 = ['Comprehensive', 'Third Party insurance', 'Zero Dep', 'Not Available', 'Third Party']
d2 = ['Petrol', 'Diesel', 'CNG']
d3 = ['Manual', 'Automatic']
d4 = ['First Owner', 'Second Owner', 'Third Owner', 'Fifth Owner']

# UI
st.title("🚗 Car Price Prediction Dashboard")
st.write("Enter the car details below to estimate car price.")

col1, col2 = st.columns(2)

with col1:
    ins_val = st.selectbox("Insurance Validity", d1)
    fuel_type = st.selectbox("Fuel Type", d2)
    transmission = st.selectbox("Transmission", d3)

with col2:
    seats = st.number_input("Seats", min_value=2, max_value=10, value=5)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=10000)
    ownership = st.selectbox("Ownership", d4)

# Prediction
if st.button("Predict Price"):

    # Create dataframe
    test = pd.DataFrame([{
        'insurance_validity': ins_val,
        'fuel_type': fuel_type,
        'seats': seats,
        'kms_driven': kms_driven,
        'ownership': ownership,
        'transmission': transmission
    }])

    # Convert to dummy columns
    test = pd.get_dummies(test)

    # Match training columns
    test = test.reindex(columns=cols, fill_value=0)

    # Predict
    yp = model.predict(test)[0]

    st.success(f"### Predicted Car Price: ₹ {yp:.2f} Lakhs")
    st.balloons()