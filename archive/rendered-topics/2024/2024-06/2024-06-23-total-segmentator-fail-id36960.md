---
topic_id: 36960
title: "Total Segmentator Fail"
date: 2024-06-23
url: https://discourse.slicer.org/t/36960
---

# Total segmentator fail

**Topic ID**: 36960
**Date**: 2024-06-23
**URL**: https://discourse.slicer.org/t/total-segmentator-fail/36960

---

## Post #1 by @changjiang (2024-06-23 00:55 UTC)

<p>[Python] Failed to compute results.<br>
[Python] Command '[‘C:/ProgramData/NA-MIC/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, '<a href="https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip'%5D'" rel="noopener nofollow ugc">https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip’]’</a> returned non-zero exit status 2.<br>
Traceback (most recent call last):<br>
File “C:/ProgramData/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 262, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “C:/ProgramData/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 664, in setupPythonRequirements<br>
slicer.util.pip_install(self.totalSegmentatorPythonPackageDownloadUrl)<br>
File “C:\ProgramData\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py”, line 3578, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\ProgramData\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py”, line 3540, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\ProgramData\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py”, line 3509, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command '[‘C:/ProgramData/NA-MIC/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, '<a href="https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip'%5D'" rel="noopener nofollow ugc">https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip’]’</a> returned non-zero exit status 2.</p>

---

## Post #2 by @lassoan (2024-06-25 14:42 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-segment-uterus-and-ovary-automatically/37006">How to segment uterus and ovary automatically</a></p>

---
