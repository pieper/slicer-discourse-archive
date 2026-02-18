# Whitematteranalysis install on Ubuntu20.02 errors

**Topic ID**: 24977
**Date**: 2022-08-29
**URL**: https://discourse.slicer.org/t/whitematteranalysis-install-on-ubuntu20-02-errors/24977

---

## Post #1 by @mxd (2022-08-29 13:41 UTC)

<p>I am on Ubuntu 20.02 system and following the slicer DMRI tutorial , the White MatterAnalysis  successfully built, but when I run &gt;wm_quality_control_tractyography.py --help, I get errors;</p>
<p>Successfully built WhiteMatterAnalysis<br>
(base) marie@marie-Precision-5820-Tower-X-Series:~$ wm_quality_control_tractography.py --help<br>
Traceback (most recent call last):<br>
File “/home/marie/anaconda3/lib/python3.7/site-packages/vtkmodules/vtkIOParallel.py”, line 5, in <br>
from .vtkIOParallelPython import *<br>
ImportError: libjsoncpp.so.19: cannot open shared object file: No such file or directory</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “/home/marie/anaconda3/bin/wm_quality_control_tractography.py”, line 4, in <br>
<strong>import</strong>(‘pkg_resources’).run_script(‘WhiteMatterAnalysis==0.3.0’, ‘wm_quality_control_tractography.py’)<br>
File “/home/marie/anaconda3/lib/python3.7/site-packages/pkg_resources/<strong>init</strong>.py”, line 667, in run_script<br>
self.require(requires)[0].run_script(script_name, ns)<br>
File “/home/marie/anaconda3/lib/python3.7/site-packages/pkg_resources/<strong>init</strong>.py”, line 1463, in run_script<br>
exec(code, namespace, namespace)<br>
File “/home/marie/anaconda3/lib/python3.7/site-packages/WhiteMatterAnalysis-0.3.0-py3.7-linux-x86_64.egg/EGG-INFO/scripts/wm_quality_control_tractography.py”, line 9, in <br>
import vtk<br>
File “/home/marie/anaconda3/lib/python3.7/site-packages/vtk.py”, line 32, in <br>
all_spec.loader.exec_module(all_m)<br>
File “/home/marie/anaconda3/lib/python3.7/site-packages/vtkmodules/all.py”, line 83, in <br>
from .vtkIOParallel import *<br>
File “/home/marie/anaconda3/lib/python3.7/site-packages/vtkmodules/vtkIOParallel.py”, line 9, in <br>
from vtkIOParallelPython import *<br>
ModuleNotFoundError: No module named ‘vtkIOParallelPython’</p>
<p>Any help would be appreciated.</p>

---
