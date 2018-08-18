from tkinter import *
import numpy as np

class Jogo:
    def playerClickB1(self):
        self.b1["image"] = self.imagem1
        self.b1["width"] = 93
        self.b1["height"] = 75
        self.matrix[0][0] = 1
        self.b1["text"] = self.matrix[0][0]
        
    def playerClickB2(self):
        self.b2["image"] = self.imagem1
        self.b2["width"] = 90
        self.b2["height"] = 75
        self.matrix[1][0] = 1
        self.b2["text"] = self.matrix[1][0]
        
    def playerClickB3(self):
        self.b3["image"] = self.imagem1
        self.b3["width"] = 90
        self.b3["height"] = 75
        self.matrix[2][0] = 1
        self.b3["text"] = self.matrix[2][0]

    def playerClickB4(self):
        self.b4["image"] = self.imagem1
        self.b4["width"] = 90
        self.b4["height"] = 75
        self.matrix[3][0] = 1
        self.b4["text"] = self.matrix[3][0]    


    def __init__(self, master=None):
        self.imagem1 = PhotoImage(file="bola.png")
        #global scope
        self.total = Frame(master)
        self.total["pady"] = 50
        self.total.pack()
        # 0 = valor padrao vazio
        # 1 = player click
        # 2 = ia click
        self.matrix = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
            ]
        #função de click do player
        
        #rows
        self.row1 = Frame(self.total)
        self.row1["pady"] = 0
        self.row1.pack()

        self.row2 = Frame(self.total)
        self.row2["pady"] = 0
        self.row2.pack()

        self.row3 = Frame(self.total)
        self.row3["pady"] = 0
        self.row3.pack()

        self.row4 = Frame(self.total)
        self.row4["pady"] = 0
        self.row4.pack()
        #buttons
        self.b1 = Button(self.row1)
        self.b1["font"] = ("Calibri", "9")
        self.b1["width"] = 10
        self.b1["height"] = 5
        self.b1["command"] = self.playerClickB1 
        self.b1["text"] = self.matrix[0][0]
        self.b1.pack(side=LEFT)

        self.b2 = Button(self.row1)
        self.b2["font"] = ("Calibri", "9")
        self.b2["width"] = 10
        self.b2["height"] = 5
        self.b2["command"] = self.playerClickB2
        self.b2["text"] = self.matrix[1][0]
        self.b2.pack (side=LEFT)

        self.b3 = Button(self.row1)
        self.b3["font"] = ("Calibri", "9")
        self.b3["width"] = 10
        self.b3["height"] = 5
        self.b3["command"] = self.playerClickB3
        self.b3["text"] = self.matrix[2][0]
        self.b3.pack (side=LEFT)

        self.b4 = Button(self.row1)
        self.b4["font"] = ("Calibri", "10")
        self.b4["width"] = 10
        self.b4["height"] = 5
        self.b4["command"] = self.playerClickB4
        self.b4["text"] = self.matrix[3][0]
        self.b4.pack (side=LEFT)
    
        self.b5 = Button(self.row2)
        self.b5["font"] = ("Calibri", "9")
        self.b5["width"] = 10
        self.b5["height"] = 5
        self.b5.pack(side=LEFT)

        self.b6 = Button(self.row2)
        self.b6["font"] = ("Calibri", "9")
        self.b6["width"] = 10
        self.b6["height"] = 5
        self.b6.pack(side=LEFT)

        self.b7 = Button(self.row2)
        self.b7["font"] = ("Calibri", "9")
        self.b7["width"] = 10
        self.b7["height"] = 5
        self.b7.pack(side=LEFT)

        self.b8 = Button(self.row2)
        self.b8["font"] = ("Calibri", "9")
        self.b8["width"] = 10
        self.b8["height"] = 5
        self.b8.pack(side=LEFT)

        self.b9 = Button(self.row3)
        self.b9["font"] = ("Calibri", "9")
        self.b9["width"] = 10
        self.b9["height"] = 5
        self.b9.pack(side=LEFT)

        self.b10 = Button(self.row3)
        self.b10["font"] = ("Calibri", "9")
        self.b10["width"] = 10
        self.b10["height"] = 5
        self.b10.pack(side=LEFT)

        self.b11 = Button(self.row3)
        self.b11["font"] = ("Calibri", "9")
        self.b11["width"] = 10
        self.b11["height"] = 5
        self.b11.pack(side=LEFT)

        self.b12 = Button(self.row3)
        self.b12["font"] = ("Calibri", "9")
        self.b12["width"] = 10
        self.b12["height"] = 5
        self.b12.pack(side=LEFT)

        self.b13 = Button(self.row4)
        self.b13["font"] = ("Calibri", "9")
        self.b13["width"] = 10
        self.b13["height"] = 5
        self.b13.pack(side=LEFT)

        self.b14 = Button(self.row4)
        self.b14["font"] = ("Calibri", "9")
        self.b14["width"] = 10
        self.b14["height"] = 5
        self.b14.pack(side=LEFT)

        self.b15 = Button(self.row4)
        self.b15["font"] = ("Calibri", "9")
        self.b15["width"] = 10
        self.b15["height"] = 5
        self.b15.pack(side=LEFT)

        self.b16 = Button(self.row4)
        self.b16["font"] = ("Calibri", "9")
        self.b16["width"] = 10
        self.b16["height"] = 5
        self.b16.pack(side=LEFT)


root = Tk()
root.title("Jogo da Velha")
root.geometry("500x500")
Jogo(root)
root.mainloop()