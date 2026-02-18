# Failed to compute results. No module named 'torch'

**Topic ID**: 29280
**Date**: 2023-05-04
**URL**: https://discourse.slicer.org/t/failed-to-compute-results-no-module-named-torch/29280

---

## Post #1 by @TSMemo (2023-05-04 03:31 UTC)

<p>Hi,<br>
I’m having trouble applying the program ‘Total Segmentator’. I’ve tried every possible method below Mr Anish_Raj’s question posted on December 22, 2022 but still encountered a failure about PyTorch as mentioned in the topic.<br>
Detailed error:<br>
Traceback (most recent call last):<br>
File “E:\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “E:/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 255, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “E:/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 618, in setupPythonRequirements<br>
torch = torchLogic.installTorch(askConfirmation=True)<br>
File “E:/Slicer 5.2.2/NA-MIC/Extensions-31382/PyTorch/lib/Slicer-5.2/qt-scripted-modules/PyTorchUtils.py”, line 195, in installTorch<br>
import torch<br>
ModuleNotFoundError: No module named ‘torch’<br>
Please tell me which steps need to be corrected,<br>
Thanks.</p>

---

## Post #2 by @rbumm (2023-05-04 12:27 UTC)

<p>Please start all over again and <a href="https://discourse.slicer.org/t/totalsegmentator-error-at-first-run-command-pip-install-git-https-github-com-wasserth-totalsegmentator-git-no-deps-returned-non-zero-exit-status/26715/38">follow these instructions</a>.</p>

---

## Post #3 by @TSMemo (2023-05-05 06:39 UTC)

<aside class="quote no-group" data-username="TSMemo" data-post="1" data-topic="29280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsmemo/48/65881_2.png" class="avatar"> TSMemo:</div>
<blockquote>
<p>m</p>
</blockquote>
</aside>
<p>Thanks a lot for your instructions, it turned out to be a problem with the modules of Python that I installed before, and the performance of my hardware was not good enough for some examples about image processing. I tried your steps again strictly in the lab for postgraduates and got the results successfully.</p>

---
