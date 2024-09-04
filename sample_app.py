import serial
import pydantic

import streamlit as st
import time
from localpackage import write_counter

st.title('Sample App')
st.write('This is a sample app.')
st.write('You can use this app to test the Streamlit deployment process.')

time_counter = st.empty()
while True:
    write_counter(time_counter)