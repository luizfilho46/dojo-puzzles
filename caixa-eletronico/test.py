from app import CaixaEletronico
import unittest

class TestCaixaEletronico(unittest.TestCase):

    def test_caixa_eletronico_sacar_cem(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(100), [1, 0, 0, 0])
    def test_caixa_eletronico_sacar_cinquenta(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(50), [0, 1, 0, 0])
    def test_caixa_eletronico_sacar_vinte(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(20), [0, 0, 1, 0])
    def test_caixa_eletronico_sacar_dez(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(10), [0, 0, 0, 1])
    def test_caixa_eletronico_sacar_trinta(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(30), [0, 0, 1, 1])
    def test_caixa_eletronico_sacar_quarenta(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(40), [0, 0, 2, 0])
    def test_caixa_eletronico_sacar_noventa(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(90), [0, 1, 2, 0])
    def test_caixa_eletronico_sacar_setenta(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(70), [0, 1, 1, 0])
    def test_caixa_eletronico_sacar_sessenta(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(60), [0, 1, 0, 1])
    def test_caixa_eletronico_sacar_cento_e_trinta(self):
        caixa = CaixaEletronico()
        self.assertEqual(caixa.sacar(130), [1, 0, 1, 1])


if __name__ == '__main__':
    unittest.main()