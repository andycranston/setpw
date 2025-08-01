# setpw

The purpose of the `setpw.bat` batch file and supporting `setpw.py` Python program
is to set the value of an environment variable with a password.  To prevent
the password being seen the characters in it are NOT displayed as it is typed.
Instead the '*' character is displayed.  Also the user has to enter the
password twice to help make sure it is correct.

ADDENDUM: This repository now includes a Bourne style shell script
called `setpw.sh` for UNIX/Linux users which does the same thing.  Skip to
the section "For UNIX/Linux users" near the bottom of this document
if that is what you want.

Windows users read on ...

## Typical usage of setpw

Here is a typical usage to set the environment variable `PWORD` to the value of
a password entered by the user:

```
C:\Users\andyc>call setpw PWORD
Enter password.........: ********
Enter password again...: ********
Environment variable PWORD set to password entered above

C:\Users\andyc>
```

The value of environment variable `PWORD` is now set to the password text that
was entered.  You could verify this by typing:

```
echo %PWORD%
```

but this would defeat the whole purpose as the password would now be visible
on the screen.  However, I do recommend doing this with a dummy/test password
like `notmypassword` just so you can see the program working.

Note the requirement to `CALL` the `setpw.bat` batch file - this is because the `setpw.bat`
batch file much be run in the same environment and not as a subprocess.

The `setpw.bat` batch file calls the `setpw.py` Python program which does the bulk
of the work.

## Why is setpw useful?

I often do live demonstrations and record demonstrations on Youtube when I
have to set an environment variable to contain a password.  Calling `setpw.bat` ensures
the password is not seen by the viewers.

## Installation

Run the INSTALL-WIN.bat Windows batch file as follows:
    
```
INSTALL-WIN.bat
```

It will display something similar to:

```
To copy the setpw.bat and setpw.py files to C:\Users\andy.PROBOOK-6465B\AppData\
Local\Microsoft\WindowsApps
Press any key to continue . . .
```

Press return to allow the batch file to continue. The batch file
will now displays two additional lines:
    
```
        1 file(s) copied.
        1 file(s) copied.
```

That's it.


## Warnings

The password is stored in a temporary file called:

```
%TEMP%\deleteme.pw
```

by the `setpw.py` Python program but then this file is almost immediately deleted
by the `setpw.bat` batch file.

There is a small possibility that if an unexpected error occurs or if there is
a system crash/hang at exactly the wrong moment then this file might not get
deleted and the password then be vunerable to discovery.

Also the password has been written to disk so, even after the file is deleted, a determined
"bad actor" could scan this disk blocks and potentially retrieve the password. See below for a
mitigation against this.

For these reasons I highly recommend that you DO NOT use this program on production or other critical systems.
What you determine to be "critical" is your own choice and yours alone!

## Password written to disk mitigation

There is a utility called sdelete for windows which securely deletes a file. The basic idea
is that before deleting the file it opens the file and overwrites the current content with
zero bytes before deleting the file.

You can download sdelete here:
    
[The sdelete (secure delete) program from sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete)

Extract the ZIP file and copy the file:
    
```
sdelete.exe
```

from the acrhive to the followign directory on your Windows machine:
    
```
%LOCALAPPDATA%\Microsoft\WindowsApps
```

Now when the `setpw.bat` batch file runs it will detect that the sdelete command is available
and use sdelete to delete the sensitive temporary password file instead of the far less
secure DEL command.

While this is an improvement I would still recommend NEVER using setpw for production
and critical systems.

## For UNIX/Linux users

The Bourne style shell script `setpw.sh` should be copied to
a directory in your PATH and called `setpw`.  Something similar to:

```
cp setpw.sh $HOME/bin
cd $HOME/bin
mv setpw.sh setpw
chmod a+x setpw
```

It can now be run from the UNIX command line as follows:

```
. setpw PWORD
```

Note the "." at thre beginning to "source" the shell script.  This is because,
like the Windows version, setpw must be run in the current environment and
not as a subprocess.

## Links

Useful links used in the development of this repo:

[The sdelete (secure delete) program from sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/sdelete)

----------------
End of README.md
