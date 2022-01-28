import unittest
import os

from ioc_html2pdf import parse_document


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can parse a simple file
        """
        with open("testFile.html", "w") as fp:
            fp.write("""
<!DOCTYPE html>
<html lang='en'>
    <head>
        <meta charset='utf-8'>
        <title>Test</title>
    </head>
    <body>
        <div>
            <p>hello!</p>
            <p><b>bye!</b></p>
        </div>
    </body>
</html>""");
        result = parse_document(["", "testFile.html"])
        self.assertEqual(result, True)

    def test_list_fraction(self):
        """
        Test that it fails on entering a non existant filename
        """
        result = parse_document(["","nonexistingFile"])
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
