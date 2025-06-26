import unittest
from backend.services.scraper import BibliotecaScraper
from backend.config import Config

class TestBibliotecaScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = BibliotecaScraper()
        self.scraper.iniciar_sesion()

    def test_buscar_libro_mcGraw(self):
        referencia = "anatomía"
        categoria = "Ciencias Médicas"  # esta categoría debe contener McGraw Hill Access Medicine

        resultado = self.scraper.buscar_libro(referencia, categoria)

        self.assertIsInstance(resultado, dict)
        self.assertIn("encontrado", resultado)
        self.assertIn("fuente", resultado)
        self.assertIn("url", resultado)
        print("Resultado:", resultado)

    def tearDown(self):
        self.scraper.cerrar()

if __name__ == "__main__":
    unittest.main()