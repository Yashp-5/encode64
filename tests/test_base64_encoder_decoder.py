
import sys
from unittest.mock import MagicMock

# Mock tkinter if it's not available
sys.modules['tkinter'] = MagicMock()
sys.modules['tkinter.messagebox'] = MagicMock()
sys.modules['tkinter.filedialog'] = MagicMock()

import unittest
from unittest.mock import MagicMock
from encodeIT import Base64EncoderDecoderApp  # Adjust this import to match your module name

class TestBase64EncoderDecoder(unittest.TestCase):

    def setUp(self):
        # Mock the Tkinter root window
        mock_root = MagicMock()
        self.app = Base64EncoderDecoderApp(mock_root)

    def test_encode_json_to_base64(self):
        json_data = {"key": "value"}
        result = self.app.encode_json_to_base64(json_data)
        self.assertEqual(result, "eyJrZXkiOiAidmFsdWUifQ==")

    def test_decode_base64_to_json(self):
        base64_data = "eyJrZXkiOiAidmFsdWUifQ=="
        result = self.app.decode_base64_to_json(base64_data)
        self.assertEqual(result, {"key": "value"})

if __name__ == "__main__":
    unittest.main()

