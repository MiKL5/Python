# **Les erreurs**<a href="../../../../"><img align="right" src="../../../../assets/logo/Python-logo-notext.svg" alt="Python" height="64px"></a>
## **Syntaxe**
Elles empêchent l'exécution du code.

Les plus communes sont :
* Les erreurs de casses ;
* Les mots réservés ;
* L'oubli des guillemets.

Il y en a quelques centaines d'autres.
### **Les mots reservés**
```py
False
None
True
and
as
assert
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
non local
not
or
pass
raise
return
try
while
with
yield
```
## **Exécution "RuntimeError"**
Elles peuvent survenirent n'importe quand.

Python n'utilise que ce qu'il connaît (les variables).

Elles sont mieux identifiables :
* "NameError" = variable non définie ;
* "TypeError" = utilisation d'une fonctionnalité avec une variable du mauvais type.  
Il en existe des centaines d'autres.
## **Sémantique (erreur de logique)**
Plante rarement le programme, bien souvent, il n'est pas retourner ce que l'on attend.  
Souvent, ce sont des erreurs d'inatention ou erreurs obligeant à revoir l'entièreté du programme et recommancer presque au début.  
Souvent, l'utilisation d'un débogueur avancé permet de revoir le scrit step by step. Ou la fonction `print()`.
## **Liste non exhaustive de modules de librairies dont il ne faut pas utiliser le nom pour un fichier**
```py
abc
aifc
argparse
array
ast
asynchat
asyncio
asyncore
atexit
audioop
base64
bdb
binascii
binhex
bisect
builtins
bz2
calendar
cgi
cgitb
chunk
cmath
cmd
code
codecs
codeop
colorsys
compileall
configparser
contextlib
contextvars
copy
copyreg
crypt
csv
ctypes
dataclasses
datetime
decimal
difflib
dis
distutils
doctest
dummy_threading
email
encodings
ensurepip
enum
errno
faulthandler
fcntl
filecmp
fileinput
fnmatch
formatter
fractions
ftplib
functools
gc
getopt
getpass
gettext
glob
grp
gzip
hashlib
heapq
hmac
html
http
imaplib
imghdr
imp
importlib
inspect
io
ipaddress
itertools
json
keyword
lib2to3
linecache
locale
logging
lzma
mailbox
mailcap
marshal
math
mimetypes
mmap
modulefinder
msilib
msvcrt
multiprocessing
netrc
nis
nntplib
numbers
operator
optparse
os
ossaudiodev
parser
pathlib
pdb
pickle
pickletools
pipes
pkgutil
platform
plistlib
poplib
posix
pprint
profile
pstats
pty
pwd
py_compile
pyclbr
pydoc
queue
quopri
random
re
readline
reprlib
resource
rlcompleter
runpy
sched
secrets
select
selectors
shelve
shlex
shutil
signal
site
smtpd
smtplib
sndhdr
socket
socketserver
spwd
sqlite3
ssl
stat
statistics
string
stringprep
struct
subprocess
sunau
symbol
symtable
sys
sysconfig
syslog
tabnanny
tarfile
telnetlib
tempfile
termios
test
textwrap
threading
time
timeit
tkinter
token
tokenize
trace
traceback
tracemalloc
tty
turtle
turtledemo
types
typing
unicodedata
unittest
urllib
uu
uuid
venv
warnings
wave
weakref
webbrowser
winreg
winsound
wsgiref
xdrlib
xml
xmlrpc
zipapp
zipfile
zipimport
zlib
```