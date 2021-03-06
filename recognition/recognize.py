import cv2
import pickle
import face_recognition

class recognize:
    def __init__(self):
        self.data = pickle.loads(open("./encodings.pickle", "rb").read())
        self.detector = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

    def recognize_face(self, frame):
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rects = self.detector.detectMultiScale(gray, scaleFactor=1.1, flags=cv2.CASCADE_SCALE_IMAGE)
        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        for encoding in encodings:
            matches = face_recognition.compare_faces(self.data["encodings"], encoding)
            name = 'Unknown'
            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                for i in matchedIdxs:
                    name = self.data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)
            names.append(name)
            for ((top, right, bottom, left), name) in zip(boxes, names):
                # draw the predicted face name on the image
                cv2.rectangle(frame, (left, top), (right, bottom),(0, 0, 255), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                if name == 'Unknown':
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
						0.75, (0, 0, 255), 2)
                else:
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
						0.75, (0, 255, 0), 2)
            
        return frame
