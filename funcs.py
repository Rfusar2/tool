from base64 import b64encode, b64decode
from os.path import exists, join, splitext
import zipfile, tarfile
from PIL import Image, ImageSequence


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

class Compress():
    def __init__():
        ...

class Convert():
    @staticmethod
    def convert_image(
            input_path, 
            output_path, 
            format, 
            size,
            bw,
            remove_pages,
            add_pages
        ):
        remove_pages = set(remove_pages or [])
        add_pages = add_pages or []
        
        pages = Convert.load_images(input_path)
        pages = [p for i, p in enumerate(pages) if i not in remove_pages]
        for extra_path in add_pages:
            pages.extend(Convert.load_images(extra_path))

        processed = []
        for img in pages:
            img = img.copy()
            # resize
            img.thumbnail(size)
            # color
            color = "L" if bw else "RGB"
            img = img.convert(color)
            processed.append(img)

        if not processed:
            raise ValueError("Nessuna pagina risultante")

        # --- Save ---
        first, *rest = processed

        if format.upper() in ["PDF", "TIFF"]:
            first.save(
                output_path,
                save_all=True,
                append_images=rest
            )
        else:
            # se non multipagina → salva solo la prima
            first.save(output_path, format=format)

        #with Image.open(input_path) as img:
        #    color = "L" if bw else "RGB"
        #    img.thumbnail(size)
        #    img.convert(color).save(output_path, format=format)

    @staticmethod
    def load_images(path):
        ext = splitext(path)[1].lower()
    
        img = Image.open(path)
    
        if getattr(img, "is_animated", False) or hasattr(img, "n_frames"):
            return [frame.copy() for frame in ImageSequence.Iterator(img)]
        else:
            return [img]

class Compress():
    @staticmethod
    def compress_image(input_path, output_path, quality=60):
        with Image.open(input_path) as img:
            img.save(output_path, optimize=True, quality=quality)
