# Elastix not working

**Topic ID**: 43205
**Date**: 2025-06-03
**URL**: https://discourse.slicer.org/t/elastix-not-working/43205

---

## Post #1 by @danielacpanciera (2025-06-03 12:58 UTC)

<p>Hi all,</p>
<p>I recently installed Slicer 5.8.0 (and also 5.8.1) on my work’s laptop and I am having the following issue with Elastix since the update on <em>Mon Mar 03 2025</em>.</p>
<p>[Python] Elastix primary method failed: module ‘Elastix’ has no attribute ‘RegistrationPresets_ParameterFilenames’. Falling back to alternative method.<br>
Traceback (most recent call last):<br>
File “C:/Users/Public/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/OpenDose3D/lib/Slicer-5.8/qt-scripted-modules/OpenDose3D.py”, line 1228, in onRunTestButton<br>
self.test.FullTest_positive()<br>
File “C:\Users\Public\AppData\Local\slicer.org\Slicer 5.8.1\slicer.org\Extensions-33241\OpenDose3D\lib\Slicer-5.8\qt-scripted-modules\Logic\OpenDose3DTest.py”, line 542, in FullTest_positive<br>
self.logic.createTransforms(referenceNode.data)<br>
File “C:\Users\Public\AppData\Local\slicer.org\Slicer 5.8.1\slicer.org\Extensions-33241\OpenDose3D\lib\Slicer-5.8\qt-scripted-modules\Logic\OpenDose3DLogic.py”, line 1097, in createTransforms<br>
elastixLogic.registerVolumes(<br>
File “C:/Users/Public/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerElastix/lib/Slicer-5.8/qt-scripted-modules/Elastix.py”, line 581, in registerVolumes<br>
self.logProcessOutput(elastixProcess)<br>
File “C:/Users/Public/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerElastix/lib/Slicer-5.8/qt-scripted-modules/Elastix.py”, line 527, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
subprocess.CalledProcessError: Command ‘elastix’ returned non-zero exit status 1.</p>
<p>On my personal laptop (Slicer 5.8.0) with Elastix updated on Fri Jan 24 2025 it is working fine.<br>
Is there a way to install the previous Elastix version?</p>

---

## Post #2 by @danielacpanciera (2025-06-05 15:26 UTC)

<p>From what I was told, it seems the problem started with version 5.8.0 of 3D Slicer, and it appears to affect some Windows systems. I was recommended to install a previous version of 3D Slicer (e.g. 5.6.2) and manually install OpenDose3D (download from gitlab), and it has worked fine.</p>

---
