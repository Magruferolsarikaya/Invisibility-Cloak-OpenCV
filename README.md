# Invisibility Cloak 🪄

This project recreates the famous Harry Potter Invisibility Cloak using Python and OpenCV. By using color masking and image processing techniques, the program detects a specific color in real-time and replaces it with a pre-captured background, making the object (and anything behind it) disappear!

## 🌟 Features
* **Background Capture:** Automatically captures the static background upon launch.
* **HSV Color Space:** Uses HSV for accurate color detection regardless of minor lighting changes.
* **Real-time Masking:** Applies bitwise operations to seamlessly blend the saved background over the target color.

## 🚀 How to Run
```bash
pip install opencv-python numpy
python visibility.py
