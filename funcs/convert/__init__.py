from .. import *

class Convert():
    @staticmethod
    def convert_image(
            input_path, 
            output_path, 
            size,
            bw,
            remove_pages,
            add_pages
        ):
        remove_pages = set(remove_pages or [])
        add_pages = add_pages or []
        
        ext = splitext(output_path)[1].lower().replace(".", "")
        format = ext.upper() if ext != "jpg" else "JPEG"

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

    @staticmethod
    def load_images(path):
        ext = splitext(path)[1].lower()
    
        img = Image.open(path)
    
        if getattr(img, "is_animated", False) or hasattr(img, "n_frames"):
            return [frame.copy() for frame in ImageSequence.Iterator(img)]
        else:
            return [img]
    
    @staticmethod
    def compress_image(input_path, output_path, quality=60):
        with Image.open(input_path) as img:
            img.save(output_path, optimize=True, quality=quality)
