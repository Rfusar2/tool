from base64 import b64encode, b64decode
from os.path import exists

#* WORKS
def b64(convert, text=None, file=None):
    content = bytes()

    if text: content = text.encode("utf-8")

    elif file:
        if not exists(file): print("file not exist, i'am sorry :(")

        with open(file, "rb") as f:
            content = f.read()

    if convert:
        return b64encode(content).decode("utf-8")

    else:
        return b64decode(content).decode("utf-8")
