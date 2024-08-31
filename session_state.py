import streamlit as st


def init_session_state():
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        reset_all()


def reset_all():
    st.session_state.light_adjustments = {
        "Exposure": 1.0,
        "Contrast": 1.0,
        "Highlights": 1.0,
        "Shadows": 1.0,
        "Whites": 1.0,
        "Blacks": 1.0,
    }
    st.session_state.color_adjustments = {
        "Temperature": 0.0,
        "Tint": 0.0,
        "Vibrance": 0.0,
        "Saturation": 1.0,
    }
    st.session_state.other_adjustments = {
        "Sharpness": 1.0,
        "Hue": 0.0,
    }
    st.session_state.rotation = 0
    st.session_state.flip_direction = "None"
