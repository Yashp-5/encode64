import unittest
from encodeIT import Base64EncoderDecoderApp  # Adjust this import based on your actual module name

class TestBase64EncoderDecoder(unittest.TestCase):

    def setUp(self):
        # Create a root window and instance of the app
        self.app = Base64EncoderDecoderApp(None)  # Pass None or a mock root if running headless

    def test_encode_json_to_base64(self):
        # Test data
        json_data = {"key": "value", "number": 123}
        expected_base64 = 'eyJrZXkiOiAidmFsdWUiLCAibnVtYmVyIjogMTIzfQ=='  # This is the Base64 encoded version of the JSON string

        # Test encoding
        result = self.app.encode_json_to_base64(json_data)
        self.assertEqual(result, expected_base64)

    def test_decode_base64_to_json(self):
        # Test data
        base64_data = 'eyJrZXkiOiAidmFsdWUiLCAibnVtYmVyIjogMTIzfQ=='
        expected_json = {"key": "value", "number": 123}

        # Test decoding
        result = self.app.decode_base64_to_json(base64_data)
        self.assertEqual(result, expected_json)

if __name__ == '__main__':
    unittest.main()
