import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # Viitegeneraattori palauttaa aina 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5
            return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "leipä", 3)
            return None

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # Alustetaan Kauppa-olio mockeilla
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # Aloitetaan asiointi ja lisätään tuote koriin
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        
        # Suoritetaan maksaminen
        self.kauppa.tilimaksu("pekka", "12345")
        
        # Varmistetaan, että pankin metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_ostoksen_jarjestys_ja_oikeat_parametrit(self):
        # Aloitetaan asiointi ja lisätään tuote koriin
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        
        # Suoritetaan maksaminen
        self.kauppa.tilimaksu("pekka", "12345")
        
        # Varmistetaan, että pankin metodia tilisiirto kutsutaan oikeilla arvoilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
    
    def test_ostokset_kaksi_eri_tuotetta(self):
        # Aloitetaan asiointi ja lisätään kaksi eri tuotetta koriin
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        
        # Suoritetaan maksaminen
        self.kauppa.tilimaksu("pekka", "12345")
        
        # Varmistetaan, että pankin metodia tilisiirto kutsutaan oikeilla arvoilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)
    
    def test_ostokset_kaksi_samaa_tuotetta(self):
        # Aloitetaan asiointi ja lisätään kaksi samaa tuotetta koriin
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        
        # Suoritetaan maksaminen
        self.kauppa.tilimaksu("pekka", "12345")
        
        # Varmistetaan, että pankin metodia tilisiirto kutsutaan oikeilla arvoilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)
    
    def test_ostokset_varastossa_on_ja_ei_on_tuote(self):
        # Aloitetaan asiointi ja lisätään tuote, jota on varastossa tarpeeksi ja tuote, joka on loppu
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        
        # Suoritetaan maksaminen
        self.kauppa.tilimaksu("pekka", "12345")
        
        # Varmistetaan, että pankin metodia tilisiirto kutsutaan oikeilla arvoilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)