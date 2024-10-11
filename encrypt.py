def encrypt_string(text):
    encrypted = []
    for c in text:
        if c.islower():
            if c == "z":
                encrypted.append("a")
            else:    
                encrypted.append(chr(ord(c) + 1).lower())
        elif c.isupper():
            if c == "Z":
                encrypted.append("A")
            else:    
                encrypted.append(chr(ord(c) + 1).upper())
        else:
            encrypted.append(c)
                   
        # TODO: Check if `c` is a letter different from 'z' and 'Z'. If so, increment by 1.
        # If 'c' is 'z', change it to 'a'. If 'c' is 'Z', change it to 'A'.
        # Otherwise, keep 'c' unchanged and add it to the encrypted list.
    return ''.join(encrypted)
encrypted_text = encrypt_string("Hello, Python!")
print("The encrypted text is:", encrypted_text) # Should print out "Ifmmp, Qzuipo!"    