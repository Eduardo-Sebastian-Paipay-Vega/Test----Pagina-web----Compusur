from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from odoo_images_mcp import image_path, upload

class ImageScopeTests(unittest.TestCase):
    def test_private_fixture_allowed(self):
        path=image_path('tests/fixtures/odoo-image-test.png')
        self.assertEqual(path.suffix,'.png')

    def test_fixture_cannot_be_public(self):
        with self.assertRaises(ValueError):image_path('tests/fixtures/odoo-image-test.png',True)

    def test_files_outside_design_assets_rejected(self):
        with self.assertRaises(ValueError):image_path('README.md')

    def test_no_arbitrary_model_or_operation(self):
        with self.assertRaises(ValueError):upload({'file':'tests/fixtures/odoo-image-test.png','model':'res.partner'})

if __name__=='__main__':unittest.main()
