---
topic_id: 42528
title: "Dentalsegmentator And Totalsegmentator Error"
date: 2025-04-10
url: https://discourse.slicer.org/t/42528
---

# DentalSegmentator and TotalSegmentator error

**Topic ID**: 42528
**Date**: 2025-04-10
**URL**: https://discourse.slicer.org/t/dentalsegmentator-and-totalsegmentator-error/42528

---

## Post #1 by @Laura_Rodriguez1 (2025-04-10 18:24 UTC)

<p>HI, I NEED HELP, I TRY TO USE TOTAL AND DENTAL SEGMENTATOR AND I GET THE FOLLOWING ERRORS</p>
<p>TOTAL SEGMENTATOR ERROR<br>
Traceback (most recent call last):<br>
File “C:\Users\LENOVO}\AppData\Local\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py”, line 3303, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/LENOVO}/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 319, in onPackageUpgrade<br>
self.logic.setupPythonRequirements(upgrade=True)<br>
File “C:/Users/LENOVO}/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 818, in setupPythonRequirements<br>
raise InstallError(“This module requires SlicerNNUNet extension. Install it from the Extensions Manager.”)<br>
TotalSegmentator.InstallError: This module requires SlicerNNUNet extension. Install it from the Extensions Manager.</p>
<p>DENTAL SEGMENTATOR ERROR</p>
<p>Start nnUNet install with requirements : nnunetv2<br>
Installing nnunetv2 --no-deps…<br>
Install returned non-zero exit status : Command ‘[‘C:/Users/LENOVO}/AppData/Local/slicer.org/Slicer 5.8.1/bin/../bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘nnunetv2’, ‘–no-deps’]’ returned non-zero exit status 1.. Attempting to continue…<br>
2025/04/10 13:18:29.470 :: Error occurred during install : nnunetv2</p>

---
