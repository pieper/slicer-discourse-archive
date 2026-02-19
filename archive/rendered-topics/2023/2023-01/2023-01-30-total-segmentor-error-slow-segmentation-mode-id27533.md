---
topic_id: 27533
title: "Total Segmentor Error Slow Segmentation Mode"
date: 2023-01-30
url: https://discourse.slicer.org/t/27533
---

# Total Segmentor error ( slow segmentation mode)

**Topic ID**: 27533
**Date**: 2023-01-30
**URL**: https://discourse.slicer.org/t/total-segmentor-error-slow-segmentation-mode/27533

---

## Post #1 by @Chuns_SS (2023-01-30 05:08 UTC)

<p>I’m getting the following error using slower long segmentation mode. Fast seems ok.<br>
I’m on a linux Ubuntu 22.04 platform Nvidia rtx 3060, cuda 11.8 cudnn 8.7.0. Git installed</p>
<p>ReferenceImageExtentOffset attribute was not found in NRRD segmentation file. Assume no offset.</p>
<p>Traceback (most recent call last):<br>
File “/home/sam/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/home/sam/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 749, in process<br>
self.logProcessOutput(proc)<br>
File “/home/sam/Slicer-5.3.0-2023-01-28-linux-amd64/NA-MIC/Extensions-31553/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 656, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/home/sam/Slicer-5.3.0-2023-01-28-linux-amd64/bin/…/bin/PythonSlicer’, ‘/home/sam/Slicer-5.3.0-2023-01-28-linux-amd64/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/tmp/Slicer-sam/__SlicerTemp__2023-01-30_01+05+23.185/total-segmentator-input.nii’, ‘-o’, ‘/tmp/Slicer-sam/__SlicerTemp__2023-01-30_01+05+23.185/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>
<p>Any help most appreciated.</p>

---
