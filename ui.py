import streamlit as st
from session_state import reset_all
import io


def create_main_layout(image):
    col1, col2 = st.columns(2)
    col1.image(image, caption="Original Image", use_column_width=True)
    return col1, col2


def create_sidebar():
    st.sidebar.header("Adjustment Options")

    if st.sidebar.button("Reset All"):
        reset_all()
        st.rerun()

    create_adjustment_sliders("Light", st.session_state.light_adjustments)
    create_adjustment_sliders("Color", st.session_state.color_adjustments, color=True)
    create_adjustment_sliders("Others", st.session_state.other_adjustments, others=True)

    st.session_state.flip_direction = st.sidebar.selectbox(
        "Flip",
        ["None", "Horizontal", "Vertical"],
        index=["None", "Horizontal", "Vertical"].index(st.session_state.flip_direction)
    )


def create_adjustment_sliders(title, adjustments, color=False, others=False):
    st.sidebar.subheader(title)
    for adjustment in adjustments:
        if color and adjustment in ["Temperature", "Tint"]:
            adjustments[adjustment] = st.sidebar.slider(
                adjustment, -1.0, 1.0, adjustments[adjustment], 0.01
            )
        elif others and adjustment == "Hue":
            adjustments[adjustment] = st.sidebar.slider(
                adjustment, -1.0, 1.0, adjustments[adjustment], 0.01
            )
        else:
            adjustments[adjustment] = st.sidebar.slider(
                adjustment, 0.0, 2.0, adjustments[adjustment], 0.01
            )


def download_button(image):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    st.download_button(
        label="Download Edited Image",
        data=img_byte_arr,
        file_name="edited_image.png",
        mime="image/png"
    )
