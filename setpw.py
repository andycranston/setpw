#
# @(!--#) @(#) setpw.py, version 002, 07-july-2025
#
# Windows only.
#
# get a password value from the user and store it in
# a plain text file
#
# NOT FOR PRODUCTION USE!!!
#

################################################################################################

#
# imports
#

import sys
import os
import msvcrt

################################################################################################

#
# constants
#

DEFAULTPWFILENAME = "deleteme.pw"

################################################################################################

def readhidden():
    text = ""

    while True:
        key = msvcrt.getch()
        
        if key == b'\x00':
            continue

        if (key == b'\r'):
            break

        if (key == b'\x08'):
            # remove last byte
            if len(text) == 0:
                continue
            elif len(text) == 1:
                text = ""
                print("\b \b", end='')
                sys.stdout.flush()
                continue
            else:
                text = text[0:len(text)-1]
                print("\b \b", end='')
                sys.stdout.flush()
                continue

        text += str(key, 'utf-8')
        print("*", end='')
        sys.stdout.flush()

    print("")
    sys.stdout.flush()

    return text

################################################################################################

#
# Main
#

progname = os.path.basename(sys.argv[0])

print("Enter password.........: ", end='')
sys.stdout.flush()
pw = readhidden()

if len(pw) == 0:
    print("{}: no password entered".format(progname), file=sys.stderr)
    sys.exit(1)

print("Enter password again...: ", end='')
sys.stdout.flush()
vpw = readhidden()

if len(pw) != len(vpw):
    print("{}: passwords are not the same number of characters".format(progname), file=sys.stderr)
    sys.exit(1)

if pw != vpw:
    print("{}: passwords do not match".format(progname), file=sys.stderr)
    sys.exit(1)

if len(sys.argv) <= 1:
    pwfilename = DEFAULTPWFILENAME
else:
    pwfilename = sys.argv[1]

try:
    pwfile = open(pwfilename, "w+")
except IOError:
    print("{}: unable to create special password file \"{}\" for writing - permission problem?".format(progname, pwfilename), file=sys.stderr)
    sys.exit(1)

print(pw, file=pwfile)

pwfile.flush()
pwfile.close()

sys.exit(0)
