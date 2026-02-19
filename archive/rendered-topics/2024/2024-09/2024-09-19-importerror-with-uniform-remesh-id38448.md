---
topic_id: 38448
title: "Importerror With Uniform Remesh"
date: 2024-09-19
url: https://discourse.slicer.org/t/38448
---

# ImportError with Uniform Remesh

**Topic ID**: 38448
**Date**: 2024-09-19
**URL**: https://discourse.slicer.org/t/importerror-with-uniform-remesh/38448

---

## Post #1 by @kucerabi (2024-09-19 19:41 UTC)

<p>Every time I try to use Uniform Remesh in the Surface Toolbox, I get this error:</p>
<p>[Python] Failed to compute output model: DLL load failed while importing _clustering: The specified module could not be found.<br>
Traceback (most recent call last):<br>
File “C:/Users/kucerabi/Desktop/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SurfaceToolbox.py”, line 278, in onApplyButton<br>
self.logic.applyFilters(self.<em>parameterNode)<br>
File “C:/Users/kucerabi/Desktop/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SurfaceToolbox.py”, line 579, in applyFilters<br>
SurfaceToolboxLogic.remesh(outputModel, outputModel,<br>
File “C:/Users/kucerabi/Desktop/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SurfaceToolbox.py”, line 404, in remesh<br>
if not SurfaceToolboxLogic.installRemeshPrerequisites():<br>
File “C:/Users/kucerabi/Desktop/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SurfaceToolbox.py”, line 387, in installRemeshPrerequisites<br>
import pyacvd<br>
File "C:\Users\kucerabi\Desktop\Slicer 5.6.2\lib\Python\Lib\site-packages\pyacvd_<em>init</em></em>.py", line 3, in <br>
from pyacvd.clustering import Clustering<br>
File “C:\Users\kucerabi\Desktop\Slicer 5.6.2\lib\Python\Lib\site-packages\pyacvd\clustering.py”, line 16, in <br>
from pyacvd import _clustering<br>
ImportError: DLL load failed while importing _clustering: The specified module could not be found.</p>
<p>Why am I getting this? What can I do to resolve it?</p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2024-09-19 20:20 UTC)

<p>Looks like remeshing python package didn’t install for some reason. Try installing manually and see if you are getting an error<br>
<code>pip_install("pyacvd")</code></p>

---

## Post #3 by @lassoan (2024-09-20 05:43 UTC)

<p>Unfortunately, pyacvd developers broke their package in their 0.3.0 version by adding C code that needs to be compiled and it is only compatible with VTK hosted on PyPI. I’ve <a href="https://github.com/pyvista/pyacvd/issues/56">submitted an issue to their tracker</a>, but since probably they will not fix this for a long time, I’ll add a version restriction to only use pyacvd&lt;0.3.</p>
<p>In the meantime, you can fix the issue by executing <code>slicer.util.pip_install("pyacvd&lt;0.3")</code> in the Slicer Python console.</p>

---

## Post #4 by @lassoan (2024-09-20 18:13 UTC)

<p>I’ve tested this a bit more and on my computer on a fresh Slicer-5.6.2 installation everything works.</p>
<p>Could you please check if this file exists on your computer?</p>
<blockquote>
<p>C:\Users\kucerabi\Desktop\Slicer 5.6.2\lib\Python\Lib\site-packages\pyacvd_clustering.cp39-win_amd64.pyd</p>
</blockquote>
<p>Maybe you have some third-party antivirus software installed that removes binaries that it does not like.</p>

---

## Post #5 by @lassoan (2024-09-25 03:16 UTC)

<p><a class="mention" href="/u/kucerabi">@kucerabi</a> have you had a chance to check if the .pyd file exists on your computer?</p>

---

## Post #6 by @kucerabi (2024-09-25 16:39 UTC)

<p>I have the .pyd file on my computer, but it still wouldn’t run. However, slicer.util.pip_install(“pyacvd&lt;0.3”) resolved the issue.</p>
<p>Thank you!</p>

---

## Post #7 by @lassoan (2024-09-25 22:41 UTC)

<p>Thank you, this information is very useful. I’ve noticed a difference between pyacvd-0.2 and pyacvd-0.3: the .pyd file in the more recent version uses OpenMP.</p>
<p><del>To test if this is indeed causing the incompatibility of pyacvd-0.3 with your computer, would you mind do these steps:<br>
-install pyacvd-0.3.0 by runnning this in the Slicer Python console: <code>pip_install('pyacvd==0.3.0')</code><br>
-download <a href="https://raw.githubusercontent.com/rorymulcahey/libomp140.x86_64.dll/refs/heads/main/libomp140.x86_64.dll">libomp140.x86_64.dll</a> library (if you want to learn more about this file, see <a href="https://github.com/rorymulcahey/libomp140.x86_64.dll">[1]</a> or <a href="https://discuss.pytorch.org/t/failed-to-import-pytorch-fbgemm-dll-or-one-of-its-dependencies-is-missing/201969/76">[2]</a>)<br>
-copy the downloaded <code>libomp140.x86_64.dll</code> to the folder: <code>C:\Users\kucerabi\Desktop\Slicer 5.6.2\lib\Python\Lib\site-packages\pyacvd\</code><br>
-test if uniform remeshing works and let us know here!</del></p>

---

## Post #8 by @lassoan (2024-09-25 22:45 UTC)

<p>The <a href="https://github.com/pyvista/pyacvd/issues/56#issuecomment-2375355929">developer of pyacvd will remove OpenMP dependency from pyacvd</a>, so you can also just wait for a few days and test with the latest pyacvd version.</p>

---

## Post #9 by @lassoan (2024-09-26 00:50 UTC)

<p>A new version of pyacvd is ready that does not depend on OpenMP. Please try if it works:</p>
<pre><code>pip_install("pyacvd==0.3.1")
</code></pre>

---
