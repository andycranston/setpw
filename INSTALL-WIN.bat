@ECHO OFF
REM
REM @(!--#) @(#) INSTALL-WIN.bat, version 003, 07-july-2025
REM

SET DESTDIR=%LOCALAPPDATA%\Microsoft\WindowsApps

ECHO To copy the setpw.bat and setpw.py files to %DESTDIR%
PAUSE

COPY setpw.bat %DESTDIR%\setpw.bat
COPY setpw.py  %DESTDIR%\setpw.py

:END

REM End of file: INSTALL-WIN.bat
