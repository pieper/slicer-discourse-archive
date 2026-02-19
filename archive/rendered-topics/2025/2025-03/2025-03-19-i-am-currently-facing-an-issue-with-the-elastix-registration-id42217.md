---
topic_id: 42217
title: "I Am Currently Facing An Issue With The Elastix Registration"
date: 2025-03-19
url: https://discourse.slicer.org/t/42217
---

# I am currently facing an issue with the Elastix registration module in 3D Slicer 

**Topic ID**: 42217
**Date**: 2025-03-19
**URL**: https://discourse.slicer.org/t/i-am-currently-facing-an-issue-with-the-elastix-registration-module-in-3d-slicer/42217

---

## Post #1 by @xiaoguan (2025-03-19 12:52 UTC)

<p>Dear users of slicer,</p>
<p>I hope this message finds you well. I am currently facing an issue with the Elastix registration module in 3D Slicer and would greatly appreciate your assistance in resolving it.The error log is below:<br>
Traceback (most recent call last):<br>
File “C:/Slicer 5.9.0-2025-02-12/slicer.org/Extensions-33478/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py”, line 296, in onApplyButton<br>
self.logic.registerVolumesUsingParameterNode(self._parameterNode)<br>
File “C:/Slicer 5.9.0-2025-02-12/slicer.org/Extensions-33478/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py”, line 534, in registerVolumesUsingParameterNode<br>
self.registerVolumes(<br>
File “C:/Slicer 5.9.0-2025-02-12/slicer.org/Extensions-33478/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py”, line 581, in registerVolumes<br>
self.logProcessOutput(elastixProcess)<br>
File “C:/Slicer 5.9.0-2025-02-12/slicer.org/Extensions-33478/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py”, line 527, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
subprocess.CalledProcessError: Command ‘elastix’ returned non-zero exit status 1.</p>

---

## Post #2 by @lassoan (2025-03-19 12:56 UTC)

<p>There were some issues in Elastix that were solved. Please try the latest Slicer Stable Release (and update Elastix) or latest Slicer Preview Release. If you still encounter problems, copy here the application log (menu: Help / Report a bug), which contains the error message that Elastix provides.</p>

---

## Post #3 by @xiaoguan (2025-03-20 11:16 UTC)

<p>Thank you for your guidance. I have followed your suggestions and updated both 3D Slicer and Elastix. Unfortunately, the same error persists. Below are the application log:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - Session start time .......: 20250320_190813
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - Slicer version ...........: 5.9.0-2025-03-17 (revision 33550 / d89d014) win-amd64 - installed release
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 19041, Code Page 65001) - 64-bit
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - Memory ...................: 8078 MB physical, 12430 MB virtual
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - DCMTK configuration ......: version 3.6.8, no SSL
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - Application path .........: C:/Slicer 5.9.0-2025-03-17/bin
[DEBUG][Qt] 20.03.2025 19:08:13 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-33550/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules
[DEBUG][Python] 20.03.2025 19:08:16 [Python] (C:\Slicer 5.9.0-2025-03-17\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 20.03.2025 19:08:16 [Python] (C:\Slicer 5.9.0-2025-03-17\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 20.03.2025 19:08:16 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Python] 20.03.2025 19:08:16 [Python] (C:\Slicer 5.9.0-2025-03-17\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: Elastix
[DEBUG][Qt] 20.03.2025 19:08:24 [] (unknown:0) - "Volume" Reader has successfully read the file "E:/glioma/ba ai ping/1/20230719_210340t1mpragetrap2iso10s012a1001.nii" "[0.28s]"
[DEBUG][Qt] 20.03.2025 19:08:25 [] (unknown:0) - "Volume" Reader has successfully read the file "E:/glioma/ba ai ping/1/20230719_210340t1tirmtradarkfluidp2s005a1001.nii" "[0.07s]"
[DEBUG][Qt] 20.03.2025 19:08:25 [] (unknown:0) - "Volume" Reader has successfully read the file "E:/glioma/ba ai ping/1/20230719_210340t2bladetrap2s006a1001.nii" "[0.06s]"
[DEBUG][Qt] 20.03.2025 19:08:25 [] (unknown:0) - "Volume" Reader has successfully read the file "E:/glioma/ba ai ping/1/20230719_210340t2tirmtradarkfluidp3s007a1001.nii" "[0.12s]"
[DEBUG][Qt] 20.03.2025 19:08:25 [] (unknown:0) - "Volume" Reader has successfully read the file "E:/glioma/ba ai ping/1/20230719_210340resolve3scantracetra160p2s010a1001.nii" "[0.05s]"
[DEBUG][Qt] 20.03.2025 19:08:31 [] (unknown:0) - Switch to module:  "Elastix"
[INFO][Python] 20.03.2025 19:09:18 [Python] (C:/Slicer 5.9.0-2025-03-17/slicer.org/Extensions-33550/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py:411) - Volume registration is started in working directory: E:/elastix/Elastix/20250320_190918_164
[INFO][Python] 20.03.2025 19:09:18 [Python] (C:/Slicer 5.9.0-2025-03-17/slicer.org/Extensions-33550/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py:411) - Register volumes...
[INFO][Python] 20.03.2025 19:09:18 [Python] (C:/Slicer 5.9.0-2025-03-17/slicer.org/Extensions-33550/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py:472) - Register volumes using: C:\Slicer 5.9.0-2025-03-17\slicer.org\Extensions-33550\SlicerElastix\lib\Slicer-5.9\elastix.exe: ['-f', 'E:/elastix/Elastix/20250320_190918_164\\input\\fixed.mha', '-m', 'E:/elastix/Elastix/20250320_190918_164\\input\\moving.mha', '-p', 'E:\\elastix\\Elastix\\20250320_190917_809\\Parameters_Rigid.txt', '-p', 'E:\\elastix\\Elastix\\20250320_190917_809\\Parameters_BSpline.txt', '-out', 'E:/elastix/Elastix/20250320_190918_164\\result-transform']
[INFO][Python] 20.03.2025 19:09:20 [Python] (C:/Slicer 5.9.0-2025-03-17/slicer.org/Extensions-33550/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py:411) - 
elastix is started at Thu Mar 20 19:09:20 2025.

which elastix:   C:\Slicer 5.9.0-2025-03-17\slicer.org\Extensions-33550\SlicerElastix\lib\Slicer-5.9\elastix.exe
  elastix version: 5.1.0
  Git revision SHA: d652938573e5f193955908eba225a854b31ce36a
  Git revision date: Thu Jan 12 14:20:18 2023 +0100
  Build date: Mar 18 2025 04:13:51
  Compiler: Visual C++ version 194234436.0
  Memory address size: 64-bit
  CMake version: 3.22.1
  ITK version: 5.4.0

Command-line arguments:
  -f E:/elastix/Elastix/20250320_190918_164\input\fixed.mha -m E:/elastix/Elastix/20250320_190918_164\input\moving.mha -p E:\elastix\Elastix\20250320_190917_809\Parameters_Rigid.txt -p E:\elastix\Elastix\20250320_190917_809\Parameters_BSpline.txt -out E:/elastix/Elastix/20250320_190918_164\result-transform

elastix runs at: LAPTOP-75AUUON7
  Windows  Personal (x64),  (Build 9200)
  with 8078 MB memory, and 4 cores @ 1992 MHz.
-------------------------------------------------------------------------

Running elastix with parameter file 0: "E:\elastix\Elastix\20250320_190917_809\Parameters_Rigid.txt".

Current time: Thu Mar 20 19:09:20 2025.
Reading the elastix parameters from file ...
[ERROR][Python] 20.03.2025 19:09:20 [Python] (C:\Slicer 5.9.0-2025-03-17\bin\Python\slicer\util.py:3145) - Failed to compute results.

Command 'elastix' returned non-zero exit status 1.
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) -   File "C:/Slicer 5.9.0-2025-03-17/slicer.org/Extensions-33550/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py", line 296, in onApplyButton
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) -     self.logic.registerVolumesUsingParameterNode(self._parameterNode)
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) -   File "C:/Slicer 5.9.0-2025-03-17/slicer.org/Extensions-33550/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py", line 534, in registerVolumesUsingParameterNode
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) -     self.registerVolumes(
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) -   File "C:/Slicer 5.9.0-2025-03-17/slicer.org/Extensions-33550/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py", line 581, in registerVolumes
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) -     self.logProcessOutput(elastixProcess)
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) -   File "C:/Slicer 5.9.0-2025-03-17/slicer.org/Extensions-33550/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules/Elastix.py", line 527, in logProcessOutput
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) -     raise subprocess.CalledProcessError(return_code, "elastix")
[CRITICAL][Stream] 20.03.2025 19:09:28 [] (unknown:0) - subprocess.CalledProcessError: Command 'elastix' returned non-zero exit status 1.
</code></pre>

---
