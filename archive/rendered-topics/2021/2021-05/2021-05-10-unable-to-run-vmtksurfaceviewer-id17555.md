---
topic_id: 17555
title: "Unable To Run Vmtksurfaceviewer"
date: 2021-05-10
url: https://discourse.slicer.org/t/17555
---

# Unable to run vmtksurfaceviewer

**Topic ID**: 17555
**Date**: 2021-05-10
**URL**: https://discourse.slicer.org/t/unable-to-run-vmtksurfaceviewer/17555

---

## Post #1 by @banderies (2021-05-10 23:08 UTC)

<p>I installed VMTK using Anaconda as the website describes. When I try to run vmtksurfaceviewer, I get the following error:</p>
<p>Unexpected error: &lt;class ‘ModuleNotFoundError’&gt;<br>
Traceback (most recent call last):<br>
File “/home/m166585/anaconda3/envs/vmtk/lib/python3.6/site-packages/vtk/vtkRenderingOpenGL2.py”, line 5, in <br>
from .vtkRenderingOpenGL2Python import *<br>
ImportError: libOSMesa.so.8: cannot open shared object file: No such file or directory</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “/home/m166585/anaconda3/envs/vmtk/bin/vmtksurfaceviewer”, line 20, in <br>
from vmtk import pypeserver<br>
File “/home/m166585/anaconda3/envs/vmtk/lib/python3.6/site-packages/vmtk/pypeserver.py”, line 16, in <br>
import vtk<br>
File “/home/m166585/anaconda3/envs/vmtk/lib/python3.6/site-packages/vtk/<strong>init</strong>.py”, line 33, in <br>
from .vtkRenderingOpenGL2 import *<br>
File “/home/m166585/anaconda3/envs/vmtk/lib/python3.6/site-packages/vtk/vtkRenderingOpenGL2.py”, line 9, in <br>
from vtkRenderingOpenGL2Python import *<br>
ModuleNotFoundError: No module named ‘vtkRenderingOpenGL2Python’</p>
<p>I would appreciate any help!<br>
Thanks,<br>
Barrett</p>

---

## Post #2 by @lassoan (2021-05-11 04:12 UTC)

<p><a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/25">We are working on updating VMTK’s build infrastructure</a>, which should make it available on Windows/Linux/Mac on PyPI (and so in conda environments, too).</p>
<p>In the meantime, you can use VMTK in Slicer’s Python environment and use Slicer as a surface viewer.</p>

---
