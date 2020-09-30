# Script to recognize faces

## encode.py
Script to encode images to pickle encoding

Store images in ./dataset/<person_name>/<image_name.jpg>

    python encode_faces.py --dataset ./dataset/ --encodings encodings.pickle --detection-method cnn

## recognize.py
Initialize object in the begining

Call recognize_face function on each frame to detect and recognize faces