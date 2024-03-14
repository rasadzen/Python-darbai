import cv2
import pandas as pd
import os
import matplotlib.pyplot as plt


# #vaizdo ikelimas
# image = cv2.imread('short-haired-german-shepherd-puppies.jpeg')
#
# #parodyti orginalu vaizda
# cv2.imshow('Orginalus vaizdas', image)
# cv2.waitKey(0)   #laukiama bet kokio klaviso paspaudimo, tiek kiek nurodyta skliaustuose, 0 laukia bet kiek
# cv2.destroyAllWindows()
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Pilku atspalviu vaizdas', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def find_faces(image_path):
    #ikeliame veidu atpazinimo modeli
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    #ikeliame vaizda ir pakeiciame i pilka atspalvi
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # atrandame veidus vaizde
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces: #nusibreziam kvadraciukus ant veidu kad matyt ka atpazista
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('veidai', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return faces


images_folder = 'C:/Users/Rasa/Desktop/img/'
data = []

# files = [f for f in os.listdir(images_folder) if f.endswith('.jpg') or f.endswith('.png')]   # cia jei norim pasitikrinti ar grazina info

for filename in os.listdir(images_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        path = os.path.join(images_folder, filename)
        faces = find_faces(path)
        data.append({'filename': filename, 'faces_count': len(faces)})

df = pd.DataFrame(data)
# print(df)   # cia matom kiekvienam faile kiek veidu

average_faces = df['faces_count'].mean()
# print(f'Vidutinis veidu skaicius vaizduose: {average_faces}')

max_faces = df.loc[df['faces_count'].idxmax()]
# print(f'Daugiausiai veidu turintis vaizdas: {max_faces["filename"]}, veidu skaicius: {max_faces["faces_count"]}')

df['faces_count'].plot(kind='hist', title='Veidu skaiciaus pasiskirstymas')
plt.xlabel('Veidu skaicius')
plt.ylabel('Vaizdu skaicius')
plt.show()

