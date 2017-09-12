import tkinter as tk
import random

from tkinter import mainloop

class Barve():
    def __init__(self, okno):

        self.kombinacija_1 = tk.Label(okno, text='prva kombinacija')
        self.kombinacija_1.grid(row=6, column=0)
        self.kombinacija_2 = tk.Label(okno, text='druga kombinacija')
        self.kombinacija_2.grid(row=7, column=0)
        self.kombinacija_3 = tk.Label(okno, text='tretja kombinacija')
        self.kombinacija_3.grid(row=8, column=0)
        self.kombinacija_4 = tk.Label(okno, text='cetrta kombinacija')
        self.kombinacija_4.grid(row=9, column=0)
        self.kombinacija_5 = tk.Label(okno, text='peta kombinacija')
        self.kombinacija_5.grid(row=10, column=0)
        self.kombinacija_6 = tk.Label(okno, text='sesta kombinacija')
        self.kombinacija_6.grid(row=11, column=0)

        self.navodilo = tk.Label(okno, text='Izberi prvo kombinacijo:')
        self.navodilo.grid(row=4, column=1)
        self.niz = ''
        self.niz_random = ''
        self.stevec = 1
        self.izvedi = ''
        self.pozicija = ''
        self.barva = ''

        oznaka = tk.Label(okno, text='Igra memo', fg='black').grid(row=0, column=1)
        navodila = tk.Label(okno, text='Računalnik naključno določi kombinacijo štirih barv od šestih.\n Poskusi ugotoviti to kombinacijo. Na voljo imaš 6 poizkusov.\n Za pričetek klikni gumb Začni ter klini na 4 barve za vsako kombinacjo. Srečno!', fg='blue').grid(row=2, columnspan=4)
        gumb_oranzna = tk.Button(okno, bg='orange', command=self.oranzna).grid(row=5, column=3)
        gumb_rdeca = tk.Button(okno, bg='red', command=self.rdeca).grid(row=6, column=3)
        gumb_zelena = tk.Button(okno, bg='green', command=self.zelena).grid(row=7, column=3)
        gumb_rumena = tk.Button(okno, bg='violet', command=self.vijolicna).grid(row=8, column=3)
        gumb_turkizna = tk.Button(okno, bg='turquoise', command=self.turkizna).grid(row=9, column=3)
        gumb_modra = tk.Button(okno, bg='blue', command=self.modra).grid(row=10, column=3)
        gumb_zacni = tk.Button(okno, text='Začni', command=self.random_kombinacija).grid(row=12, column=2)
        pravo_mesto = tk.Label(okno, text='je na pravem mestu').grid(row=5, column=1)
        pravilna_barva =tk.Label(okno, text='prava barba, napačno mesto').grid(row=5, column=2)

        self.pravilno_postavljene_1 = tk.Label(okno, text='')
        self.prava_barva_1 = tk.Label(okno, text='')
        self.pravilno_postavljene_2 = tk.Label(okno, text='')
        self.prava_barva_2 = tk.Label(okno, text='')
        self.pravilno_postavljene_3 = tk.Label(okno, text='')
        self.prava_barva_3 = tk.Label(okno, text='')
        self.pravilno_postavljene_4 = tk.Label(okno, text='')
        self.prava_barva_4 = tk.Label(okno, text='')
        self.pravilno_postavljene_5 = tk.Label(okno, text='')
        self.prava_barva_5 = tk.Label(okno, text='')
        self.pravilno_postavljene_6 = tk.Label(okno, text='')
        self.prava_barva_6 = tk.Label(okno, text='')
        self.pravilno_postavljene_1.grid(row=6, column=1)
        self.prava_barva_1.grid(row=6, column=2)
        self.pravilno_postavljene_2.grid(row=7, column=1)
        self.prava_barva_2.grid(row=7, column=2)
        self.pravilno_postavljene_3.grid(row=8, column=1)
        self.prava_barva_3.grid(row=8, column=2)
        self.pravilno_postavljene_4.grid(row=9, column=1)
        self.prava_barva_4.grid(row=9, column=2)
        self.pravilno_postavljene_5.grid(row=10, column=1)
        self.prava_barva_5.grid(row=10, column=2)
        self.pravilno_postavljene_6.grid(row=11, column=1)
        self.prava_barva_6.grid(row=11, column=2)

    def prva_kombinacija(self):
        self.kombinacija_1.configure(text=self.niz)
        self.navodilo.configure(text='Izberi naslednjo kombinacijo')

    def druga_kombinacija(self):
        self.kombinacija_2.configure(text=self.niz)

    def tretja_kombinacija(self):
        self.kombinacija_3.configure(text=self.niz)

    def cetrta_kombinacija(self):
        self.kombinacija_4.configure(text=self.niz)

    def peta_kombinacija(self):
        self.kombinacija_5.configure(text=self.niz)

    def sesta_kombinacija(self):
        self.kombinacija_6.configure(text=self.niz)
        self.navodilo.configure(text='konec igre')


    def random_kombinacija(self):
        for _ in range(4):
            self.niz_random += random.choice(['O', 'R', 'Z', 'V', 'T', 'M'])

    def primerjaj(self):
        pravilno_postavljena = 0
        pravilna_barva = 0
        for i in range(0, 4):
            if self.niz == self.niz_random:
                self.navodilo.configure(text='ZMAGAL SI!')
            elif self.niz[i] == self.niz_random[i]:
                pravilno_postavljena += 1
            elif self.niz[i] in self.niz_random:
                pravilna_barva += 1
        if self.stevec == 1:
            self.pozicija = self.pravilno_postavljene_1.configure(text=pravilno_postavljena)
            self.barva = self.prava_barva_1.configure(text=pravilna_barva)
        elif self.stevec == 2:
            self.pozicija = self.pravilno_postavljene_2.configure(text=pravilno_postavljena)
            self.barva = self.prava_barva_2.configure(text=pravilna_barva)
        elif self.stevec == 3:
            self.pozicija = self.pravilno_postavljene_3.configure(text=pravilno_postavljena)
            self.barva = self.prava_barva_3.configure(text=pravilna_barva)
        elif self.stevec == 4:
            self.pozicija = self.pravilno_postavljene_4.configure(text=pravilno_postavljena)
            self.barva = self.prava_barva_4.configure(text=pravilna_barva)
        elif self.stevec == 5:
            self.pozicija = self.pravilno_postavljene_5.configure(text=pravilno_postavljena)
            self.barva = self.prava_barva_5.configure(text=pravilna_barva)
        elif self.stevec == 6:
            self.pozicija = self.pravilno_postavljene_6.configure(text=pravilno_postavljena)
            self.barva = self.prava_barva_6.configure(text=pravilna_barva)
        self.niz = ''

    def vrstice(self):
        if self.stevec == 1:
            self.izvedi = self.prva_kombinacija()
        elif self.stevec == 2:
            self.izvedi = self.druga_kombinacija()
        elif self.stevec == 3:
            self.izvedi = self.tretja_kombinacija()
        elif self.stevec == 4:
            self.izvedi = self.cetrta_kombinacija()
        elif self.stevec == 5:
            self.izvedi = self.peta_kombinacija()
        elif self.stevec == 6:
            self.izvedi = self.sesta_kombinacija()


    def oranzna(self):
        self.niz += 'O'
        if len(self.niz) == 4:
            self.vrstice()
            self.primerjaj()
            self.stevec += 1
    def rdeca(self):
        self.niz += 'R'
        if len(self.niz) == 4:
            self.vrstice()
            self.primerjaj()
            self.stevec += 1
    def zelena(self):
        self.niz += 'Z'
        if len(self.niz) == 4:
            self.vrstice()
            self.primerjaj()
            self.stevec += 1
    def vijolicna(self):
        self.niz += 'V'
        if len(self.niz) == 4:
            self.vrstice()
            self.primerjaj()
            self.stevec += 1
    def turkizna(self):
        self.niz += 'T'
        if len(self.niz) == 4:
            self.vrstice()
            self.primerjaj()
            self.stevec += 1
    def modra(self):
        self.niz += 'M'
        if len(self.niz) == 4:
            self.vrstice()
            self.primerjaj()
            self.stevec += 1

okno = tk.Tk()
barve = Barve(okno)
mainloop()





