from metamorphism import Metamorphism as meta

print("[+] This is the code before running metamorphism")

# Generates a key using fernet
key = meta.generate_key()

# Code written here should still be in the correct python format
# Use exit() or sys.exit(0) at the end of the code to prevent it
# from running twice
new_code = """
print('[+] I was added in at run time!!!')
exit()
"""

# Encrypts the content using fernet and the newly generated key
encrypted_content = meta.encrypt_content(key=key, content=new_code)


m = meta(
        encryption_key=key,             # required
        new_content=encrypted_content,  # Required
        file_path=__file__,             # Required
        extension=".py"                 # Not required if a .py file
)


# Once called all code in the file will be changed with the new decrypted code
m.change_code_base() 
# Any code after this will never get executed
print("[+] I will never get executed :( ")
