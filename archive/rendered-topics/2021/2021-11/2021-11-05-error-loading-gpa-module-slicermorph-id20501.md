# Error loading GPA module (Slicermorph)

**Topic ID**: 20501
**Date**: 2021-11-05
**URL**: https://discourse.slicer.org/t/error-loading-gpa-module-slicermorph/20501

---

## Post #1 by @Ale (2021-11-05 18:18 UTC)

<p>Hi I did a fresh install of Slicer (4.11.20210226) in a Linux machine (Debian stable branch). I installed Slicermorph trough Extension Manager without a problem. But after restart can’t run GPA module. Running Slicer in terminal I get this error:</p>
<p>./Slicer<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/marmo/Descargas/Slicer-4.11.20210226-linux-amd64/lib/Python/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/home/marmo/Descargas/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/GPA.py”, line 14, in <br>
import Support.gpa_lib as gpa_lib<br>
File “/home/marmo/Descargas/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/Support/gpa_lib.py”, line 4, in <br>
import scipy.linalg as sp<br>
File “/home/marmo/Descargas/Slicer-4.11.20210226-linux-amd64/lib/Python/lib/python3.6/site-packages/scipy/linalg/<strong>init</strong>.py”, line 194, in <br>
from .misc import *<br>
File “/home/marmo/Descargas/Slicer-4.11.20210226-linux-amd64/lib/Python/lib/python3.6/site-packages/scipy/linalg/misc.py”, line 3, in <br>
from .blas import get_blas_funcs<br>
File “/home/marmo/Descargas/Slicer-4.11.20210226-linux-amd64/lib/Python/lib/python3.6/site-packages/scipy/linalg/blas.py”, line 213, in <br>
from scipy.linalg import _fblas<br>
ImportError: /home/marmo/Descargas/Slicer-4.11.20210226-linux-amd64/lib/Python/lib/python3.6/site-packages/scipy/linalg/_fblas.cpython-36m-x86_64-linux-gnu.so: ELF load command address/offset not properly aligned<br>
loadSourceAsModule - Failed to load file “/home/marmo/Descargas/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/GPA.py”  as module “GPA” !<br>
Fail to instantiate module  “GPA”<br>
libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
libpng warning: iCCP: known incorrect sRGB profile<br>
The following modules failed to be instantiated:<br>
GPA<br>
Switch to module:  “Welcome”</p>
<p>Sytem:<br>
Distributor ID: Debian<br>
Description:    Debian GNU/Linux 11 (bullseye)<br>
Release:        11<br>
Codename:       bullseye</p>
<p>Thanks in advance</p>
<p>Ale</p>

---

## Post #2 by @muratmaga (2021-11-05 18:21 UTC)

<p>I have seen this error, not sure why it happens,as we do not install scipy. But this should fix:</p>
<ol>
<li>Open a fresh slicer,</li>
<li>go to python window and type</li>
<li><code>pip_uninstall("scipy")</code></li>
<li><code>pip_install("scipy")</code></li>
<li>restart your slicer and try gpa again.</li>
</ol>

---

## Post #3 by @jamesobutler (2021-11-05 19:39 UTC)

<p>This was resolved in <a href="https://github.com/Slicer/Slicer/commit/fef09b54bd55a5b6bd5870f6f05cde988f8691e3" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix import of python modules on Linux selectively stripping libr… · Slicer/Slicer@fef09b5 · GitHub</a>. It shouldn’t be a problem if you use latest Slicer Preview as that commit came a few days after the latest Stable release back in February.</p>

---
