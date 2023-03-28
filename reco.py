import face_recognition
import tkinter as tk
from tkinter import filedialog

# Définir les noms des personnes et les chemins des fichiers d'image correspondants
john_image_paths = ["john1.jpg", "john2.jpg","john50.jpg"]
marie_image_paths = ["marie1.jpg", "marie2.jpg","marie50.jpg"]
paul_image_paths = ["paul1.jpg", "paul2.jpg","paul50.jpg"]

# Charger les images et les encodages de visage correspondants
john_images = [face_recognition.load_image_file(path) for path in john_image_paths]
john_encodings = [face_recognition.face_encodings(image)[0] for image in john_images]
marie_images = [face_recognition.load_image_file(path) for path in marie_image_paths]
marie_encodings = [face_recognition.face_encodings(image)[0] for image in marie_images]
paul_images = [face_recognition.load_image_file(path) for path in paul_image_paths]
paul_encodings = [face_recognition.face_encodings(image)[0] for image in paul_images]

# Fonction pour sélectionner l'image à comparer
def select_image():
    # Ouvrir une boîte de dialogue pour sélectionner l'image
    file_path = filedialog.askopenfilename()
    # Charger l'image sélectionnée et l'encodage de visage correspondant
    image = face_recognition.load_image_file(file_path)
    encoding = face_recognition.face_encodings(image)[0]
    # Calculer les distances de l'image sélectionnée par rapport à chaque encodage de visage connu
    john_distances = face_recognition.face_distance(john_encodings, encoding)
    marie_distances = face_recognition.face_distance(marie_encodings, encoding)
    paul_distances = face_recognition.face_distance(paul_encodings, encoding)
    # Trouver le nom de la personne dont l'encodage de visage correspond le mieux à l'image sélectionnée
    min_distance = min(john_distances.min(), marie_distances.min(), paul_distances.min())
    if min_distance == john_distances.min():
        result_label.config(text="Tu ressembles le plus à John!", fg="green")
    elif min_distance == marie_distances.min():
        result_label.config(text="Tu ressembles le plus à Marie!", fg="green")
    elif min_distance == paul_distances.min():
        result_label.config(text="Tu ressembles le plus à Paul!", fg="green")
    image_label.config(image=tk.PhotoImage(file=file_path))
    image_label.image = tk.PhotoImage(file=file_path)

# Créer une fenêtre avec un bouton pour sélectionner l'image et un label pour afficher le résultat
window = tk.Tk()
window.title("Reconnaissance faciale")
window.geometry("800x600")
window.configure(bg="white")

header_label = tk.Label(window, text="Reconnaissance faciale", font=("Arial", 24), bg="white", pady=20)
header_label.pack()

select_button = tk.Button(window, text="Sélectionner une image", font=("Arial", 14), command=select_image, bg="gray", fg="white", pady=10)
select_button.pack(pady=20)

image_label = tk.Label(window, bg="white")
image_label.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 18), bg="white")
result_label.pack()

window.mainloop()