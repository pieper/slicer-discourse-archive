---
topic_id: 16143
title: "Error Installing Pygco Python Package For Graphcut In Slicer"
date: 2021-02-22
url: https://discourse.slicer.org/t/16143
---

# Error installing pygco python package (for graphcut) in Slicer 4.11

**Topic ID**: 16143
**Date**: 2021-02-22
**URL**: https://discourse.slicer.org/t/error-installing-pygco-python-package-for-graphcut-in-slicer-4-11/16143

---

## Post #1 by @supratikbose (2021-02-22 22:18 UTC)

<p>Hi, I am trying to install pygco package in Slicer 4.11 The package installs well in regular python 3.6, 3.7 environment. But withing Slicer 4.13 installation is failing while building the wheel file. Is there any solution?<br>
Below is the error message inside python interactor window:</p>
<blockquote>
<blockquote>
<blockquote>
<p>pip_install(‘pygco’)<br>
Requirement already satisfied: pygco in c:\users\usrA147\appdata\local\na-mic\slicer 4.11.20200930\lib\python\lib\site-packages (0.0.16)<br>
Requirement already satisfied: cython in c:\users\usrA147\appdata\local\na-mic\slicer 4.11.20200930\lib\python\lib\site-packages (from pygco) (0.29.21)<br>
command: ‘C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\python-real.exe’ -u -c ‘import sys, setuptools, tokenize; sys.argv[0] = ‘"’“‘C:\Users\usrA147\AppData\Local\Temp\pip-install-yyvbemew\pygco\setup.py’”’“‘; <strong>file</strong>=’”‘“‘C:\Users\usrA147\AppData\Local\Temp\pip-install-yyvbemew\pygco\setup.py’”’“';f=getattr(tokenize, '”‘“‘open’”’“‘, open)(<strong>file</strong>);code=f.read().replace(’”‘"’\r\n’“'”‘, ‘"’"’\n’“'”‘);f.close();exec(compile(code, <strong>file</strong>, ‘"’“‘exec’”’"‘))’ bdist_wheel -d ‘C:\Users\usrA147\AppData\Local\Temp\pip-wheel-2mzmu_b6’<br>
cwd: C:\Users\usrA147\AppData\Local\Temp\pip-install-yyvbemew\pygco<br>
Complete output (16 lines):<br>
running bdist_wheel<br>
running build<br>
running build_ext<br>
cythoning gco_python.pyx to gco_python.cpp<br>
C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\Cython\Compiler\Main.py:369: FutureWarning: Cython directive ‘language_level’ not set, using 2 for now (Py2). This will change in a later release! File: C:\Users\usrA147\AppData\Local\Temp\pip-install-yyvbemew\pygco\gco_python.pyx<br>
tree = Parsing.p_module(s, pxd, full_module_name)<br>
building ‘pygco’ extension<br>
creating build<br>
creating build\temp.win-amd64-3.6<br>
creating build\temp.win-amd64-3.6\Release<br>
creating build\temp.win-amd64-3.6\Release\gco_src<br>
C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Tools\MSVC\14.16.27023\bin\HostX86\x64\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -Igco_src “-IC:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\numpy\core\include” “-IC:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\include” “-IC:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\include” “-IC:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Tools\MSVC\14.16.27023\include” “-IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.6.1\include\um” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\ucrt” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\shared” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\um” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\winrt” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\cppwinrt” /EHsc /Tpgco_python.cpp /Fobuild\temp.win-amd64-3.6\Release\gco_python.obj -fpermissive<br>
cl : Command line warning D9002 : ignoring unknown option ‘-fpermissive’<br>
gco_python.cpp<br>
gco_python.cpp(4): fatal error C1083: Cannot open include file: ‘Python.h’: No such file or directory<br>
error: command ‘C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Tools\MSVC\14.16.27023\bin\HostX86\x64\cl.exe’ failed with exit status 2</p>
</blockquote>
</blockquote>
</blockquote>
<hr>
<p>ERROR: Failed building wheel for pygco<br>
Running setup.py clean for pygco<br>
Failed to build pygco<br>
Installing collected packages: pygco<br>
Running setup.py install for pygco: started<br>
Running setup.py install for pygco: finished with status ‘error’<br>
ERROR: Command errored out with exit status 1:<br>
command: ‘C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\python-real.exe’ -u -c ‘import sys, setuptools, tokenize; sys.argv[0] = ‘"’“‘C:\Users\usrA147\AppData\Local\Temp\pip-install-yyvbemew\pygco\setup.py’”’“‘; <strong>file</strong>=’”‘“‘C:\Users\usrA147\AppData\Local\Temp\pip-install-yyvbemew\pygco\setup.py’”’“';f=getattr(tokenize, '”‘“‘open’”’“‘, open)(<strong>file</strong>);code=f.read().replace(’”‘"’\r\n’“'”‘, ‘"’"’\n’“'”‘);f.close();exec(compile(code, <strong>file</strong>, ‘"’“‘exec’”’“‘))’ install --record ‘C:\Users\usrA147\AppData\Local\Temp\pip-record-j0rrv1q1\install-record.txt’ --single-version-externally-managed --compile --install-headers ‘C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Include\pygco’<br>
cwd: C:\Users\usrA147\AppData\Local\Temp\pip-install-yyvbemew\pygco<br>
Complete output (14 lines):<br>
running install<br>
running build<br>
running build_ext<br>
skipping ‘gco_python.cpp’ Cython extension (up-to-date)<br>
building ‘pygco’ extension<br>
creating build<br>
creating build\temp.win-amd64-3.6<br>
creating build\temp.win-amd64-3.6\Release<br>
creating build\temp.win-amd64-3.6\Release\gco_src<br>
C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Tools\MSVC\14.16.27023\bin\HostX86\x64\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -Igco_src “-IC:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\numpy\core\include” “-IC:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\include” “-IC:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\include” “-IC:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Tools\MSVC\14.16.27023\include” “-IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.6.1\include\um” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\ucrt” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\shared” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\um” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\winrt” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.17763.0\cppwinrt” /EHsc /Tpgco_python.cpp /Fobuild\temp.win-amd64-3.6\Release\gco_python.obj -fpermissive<br>
cl : Command line warning D9002 : ignoring unknown option ‘-fpermissive’<br>
gco_python.cpp<br>
gco_python.cpp(4): fatal error C1083: Cannot open include file: ‘Python.h’: No such file or directory<br>
error: command ‘C:\Program Files (x86)\Microsoft Visual Studio\2017\BuildTools\VC\Tools\MSVC\14.16.27023\bin\HostX86\x64\cl.exe’ failed with exit status 2<br>
----------------------------------------<br>
ERROR: Command errored out with exit status 1: ‘C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\python-real.exe’ -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '”‘“‘C:\Users\usrA147\AppData\Local\Temp\pip-install-yyvbemew\pygco\setup.py’”’“‘; <strong>file</strong>=’”‘“‘C:\Users\usrA147\AppData\Local\Temp\pip-install-yyvbemew\pygco\setup.py’”’“';f=getattr(tokenize, '”‘“‘open’”’“‘, open)(<strong>file</strong>);code=f.read().replace(’”‘"’\r\n’“'”‘, ‘"’"’\n’“'”‘);f.close();exec(compile(code, <strong>file</strong>, ‘"’“‘exec’”’"‘))’ install --record ‘C:\Users\usrA147\AppData\Local\Temp\pip-record-j0rrv1q1\install-record.txt’ --single-version-externally-managed --compile --install-headers ‘C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Include\pygco’ Check the logs for full command output.<br>
WARNING: You are using pip version 20.1.1; however, version 21.0.1 is available.<br>
You should consider upgrading via the ‘C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\python-real.exe -m pip install --upgrade pip’ command.<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py”, line 2569, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py”, line 2545, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\usrA147\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py”, line 2517, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/usrA147/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pygco’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @lassoan (2021-02-22 23:30 UTC)

<p>Usually we don’t deal with packages that do not provide wheels, as they tend to be low-quality, non-well-maintained software. The easiest workaround is to install anaconda and Python 3.6.7 virtual environment, let anaconda build the wheel, and Slicer will find it in the anaconda cache.</p>
<p>It could be interesting to check what pygco can do, but it is quite likely Slicer’s grow cut segmenter in “Grow from seeds” effect, or watershed segmenter in “Watershed” effect (provided by SegmentEditorExtraEffects extension) will do a much better job on 3D medical images than any of the general-purpose graph cut implementations where segmenting 3D medical images was just one of the many applications.</p>

---

## Post #3 by @supratikbose (2021-02-23 00:21 UTC)

<p>Hi Andras,<br>
thanks for your reply. I have two quesries:<br>
(1) Assuming I build the wheel file in Anaconda Python 3.6.7 environment - How do I make slicer point to Anaconda cache? Or do I invoke pip_install() in Slicer and pass the wheel file location in the argument.<br>
(2) In terms of using Slicer’s grow-cut segment (a) can you point me to any example where it is being invoked programmatically - I guess I can search in Slicer github code; (b) And does it take background seed information too or just foreground seed? Thanks</p>

---

## Post #4 by @lassoan (2021-02-23 02:10 UTC)

<p>We have found out accidentally that pip cache is shared between all python installations. Therefore you don’t need to do anything special - pip in Slicer’s virtual environment will find the wheel that conda built. There is no guarantee that it works like this in all computers but it worked several times, for various packages on different computers, and it is easy to try.</p>
<p>There are examples of using Grow from seeds from Python scrioting, without GUI in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>. However, since there are so many algorithms, it usually better to explore the methods with interactive GUI first, find out which works the best, and then automate the workflow.</p>
<p>There are several methods that does not require any background regions or can automatically determine the background seeds, and there are methods that can take any number of foreground/background input labels.</p>
<p>If you tell a bit more about what would you like to segment then we can give more specific advice.</p>

---
