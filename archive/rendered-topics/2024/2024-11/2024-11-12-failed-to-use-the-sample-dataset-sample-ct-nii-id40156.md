---
topic_id: 40156
title: "Failed To Use The Sample Dataset Sample Ct Nii"
date: 2024-11-12
url: https://discourse.slicer.org/t/40156
---

# Failed to use the sample dataset (sample_ct.nii )

**Topic ID**: 40156
**Date**: 2024-11-12
**URL**: https://discourse.slicer.org/t/failed-to-use-the-sample-dataset-sample-ct-nii/40156

---

## Post #1 by @bkasmai (2024-11-12 18:35 UTC)

<p>Loaded a sample ct niftii dataset (example_ct), clicked on Apply and selected Fast(~2 minutes). I get the following error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\Users\Bahman\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py", line 3255, in tryWithErrorDisplay
    yield
  File "C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1002, in process
    self.processVolume(inputFile, inputVolume,
  File "C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1076, in processVolume
    self.logProcessOutput(proc)
  File "C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 848, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Bahman\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Bahman/AppData/Local/Temp/Slicer/__SlicerTemp__2024-11-12_18+27+58.379/total-segmentator-input.nii', '-o', 'C:/Users/Bahman/AppData/Local/Temp/Slicer/__SlicerTemp__2024-11-12_18+27+58.379/segmentation', '--ml', '--task', 'total', '--fast']' returned non-zero exit status 1.
</code></pre>
<p>and in the console:</p>
<pre><code class="lang-auto">Requirement already satisfied: pillow&lt;10.1 in c:\users\bahman\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (10.0.1)
[Python] Failed to compute results.
[Python] Command '['C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Bahman\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Bahman/AppData/Local/Temp/Slicer/__SlicerTemp__2024-11-12_18+27+58.379/total-segmentator-input.nii', '-o', 'C:/Users/Bahman/AppData/Local/Temp/Slicer/__SlicerTemp__2024-11-12_18+27+58.379/segmentation', '--ml', '--task', 'total', '--fast']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1002, in process
    self.processVolume(inputFile, inputVolume,
  File "C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1076, in processVolume
    self.logProcessOutput(proc)
  File "C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 848, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/Bahman/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Bahman\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Bahman/AppData/Local/Temp/Slicer/__SlicerTemp__2024-11-12_18+27+58.379/total-segmentator-input.nii', '-o', 'C:/Users/Bahman/AppData/Local/Temp/Slicer/__SlicerTemp__2024-11-12_18+27+58.379/segmentation', '--ml', '--task', 'total', '--fast']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @lassoan (2024-11-12 18:51 UTC)

<p>A regression was introduced in one of the nnunet packages a few days ago (<a href="https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-returned-non-zero-exit-status-1/38142/9" class="inline-onebox">TotalSegmentator Failed to compute results....returned non-zero exit status 1 - #9 by lassoan</a>). You can update or reinstall TotalSegmentator extension to fix the issue.</p>

---

## Post #3 by @bkasmai (2024-11-12 18:58 UTC)

<p>Thanks so much. All ok now. I spent hours trying to find a solution.</p>

---
