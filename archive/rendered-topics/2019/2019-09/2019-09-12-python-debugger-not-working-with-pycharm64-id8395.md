# Python debugger not working with pycharm64

**Topic ID**: 8395
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/python-debugger-not-working-with-pycharm64/8395

---

## Post #1 by @ungi (2019-09-12 02:23 UTC)

<p>I’ve installed a new version of PyCharm, and tried to set up Python debugger in Slicer. But I got the error message below. I tried to find the missing registry entry, but noticed that I don’t have a pycharm.exe file, only a pycharm64.exe, with matching registry entry. Is it possible that Python debugger module needs to be updated to look for pycharm64.exe as well as pycharm.exe?</p>
<p>I use Slicer 4.10.</p>
<p>SystemError: D:\D\S\Slicer-4100-build\Python-2.7.13\Objects\classobject.c:521: bad argument to internal function<br>
Traceback (most recent call last):<br>
File “C:/Users/tamas/AppData/Roaming/NA-MIC/Extensions-27501/DebuggingTools/lib/Slicer-4.10/qt-scripted-modules/PyDevRemoteDebug.py”, line 199, in onDebuggerSelected<br>
eggDir=self.logic.getPyCharmDebugEggPath(enableAutoDetect=True)<br>
File “C:/Users/tamas/AppData/Roaming/NA-MIC/Extensions-27501/DebuggingTools/lib/Slicer-4.10/qt-scripted-modules/PyDevRemoteDebug.py”, line 489, in getPyCharmDebugEggPath<br>
aKey = _winreg.OpenKey(aReg, r"Applications\pycharm.exe\shell\open\command")<br>
WindowsError: [Error 2] The system cannot find the file specified</p>

---

## Post #2 by @ungi (2019-09-12 02:30 UTC)

<p>I’ve created a registry entry called ‘pycharm.exe’ and copied the same values inside. Now I don’t get the above error message. But I hit another problem. I don’t have a “pycharm-debug.egg”. I only have this single egg file:<br>
“c:\Program Files\JetBrains\PyCharm 2019.2.1\debug-eggs\pydevd-pycharm.egg”<br>
Maybe they renamed this file in the new PyCharm?</p>

---

## Post #3 by @ungi (2019-09-12 02:32 UTC)

<p>I’ve copied pydevd-pycharm.egg and renamed it pycharm-debug.egg.<br>
Now, the debugger works. So, searching for these new names, or asking the user to input these values would probably solve the problem.</p>

---

## Post #4 by @lassoan (2019-09-12 21:15 UTC)

<p>Thanks for reporting. These have been all fixed in recent versions of the DebuggingTools extension (available for latest stable 4.10.2 and recent preview releases but not for older Slicer releases such as 4.10.0).</p>

---
