from argparse import ArgumentParser
from sys import exit
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
            {"cmds": ["-so", "--string-output"], "help": "string output"},
            {"cmds": ["-fi", "--file-input"], "help": "file input"},
            {"cmds": ["-fsi", "--files-intput"], "help": "files input"},
            {"cmds": ["-fo", "--file-output"], "help": "file output"},
            {"cmds": ["-a", "--action"], "help": "action command", "valid": ["create", "extract"]},
        
            #MODES
            {"cmds": ["-z", "--compress"], "help": "active compress mode"},
            {"cmds": ["-g", "--generate"], "help": "actuve generate mode"},
            {"cmds": ["-c", "--crypto"], "help": "actuve cripto mode"},
            {"cmds": ["-m", "--image"], "help": "active convert mode"},

            #CRYPTO
            {"cmds": ["-gk", "--generate-key"], "help": "generate a key for crypto"},

            #GENERATE
            {"cmds": ["-l", "--length"], "help": "[-g] length of generate text"},
            {"cmds": ["-t", "--type"], "help": """[-g] type of generate text:
            - a: only ascii letters lower case
            - A: only ascii letters upper case
            - 0: only numbers
            - @: all without special chars
            - <empty>: all chars""", "valid": ["a", "A", "0", "@"]},
        
            #IMAGE
            {"cmds": ["-q", "--quality-image"], "help": "[-m] quality image output (compressed)"},
            {"cmds": ["-bw", "--black-white"], "help": "[-m] if you want convert in black and white"},
            {"cmds": ["-s", "--size"], "help": "[-m] number,number | [0] width, [1] height"},
            {"cmds": ["-ap", "--add-pages"], "help": "[-m] 0.txt,1.txt,.. | file names for adding into document as first page"},
            {"cmds": ["-dp", "--delete-pages"], "help": "[-m] 0,1,.. | number pages for deleting into document."},
        ]
        self.createCommands()


    def createCommands(self):
        for C in self.COMMANDS:
            obj = {}
            obj["help"] = C["help"]
            obj["required"] = False
            if C["cmds"][0] in ["tb64", "fb64", "-z", "-c", "-g", "-m", "-bw", "-gk"]:
                obj["action"] = "store_true"
            
            if C.get("valid"): obj["choices"] = C["valid"]



            self.cmd.add_argument(C["cmds"][0], C["cmds"][1], **obj)

        self.args = self.cmd.parse_args()



    def start(self):
        ad = self.args.__dict__
        args = self.args
        print(ad)
        if not any(map(lambda x: ad[x], ad.keys())): self.cmd.print_help(); exit(1)

        MANAGE_FILES = ad["file_input"] and ad["file_output"]
        
        CHECK_IMAGE = ad["image"] and MANAGE_FILES
        CHECK_COMPRESS = ad["compress"]
        CHECK_CRYPTO = ad["crypto"]
        CHECK_GENERATE = ad["generate"]
        
        if CHECK_COMPRESS and ad["file_output"] and ad["files_intput"]:
            args.files_intput = args.files_intput.split(",") if args.files_intput else []
            if len(args.files_intput)==0: self.cmd.print_help(); exit(1);
            Compress.zip(args.action, args.file_intput, args.file_output, args.files_intput)
            exit(0)           

        if CHECK_COMPRESS and MANAGE_FILES:
            Compress.zip(args.action, args.file_input, args.file_output, args.files_intput)
            exit(0)           
        
        if CHECK_CRYPTO and ad["generate_key"]: Crypto.gen_key(); exit(0);

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
