from argparse import ArgumentParser

from funcs.compress import Compress
from funcs.convert import Convert
from funcs.crypto import Crypto

class MasterTool():
    def __init__(self):
        self.cmd = ArgumentParser( 
            prog="master-tool", description="help to manipulate data" 
        )

        self.COMMANDS = [
            {"cmds": ["-si", "--string-input"], "help": "string input"},
            {"cmds": ["-fi", "--file-input"], "help": "file input"},
            {"cmds": ["-so", "--string-output"], "help": "string output"},
            {"cmds": ["-fo", "--file-output"], "help": "file output"},
        
            #COMPRESS
            {"cmds": ["-c", "--compress"], "help": "active compress mode"},
        
            #GENRATE
            {"cmds": ["-g", "--generate"], "help": "actuve generate mode"},
            {"cmds": ["-l", "--length"], "help": "length of generate text"},
            {"cmds": ["-t", "--type"], "help": """type of generate text:
            - a: only ascii letters lower case
            - A: only ascii letters upper case
            - 0: only numbers
            - @: all without special chars
            - <empty>: all chars""", "valid": ["a", "A", "0", "@"]},
        
            #IMAGE
            {"cmds": ["-m", "--image"], "help": "active convert mode"},
            {"cmds": ["-q", "--quality-image"], "help": "quality image output (compressed)"},
            {"cmds": ["-bw", "--black-white"], "help": "if you want convert in black and white"},
            {"cmds": ["-s", "--size"], "help": "number,number | [0] width, [1] height"},
            {"cmds": ["-ap", "--add-pages"], "help": "0.txt,1.txt,.. | file names for adding into document as first page"},
            {"cmds": ["-dp", "--delete-pages"], "help": "0,1,.. | number pages for deleting into document."},
        ]
        self.createCommands()

    def createCommands(self):
        for C in self.COMMANDS:
            obj = {}
            obj["help"] = C["help"]
            obj["required"] = False
            if C["cmds"][0] in ["tb64", "fb64", "-c", "-g", "-m", "-bw"]:
                obj["action"] = "store_true"
            
            if C.get("valid"): obj["choices"] = C["valid"]

            self.cmd.add_argument(C["cmds"][0], C["cmds"][1], **obj)

        self.args = self.cmd.parse_args()

    def start(self):
        ad = self.args.__dict__
        args = self.args
        #print(ad)
        if not any(map(lambda x: ad[x], ad.keys())): cmd.print_help(); exit(1)

        MANAGE_FILES = ad["file_input"] and ad["file_output"]
        
        CHECK_IMAGE = ad["image"] and MANAGE_FILES
        CHECK_COMPRESS = ad["compress"] and MANAGE_FILES
        CHECK_GENERATE = ad["generate"]
        
        if CHECK_GENERATE:
            Crypto.gen_password(int(args.length), args.type)
            exit(0)           
        
        if CHECK_IMAGE:
            args.size = args.size.split(",") if args.size else [800, 800]
            args.size = [int(args.size[0]), int(args.size[1])]
            
            if args.add_pages: args.add_pages = args.add_pages.split(",")
            if args.delete_pages: args.delete_pages = args.delete_pages.split(",")
            
            Convert.convert_image(
                args.file_input, 
                args.file_output, 
                args.size, 
                args.black_white,
                args.delete_pages,
                args.add_pages,
            )                 
            exit(0)           
                              
        if CHECK_COMPRESS:
            Convert.compress_image(args.file_input, args.file_output)
            exit(0)
