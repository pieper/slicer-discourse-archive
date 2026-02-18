# TotalSegmentator error

**Topic ID**: 27701
**Date**: 2023-02-08
**URL**: https://discourse.slicer.org/t/totalsegmentator-error/27701

---

## Post #1 by @Ackta (2023-02-08 11:13 UTC)

<p>Operating system: windows 10<br>
Slicer version: 5.2.1<br>
Expected behavior:<br>
Actual behavior:<br>
Hi, when i try to use totalsegmentator i`ve thi error<br>
“Traceback (most recent call last):<br>
File “C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 749, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 656, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/Administrator/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘F:/User TMP/Slicer/__SlicerTemp__2023-02-08_12+06+56.965/total-segmentator-input.nii’, ‘-o’, ‘F:/User TMP/Slicer/__SlicerTemp__2023-02-08_12+06+56.965/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.<br>
And This Processing started<br>
Writing input file to F:/User TMP/Slicer/__SlicerTemp__2023-02-08_12+22+06.226/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘F:/User TMP/Slicer/__SlicerTemp__2023-02-08_12+22+06.226/total-segmentator-input.nii’, ‘-o’, 'F:/User TMP/Slicer/<em><em>SlicerTemp__2023-02-08_12+22+06.226/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
Traceback (most recent call last):<br>
File “C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 241, in <br>
main()<br>
File “C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 87, in main<br>
parser.add_argument(‘–version’, action=‘version’, version=require(“TotalSegmentator”)[0].version)<br>
File "C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\pkg_resources_<em>init</em></em>.py", line 909, in require<br>
needed = self.resolve(parse_requirements(requirements))<br>
File "C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\pkg_resources_<em>init</em></em>.py”, line 795, in resolve<br>
raise DistributionNotFound(req, requirers)<br>
pkg_resources.DistributionNotFound: The ‘scikit-learn’ distribution was not found and is required by batchgenerators<br>
"<br>
Thanks for Help</p>

---

## Post #2 by @lassoan (2023-02-08 11:47 UTC)

<p>It seems that wrong version of Python packages are found in your Slicer’s Python environment. Have you tried to install some Python packages manually?</p>
<p>I would recommend to uninstall Slicer, remove the complete <code>C:\Users\Administrator\AppData\Local\NA-MIC\Slicer 5.2.1</code> folder and reinstall Slicer and TotalSegmentator extension from scratch.</p>

---

## Post #3 by @Ackta (2023-02-08 11:56 UTC)

<p>3.11.2<br>
ok i try Thanks</p>

---
