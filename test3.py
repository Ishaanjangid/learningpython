if myMode.lower().startswith('e'):
    # Then encrypt the message
    crypto_txt = encryptText(message,keyA,KeyB)
else:
    # Then decrypt the message
    crypto_txt = decryptText(message,keyA,KeyB)