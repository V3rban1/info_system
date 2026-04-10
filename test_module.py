import unittest
from unittest.mock import patch
from io import StringIO

# Импорт программного модуля из файла
from upd_pz4 import program_module


class TestMainLogic(unittest.TestCase):

    def test_string_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            program_module('gugu_gaga')
            self.assertEqual(fake_out.getvalue().strip(), 'Ваш запрос содержит только строку.')

    def test_integer_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            program_module('1415')
            self.assertEqual(fake_out.getvalue().strip(), 'Вы ввели число: 1415')

    def test_float_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            program_module('3256.264')
            self.assertEqual(fake_out.getvalue().strip(), 'Ваш запрос содержит только строку.')

    def test_web_resource(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            program_module('https://mail.ru')
            self.assertEqual(fake_out.getvalue().strip(), 'Ваш запрос похож на веб-ресурс.')


if __name__ == '__main__':
    unittest.main()