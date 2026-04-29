import streamlit as st

# 1. Make the label big using simple Markdown (no CSS needed)
st.markdown("## **Aggressiveness**")

# 2. Create columns: One small (2), one large (3)
# The slider will only fill the first column, keeping it small and left-aligned.
col1, col2 = st.columns([2, 3])

with col1:
    # Use label_visibility="collapsed" since we wrote our own label above
    aggressiveness = st.slider(
        "Aggressiveness", 
        min_value=0, 
        max_value=10, 
        label_visibility="collapsed"
    )

st.title("")

st.markdown("### **Whale**")

whale_qty = st.text_input(label="Qty: ", key=1)


st.title("")

st.markdown("### **Market Maker**")

market_maker_qty = st.text_input(label="Qty: ", key=2)


st.title("")

st.markdown("### **Noisy Trader**")

noise_trader_qty = st.text_input(label="Qty: ", key=3)


st.title("")

st.markdown("### **Trend Follower**")

trend_follower_qty = st.text_input(label="Qty: ", key=4)


st.title("")

if "button_text" not in st.session_state:
    st.session_state.button_text = "Start Simulation"

# 3. Use a unique 'key' so Streamlit can track this specific widget 
# even when the label text changes.
if st.button(st.session_state.button_text, key="sim_controller"):
    # Toggle the logic
    if st.session_state.button_text == "Start Simulation":
        st.session_state.button_text = "Stop Simulation"
    else:
        st.session_state.button_text = "Start Simulation"
    
    st.rerun()