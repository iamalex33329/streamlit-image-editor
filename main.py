from image_processing import apply_adjustment, flip_image
from session_state import init_session_state, reset_all
from ui import create_sidebar, create_main_layout, download_button

from PIL import Image

import streamlit as st


def main():
    st.set_page_config(layout="wide")
    st.title("Advanced Image Editor")

    init_session_state()

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')

        col1, col2 = create_main_layout(image)

        create_sidebar()

        all_adjustments = {**st.session_state.light_adjustments,
                           **st.session_state.color_adjustments,
                           **st.session_state.other_adjustments}

        edited_image = apply_adjustment(image, all_adjustments)

        if st.session_state.flip_direction != "None":
            edited_image = flip_image(edited_image, st.session_state.flip_direction)

        col2.image(edited_image, caption="Edited Image", use_column_width=True)

        download_button(edited_image)


if __name__ == "__main__":
    main()
