@ECHO OFF
REM
REM @(!--#) @(#) setpw.py, version 001, 30-march-2018
REM
REM Usage:
REM         call setpw VARNAME
REM
REM where VARNAME is the name of an environmental variable
REM

REM Set location of Python program
SET PYTHONPROG=C:\Windows\setpw.py

REM Set name of temporary password file
SET TEMPPASSFILE=%TEMP%\deleteme.pw

REM Get the environmental variable from the command line
IF "%1"=="" GOTO NOVARNAME
SET VARNAME=%1

REM Run the setpw.py program
IF NOT EXIST %PYTHONPROG% GOTO NOPYTHON
python %PYTHONPROG% %TEMPPASSFILE%
IF ERRORLEVEL 1 GOTO END
IF NOT EXIST %TEMPPASSFILE% GOTO END
SET /P %VARNAME%= < %TEMPPASSFILE%
IF EXIST %TEMPPASSFILE% DEL %TEMPPASSFILE%
ECHO Environment variable %VARNAME% set to password entered above
GOTO END

REM Error - no environmental variable name specified on command line
:NOVARNAME
ECHO ERROR: No environment variable name specified
GOTO END

REM Error - unable to locate the setpw.py Pythom program
:NOPYTHON
ECHO ERROR: Cannot find the Python program %PYTHONPROG%
GOTO END

REM End of batch file
:END
