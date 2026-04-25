from sys import exit
from cmd import MasterTool

m = MasterTool()
m.start()

m.cmd.print_help()
exit(1)
