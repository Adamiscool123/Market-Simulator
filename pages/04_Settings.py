import streamlit as st

aggressiveness = st.slider("Aggressiveness", min_value=0, max_value=10, width="stretch")

st.markdown(
    """
        <style>
            .stSlider label{
                font-size = 40px;
                font-weight = bold;
            }
        
        <style>

    """
)