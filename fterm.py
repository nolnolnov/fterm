print("\033[H\033[J")
from pystyle import *
fterm_t="""
  __  _____
 / _||_   _|  ___  _ __  _ __ ___
| |_   | |   / _ || '__|| '_ ` _ |
|  _|  | |  |  __/| |   | | | | | |
|_|    |_|   |___||_|   |_| |_| |_|
"""
print()
print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(fterm_t)))