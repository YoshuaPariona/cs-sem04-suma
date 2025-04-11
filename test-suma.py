import unittest
from suma import Suma

class MyTestCase(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 20

        resultadoEsperado = 30

        objSuma = Suma(operando1, operando2)

        # Act

        resultadoActual = objSuma.calcularSuma()

        # Assert

        self.assertEqual(resultadoEsperado, resultadoActual, "Falló la suma")


    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = Suma(7, "r")
        with self.assertRaises(ValueError):
            objSuma.calcularSuma()

if __name__ == '__main__':
    unittest.main()

