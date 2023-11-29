import shutil, os, random

nombre = len(os.listdir('./'))

# Afficher le dossier bryaned
for i in range (1,nombre+1):  
    nom = "bryan" + str(i)   
    if len(os.listdir('./'+ nom)) != 0:
        print(nom)
    else:
        os.remove("./"+nom)