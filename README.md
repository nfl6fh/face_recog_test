# face_recog_test

## Instructions to run using the command line (terminal on MacOS)

1. Clone the repository using `git clone https://github.com/nfl6fh/face_recog_test`
2. Enter the directory using `cd face_recog_test`
3. Activate the virtual environment with `source env/bin/activate`
4. Edit the main.py file everywhere you see a `TODO` following the directions in the comments
5. Run the program using `python main.py`
6. In order to stop the program, press `q` while in the video window

## Some common errors

- `ModuleNotFoundError: No module named 'cv2'` - This means you need to install OpenCV. You can do this by running `pip install opencv-python` in the terminal.
- `ModuleNotFoundError: No module named 'face_recognition'` - This means you need to install the face_recognition library. You can do this by running `pip install face_recognition` in the terminal.
- `ModuleNotFoundError: No module named 'numpy'` - This means you need to install numpy. You can do this by running `pip install numpy` in the terminal.
- failed to build dlib error - This probably means you need to install cmake. You can do this by running `brew install cmake` in the terminal.