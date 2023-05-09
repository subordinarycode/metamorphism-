import importlib
import sys
from cryptography.fernet import Fernet
import os.path import isfile


class Metamorphism:
    def __init__(
            self,
            new_content: bytes,
            file_path: str,
            encryption_key: bytes,
            extension: str = ".py"
    ) -> None:
        """
        Initializes a Metamorphism object.

        Parameters:
        - new_content: Encrypted Python code to replace the existing code.
        - file_path: Path to the script file that you want to modify.
        - encryption_key: Key to decrypt the new code.
        - extension: File extension of the script file. By default, it is '.py'.
        """

        if not isinstance(new_content, bytes):
            raise TypeError("new_content should be bytes")
        if not isinstance(file_path, str):
            raise TypeError("file_path should be str")
        if not isinstance(encryption_key, bytes):
            raise TypeError("encryption_key should be bytes")
        if not isinstance(extension, str):
            raise TypeError("extension should be str")

        if not isfile(file_path):
            raise FileNotFoundError(f"{file_path} does not exist or is not a file")

        self.file_path = file_path
        self.key = encryption_key
        self.new_content = self.decrypt_content(content=new_content, key=self.key)
        self.file_extension = extension

    @staticmethod
    def generate_key():
        """
        Generates a new encryption key.

        Returns:
        - A new encryption key as bytes.
        """
        return Fernet.generate_key()

    @staticmethod
    def encrypt_content(key: bytes, content: str) -> bytes:
        """
        Encrypts a string of Python code using a given key.

        Parameters:
        - key: Encryption key as bytes.
        - content: Python code as string.

        Returns:
        - Encrypted Python code as bytes.
        """
        if not isinstance(key, bytes):
            raise TypeError("Invalid key. Key must be in bytes.")
        if not isinstance(content, str):
            raise TypeError("Invalid content. Content must be of type str")

        f = Fernet(key)
        encrypted_message = f.encrypt(content.encode())
        return encrypted_message

    @staticmethod
    def decrypt_content(key: bytes, content: bytes) -> bytes:
        """
        Decrypts a string of Python code using a given key.

        Parameters:
        - key: Encryption key as bytes.
        - content: Python code as string.

        Returns:
        - Decrypted Python code as bytes.
        """
        if not isinstance(key, bytes):
            raise TypeError("Invalid key. Key must be in bytes.")
        if not isinstance(content, bytes):
            raise TypeError("Invalid file content. Content must be in bytes.")

        decrypted_message = Fernet(key).decrypt(content)
        return decrypted_message

    def change_code_base(self) -> None:
        """
        Changes the code base of the script file to the new code and runs it.
        """
        try:
            with open(self.file_path, "wb") as f:
                f.write(self.new_content)

            if sys.platform == 'win32':
                divider = "\\"
            else:
                divider = "/"
            module_name = self.file_path.split(divider)[-1].rstrip(self.file_extension)

            module = importlib.import_module(module_name)

            importlib.reload(module)
        except Exception as e:
            raise RuntimeError(f"Failed to change code base: {e}")
