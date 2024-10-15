# face_recog_test

## Instructions to run using the command line (terminal on MacOS)

1. Clone the repository using `git clone https://github.com/nfl6fh/face_recog_test`
2. Enter the directory using `cd face_recog_test`
3. Install the dependencies using `pip3 install -r requirements.txt`
4. In order to add people to recognize, create a folder in the faces folder with the name of the person in the format: first_last. Then add images of the person in the folder. The images should be in .jpeg or .jpg or .png format
5. Run the program using `python3 main.py`
6. In order to stop the program, press `q` while in the video window

## Some common errors (these shouldn't happen because of the requirements.txt file, but just in case)

- `ModuleNotFoundError: No module named 'cv2'` - This means you need to install OpenCV. You can do this by running `pip3 install opencv-python` in the terminal.
- `ModuleNotFoundError: No module named 'face_recognition'` - This means you need to install the face_recognition library. You can do this by running `pip3 install dlib` and then `pip3 install face_recognition` in the terminal.
- `ModuleNotFoundError: No module named 'numpy'` - This means you need to install numpy. You can do this by running `pip3 install numpy` in the terminal.
- failed to build dlib error while running `pip3 install face_recognition` or `pip3 install dlib` - This probably means you need to install cmake. You can do this by running `brew install cmake` in the terminal.