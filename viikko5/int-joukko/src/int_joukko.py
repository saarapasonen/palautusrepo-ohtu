KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self._tarkista_arvo(kapasiteetti, KAPASITEETTI)
        self.kasvatuskoko = self._tarkista_arvo(kasvatuskoko, OLETUSKASVATUS)

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    @staticmethod
    def _tarkista_arvo(arvo, oletusarvo):
        if arvo is None:
            return oletusarvo
        if not isinstance(arvo, int) or arvo < 0:
            raise ValueError("Virheellinen arvo")
        return arvo

    def kuuluu(self, luku):
        return luku in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False

        if self.alkioiden_lkm == len(self.ljono):
            self._kasvata_listaa()

        self.ljono[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1
        return True

    def _kasvata_listaa(self):
        uusi_koko = len(self.ljono) + self.kasvatuskoko
        uusi_lista = self._luo_lista(uusi_koko)
        self._kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista

    def poista(self, luku):
        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == luku:
                self._siirra_vasemmalle(i)
                self.alkioiden_lkm -= 1
                return True
        return False

    def _siirra_vasemmalle(self, indeksi):
        for i in range(indeksi, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0

    def _kopioi_lista(self, lähde, kohde):
        for i in range(len(lähde)):
            kohde[i] = lähde[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            tulos.lisaa(luku)
        for luku in b.to_int_list():
            tulos.lisaa(luku)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            if b.kuuluu(luku):
                tulos.lisaa(luku)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            if not b.kuuluu(luku):
                tulos.lisaa(luku)
        return tulos

    def __str__(self):
        sisalto = ", ".join(map(str, self.ljono[:self.alkioiden_lkm]))
        return f"{{{sisalto}}}"