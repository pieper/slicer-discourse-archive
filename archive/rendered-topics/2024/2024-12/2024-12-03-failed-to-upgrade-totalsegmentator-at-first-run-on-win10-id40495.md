---
topic_id: 40495
title: "Failed To Upgrade Totalsegmentator At First Run On Win10"
date: 2024-12-03
url: https://discourse.slicer.org/t/40495
---

# Failed to upgrade TotalSegmentator at first run on WIN10

**Topic ID**: 40495
**Date**: 2024-12-03
**URL**: https://discourse.slicer.org/t/failed-to-upgrade-totalsegmentator-at-first-run-on-win10/40495

---

## Post #1 by @sfcwefvwr (2024-12-03 15:04 UTC)

<p>[Python] Failed to upgrade TotalSegmentator<br>
[Python] Command ‘[‘D:/YYC/software/slicer/Slicer 5.7.0-2024-11-29/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘black;extra’, ‘==’, ‘dev’]’ returned non-zero exit status 2.<br>
Traceback (most recent call last):<br>
File “D:/YYC/software/slicer/Slicer 5.7.0-2024-11-29/slicer.org/Extensions-33134/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 319, in onPackageUpgrade<br>
self.logic.setupPythonRequirements(upgrade=True)<br>
File “D:/YYC/software/slicer/Slicer 5.7.0-2024-11-29/slicer.org/Extensions-33134/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 819, in setupPythonRequirements<br>
self.pipInstallSelective(‘nnunetv2’, nnunetRequirement, packagesToSkip)<br>
File “D:/YYC/software/slicer/Slicer 5.7.0-2024-11-29/slicer.org/Extensions-33134/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 706, in pipInstallSelective<br>
slicer.util.pip_install(requirement)<br>
File “D:\YYC\software\slicer\Slicer 5.7.0-2024-11-29\bin\Python\slicer\util.py”, line 3934, in pip_install<br>
_executePythonModule(“pip”, args)<br>
File “D:\YYC\software\slicer\Slicer 5.7.0-2024-11-29\bin\Python\slicer\util.py”, line 3888, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “D:\YYC\software\slicer\Slicer 5.7.0-2024-11-29\bin\Python\slicer\util.py”, line 3854, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘D:/YYC/software/slicer/Slicer 5.7.0-2024-11-29/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘black;extra’, ‘==’, ‘dev’]’ returned non-zero exit status 2.</p>

---
