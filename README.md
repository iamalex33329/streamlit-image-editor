# Advanced Image Editor

This is a Streamlit-based web application that allows users to upload and edit image with various adjustments.

![Screenshot](https://github.com/iamalex33329/streamlit-image-editor/blob/main/images/Screenshot.png)

## Features

- Image upload
- Light adjustments (Exposure, Contrast, Highlights, Shadows, Whites, Blacks)
- Color adjustments (Temperature, Tint, Vibrance, Saturation)
- Other adjustments (Sharpness, Hue)
- Image flipping (Horizontal, Vertical)
- Real-time preview of edits
- Download edited image

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/iamalex33329/streamlit-image-editor.git
   cd advanced-image-editor
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Upload an image using the file uploader.

4. Use the sidebar sliders to adjust various parameters of the image.

5. The edited image will be displayed in real-time.

6. When satisfied with the edits, click the "Download Edited Image" button to save your work.

## Project Structure

- `main.py`: The main Streamlit application file.
- `image_processing.py`: Contains functions for image processing and adjustments.
- `session_state.py`: Manages the Streamlit session state and reset functionality.
- `ui.py`: Contains functions for creating UI components.