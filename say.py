import sys

from saying import hello

if len(sys.argv)==2:
    print(hello(sys.argv[1]))

