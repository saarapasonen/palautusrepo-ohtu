import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
from ostoskori import Ostoskori

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

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

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

##uusi tehtävän 4 testi
    def test_aloita_asiointi_nollaa_ostokset(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        
        hinta1 = self.kauppa._ostoskori.hinta()
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        
        hinta2 = self.kauppa._ostoskori.hinta()
        
        self.assertNotEqual(hinta1, hinta2)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
       
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_ostoksen_jarjestys_ja_oikeat_parametrit(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
       
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
    
    def test_ostokset_kaksi_eri_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)
    
    def test_ostokset_kaksi_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)
    
    def test_ostokset_varastossa_on_ja_ei_on_tuote(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

##uusi tehtävän 4 testi viitenumeroille
    def test_uusi_viitenumero_jokaiselle_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.viitegeneraattori_mock.uusi.assert_called_once()
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.viitegeneraattori_mock.uusi.assert_called_with()
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)


####################

    def test_poista_korista(self):
        # Aloitetaan asiointi ja lisätään tuote koriin
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        
        # Varmistetaan, että ostoskorissa on tuote
        self.assertEqual(len(self.kauppa._ostoskori._tuotteet), 1)

        # Poistetaan tuote korista
        self.kauppa.poista_korista(1)
        
        # Varmistetaan, että ostoskorissa ei ole tuotetta
        self.assertEqual(len(self.kauppa._ostoskori._tuotteet), 0)
        
        # Varmistetaan, että varastoon palautetaan oikea tuote
        self.varasto_mock.palauta_varastoon.assert_called_once_with(Tuote(1, "maito", 5))


