import face_recognition
# import imutils
import pickle
import cv2
import os

def process(videofile):
    # print(f'Wd: {os.getcwd()}')Wd: /home/nam/Desktop/Face_reg/project
    videofile = os.path.join('media', videofile)
    data = pickle.loads(open('Image/encodings.pickle', 'rb').read())
    print(f'File: {videofile}')
    # stream = cv2.VideoCapture(videofile)
    # writer = None
    # while True:
    #     (grabbed, frame) = stream.read()
    #     if not grabbed:
    #         break

    #     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #     boxes = face_recognition.face_locations(rgb, model='hog')
    #     encodings = face_recognition.face_encodings(rgb, boxes)
    #     names = []
    #     for encoding in encodings:
    #         matches = face_recognition.compare_faces(data['encodings'], encoding)
    #         name = 'Unknown'

    #         if True in matches:
    #             matchedIdxs = [i for (i, b) in enumerate(matches) if b]
    #             counts = {}

    #             for i in matchedIdxs:
    #                 name = data['names'][i]
    #                 counts[name] = counts.get(name, 0) + 1

    #             name = max(counts, key= counts.get)
            
    #         names.append(name)
        
    #     for ((top, right, bottom, left), name) in zip(boxes, names):
    #         cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
    #         y = top - 15 if top - 15 > 15 else top + 15
    #         cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 2)

    #         fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    #         writer = cv2.VideoWriter("media/video/response.avi", fourcc, 24, (frame.shape[1], frame.shape[0]), True)

    #     if writer is not None:
    #         writer.write(frame)


    # stream.release()

    # if writer is not None:
    #     writer.release()