---
topic_id: 44331
title: "Failed To Install Pytorch Offline"
date: 2025-09-03
url: https://discourse.slicer.org/t/44331
---

# Failed to Install PyTorch Offline

**Topic ID**: 44331
**Date**: 2025-09-03
**URL**: https://discourse.slicer.org/t/failed-to-install-pytorch-offline/44331

---

## Post #1 by @bulala (2025-09-03 14:26 UTC)

<p>I‘m trying to install Pytorch for 3D Slicer 5.8.1 on a computer that has no internet access.Although I have already installed PyTorch, a “PyTorch not installed” prompt appears when I try to activate the TotalSegmentator License. Could this be because the PyTorch version I’m using is too old and not detected?</p>
<p>The version I currently have is [please fill in your current PyTorch version here]. How can I resolve this issue? Could you provide a download link for a newer PyTorch version compatible with 3D Slicer 5.8.1?</p>
<p>Additionally, I would like to know if these extension tools can be used without an internet connection.</p>
<p>install:Y:\3dSlice\<strong>Slicer-5.8.1</strong>-win-amd64\<a href="https://slicer.org/" rel="noopener nofollow ugc">slicer.org</a>\Extensions-33241\PyTorch\lib**\Slicer-5.0\**qt-scripted-modules</p>
<p>version from :<strong>30822-win-amd64-PyTorch-gitb1f33d6-2022-06-18 (1)</strong></p>
<p>failed log:</p>
<p>Failed to set TotalSegmentator license.</p>
<p>This module requires PyTorch extension. Install it from the Extensions Manager.</p>
<p>Traceback (most recent call last):</p>
<p>File “Y:/3dSlice/Slicer-5.8.1-win-amd64/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 778, in setupPythonRequirements</p>
<p>import PyTorchUtils</p>
<p>ModuleNotFoundError: No module named ‘PyTorchUtils’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “Y:\3dSlice\Slicer-5.8.1-win-amd64\bin\Python\slicer\util.py”, line 3303, in tryWithErrorDisplay</p>
<p>yield</p>
<p>File “Y:/3dSlice/Slicer-5.8.1-win-amd64/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 336, in onSetLicense</p>
<p>self.logic.setupPythonRequirements()</p>
<p>File “Y:/3dSlice/Slicer-5.8.1-win-amd64/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 780, in setupPythonRequirements</p>
<p>raise InstallError(“This module requires <strong>PyTorch</strong> extension. Install it from the Extensions Manager.”)</p>
<p>TotalSegmentator.InstallError: This module requires PyTorch extension. Install it from the Extensions Manager.</p>

---
