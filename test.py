# coding:utf-8
import matplotlib.pyplot as plt
import os
import tkinter
import matplotlib as mpl

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')

# def player(*players):
#     print("There are : " + str(len(players)))
#     for player in players:
#         print(player)


# dico ={"nom" : "mike", "object" : {0:".", 1 : "." , 2: ".", 3 : "o"}}
# print(dico["object"][2])
# dico["chien"] = "c'est un animal intelligent"

# del dico["object"][0]

# ----------------- Pour énumérer les valeurs des valeurs ---------------
# for key, value in enumerate(dico.values()):
#     print(key, value)

# ------------- Pour avoir clé et valeur -------------------
# for k,v in dico.items():
#     print("clé --{}--   valeur --{}--".format(k , v))

app = tkinter.Tk()
app.title('my first programme')
app.mainloop()
