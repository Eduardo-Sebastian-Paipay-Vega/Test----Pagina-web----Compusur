from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import project
from export_policy import validate_export

class ExportContractTests(unittest.TestCase):
    def test_valid_static_block(self):
        validate_export('<section class="cs-site"><a href="/shop">Tienda</a></section>',
                        '@media (max-width:600px){.cs-site h2{color:blue}}', [])

    def test_rejects_runtime_and_nonportable_paths(self):
        for content in ('<script>fetch("/api")</script>', '<div onclick="buy()">Comprar</div>',
                        '<form action="/checkout"></form>', '<a href="//cdn.example.com">X</a>',
                        '<img alt="Equipo" src="C:\\imagenes\\equipo.png">',
                        '<div t-foreach="products"></div>'):
            with self.subTest(content=content), self.assertRaises(ValueError):
                validate_export(content, '.cs-site{color:blue}', [])

    def test_rejects_global_css_and_external_dependencies(self):
        for css in ('body{color:red}', '.cs-site-other{color:red}',
                    '@import "https://example.com/a.css";',
                    '.cs-site{background:url(https://example.com/image.png)}'):
            with self.subTest(css=css), self.assertRaises(ValueError):
                validate_export('<section class="cs-site"></section>', css, [])

    def test_rejects_missing_image(self):
        with self.assertRaisesRegex(ValueError, 'Recursos sin archivo'):
            validate_export('<img alt="Equipo" src="assets/media/equipo.webp">', '.cs-site{color:blue}', [])

    def test_rejects_server_and_framework_files(self):
        for filename in ('server.py', 'App.jsx', 'config.env', 'bundle.js'):
            with self.subTest(filename=filename), self.assertRaises(ValueError):
                validate_export('<section></section>', '.cs-site{color:blue}', [(Path(filename), Path(filename))])

    def test_invalid_export_preserves_previous_package(self):
        with tempfile.TemporaryDirectory(prefix='compusur-export-test-') as directory:
            test_root = Path(directory).resolve()
            previous = test_root / 'dist/compusur-diseno-borrador.zip'
            previous.parent.mkdir()
            previous.write_bytes(b'previous-package')
            original_read = project.read
            def read_with_script(path):
                text = original_read(path)
                return text + '<script>run()</script>' if path == 'blocks/inicio.html' else text
            with patch.object(project, 'ROOT', test_root), patch.object(project, 'read', side_effect=read_with_script):
                with self.assertRaises(ValueError):
                    project.export_odoo()
            self.assertEqual(previous.read_bytes(), b'previous-package')
            self.assertFalse((test_root/'dist/odoo/inicio.fragment.html').exists())

if __name__ == '__main__':
    unittest.main()
