# Error using TotalSegmentator in Slicer

**Topic ID**: 36255
**Date**: 2024-05-19
**URL**: https://discourse.slicer.org/t/error-using-totalsegmentator-in-slicer/36255

---

## Post #1 by @khajta (2024-05-19 01:11 UTC)

<p>Dear experts,</p>
<p>I tried to use TotalSegmentator extionsion, but it showed the error. Thank you in advance for suggestions.</p>
<p>Best regards,<br>
Khajonsak<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bd241e300e988a6c00832daf5b0dbc06482fd2a.png" alt="Screenshot 2024-05-19 100254" data-base62-sha1="6fF0loMY96L5bpt0Dnd0hnv1hzA" width="518" height="284"></p>

---

## Post #2 by @Matteboo (2024-05-21 11:32 UTC)

<p>Hello, could you copy paste the whole error message, it’s difficult to help you without getting the full error</p>

---

## Post #3 by @khajta (2024-06-07 03:30 UTC)

<p>Thank you for your reply. Sorry for very late reply. These are the error.</p>
<p>Command ‘[‘C:/Users/アイソトープ部/OneDrive/デスクトップ/Nook/3DSlicer software/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\アイソトープ部\OneDrive\デスクトップ\Nook\3DSlicer software\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-07_12+28+22.569/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-07_12+28+22.569/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\アイソトープ部\OneDrive\デスクトップ\Nook\3DSlicer software\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/アイソトープ部/OneDrive/デスクトップ/Nook/3DSlicer software/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 298, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/アイソトープ部/OneDrive/デスクトップ/Nook/3DSlicer software/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 961, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/Users/アイソトープ部/OneDrive/デスクトップ/Nook/3DSlicer software/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1035, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/Users/アイソトープ部/OneDrive/デスクトップ/Nook/3DSlicer software/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 807, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/アイソトープ部/OneDrive/デスクトップ/Nook/3DSlicer software/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\アイソトープ部\OneDrive\デスクトップ\Nook\3DSlicer software\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-07_12+28+22.569/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/アイソトープ部/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-07_12+28+22.569/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>

---

## Post #4 by @lassoan (2024-06-19 13:54 UTC)

<p>It is possible that the special characters in the path cause problems. Please try to install Slicer in a short and simple path without any special characters (such as <code>C:\tmp\Slicer</code>) and set the temporary folder in Slicer’s application settings to a similar one (such as <code>C:\temp\SlicerTemp</code>).</p>

---
