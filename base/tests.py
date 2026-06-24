from django.test import SimpleTestCase

class BasicTests(SimpleTestCase):
    
    def test_suma_basica(self):
        self.assertEqual(1 + 1, 2)
    
    def test_string(self):
        self.assertEqual("django".upper(), "DJANGO")
    
    def test_lista(self):
        lista = [1, 2, 3]
        self.assertIn(2, lista)