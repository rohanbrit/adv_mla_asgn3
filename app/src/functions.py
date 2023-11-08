from datetime import datetime
import time
import streamlit as st
import pandas as pd

    
def predict(origin_airport, destination_airport, departure_date, departure_time, cabin_type):
    data = {
        'searchDate': datetime.now(),
        'flightDate': datetime.combine(departure_date, departure_time),
        'startingAirport': origin_airport,
        'destinationAirport': destination_airport,
        'segmentsCabinCode': cabin_type
    }
    df = pd.DataFrame([data])
    with st.spinner('Loading the predictions...'):

        airline_predict()
        layover_predict()
        refund_predict()
        smit_predict()

    #st.success(departure_date)
    return df, df, df, df

def airline_predict():
    
    time.sleep(1)

def layover_predict():
    time.sleep(1)

def refund_predict():
    time.sleep(1)

def smit_predict():
    time.sleep(1)