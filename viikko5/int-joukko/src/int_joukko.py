KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  
        self.kapasiteetti = kapasiteetti

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kasvatuskoko")  
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.lukujono

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            if self.alkioiden_lkm >= len(self.lukujono):
                self.kasvata_kapasiteettia()
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1
            return True
        return False

    def kasvata_kapasiteettia(self):
        uusi_lukujono = self._luo_lista(len(self.lukujono) + self.kasvatuskoko)
        self.kopioi_lista(self.lukujono, uusi_lukujono)
        self.lukujono = uusi_lukujono
    
    def etsi_indeksi(self, luku):
        for indeksi in range(self.alkioiden_lkm):
            if self.lukujono[indeksi] == luku:
                return indeksi
        return -1

    def poista(self, luku):
        kohta = self.etsi_indeksi(luku)
        if kohta != -1:
            for indeksi in range(kohta, self.alkioiden_lkm - 1):
                self.lukujono[indeksi] = self.lukujono[indeksi + 1]
            self.lukujono[self.alkioiden_lkm - 1] = 0
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self): #poimi alkiot
        return self.lukujono[:self.alkioiden_lkm]

    def kopioi_lista(self, lista1, lista2):
        for i in range(len(lista1)):
            lista2[i] = lista1[i]

    @staticmethod
    def yhdiste(joukko1, joukko2):
        yhdiste_joukko = IntJoukko()
        for luku in joukko1.to_int_list():
            yhdiste_joukko.lisaa(luku)
        for luku in joukko2.to_int_list():
            yhdiste_joukko.lisaa(luku)
        return yhdiste_joukko

    @staticmethod
    def leikkaus(joukko1, joukko2):
        leikkaus_joukko = IntJoukko()
        lista1 = set(joukko1.to_int_list())
        lista2 = set(joukko2.to_int_list())
        intersection = lista1 & lista2
        for luku in intersection:
            leikkaus_joukko.lisaa(luku)
        return leikkaus_joukko

    @staticmethod
    def erotus(joukko1, joukko2):
        erotus_joukko = IntJoukko()
        for luku in joukko1.to_int_list():
            if not joukko2.kuuluu(luku):
                erotus_joukko.lisaa(luku)
        return erotus_joukko

    def __str__(self):
        return "{" + ", ".join(str(self.lukujono[i]) for i in range(self.alkioiden_lkm)) + "}"