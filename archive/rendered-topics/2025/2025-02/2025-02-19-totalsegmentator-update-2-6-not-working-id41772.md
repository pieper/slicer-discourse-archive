---
topic_id: 41772
title: "Totalsegmentator Update 2 6 Not Working"
date: 2025-02-19
url: https://discourse.slicer.org/t/41772
---

# TotalSegmentator update 2.6 Not Working

**Topic ID**: 41772
**Date**: 2025-02-19
**URL**: https://discourse.slicer.org/t/totalsegmentator-update-2-6-not-working/41772

---

## Post #1 by @Khaldoun (2025-02-19 14:54 UTC)

<p>Operating system:windows 10 Professional<br>
Slicer version: 5.8.0<br>
Expected behavior:Previous version 2.4 of TotalSementator was perfectly working but after the update to 2.6 even forcing reinstall it is not working and it should be working<br>
Actual behavior: Not working with the following error message:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\g-tnn5319433pc\AppData\Local\slicer.org\Slicer 5.8.0\bin\Python\slicer\util.py”, line 3303, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/g-tnn5319433pc/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 307, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/g-tnn5319433pc/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 1037, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/Users/g-tnn5319433pc/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 1104, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/Users/g-tnn5319433pc/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 883, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/g-tnn5319433pc/AppData/Local/slicer.org/Slicer 5.8.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\g-tnn5319433pc\AppData\Local\slicer.org\Slicer 5.8.0\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/g-tnn5319433pc/AppData/Local/Temp/Slicer/__SlicerTemp__2025-02-19_15+46+39.050/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/g-tnn5319433pc/AppData/Local/Temp/Slicer/__SlicerTemp__2025-02-19_15+46+39.050/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @Arash1 (2025-02-20 19:47 UTC)

<aside class="quote no-group" data-username="Khaldoun" data-post="1" data-topic="41772">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/3ab097/48.png" class="avatar"> Khaldoun:</div>
<blockquote>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError:</p>
</blockquote>
</aside>
<p>Hello<br>
With the new version, did you check the “PyTorch Utils” and ensure the Torch and TorchVision are correctly installed? I am not sure if you are using CUDA or not but I might not be a bad idea to uninstall and reinstall the Pytorch and then force reinstall the Python package for the TotalSegmentator.<br>
Please let me know if this helps.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1277b93dd415a6b187b0ae8b3a42db02b0db9526.png" alt="image" data-base62-sha1="2Dn6gCl5x8czU2bm0Eyq98cjpXg" width="551" height="79"></p>

---
