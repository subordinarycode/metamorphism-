# Python class for runtime metamorphism

This is a Python class that allows you to change the code base of a script at runtime by replacing the existing code with new encrypted code and executing it.

## Usage

To use this class, you need to import it into your Python script and create an instance of the `metamorphism` class with the following parameters:

- `new_content`: Encrypted Python code to replace the existing code.
- `file_path`: Path to the script file that you want to modify. Usually, you can use the `__file__` variable to get the path of the current script.
- `encryption_key`: Key to decrypt the new code.
- `extension` (optional): File extension of the script file. By default, it is `.py`.

Then, you can call the `change_code_base()` method of the `metamorphism` object to replace the code and execute the new code.

Here's an example of how to generate a payload using the `metamorphism` class:

```python
from metamorphism import Metamorphism as meta

# Generates a key using fernet
key = meta.generate_key()

# Code written here should still be in the correct python format
# Use exit() or sys.exit(0) at the end of the code to prevent it
# from running twice
new_code = """
print('[+] Im the new payload added in at run time!!!')
exit()
"""

# Encrypts the content using fernet and the newly generated key
encrypted_content = meta.encrypt_content(key=key, content=new_code)
print(key)
print(encrypted_content)

```

Here's an example of how the execute the new payload using the `metamorphism` class
```python
from metamorphism import Metamorphism as meta

key = b'<your encryption key>'

data = b'<your encrypted payload>'

m = meta(
        encryption_key=key,             # Required
        new_content=encrypted_content,  # Required
        file_path=__file__,             # Required
        extension=".py"                 # Defauly .py
)


# Once called all code in the file will be changed with the new decrypted code
m.change_code_base()
# Any code after this will never get executed
print("[+] I will never get executed :( ")
```

## Methods

### `__init__(self, new_content: bytes, file_path: str, encryption_key: bytes, extension: str = ".py")`

Constructor method that initializes a `metamorphism` object with the following parameters:

- `new_content`: Encrypted Python code to replace the existing code.
- `file_path`: Path to the script file that you want to modify.
- `encryption_key`: Key to decrypt the new code.
- `extension` (optional): File extension of the script file. By default, it is `.py`.

### `generate_key() -> bytes`

Static method that generates a new key for encrypting the new code.

### `encrypt_content(key: bytes, content: str) -> bytes`

Static method that encrypts a string of Python code using a given key.

### `decrypt_content(key: bytes, content: bytes) -> bytes`

Static method that decrypts a byte string of encrypted Python code using a given key.

### `change_code_base(self) -> None`

Method that replaces the existing code with the new code and executes it. This method performs the following steps:

1. Writes the new code to the script file.
2. Extracts the name of the script file and removes the file extension.
3. Loads the script file as a Python module.
4. Reloads the module to execute the new code.
