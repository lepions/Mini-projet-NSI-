from tkinter import *     #permet d'importer toutes les fonctionnalitée relatives a tkinter
import tkinter
import tkinter as tk

def encodage():
    phrase=entry_phrase.get()   #la variariable phrase est initiaisée a ce qui a été tapé dans la barre1  l'aide de la foncion get
    decalage=int(entry_decalage.get())  #la variariable decalage est initiaisée a ce qui a été tapé dans la barre2  l'aide de la foncion get puis le convertit en nombre enter avec int
    liste=""    #la variariable phrase est initiaisée 
    for i in phrase: #boucle for qui prends en parametre la phrase
        liste+=str(chr(ord(i)+decalage))    #on transforme i en son nombre de la table ascii avec ord, on lui ajoute le decalage puis on reconvertit en cracteres a l'aide de la fonction chr, on l'ajoute ensuite a la liste
    Label(text="Votre phrase est:").pack()  #fonction label qui permet d'afficher du texte
    Label(text=liste).pack()    #fonction label qui permet d'afficher liste
    return liste 
    
def decodage():
    phrase=entry_phrase.get()   #la variariable phrase est initiaisée a ce qui a été tapé dans la barre1  l'aide de la foncion get
    decalage=int(entry_decalage.get())  #la variariable decalage est initiaisée a ce qui a été tapé dans la barre2  l'aide de la foncion get puis le convertit en nombre enter avec int
    liste=""    #la variariable phrase est initiaisée 
    for i in phrase:    #boucle for qui prends en parametre la phrase
        liste+=str(chr(ord(i)-decalage))     #on transforme i en son nombre de la table ascii avec ord, on lui soustrait le decalage puis on reconvertit en cracteres a l'aide de la fonction chr, on l'ajoute ensuite a la liste
    Label(text="Votre phrase est:").pack()
    Label(text=liste).pack()    #fonction label qui permet d'afficher du texte
    return liste    #fonction label qui permet d'afficher liste
    
    
fenetre = tkinter.Tk()  #debut de ce qu'il y a dans la fenetre
fenetre.title("encodage/decodage")  #permet de donner un titre a la fenetre
fenetre.configure(background='blue')    #permet de mettre un fond de couleur
fenetre.geometry('300x400')   #definit la taille de la fenetre

Label(text='Donnez la phrase a encoder ou a decoder :').pack(pady = 20)  #fonction label qui permet d'afficher du texte
entry_phrase = Entry()    #barre d'entrée crée avec la fonction entry, elle permet d'entrer la phrase a encoder ou decoder
entry_phrase.pack()   #nessesaire a l'affichage de la barre d'entée

Label(text='Donnez le decalage :').pack(pady = 20)   #fonction label qui permet d'afficher du texte
entry_decalage = Entry()    #barre d'entrée crée avec la fonction entry, elle permet d'entrer le decalage
entry_decalage.pack()   #nessesaire a l'affichage de la barre d'entée

Label(text='Que voulez vous faire ?').pack(pady = 20)    #fonction label qui permet d'afficher du texte
bouton1 = tkinter.Button(fenetre, text ="Encodage",command=encodage)    #definit le premier bouton, son texte sera "encodage" et lorqu'il sera pressé il lancera la fonction encodage définie precedement
bouton1.pack()   #nessesaire a l'affichage du bouton1
bouton2 = tkinter.Button(fenetre, text ="Decodage",command=decodage)    #definit le deuxieme bouton, son texte sera "decodage" et lorqu'il sera pressé il lancera la fonction decodage définie precedement
bouton2.pack()  #nessesaire a l'affichage du bouton1

retour = Button(text='Retour', command=quit)  #definit bouton de retour en cas d'erreur, son texte sera "retour" et lorqu'il sera pressé il lancera la fonction quit qui ermet de fermer la page
retour.pack(pady = 20) #nessesaire a l'affichage du bouton retour

fenetre.mainloop()  #permet de fermer la fenetre