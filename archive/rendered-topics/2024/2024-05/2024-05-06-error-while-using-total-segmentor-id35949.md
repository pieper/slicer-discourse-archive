# Error while using Total Segmentor

**Topic ID**: 35949
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/error-while-using-total-segmentor/35949

---

## Post #1 by @Aayush_Agrawal_ch21b (2024-05-06 15:57 UTC)

<p>Traceback (most recent call last):<br>
File “C:\Users\INSPIRE01\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/INSPIRE01/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 271, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/INSPIRE01/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 859, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/INSPIRE01/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 697, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/INSPIRE01/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\INSPIRE01\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/INSPIRE01/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-05_07+24+30.600/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/INSPIRE01/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-05_07+24+30.600/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 2.</p>
<p>I keep getting this error while trying to use TotalSegmentor. PyTorch is installed properly.</p>

---

## Post #2 by @jamesobutler (2024-05-06 16:29 UTC)

<p>Please try with latest Slicer stable (currently 5.6.1) which you can download from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>. There have been updates to the latest TotalSegmentator that are available in the latest stable release that are not in the older Slicer 5.2.2 that you are using. Please report back after trying the latest Slicer stable version.</p>

---
