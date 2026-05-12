import Variable
import streamlit as st
import time

v = st.session_state.variables

v.print_book()

if v.simulation:
    v.run_simulation(st.session_state.market)

if v.simulation:
    time.sleep(0.5)
    st.rerun()