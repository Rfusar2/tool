from argparse import ArgumentParser
import funcs

cmd = ArgumentParser(
    prog="Converter",
    description="help to convert data",
)

cmd.add_argument( "-s","--string", help="string to convert", required=False )
cmd.add_argument( "-f","--file", help="file to convert", required=False )

cmd.add_argument( "-tb64","--to_base64", action="store_true", help="from base64 to binary", required=False )
cmd.add_argument( "-fb64","--from_base64", action="store_true", help="convert to base64", required=False )
#cmd.add_argument( "-url","--url-link", action="store_true", help="convert in url text", required=False )

args = cmd.parse_args()

#*BASE64
if args.to_base64 or args.from_base64:
    to_base64 = True if args.to_base64 else False
    if args.file:
        print(funcs.b64(convert=to_base64, file=args.file))
    elif args.string:
        print(funcs.b64(convert=to_base64, text=args.string))
