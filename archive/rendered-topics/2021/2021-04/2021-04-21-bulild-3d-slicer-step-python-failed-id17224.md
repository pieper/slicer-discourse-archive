---
topic_id: 17224
title: "Bulild 3D Slicer Step Python Failed"
date: 2021-04-21
url: https://discourse.slicer.org/t/17224
---

# Bulild 3D Slicer - step: python failed

**Topic ID**: 17224
**Date**: 2021-04-21
**URL**: https://discourse.slicer.org/t/bulild-3d-slicer-step-python-failed/17224

---

## Post #1 by @wlixism (2021-04-21 14:50 UTC)

<p>Dear all,<br>
I was asked to create a 3D slicer module at work.<br>
I ran cmake according to the build instructions, but I got some errors in python step.<br>
I guess the cause was that my env PYTHONHOME was used.<br>
In that case, should I delete the environment variable PYTHONHOME and re-build it?<br>
Or do I need to modify some cmake files for python step?</p>
<p>I’m sorry for the childish question and not good at English.</p>
<p>Operating system: Windows10 64bit Home<br>
Slicer version: Nightly</p>
<p>cmake log:<br>
Performing install step for ‘python’<br>
Microsoft (R) Build Engine for .NET Framework version 16.9.0+5e4b48a27<br>
…<br>
Creating ‘bin/Release/Modules/Setup.local’<br>
python.vcxproj → C:\cw\3dslicer\release\python-build\bin\Release\python.exe<br>
Copying ‘pyconfig.h’ to ‘bin/Release/PC’<br>
– Install configuration: “Release”<br>
…<br>
– Installing: C:/cw/3dslicer/release/python-install/Lib/zipfile.py<br>
EXEC : Fatal Python error : Py_Initialize: can’t initialize sys standard streams [C:\cw\3dslicer\release\python-build\i<br>
nstall.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
Traceback (most recent call last):<br>
File “C:\lib\anaconda3\Lib\abc.py”, line 64, in <br>
ModuleNotFoundError: No module named ‘_abc’</p>
<pre><code>During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\lib\anaconda3\Lib\io.py", line 52, in &lt;module&gt;
  File "C:\lib\anaconda3\Lib\abc.py", line 68, in &lt;module&gt;
  File "C:\lib\anaconda3\Lib\_py_abc.py", line 35
    def __new__(mcls, name, bases, namespace, /, **kwargs):
                                              ^
SyntaxError: invalid syntax
</code></pre>
<p>EXEC : Fatal Python error : Py_Initialize: can’t initialize sys standard streams [C:\cw\3dslicer\release\python-build\i<br>
nstall.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
Traceback (most recent call last):<br>
File “C:\lib\anaconda3\Lib\abc.py”, line 64, in <br>
ModuleNotFoundError: No module named ‘_abc’</p>
<pre><code>During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\lib\anaconda3\Lib\io.py", line 52, in &lt;module&gt;
  File "C:\lib\anaconda3\Lib\abc.py", line 68, in &lt;module&gt;
  File "C:\lib\anaconda3\Lib\_py_abc.py", line 35
    def __new__(mcls, name, bases, namespace, /, **kwargs):
</code></pre>
<p>[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: Command “setlocal [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: C:\scoop\apps\cmake\3.20.1\bin\cmake.exe -DBUILD_TYPE=Release -P cmake_install.cmake [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: :cmEnd [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: :cmErrorLevel [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: exit /b %1 [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: :cmDone [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: if %errorlevel% neq 0 goto :VCEnd [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(155,5): error MSB3073: :VCEnd” finished with code -1. [C:\cw\3dslicer\release\python-build\install.vcxproj] [C:\cw\3dslicer\release\python.vcxproj]<br>
[MSVC path]\v160\Microsoft.CppCommon.targets(240,5): error MSB8066: ‘C:\cw\3dslicer\release\CMakeFiles\40ca38eeee47de97ec6ff776c317e3f0\python-mkdir.rule;C:\cw\3dslicer\release\CMakeFiles\40ca38eeee47de97ec6ff776c317e3f0\python-download.rule;C:\cw\3dslicer\release\CMakeFiles\40ca38eeee<br>
47de97ec6ff776c317e3f0\python-update.rule;C:\cw\3dslicer\release\CMakeFiles\40ca38eeee47de97ec6ff776c317e3f0\python-patch.rule;C:\cw\3dslicer\release\CMakeFiles\40ca38eeee47de97ec6ff776c317e3f0\python-configure.rule;C:\cw\3dslicer\release\CMakeFiles\40ca38eeee47de97ec6ff776c317e3f0\python-build.rule;C:\cw\3dslicer\release\CMakeFiles\40ca38eeee47de97ec6ff7<br>
76c317e3f0\python-install.rule;C:\cw\3dslicer\release\CMakeFiles\40ca38eeee47de97ec6ff776c317e3f0\python-configure_python_launcher.rule;C:\cw\3dslicer\release\CMakeFiles\79fe27a2f529f2d6c83674a26c4a115b\python-complete.rule;C:\cw\3dslicer\release\CMakeFiles\37bc3efd16376f2989467fd22aa298bd\python.rule’ of custom build is finished at exit code 1. [C:\cw\3dslicer\release\pyth<br>
on.vcxproj]</p>
<p>Best Regards,<br>
Tsubasa Tanaka</p>

---
