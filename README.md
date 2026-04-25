# Converter

this tool must help me for converting data

- [] IMAGE
- [] CRYPTO
- [] COMPRESS

```txt
usage: master-tool [-h] [-si STRING_INPUT] [-fi FILE_INPUT]
                   [-so STRING_OUTPUT] [-fo FILE_OUTPUT] [-z] [-g] [-c] [-m]
                   [-gk] [-l LENGTH] [-t {a,A,0,@}] [-q QUALITY_IMAGE] [-bw]
                   [-s SIZE] [-ap ADD_PAGES] [-dp DELETE_PAGES]

help to manipulate data

options:
  -h, --help            show this help message and exit
  -si STRING_INPUT, --string-input STRING_INPUT
                        string input
  -fi FILE_INPUT, --file-input FILE_INPUT
                        file input
  -so STRING_OUTPUT, --string-output STRING_OUTPUT
                        string output
  -fo FILE_OUTPUT, --file-output FILE_OUTPUT
                        file output
  -z, --compress        active compress mode
  -g, --generate        actuve generate mode
  -c, --crypto          actuve cripto mode
  -m, --image           active convert mode

  -gk, --generate-key   generate a key for crypto
  -l LENGTH, --length LENGTH
                        [-g] length of generate text
  -t {a,A,0,@}, --type {a,A,0,@}
                        [-g] type of generate text: - a: only ascii letters
                        lower case - A: only ascii letters upper case - 0:
                        only numbers - @: all without special chars - <empty>:
                        all chars
  -q QUALITY_IMAGE, --quality-image QUALITY_IMAGE
                        [-m] quality image output (compressed)
  -bw, --black-white    [-m] if you want convert in black and white
  -s SIZE, --size SIZE  [-m] number,number | [0] width, [1] height
  -ap ADD_PAGES, --add-pages ADD_PAGES
                        [-m] 0.txt,1.txt,.. | file names for adding into
                        document as first page
  -dp DELETE_PAGES, --delete-pages DELETE_PAGES
                        [-m] 0,1,.. | number pages for deleting into document.
```
