# import  json
# import base64
# import threading
# import tkinter as tk
# from tkinter import messagebox
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(message)s',handlers=[
#     logging.FileHandler("base64_encoder_decode.log"),
#     logging.StreamHandler()
# ])

# class Base64EncoderDecoderApp:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Base64 Encoder/Decoder")
#         self.root.geometry("1000x800")
#         self.create_widgets()
        
#     def create_widgets(self):
#         self.json_input_label=tk.Label(self.root, text="Enter JSON data:")
#         self.json_input_label.pack(pady=10)
#         self.json_input=tk.Text(self.root, height=10, width=60)
#         self.json_input.pack(pady=10)
        
#         self.base64_output_label= tk.Label(self.root, text="Base64 Output:")
#         self.base64_output_label.pack(pady=10)
#         self.base64_output=tk.Text(self.root, height=10, width=60)
#         self.base64_output.pack(pady=10)
        
#         self.encode_button = tk.Button(self.root, text="Encode to Base64", command=self.encode_json)
#         self.encode_button.pack(pady=10)

#         self.decode_button = tk.Button(self.root, text="Decode from Base64", command=self.decode_base64)
#         self.decode_button.pack(pady=10)

#         self.upload_button = tk.Button(self.root, text="Upload JSON File", command=self.upload_json_file)
#         self.upload_button.pack(pady=10)
        
#         self.status_label = tk.Label(self.root, text="", fg="red")
#         self.status_label.pack(pady=5)
#     def encode_json(self):
#         """Handles the encoding of JSON to Base64."""
#         try:
#             json_data = self.json_input.get("1.0", "end-1c")
#             if not json_data:
#                 self.show_error("Input is empty!")
#                 return

#             # Validate and parse the JSON
#             try:
#                 parsed_json = json.loads(json_data)
#             except json.JSONDecodeError:
#                 self.show_error("Invalid JSON data!")
#                 return

#             # Run the encoding in a separate thread
#             threading.Thread(target=self._encode_base64, args=(parsed_json,)).start()

#         except Exception as e:
#             logging.error(f"Error in encode_json: {e}")
#             self.show_error(f"Error during encoding: {str(e)}")

#     def _encode_base64(self, json_data):
#         """Encodes JSON to Base64 in a separate thread."""
#         try:
#             encoded_data = self.encode_json_to_base64(json_data)
#             self.update_output(encoded_data)
#         except Exception as e:
#             logging.error(f"Error during base64 encoding: {e}")
#             self.show_error(f"Error: {str(e)}")

#     def decode_base64(self):
#         """Handles decoding of Base64 to JSON."""
#         try:
#             base64_data = self.base64_output.get("1.0", "end-1c")
#             if not base64_data:
#                 self.show_error("Base64 input is empty!")
#                 return

#             # Run the decoding in a separate thread
#             threading.Thread(target=self._decode_base64, args=(base64_data,)).start()

#         except Exception as e:
#             logging.error(f"Error in decode_base64: {e}")
#             self.show_error(f"Error during decoding: {str(e)}")

#     def _decode_base64(self, base64_data):
#         """Decodes Base64 back to JSON in a separate thread."""
#         try:
#             decoded_json = self.decode_base64_to_json(base64_data)
#             self.update_output(json.dumps(decoded_json, indent=4))
#         except Exception as e:
#             logging.error(f"Error during base64 decoding: {e}")
#             self.show_error(f"Error: {str(e)}")

#     def update_output(self, data):
#         """Updates the output text box with the result."""
#         self.base64_output.delete("1.0", "end-1c")
#         self.base64_output.insert("1.0", data)

#     def encode_json_to_base64(self, json_data):
#         """Encodes a Python JSON object (dict) to a base64 string."""
#         json_str = json.dumps(json_data)
#         json_bytes = json_str.encode('utf-8')
#         base64_bytes = base64.b64encode(json_bytes)
#         return base64_bytes.decode('utf-8')

#     def decode_base64_to_json(self, base64_data):
#         """Decodes a base64 string to a Python JSON object."""
#         base64_bytes = base64.b64decode(base64_data)
#         json_str = base64_bytes.decode('utf-8')
#         return json.loads(json_str)

#     def show_error(self, message):
#         """Displays an error message in the status label."""
#         self.status_label.config(text=message, fg="red")
#         logging.error(message)


# # Main execution
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Base64EncoderDecoderApp(root)
#     root.mainloop()

    
import json
import base64
import threading
import tkinter as tk
from tkinter import messagebox, filedialog
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
    logging.FileHandler("base64_encoder_decoder.log"),
    logging.StreamHandler()
])

