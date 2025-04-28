import streamlit as st
import os
from util import get_location, estimate_price, load_details

# Initialize the app and load model details
st.title("House Price Prediction")
try:
    if not os.path.exists('MultipleFiles/home_prices_model_new.pickle') or not os.path.exists('MultipleFiles/columns_new.json'):
        st.error("Model or columns file missing. Please ensure 'home_prices_model_new.pickle' and 'columns_new.json' are present.")
    else:
        load_details()
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

# Create input fields
locations = get_location()
location = st.selectbox("Select Location", options=locations, index=0)
total_sqft = st.number_input("Total Square Feet", min_value=300.0, max_value=10000.0, value=1000.0, step=10.0)
bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1, max_value=10, value=2, step=1, format="%d")
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2, step=1, format="%d")

# Predict button
if st.button("Predict Price"):
    try:
        estimated_price = estimate_price(location, total_sqft, bath, bhk)
        if estimated_price is not None:
            st.success(f"Estimated House Price: ₹ {estimated_price:.2f} Lakhs")
        else:
            st.error("Prediction failed. Please check your inputs.")
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")

# Instructions
st.markdown("""
### Instructions
1. Select the location from the dropdown.
2. Enter the total square footage of the house.
3. Specify the number of bedrooms (BHK) and bathrooms.
4. Click the 'Predict Price' button to get the estimated price.
""")
