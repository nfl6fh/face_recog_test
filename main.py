import face_recognition
import cv2
import numpy as np
import os

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

img_src = ''
while img_src not in ['0', '1']:
    img_src = input("Enter image source number (0 for webcam, 1 for iPhone camera): ") # If iPhone doesn't work try connecting with a cable

img_src = int(img_src)

try:
    video_capture = cv2.VideoCapture(img_src)
    test_resize = cv2.resize(video_capture.read()[1], (0, 0), fx=0.25, fy=0.25)
except:
    print(f"Error opening video from source {img_src}, defaulting to webcam")
    video_capture = cv2.VideoCapture(0)

# iterate through faces folder and add all the faces to the known_face_encodings array
known_face_encodings = []
known_face_names = []

for folder in os.listdir('faces'):
    name = f'{folder.split("_")[0].capitalize()} {folder.split("_")[1].capitalize()}'
    try:
        for i, file in enumerate(os.listdir(f'faces/{folder}')):
            if file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.png'):
                face_image = face_recognition.load_image_file(f'faces/{folder}/{file}')
                face_encoding = face_recognition.face_encodings(face_image)[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(name+'_'+str(i))
    except:
        if folder != '.DS_Store':
            print(f'Error loading face images for {name}')
        continue

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
last_name = ''

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    frame_flipped = cv2.flip(frame,1) if img_src == 0 else frame

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame_flipped, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index][:-2]
            if name != last_name and name != "Unknown":
                print(f'The last recognized face was: {name}')
                last_name = name

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame_flipped, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame_flipped, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame_flipped, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame_flipped)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()