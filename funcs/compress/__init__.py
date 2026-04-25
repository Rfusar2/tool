from .. import *

class Compress():

    @staticmethod
    def start(action:str, input_file:str, output_file:str, files: list[str]):

        ext = splitext(output_file)[1].lower() if output_file else None
        if not ext:
            ext = splitext(input_file)[1].lower() if input_file else None

        if ext==".zip":
            if action=="create":
                with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_DEFLATED) as z:
                    for f in files: z.write(f)

            elif action=="extract":
                with zipfile.ZipFile(input_file, 'r') as z:
                    z.extractall(output_file)

            elif action=="read":
                with zipfile.ZipFile(input_file) as z:
                    pprint(z.namelist())

            elif action=="read-file":
                with zipfile.ZipFile(input_file) as z:
                    with z.open(output_file) as f:
                        pprint(f.read())
        else:
            type_r = "r" if ext==".tar" else "r:gz" if ext==".gz" else "r:bz2" if ext==".bz2" else "r:xz" if ext==".xz" else None
            type_w = "w" if ext==".tar" else "w:gz" if ext==".gz" else "w:bz2" if ext==".bz2" else "w:xz" if ext==".xz" else None

            if action=="create":
                if type_w:
                    with tarfile.open(output_file, type_w) as tar:
                        for f in files: tar.add(f)

            elif action=="extract":
                with tarfile.open(input_file, type_r) as tar:
                    tar.extractall(output_file)

            elif action=="read":
                with tarfile.open(input_file, type_r) as tar:
                    pprint(tar.getnames())

            elif action=="read-file":
                with tarfile.open(input_file) as tar:
                    f = tar.extractfile(output_file)
                    pprint(f.read())
