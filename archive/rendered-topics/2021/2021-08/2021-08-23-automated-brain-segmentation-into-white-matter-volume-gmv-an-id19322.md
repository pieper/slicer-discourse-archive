---
topic_id: 19322
title: "Automated Brain Segmentation Into White Matter Volume Gmv An"
date: 2021-08-23
url: https://discourse.slicer.org/t/19322
---

# Automated brain segmentation into White Matter Volume, GMV, and CSF Vol?

**Topic ID**: 19322
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/automated-brain-segmentation-into-white-matter-volume-gmv-and-csf-vol/19322

---

## Post #1 by @J1234 (2021-08-23 16:18 UTC)

<p>Does anyone know if there is an extension that facilitates whole brain segmentation into CSF, gray, and white matter? I downloaded BrainVolumeRefinement, which seemed to have this capability for Slicer 4.10, but since installing I haven’t been able to find it in my modules. This makes me think it wasn’t updated to be compatible with 4.11.</p>

---

## Post #2 by @pieper (2021-08-23 16:28 UTC)

<p>I’ve had good luck with this one:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/fepegar/SlicerParcellation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/fepegar/SlicerParcellation" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/419df7551fa6ffb3a38fd97ad79b6eaff5f70ddcbea86630dad4de59181f005c/fepegar/SlicerParcellation" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/fepegar/SlicerParcellation" target="_blank" rel="noopener">GitHub - fepegar/SlicerParcellation: 3D Slicer modules for brain segmentation...</a></h3>

  <p>3D Slicer modules for brain segmentation using deep learning. - GitHub - fepegar/SlicerParcellation: 3D Slicer modules for brain segmentation using deep learning.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2021-08-25 02:37 UTC)

<p><span class="mention">@fepegar</span> It seems that this extension is not in the extension index. Is there some issue with it, or you just have not had the time to submit it a pull request yet?</p>

---

## Post #4 by @J1234 (2021-08-26 03:54 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thank you. if I can get it to work this looks like it should fit the bill.</p>
<p>I downloaded a copy to my Desktop and added it to “Additional Module Paths” in Slicer. However, whenever I try to run a segmentation I get the below error. Is this related to <a class="mention" href="/u/lassoan">@lassoan</a>’s comment about this module not being in the extension index yet?</p>
<p>Importing torch…</p>
<p>Requirement already satisfied: light-the-torch in /Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (0.3.4)</p>
<p>Requirement already satisfied: pip&lt;20.3.<em>,&gt;=20.1.</em> in /Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages (from light-the-torch) (20.2.4)</p>
<p>WARNING: You are using pip version 20.2.4; however, version 21.2.4 is available.</p>
<p>You should consider upgrading via the ‘/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip’ command.<br>
Traceback (most recent call last):<br>
File “/Users/Jesse/Desktop/SlicerParcellation-master/PyTorchUtils.py”, line 44, in importTorch<br>
import torch<br>
ModuleNotFoundError: No module named ‘torch’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “/Users/Jesse/Desktop/SlicerParcellation-master/BrainParcellation.py”, line 62, in onRunButton<br>
super().onRunButton()<br>
File “/Users/Jesse/Desktop/SlicerParcellation-master/InferenceUtils.py”, line 175, in onRunButton<br>
if not self.logic.confirmDeviceOk():<br>
File “/Users/Jesse/Desktop/SlicerParcellation-master/InferenceUtils.py”, line 257, in confirmDeviceOk<br>
if self.torchLogic.getDevice() == ‘cpu’:<br>
File “/Users/Jesse/Desktop/SlicerParcellation-master/PyTorchUtils.py”, line 73, in getDevice<br>
torch = self.torch<br>
File “/Users/Jesse/Desktop/SlicerParcellation-master/PyTorchUtils.py”, line 39, in torch<br>
self._torch = self.importTorch()<br>
File “/Users/Jesse/Desktop/SlicerParcellation-master/PyTorchUtils.py”, line 47, in importTorch<br>
torch = self.installTorch()<br>
File “/Users/Jesse/Desktop/SlicerParcellation-master/PyTorchUtils.py”, line 53, in installTorch<br>
wheelUrl = self.getTorchUrl()<br>
File “/Users/Jesse/Desktop/SlicerParcellation-master/PyTorchUtils.py”, line 62, in getTorchUrl<br>
import light_the_torch as ltt<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/light_the_torch/<strong>init</strong>.py”, line 3, in <br>
from ._pip import *<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/light_the_torch/_pip/<strong>init</strong>.py”, line 1, in <br>
from .extract import *<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/light_the_torch/_pip/extract.py”, line 5, in <br>
from pip._internal.req.req_install import InstallRequirement<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/req/<strong>init</strong>.py”, line 10, in <br>
from .req_install import InstallRequirement<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/req/req_install.py”, line 35, in <br>
from pip._internal.utils.direct_url_helpers import direct_url_from_link<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/utils/direct_url_helpers.py”, line 12, in <br>
from pip._internal.vcs import vcs<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/<strong>init</strong>.py”, line 9, in <br>
import pip._internal.vcs.subversion  # noqa: F401<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/subversion.py”, line 336, in <br>
vcs.register(Subversion)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/versioncontrol.py”, line 317, in register<br>
self._registry[cls.name] = cls()<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/vcs/subversion.py”, line 191, in <strong>init</strong><br>
use_interactive = is_console_interactive()<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pip/_internal/utils/misc.py”, line 906, in is_console_interactive<br>
return sys.stdin is not None and sys.stdin.isatty()<br>
AttributeError: ‘PythonQtStdInRedirect’ object has no attribute ‘isatty’</p>

---

## Post #5 by @pieper (2021-08-26 12:50 UTC)

<aside class="quote no-group" data-username="J1234" data-post="4" data-topic="19322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/f08c70/48.png" class="avatar"> J1234:</div>
<blockquote>
<p>return sys.stdin is not None and sys.stdin.isatty()<br>
AttributeError: ‘PythonQtStdInRedirect’ object has no attribute ‘isatty’</p>
</blockquote>
</aside>
<p>This was fixed during <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/PyTorchIntegration/">Project Week</a>, so everything should be good if you use a current nightly (not the stable release).</p>

---

## Post #6 by @J1234 (2021-08-27 03:47 UTC)

<p>Can you clarify what you mean by current nightly? I re-downloaded the most current software just to be safe and I’m still getting the error. I’m using Slicer 4.11.20210226.</p>

---

## Post #7 by @pieper (2021-08-27 12:40 UTC)

<aside class="quote no-group" data-username="J1234" data-post="6" data-topic="19322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/f08c70/48.png" class="avatar"> J1234:</div>
<blockquote>
<p>Can you clarify what you mean by current nightly?</p>
</blockquote>
</aside>
<p>I mean when you go to <a href="http://download.slicer.org">download.slicer.org</a> you pick the preview version with the most recent date.</p>

---
