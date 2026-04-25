from argparse import ArgumentParser
import funcs
from sys import exit

cmd = ArgumentParser(
    prog="master-tool",
    description="help to manipulate data",
)

COMMANDS = [
    {"cmds": ["-si", "--string-input"], "help": "string input"},
    {"cmds": ["-fi", "--file-input"], "help": "file input"},
    {"cmds": ["-so", "--string-output"], "help": "string output"},
    {"cmds": ["-fo", "--file-output"], "help": "file output"},

    #ACTIONS
    {"cmds": ["-tb64", "--to-base64"], "help": "from base64 to binary"},
    {"cmds": ["-fb64", "--from-base64"], "help": "convert to base64"},

    {"cmds": ["-c", "--compress"], "help": "active compress mode"},
    {"cmds": ["-q", "--quality-image"], "help": "quality image output (compressed)"},
    {"cmds": ["-m", "--image"], "help": "active convert mode"},
    {"cmds": ["-f", "--format"], "help": "output format"},
    {"cmds": ["-bw", "--black-white"], "help": "if you want convert in black and white"},
    {"cmds": ["-s", "--size"], "help": "number,number | [0] width, [1] height"},
    {"cmds": ["-ap", "--add-pages"], "help": "0.txt,1.txt,.. | file names for adding into document as first page"},
    {"cmds": ["-dp", "--delete-pages"], "help": "0,1,.. | number pages for deleting into document."},
]

for C in COMMANDS:
    obj = {}
    obj["help"] = C["help"]
    obj["required"] = False
    if C["cmds"][0] in ["tb64", "fb64", "-c", "-m", "-bw"]:
        obj["action"] = "store_true"

    cmd.add_argument(C["cmds"][0], C["cmds"][1], **obj)


args = cmd.parse_args()

#Check eseguito correttamente
args_dict = args.__dict__
#print(args_dict)
if not any(map(lambda x: args_dict[x], args_dict.keys())): cmd.print_help()

#CHECK_IMAGE = args_dict["image"] and args_dict["file_input"] and args_dict["file_output"]
#CHECK_COMPRESS = args_dict["compress"] and args_dict["file_input"] and args_dict["file_output"]
#CHECK_B64 = (args_dict["from_base64"] or args_dict["to_base64"]) and (args_dict["file_input"] or args_dict["string"]) and (args_dict["string_input"], args_dict["string_output"]) and args_dict["format"]

#*BASE64
#if CHECK_B64:
#    to_base64 = True if args.to_base64 else False
#    if args.file:
#        print(funcs.b64(convert=to_base64, file=args.file))
#    elif args.string:
#        print(funcs.b64(convert=to_base64, text=args.string))
#    exit(0)


#if CHECK_IMAGE:
args.size = args.size.split(",") if args.size else [800, 800]
args.size = [int(args.size[0]), int(args.size[1])]

if args.add_pages: args.add_pages = args.add_pages.split(",")
if args.delete_pages: args.delete_pages = args.delete_pages.split(",")

funcs.Convert.convert_image(
    args.file_input, 
    args.file_output, 
    args.format or "JPEG", 
    args.size, 
    args.black_white,
    args.delete_pages,
    args.add_pages,
)                 
exit(0)           
                      
#if CHECK_COMPRESS:
#    funcs.Compress.compress_image(args.file_input, args.file_output)
#    exit(0)

cmd.print_help()
