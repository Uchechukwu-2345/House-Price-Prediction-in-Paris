import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("rf_model.pkl")

st.title("🏠 Paris House Price Prediction App")

st.write("This app predicts the price of a house in Paris based on several features.")

st.divider()

# Input features
squareMeters = st.number_input("📐 Square Meters", min_value=1, value=2000)
numberOfRooms = st.number_input("🛏️ Number of Rooms", min_value=0, value=0)
cityPartRange = st.number_input("🏙️ City Part Range", min_value=1, value=10)
floors = st.number_input("🏢 Number of Floors", min_value=0, value=3)
hasStorageRoom = st.selectbox("📦 Storage Rooms", ["Yes", "No"], index=1)
attic = st.number_input("🏠 Attic",  min_value=100, max_value=10000, value=200)

# Convert storage room count to binary value
hsr = 1 if hasStorageRoom == "Yes" else 0

# Form the input array
X = np.array([[squareMeters, numberOfRooms, cityPartRange, floors, attic, hsr]])

st.divider()

if st.button("🔍 Predict Price!"):
    prediction = model.predict(X)[0]
    st.balloons()
    st.success(f"💰 Predicted House Price: €{prediction:,.2f}")


else:
    st.info("Click the 'Predict Price!' button to estimate the house price.")


    #'squareMeters', 'numberOfRooms', 'cityPartRange', 'floors',
      # 'hasStorageRoom', 'attic'