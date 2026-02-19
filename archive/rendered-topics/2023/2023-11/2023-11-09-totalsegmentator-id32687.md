---
topic_id: 32687
title: "Totalsegmentator"
date: 2023-11-09
url: https://discourse.slicer.org/t/32687
---

# TotalSegmentator

**Topic ID**: 32687
**Date**: 2023-11-09
**URL**: https://discourse.slicer.org/t/totalsegmentator/32687

---

## Post #1 by @yuanw (2023-11-09 03:02 UTC)

<p>When I use the Total Segmentator module for total segmentation, if I select full resolution, the following error will appear, but if I select fast, the following error will not appear.</p>
<p>Failed to compute results.</p>
<p>Command ‘[‘C:/Users/hooray/AppData/Local/slicer.org/Slicer 5.4.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\hooray\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Windows/Temp/Slicer/__SlicerTemp__2023-11-09_10+57+56.252/total-segmentator-input.nii’, ‘-o’, ‘C:/Windows/Temp/Slicer/__SlicerTemp__2023-11-09_10+57+56.252/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @rbumm (2023-11-09 17:22 UTC)

<p>It is probably a GPU memory issue. What is your GPU (model, brand?)</p>

---

## Post #3 by @yuanw (2023-11-13 08:25 UTC)

<p>I don’t have a GPU with more than 7G of video memory, so I am using CPU computing. Can’t CPU computing use full resolution?</p>

---

## Post #4 by @rbumm (2023-11-13 10:43 UTC)

<p>Yes, you can configure Pytorch to use the CPU only. Uninstall Pytorch, then select “cpu”, then install Pytorch again.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/466cbca1bb4f1c17c30407340c7931ec058d9111.png" alt="image" data-base62-sha1="a30odfh3wXsp4hhuwCRyqDzsfRf" width="520" height="490"></p>

---

## Post #5 by @yuanw (2023-11-17 01:57 UTC)

<p>I changed my computer to a 4060laptop gpu, and now I get the following error</p>
<p>WARNING: Ignoring invalid distribution -illow (e:\soft\slicer 5.5.0-2023-11-14\lib\python\lib\site-packages)<br>
Requirement already satisfied: pillow&lt;10.1 in e:\soft\slicer 5.5.0-2023-11-14\lib\python\lib\site-packages (10.0.1)<br>
WARNING: Ignoring invalid distribution -illow (e:\soft\slicer 5.5.0-2023-11-14\lib\python\lib\site-packages)<br>
WARNING: There was an error checking the latest version of pip.<br>
E:/Soft/Slicer 5.5.0-2023-11-14/slicer.org/Extensions-32325/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:880: UserWarning: ‘has_cuda’ is deprecated, please use ‘torch.backends.cuda.is_built()’<br>
cuda = torch.cuda if torch.has_cuda and torch.cuda.is_available() else None<br>
[Python] Failed to compute results.<br>
[Python] Command ‘[‘E:/Soft/Slicer 5.5.0-2023-11-14/bin/…/bin\PythonSlicer.EXE’, ‘E:\Soft\Slicer 5.5.0-2023-11-14\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/13790/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-17_09+51+55.923/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/13790/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-17_09+51+55.923/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.<br>
Traceback (most recent call last):<br>
File “E:/Soft/Slicer 5.5.0-2023-11-14/slicer.org/Extensions-32325/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 292, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “E:/Soft/Slicer 5.5.0-2023-11-14/slicer.org/Extensions-32325/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 967, in process<br>
self.logProcessOutput(proc)<br>
File “E:/Soft/Slicer 5.5.0-2023-11-14/slicer.org/Extensions-32325/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 787, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘E:/Soft/Slicer 5.5.0-2023-11-14/bin/…/bin\PythonSlicer.EXE’, ‘E:\Soft\Slicer 5.5.0-2023-11-14\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/13790/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-17_09+51+55.923/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/13790/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-17_09+51+55.923/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>

---
