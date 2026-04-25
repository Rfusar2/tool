from .. import *

class Compress():

    @staticmethod
    def zip(action:str, input_file:str, output_file:str, files: list[str]):
        if action=="create":
            with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_DEFLATED) as z:
                for f in files: z.write(f)

        elif action=="extract":
            with zipfile.ZipFile(input_file, 'r') as z:
                z.extractall(output_file)
