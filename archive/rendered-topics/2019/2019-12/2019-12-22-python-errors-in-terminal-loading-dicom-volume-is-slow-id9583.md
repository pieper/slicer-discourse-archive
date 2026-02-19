---
topic_id: 9583
title: "Python Errors In Terminal Loading Dicom Volume Is Slow"
date: 2019-12-22
url: https://discourse.slicer.org/t/9583
---

# Python errors in terminal, loading DICOM volume is slow

**Topic ID**: 9583
**Date**: 2019-12-22
**URL**: https://discourse.slicer.org/t/python-errors-in-terminal-loading-dicom-volume-is-slow/9583

---

## Post #1 by @chir.set (2019-12-22 17:30 UTC)

<p>The following errors appear in terminal with home built Slicer unchanged, and not with binaries from your repository :</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/<strong>init</strong>.py”, line 17, in <br>
from . import multiarray<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py”, line 14, in <br>
from . import overrides<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py”, line 7, in <br>
from numpy.core._multiarray_umath import (<br>
ModuleNotFoundError: No module named ‘numpy.core._multiarray_umath’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/home/user/programs/Slicer/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 1, in <br>
import numpy<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/<strong>init</strong>.py”, line 142, in <br>
from . import core<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/<strong>init</strong>.py”, line 47, in <br>
raise ImportError(msg)<br>
ImportError:</p>
<p>IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!</p>
<p>Importing the numpy c-extensions failed.</p>
<ul>
<li>
<p>Try uninstalling and reinstalling numpy.</p>
</li>
<li>
<p>If you have already done that, then:</p>
<ol>
<li>Check that you expected to use Python3.6 from “”,<br>
and that you have no directories in your PATH or PYTHONPATH that can<br>
interfere with the Python and numpy version “1.17.3” you’re trying to use.</li>
<li>If (1) looks fine, you can open a new issue at<br>
<a href="https://github.com/numpy/numpy/issues" class="inline-onebox" rel="noopener nofollow ugc">Issues · numpy/numpy · GitHub</a>.  Please include details on:
<ul>
<li>how you installed Python</li>
<li>how you installed numpy</li>
<li>your operating system</li>
<li>whether or not you have multiple versions of Python installed</li>
<li>if you built from source, your compiler versions and ideally a build log</li>
</ul>
</li>
</ol>
</li>
<li>
<p>If you’re working with a numpy git repository, try <code>git clean -xdf</code><br>
(removes all files not under version control) and rebuild numpy.</p>
</li>
</ul>
<p>Note: this error has many possible causes, so please don’t comment on<br>
an existing issue about this - open a new one instead.</p>
<p>Original error was: No module named ‘numpy.core._multiarray_umath’</p>
<p>loadSourceAsModule - Failed to load file “/home/user/programs/Slicer/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py”  as module “DICOMScalarVolumePlugin” !<br>
Fail to instantiate module  “DICOMScalarVolumePlugin”<br>
Traceback (most recent call last):<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/<strong>init</strong>.py”, line 17, in <br>
from . import multiarray<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py”, line 14, in <br>
from . import overrides<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py”, line 7, in <br>
from numpy.core._multiarray_umath import (<br>
ModuleNotFoundError: No module named ‘numpy.core._multiarray_umath’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/home/user/programs/Slicer/bin/…/lib/Slicer-4.11/qt-scripted-modules/Editor.py”, line 4, in <br>
import EditorLib<br>
File “/home/user/programs/Slicer/lib/Slicer-4.11/qt-scripted-modules/EditorLib/<strong>init</strong>.py”, line 37, in <br>
exec(“from .{0} import {0}Options, {0}Tool, {0}Logic, {0}”.format(effectName))<br>
File “”, line 1, in <br>
File “/home/user/programs/Slicer/lib/Slicer-4.11/qt-scripted-modules/EditorLib/PaintEffect.py”, line 10, in <br>
import numpy<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/<strong>init</strong>.py”, line 142, in <br>
from . import core<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/<strong>init</strong>.py”, line 47, in <br>
raise ImportError(msg)<br>
ImportError:</p>
<p>IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!</p>
<p>Importing the numpy c-extensions failed.</p>
<ul>
<li>
<p>Try uninstalling and reinstalling numpy.</p>
</li>
<li>
<p>If you have already done that, then:</p>
<ol>
<li>Check that you expected to use Python3.6 from “”,<br>
and that you have no directories in your PATH or PYTHONPATH that can<br>
interfere with the Python and numpy version “1.17.3” you’re trying to use.</li>
<li>If (1) looks fine, you can open a new issue at<br>
<a href="https://github.com/numpy/numpy/issues" class="inline-onebox" rel="noopener nofollow ugc">Issues · numpy/numpy · GitHub</a>.  Please include details on:
<ul>
<li>how you installed Python</li>
<li>how you installed numpy</li>
<li>your operating system</li>
<li>whether or not you have multiple versions of Python installed</li>
<li>if you built from source, your compiler versions and ideally a build log</li>
</ul>
</li>
</ol>
</li>
<li>
<p>If you’re working with a numpy git repository, try <code>git clean -xdf</code><br>
(removes all files not under version control) and rebuild numpy.</p>
</li>
</ul>
<p>Note: this error has many possible causes, so please don’t comment on<br>
an existing issue about this - open a new one instead.</p>
<p>Original error was: No module named ‘numpy.core._multiarray_umath’</p>
<p>loadSourceAsModule - Failed to load file “/home/user/programs/Slicer/bin/…/lib/Slicer-4.11/qt-scripted-modules/Editor.py”  as module “Editor” !<br>
Fail to instantiate module  “Editor”<br>
Traceback (most recent call last):<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/<strong>init</strong>.py”, line 17, in <br>
from . import multiarray<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py”, line 14, in <br>
from . import overrides<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/overrides.py”, line 7, in <br>
from numpy.core._multiarray_umath import (<br>
ModuleNotFoundError: No module named ‘numpy.core._multiarray_umath’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/home/user/programs/Slicer/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 5, in <br>
import vtk.util.numpy_support<br>
File “/home/user/programs/Slicer/lib/Slicer-4.11/python3.6/site-packages/vtkmodules/util/numpy_support.py”, line 31, in <br>
import numpy<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/<strong>init</strong>.py”, line 142, in <br>
from . import core<br>
File “/home/user/programs/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/<strong>init</strong>.py”, line 47, in <br>
raise ImportError(msg)<br>
ImportError:</p>
<p>IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!</p>
<p>Importing the numpy c-extensions failed.</p>
<ul>
<li>
<p>Try uninstalling and reinstalling numpy.</p>
</li>
<li>
<p>If you have already done that, then:</p>
<ol>
<li>Check that you expected to use Python3.6 from “”,<br>
and that you have no directories in your PATH or PYTHONPATH that can<br>
interfere with the Python and numpy version “1.17.3” you’re trying to use.</li>
<li>If (1) looks fine, you can open a new issue at<br>
<a href="https://github.com/numpy/numpy/issues" class="inline-onebox" rel="noopener nofollow ugc">Issues · numpy/numpy · GitHub</a>.  Please include details on:
<ul>
<li>how you installed Python</li>
<li>how you installed numpy</li>
<li>your operating system</li>
<li>whether or not you have multiple versions of Python installed</li>
<li>if you built from source, your compiler versions and ideally a build log</li>
</ul>
</li>
</ol>
</li>
<li>
<p>If you’re working with a numpy git repository, try <code>git clean -xdf</code><br>
(removes all files not under version control) and rebuild numpy.</p>
</li>
</ul>
<p>Note: this error has many possible causes, so please don’t comment on<br>
an existing issue about this - open a new one instead.</p>
<p>Original error was: No module named ‘numpy.core._multiarray_umath’</p>
<p>loadSourceAsModule - Failed to load file “/home/user/programs/Slicer/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py”  as module “MultiVolumeImporterPlugin” !<br>
Fail to instantiate module  “MultiVolumeImporterPlugin”<br>
The following modules failed to be instantiated:<br>
DICOMScalarVolumePlugin<br>
Editor<br>
MultiVolumeImporterPlugin<br>
Switch to module:  “Volumes”</p>
</blockquote>
<p>Slicer is usable, but loading a DICOM 512x512x2000+ volume gets <em>2 to 3 times slower</em>, i.e, about 10 mins! This, when the volume is loaded with the ‘Add data’ menu item.</p>
<p>With the DICOM module, after clicking the Import DICOM files button, the studies are well listed, but none can be loaded, and thers’s no console messages.</p>
<p>Commit 78b60185faa2e9 mentions building on Arch with system python. If it’s mandatory, I’ll do that. I wish you could comment on this issue beforehand.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2019-12-22 19:21 UTC)

<p>It seems that numpy build failed. Try rebuilding latest master version from scratch and report the <em>first</em> error that occurs during compilation (you did have not provided here any information about Python/numpy build error, which most likely the root cause of the runtime error).</p>
<p>DICOM module requires Python, so if you have any Python errors then DICOM module may not work.</p>

---

## Post #3 by @chir.set (2019-12-23 13:27 UTC)

<p>These errors do not happen after a clean build. DICOM module loads any series. Could not evaluate speed wit 'Add data ’ menu item yet.</p>
<p>Thanks.</p>

---