class Base64EncoderDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Base64 Encoder/Decoder")
        self.root.geometry("1000x800")

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Input text area for JSON data
        self.json_input_label = tk.Label(self.root, text="Enter JSON data:")
        self.json_input_label.pack(pady=10)

        self.json_input = tk.Text(self.root, height=10, width=60)
        self.json_input.pack(pady=10)

        # Base64 Output
        self.base64_output_label = tk.Label(self.root, text="Base64 Output:")
        self.base64_output_label.pack(pady=10)

        self.base64_output = tk.Text(self.root, height=10, width=60)
        self.base64_output.pack(pady=10)

        # Encode Button
        self.encode_button = tk.Button(self.root, text="Encode to Base64", command=self.encode_json)
        self.encode_button.pack(pady=10)

        # Decode Button
        self.decode_button = tk.Button(self.root, text="Decode from Base64", command=self.decode_base64)
        self.decode_button.pack(pady=10)

        # Upload JSON File Button
        self.upload_button = tk.Button(self.root, text="Upload JSON File", command=self.upload_json_file)
        self.upload_button.pack(pady=10)

        # Save Output Button
        self.save_button = tk.Button(self.root, text="Save Output to File", command=self.save_output_to_file)
        self.save_button.pack(pady=10)

        # Status label
        self.status_label = tk.Label(self.root, text="", fg="red")
        self.status_label.pack(pady=5)

    def encode_json(self):
        """Handles the encoding of JSON to Base64."""
        try:
            json_data = self.json_input.get("1.0", "end-1c")
            if not json_data:
                self.show_error("Input is empty!")
                return

            # Validate and parse the JSON
            try:
                parsed_json = json.loads(json_data)
            except json.JSONDecodeError:
                self.show_error("Invalid JSON data!")
                return

            # Run the encoding in a separate thread
            threading.Thread(target=self._encode_base64, args=(parsed_json,)).start()

        except Exception as e:
            logging.error(f"Error in encode_json: {e}")
            self.show_error(f"Error during encoding: {str(e)}")

    def _encode_base64(self, json_data):
        """Encodes JSON to Base64 in a separate thread."""
        try:
            encoded_data = self.encode_json_to_base64(json_data)
            self.update_output(encoded_data)
        except Exception as e:
            logging.error(f"Error during base64 encoding: {e}")
            self.show_error(f"Error: {str(e)}")

    def decode_base64(self):
        """Handles decoding of Base64 to JSON."""
        try:
            base64_data = self.base64_output.get("1.0", "end-1c")
            if not base64_data:
                self.show_error("Base64 input is empty!")
                return

            # Run the decoding in a separate thread
            threading.Thread(target=self._decode_base64, args=(base64_data,)).start()

        except Exception as e:
            logging.error(f"Error in decode_base64: {e}")
            self.show_error(f"Error during decoding: {str(e)}")

    def _decode_base64(self, base64_data):
        """Decodes Base64 back to JSON in a separate thread."""
        try:
            decoded_json = self.decode_base64_to_json(base64_data)
            self.update_output(json.dumps(decoded_json, indent=4))
        except Exception as e:
            logging.error(f"Error during base64 decoding: {e}")
            self.show_error(f"Error: {str(e)}")

    def update_output(self, data):
        """Updates the output text box with the result."""
        self.base64_output.delete("1.0", "end-1c")
        self.base64_output.insert("1.0", data)

    def encode_json_to_base64(self, json_data):
        """Encodes a Python JSON object (dict) to a base64 string."""
        json_str = json.dumps(json_data)
        json_bytes = json_str.encode('utf-8')
        base64_bytes = base64.b64encode(json_bytes)
        return base64_bytes.decode('utf-8')

    def decode_base64_to_json(self, base64_data):
        """Decodes a base64 string to a Python JSON object."""
        base64_bytes = base64.b64decode(base64_data)
        json_str = base64_bytes.decode('utf-8')
        return json.loads(json_str)

    def show_error(self, message):
        """Displays an error message in the status label."""
        self.status_label.config(text=message, fg="red")
        logging.error(message)

    def upload_json_file(self):
        """Handles the uploading and processing of a JSON file."""
        try:
            file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
            if not file_path:
                return  # No file selected, exit

            # Read the JSON file
            with open(file_path, "r", encoding="utf-8") as file:
                json_data = file.read()

            # Validate and parse the JSON
            try:
                parsed_json = json.loads(json_data)
                self.json_input.delete("1.0", "end-1c")  # Clear the current text
                self.json_input.insert("1.0", json_data)  # Insert the file's content
                self.status_label.config(text="File loaded successfully.", fg="green")
            except json.JSONDecodeError:
                self.show_error("Invalid JSON file content!")
        except Exception as e:
            logging.error(f"Error in uploading JSON file: {e}")
            self.show_error(f"Error during file upload: {str(e)}")

    def save_output_to_file(self):
        
        try:
            output_data = self.base64_output.get("1.0", "end-1c")
            if not output_data:
                self.show_error("Output is empty!")
                return

            # Ask the user to choose a location to save the file
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if not file_path:
                return  # No file selected, exit

            # Write the output to the file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(output_data)
            self.status_label.config(text=f"Output saved to {file_path}", fg="green")

        except Exception as e:
            logging.error(f"Error in saving output to file: {e}")
            self.show_error(f"Error during file save: {str(e)}")


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = Base64EncoderDecoderApp(root)
    root.mainloop()
