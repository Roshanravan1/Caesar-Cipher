def caesar_cipher(text, shift, mode):
  """Encrypts or decrypts a given text using the Caesar cipher.

  Args:
    text: The input text to be encrypted or decrypted.
    shift: The number of positions to shift the letters.
    mode: 'encrypt' for encryption, 'decrypt' for decryption.

  Returns:
    The encrypted or decrypted text.
  """

  result = ""
  
  # traverse text
  for char in text:
    # Encrypt this character
    if char.isupper():
      result += chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
      result += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      result += char
  
  return result

if __name__ == "__main__":
  text = input("Enter your message: ")
  shift = int(input("Enter the shift value (1-25): "))
  mode = input("Enter mode (encrypt/decrypt): ")

  if mode == 'encrypt':
    result = caesar_cipher(text, shift, mode)
    print("Encrypted text:", result)
  elif mode == 'decrypt':
    result = caesar_cipher(text, -shift, mode)
    print("Decrypted text:", result)
  else:
    print("Invalid mode")
