#coding:utf-8

########################################################
# JEUX DE SIMULATION D'HACKING CODE PAR N30-Geek
#  		Game version : V1.0 in python 10
#  Githab : https://www.github.com/N30-Geek.git
#=====================================================
#
# Licence : GNU Lunix : opensource :
# Vous pouvez modifier les codes a votre manière 
# et publier la version modifier, en indiquant l'auteur 
# principal du jeux


import tkinter as tk

root = tk.Tk()

name = "Je suis geek"
label = tk.Label(root, text=name)
label.grid(column=2, row =0)
entrer = tk.Entry(root)

botton = tk.Button(root, text="close").grid(column = 0, row =1)
root.mainloop()
