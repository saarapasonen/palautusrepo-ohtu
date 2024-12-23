from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()

        try:
            arvo = int(self._lue_syote())
        except ValueError:
            arvo = 0
        self._sovelluslogiikka.plus(arvo)
    
    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)


class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()

        try:
            arvo = int(self._lue_syote())
        except ValueError:
            arvo = 0
        self._sovelluslogiikka.miinus(arvo)


class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()

        self._sovelluslogiikka.nollaa()
    
    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)


class Kumoa:
    def __init__(self, sovelluslogiikka, viimeisin_komento):
        self._sovelluslogiikka = sovelluslogiikka
        self._viimeisin_komento = viimeisin_komento

    def suorita(self):
        if self._viimeisin_komento[0] is not None:
            self._viimeisin_komento[0].kumoa()
            self._viimeisin_komento[0] = None




class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._viimeisin_komento = [None]

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._viimeisin_komento),
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]

        if komento != Komento.KUMOA:
            komento_olio.suorita()
            self._viimeisin_komento[0] = komento_olio
            self._kumoa_painike["state"] = constants.NORMAL
        else:
            komento_olio.suorita()
            self._kumoa_painike["state"] = constants.DISABLED

        self._nollaus_painike["state"] = (constants.DISABLED if self._sovelluslogiikka.arvo() == 0 else constants.NORMAL)

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

