import unittest
from operaciones_aritmeticas import OperacionesAritmeticas

class MyTestCase(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 20

        resultadoEsperado = 30

        objSuma = OperacionesAritmeticas(operando1, operando2)

        # Act

        resultadoActual = objSuma.calcularSuma()

        # Assert

        self.assertEqual(resultadoEsperado, resultadoActual, "Falló la suma")


    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas(7, "a")
        with self.assertRaises(TypeError):
            objSuma.calcularSuma()

    def test_division_dosNumeros_retornaDivision(self):
        # Arrange
        dividendo1 = 100
        dividendo2 = 3

        resultadoEsperado = 33.333

        objSuma = OperacionesAritmeticas(dividendo1, dividendo2)

        # Act

        resultadoActual = objSuma.calcularDivision()

        # Assert

        self.assertAlmostEqual(resultadoEsperado, resultadoActual,3, "Falló la division")

    def test_division_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas(7, "a")
        with self.assertRaises(TypeError):
            objSuma.calcularDivision()

    def test_division_dividirEntreCero_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas(7, 0)
        with self.assertRaises(ZeroDivisionError):
            objSuma.calcularDivision()

if __name__ == '__main__':
    unittest.main()

