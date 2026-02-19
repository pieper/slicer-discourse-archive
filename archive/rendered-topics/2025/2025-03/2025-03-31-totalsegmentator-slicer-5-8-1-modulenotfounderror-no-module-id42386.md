---
topic_id: 42386
title: "Totalsegmentator Slicer 5 8 1 Modulenotfounderror No Module"
date: 2025-03-31
url: https://discourse.slicer.org/t/42386
---

# TotalSegmentator + Slicer 5.8.1 - "ModuleNotFoundError: No module named 'pydicom.pixels'"

**Topic ID**: 42386
**Date**: 2025-03-31
**URL**: https://discourse.slicer.org/t/totalsegmentator-slicer-5-8-1-modulenotfounderror-no-module-named-pydicom-pixels/42386

---

## Post #1 by @jochoaTX (2025-03-31 19:55 UTC)

<p>Operating system: WinPro 11<br>
Slicer version: 5.8.1<br>
Expected behavior: TotalSegmentator to totally segment<br>
Actual behavior: Pukes</p>
<p>I’ve declared defeat. Cannot solve this myself. It seems that TotalSegmentator may be looking for an earlier version of pydicom?  Any help/suggestions appreciated - for the sake of my sanity. Here’s some context:</p>
<p>Processing started<br>
Writing input file to C:/Users/jocho/AppData/Local/Temp/Slicer/__SlicerTemp__2025-03-31_11+33+57.728/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/jocho/AppData/Local/Temp/Slicer/__SlicerTemp__2025-03-31_11+33+57.728/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jocho/AppData/Local/Temp/Slicer/__SlicerTemp__2025-03-31_11+33+57.728/segmentation’, ‘–ml’, ‘–task’, ‘total’]<br>
Traceback (most recent call last):<br>
File “C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
return <em>run_code(code, main_globals, None,<br>
File “C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
exec(code, run_globals)<br>
File "C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Scripts\TotalSegmentator.exe_<em>main</em></em>.py", line 7, in <br>
File “C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 143, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 137, in totalsegmentator<br>
from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars<br>
File “C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 54, in <br>
from totalsegmentator.dicom_io import dcm_to_nifti, save_mask_as_rtstruct<br>
File “C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\dicom_io.py”, line 13, in <br>
import dicom2nifti<br>
File "C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\dicom2nifti_<em>init</em></em>.py", line 19, in <br>
from dicom2nifti.convert_dicom import dicom_series_to_nifti<br>
File “C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\dicom2nifti\convert_dicom.py”, line 17, in <br>
import dicom2nifti.common as common<br>
File “C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\dicom2nifti\common.py”, line 16, in <br>
from pydicom.pixels import apply_modality_lut<br>
ModuleNotFoundError: No module named ‘pydicom.pixels’</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>++++++++++++++<br>
Traceback (most recent call last):<br>
File “C:\ProgramData\slicer.org\Slicer 5.8.1\bin\Python\slicer\util.py”, line 3303, in tryWithErrorDisplay<br>
yield<br>
File “C:/ProgramData/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 307, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/ProgramData/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 1037, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/ProgramData/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 1104, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/ProgramData/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 883, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/ProgramData/slicer.org/Slicer 5.8.1/bin/../bin\PythonSlicer.EXE’, ‘C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/jocho/AppData/Local/Temp/Slicer/__SlicerTemp__2025-03-31_11+52+39.591/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jocho/AppData/Local/Temp/Slicer/__SlicerTemp__2025-03-31_11+52+39.591/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>
<p>+++++</p>
<p>[Python] Failed to compute results.<br>
[Python] Command ‘[‘C:/ProgramData/slicer.org/Slicer 5.8.1/bin/../bin\PythonSlicer.EXE’, ‘C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/jocho/AppData/Local/Temp/Slicer/__SlicerTemp__2025-03-31_11+52+39.591/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jocho/AppData/Local/Temp/Slicer/__SlicerTemp__2025-03-31_11+52+39.591/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.<br>
Traceback (most recent call last):<br>
File “C:/ProgramData/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 307, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/ProgramData/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 1037, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/ProgramData/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 1104, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/ProgramData/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 883, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/ProgramData/slicer.org/Slicer 5.8.1/bin/../bin\PythonSlicer.EXE’, ‘C:\ProgramData\slicer.org\Slicer 5.8.1\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/jocho/AppData/Local/Temp/Slicer/__SlicerTemp__2025-03-31_11+52+39.591/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jocho/AppData/Local/Temp/Slicer/__SlicerTemp__2025-03-31_11+52+39.591/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.<br>
[Qt] QTextCursor::setPosition: Position ‘-18456’ out of range<br>
[Qt] QTextCursor::setPosition: Position ‘-18456’ out of range<br>
[Qt] QTextCursor::setPosition: Position ‘-18456’ out of range<br>
[Qt] QTextCursor::setPosition: Position ‘-18456’ out of range<br>
[Qt] QTextCursor::setPosition: Position ‘-18456’ out of range</p>

---

## Post #2 by @lassoan (2025-03-31 20:01 UTC)

<p>Thanks for reporting. The issue is due to an unused Python package (dicom2nifti) released a corrupted version for Python-3.9 a few days ago. The <a href="https://github.com/icometrix/dicom2nifti/issues/155">error is reported to dicom2nifti developers</a> and a <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/72">fix is already implemented in TotalSegmentator extension</a>.</p>
<p>The fix will be available in the Extensions Manager from tomorrow. If you use the latest Slicer Preview Release (currently Slicer-5.8.1), then tomorrow you can go to the Extensions Manager and click “Check for updates” and then “Update all” to get the fix.</p>

---

## Post #3 by @jochoaTX (2025-04-01 00:05 UTC)

<p>Dr. Lasso-  thank you very much for your very prompt responses! It gives me some hope that I’ll be able to get this module running. At one point, a little bit Self doubt started creeping into my head.</p>
<p>I appreciate all the work that you do for this community, and I know many others do to.</p>
<p>I’ll report back tomorrow, hopefully with an affirmative that everything worked out OK. Regards!</p>

---
