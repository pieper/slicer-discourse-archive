---
topic_id: 40902
title: "My Kernel Keeps Dying Slicer 4 11 Jupyter"
date: 2024-12-30
url: https://discourse.slicer.org/t/40902
---

# My Kernel keeps dying - Slicer 4.11 - Jupyter

**Topic ID**: 40902
**Date**: 2024-12-30
**URL**: https://discourse.slicer.org/t/my-kernel-keeps-dying-slicer-4-11-jupyter/40902

---

## Post #1 by @Saladi (2024-12-30 08:26 UTC)

<p>Hi all,<br>
I am using Slicer 4.11 rn.<br>
I am trying to run the juypter server.<br>
But i keep getting this error:<br>
"  Building wheel for pywinpty (PEP 517): started<br>
WARNING: Subprocess output does not appear to be encoded as cp1252<br>
WARNING: Subprocess output does not appear to be encoded as cp1252<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Users/Pravallika/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerJupyter/lib/Slicer-4.11/qt-scripted-modules/JupyterNotebooks.py”, line 54, in installRequiredPackages<br>
slicer.util.pip_install(“jupyter jupyterlab ipywidgets pandas ipyevents ipycanvas --no-warn-script-location”)<br>
File “C:\Users\Pravallika\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2876, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\Pravallika\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2851, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\Pravallika\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2811, in logProcessOutput<br>
for line in proc.stdout:<br>
File “C:/Users/Pravallika/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/…/lib/Python/Lib\codecs.py”, line 321, in decode<br>
(result, consumed) = self._buffer_decode(data, self.errors, final)<br>
UnicodeDecodeError: ‘CP_UTF8’ codec can’t decode byte 0xf0 in position 2813: No mapping for the Unicode character exists in the target code page."</p>
<p>Though it is showing the jupyter server is running. So i tried to connect the notebook kernel, it connected but it keeps disconnecting every 5 seconds and eventually dies.<br>
Python: 3.12.6<br>
Slicer: 4.11<br>
I have installed rust as well version: 1.83.0<br>
Any leads?</p>

---

## Post #2 by @Saladi (2024-12-30 08:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> could you please help?</p>

---

## Post #3 by @muratmaga (2024-12-30 09:15 UTC)

<p>Slicer 4.11 is many years old and is not maintained. Please upgrade to the latest version 5.6.2 and try.</p>

---
