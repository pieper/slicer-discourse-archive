---
topic_id: 47404
title: "Fail to Compute Results using TotalSegmentator (returned non-zero exist status 1)"
date: 2026-06-20
url: https://discourse.slicer.org/t/47404
last_bumped: 2026-06-21T15:41:11.118Z
---

# Fail to Compute Results using TotalSegmentator (returned non-zero exist status 1)

**Topic ID**: 47404
**Date**: 2026-06-20
**URL**: https://discourse.slicer.org/t/fail-to-compute-results-using-totalsegmentator-returned-non-zero-exist-status-1/47404

---

## Post #1 by @qn_Huynh (2026-06-20 21:38 UTC)

<p>Hello Slicer Support!</p>
<p>I have been trying to run TotalSegmentator, but it has been failing. The Slicer Error message that I have been receiving states, “… returned non-zero exit status 1.”</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "F:/3DSlicer/3D Slicer 5.11.0-2026-06-12/slicer.org/Extensions-34594/TotalSegmentator/lib/Slicer-5.11/qt-scripted-modules/TotalSegmentator.py", line 363, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "F:/3DSlicer/3D Slicer 5.11.0-2026-06-12/slicer.org/Extensions-34594/TotalSegmentator/lib/Slicer-5.11/qt-scripted-modules/TotalSegmentator.py", line 1153, in process
    self.processVolume(inputFile, inputVolume,
  File "F:/3DSlicer/3D Slicer 5.11.0-2026-06-12/slicer.org/Extensions-34594/TotalSegmentator/lib/Slicer-5.11/qt-scripted-modules/TotalSegmentator.py", line 1237, in processVolume
    self.logProcessOutput(proc)
  File "F:/3DSlicer/3D Slicer 5.11.0-2026-06-12/slicer.org/Extensions-34594/TotalSegmentator/lib/Slicer-5.11/qt-scripted-modules/TotalSegmentator.py", line 983, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['F:/3DSlicer/3D Slicer 5.11.0-2026-06-12/bin/../bin\\PythonSlicer.EXE', 'F:\\3DSlicer\\3D Slicer 5.11.0-2026-06-12\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Admin/AppData/Local/Temp/Slicer/__SlicerTemp__2026-06-19_19+51+03.270/total-segmentator-input.nii', '-o', 'C:/Users/Admin/AppData/Local/Temp/Slicer/__SlicerTemp__2026-06-19_19+51+03.270/segmentation', '--device', 'cpu', '--ml', '--task', 'abdominal_muscles']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @ThomasVanParys (2026-06-21 15:41 UTC)

<p>I would uninstall and reinstall TotalSegmentator with the latest Python version. What is the RAM/CPU parameters on your device? That could also be a reason. Try TotalSegmentator with the modules test data first to see if this works…</p>

---
