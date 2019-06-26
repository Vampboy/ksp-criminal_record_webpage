import face_recognition
import cv2 
from PIL import Image

face_1_image = face_recognition.load_image_file("Test Images/115.jpg")
face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]



for i in range(1,80):
    img=face_recognition.load_image_file("Test Images/"+str(i)+".jpg")
    face_locations = face_recognition.face_locations(img)
    print(face_locations,i)
    face_encodings = face_recognition.face_encodings(img, face_locations)

    if len(face_encodings)>0:
        check=face_recognition.compare_faces(face_1_face_encoding, face_encodings)

        top, right, bottom,left = (face_recognition.face_locations(img))[0]

        print("fond face at top:{},left:{},botoom:{},right:{}".format(top,left,bottom,right))
        #face_image=img[top:bottom,left:right]
        #pil_image=Image.fromarray(face_image)
        #pil_image.save("face.jpg")

        print(check)
        if check[0]:
            print("welcome prakash: ",i)

        else :
            print("unauthorized access",i)    


