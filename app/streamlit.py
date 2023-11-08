import streamlit as st
import requests
import pandas as pd

from src import functions

refund_df = pd.DataFrame({})
coach_df = pd.DataFrame({})
airline_df = pd.DataFrame({})
smit_df = pd.DataFrame({})

# Title
st.header('Data Product with Machine Learning')

# Data Input
with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        origin_airport = st.text_input('Origin airport', placeholder='Starting airport code')
        departure_date = st.date_input('Departure date')
    with col2:
        destination_airport = st.text_input('Destination airport', placeholder='Ending airport code')
        departure_time = st.time_input('Departure time' ,step=3600)
    with col3:
        cabin_options = ['coach', 'premium coach', 'business', 'first']
        cabin_type = st.multiselect('Cabin type', options=cabin_options, placeholder='Select a cabin')
        st.write('##')
        kwargs = {
            'origin_airport':origin_airport,
            'destination_airport': destination_airport,
            'departure_date': departure_date,
            'departure_time': departure_time,
            'cabin_type': cabin_type#,
            #'tab1': tab1
        }
        predict_button = st.button('Predict', type='primary')
        if predict_button:
            refund_df, coach_df, airline_df, smit_df = functions.predict(origin_airport, destination_airport, departure_date, departure_time, cabin_type)
            #, on_click=functions.predict, kwargs=kwargs)

tab1, tab2, tab3, tab4 = st.tabs(["Archit's model", "Mahjabeen's model", "Rohan's model", "Smit's model"])

if predict_button:
    with tab1:
        st.dataframe(refund_df)

    with tab2:
        st.dataframe(coach_df)

    with tab3:
        st.dataframe(airline_df)

    with tab4:
        st.dataframe(smit_df)
