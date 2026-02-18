# Error with DiffusionQC module (GradQC)

**Topic ID**: 17330
**Date**: 2021-04-26
**URL**: https://discourse.slicer.org/t/error-with-diffusionqc-module-gradqc/17330

---

## Post #1 by @amvoid (2021-04-26 12:31 UTC)

<p>Operating system: win10/Ubuntu 20<br>
Slicer version: 4.11</p>
<p>After I install DiffusionQC extension, there come out an error whenever I star Slicer. I notice that GradQC failed to install, but I don’t know why.</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\Henry\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/Henry/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/DiffusionQC/lib/Slicer-4.11/qt-scripted-modules/GradQC.py”, line 5, in <br>
from gradqclib.slicerUserInteraction import slicerGUI<br>
File “C:\Users\Henry\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\DiffusionQC\lib\Slicer-4.11\qt-scripted-modules\gradqclib\slicerUserInteraction.py”, line 6, in <br>
from diffusionqclib.dwi_attributes import dwi_attributes<br>
File “C:\Users\Henry\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\DiffusionQC\Lib\site-packages\diffusionqclib\dwi_attributes.py”, line 4, in <br>
from nhdr_write import nhdr_write<br>
ModuleNotFoundError: No module named ‘nhdr_write’</p>
<p>And the same problem happend in Ubuntu system.</p>

---

## Post #2 by @lassoan (2021-04-26 23:20 UTC)

<p>I’m not sure if DiffusionQC extension developers monitor the Slicer forum, so it could be useful to report the problem at their issue tracker. Please copy here the link to the bug report.</p>

---

## Post #3 by @amvoid (2021-04-27 01:58 UTC)

<p><a href="https://github.com/pnlbwh/SlicerDiffusionQC/issues/46#38" rel="noopener nofollow ugc">Fail to instantiate module “GradQC” with Slicer 4.11 · Issue #46 · pnlbwh/SlicerDiffusionQC (github.com)</a></p>
<p><a href="https://github.com/pnlbwh/SlicerDiffusionQC/issues/42" rel="noopener nofollow ugc">Relative import necessary for Slicer-4.11 · Issue #42 · pnlbwh/SlicerDiffusionQC (github.com)</a></p>

---

## Post #4 by @amvoid (2021-04-27 03:14 UTC)

<p>There are some changes in version 4.11 and DiffusionQC don’t match the new version. I reinstalled version 4.10, but didn’t find the extension at all in Extensions Manager. Weird…</p>

---

## Post #5 by @lassoan (2021-05-01 14:23 UTC)

<p>You cannot use extensions that are built for Slicer with a different major or minor version. Thanks for including links to the bug reports, I can see that you are working with the developer to resolve the issues.</p>

---
