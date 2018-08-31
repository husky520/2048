def padding(text, length, filler=' '):
    text = str(text)
    filler = str(filler)
    for i in range(length):
        if len(text) >= length:
            return text
        else:
            text = filler + text
        if len(text) >= length:
            return text
        else:
            text = text + filler