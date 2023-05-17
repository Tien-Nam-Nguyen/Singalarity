import face_recognition
import cv2
import pickle
import os

knownEncodings = []
knownNames = []

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.jpg'):
        image = cv2.imread(filename)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # print('done rgb')
        boxes = face_recognition.face_locations(rgb, model= 'hog')
        # boxes = face_recognition.api.face_locations(rgb, model= 'cnn')
        encodings = face_recognition.face_encodings(rgb, boxes)

        name = filename[:-5]
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)


data = {'encodings': knownEncodings, 'names': knownNames}
f = open('encodings.pickle', 'wb')
f.write(pickle.dumps(data))
f.close()