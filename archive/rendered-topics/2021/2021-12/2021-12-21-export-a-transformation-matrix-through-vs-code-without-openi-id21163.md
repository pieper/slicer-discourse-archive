# Export a transformation matrix through VS Code without opening 3D Slicer

**Topic ID**: 21163
**Date**: 2021-12-21
**URL**: https://discourse.slicer.org/t/export-a-transformation-matrix-through-vs-code-without-opening-3d-slicer/21163

---

## Post #1 by @Martina (2021-12-21 05:15 UTC)

<p>Operating system:  Microsoft Windows 10 Home<br>
Slicer version: Slicer 4.11.20210226<br>
VS Code version: Visual Studio Code 1.63.2</p>
<p>Hi all,<br>
I am new to 3D Slicer and VS Code.<br>
I want to export a transformation matrix from 3D slicer through a python script.<br>
I need to do this because I’m trying to write a pipeline as automated as possible to load MRI brain images in hololens.<br>
Is it possible?<br>
I’ve tried to run a python script on VS Code as if it was the 3D Slicer python console (so without opening 3D Slicer) but I didn’t have any success.<br>
So far my whole settings.json script is this:</p>
<p>{<br>
“python.pythonPath”: “C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\PythonSlicer.exe”,<br>
“python.linting.pylintPath”: “C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Scripts\pylint.exe”,<br>
“python.formatting.autopep8Path”: “C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Scripts\autopep8.exe”,<br>
“python.autoComplete.extraPaths”: [<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\QtPlugins\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Scripts\”,<br>
],<br>
“python.linting.enabled”: true,<br>
“git.autofetch”: true,<br>
“python.analysis.extraPaths”: [<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\QtPlugins\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\”,<br>
“C:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Scripts\”<br>
],<br>
“python.defaultInterpreterPath”: “c:\Users\username\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\PythonSlicer.exe”<br>
}</p>
<p>I’ve installed pylint, rope, atopep8, jedi in the 3D Slicer python console.<br>
I’ve selected ~\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\PythonSlicer.exe as interpreter in VS Code.</p>
<p>I’m definitely missing something. Can someone help?<br>
Any reply is appreciated.</p>

---
