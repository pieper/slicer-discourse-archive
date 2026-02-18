# Fail to Run Total Segmentator

**Topic ID**: 28436
**Date**: 2023-03-18
**URL**: https://discourse.slicer.org/t/fail-to-run-total-segmentator/28436

---

## Post #1 by @holo031029 (2023-03-18 00:31 UTC)

<p>Version 5.3 and 5.2.2  both have the same error：<br>
Updated the Total Segmentator package and error in the first time, then RUN it again the processing started but still can’t work successfully.</p>
<p>Thanks for your help!</p>
<p>Traceback (most recent call last):<br>
File “H:\ProgramData\slicer.org\Slicer 5.3.0-2023-03-14\bin\Python\slicer\util.py”, line 2973, in tryWithErrorDisplay<br>
yield<br>
File “H:/ProgramData/slicer.org/Slicer 5.3.0-2023-03-14/slicer.org/Extensions-31671/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “H:/ProgramData/slicer.org/Slicer 5.3.0-2023-03-14/slicer.org/Extensions-31671/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 763, in process<br>
self.logProcessOutput(proc)<br>
File “H:/ProgramData/slicer.org/Slicer 5.3.0-2023-03-14/slicer.org/Extensions-31671/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 656, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘H:/ProgramData/slicer.org/Slicer 5.3.0-2023-03-14/bin/…/bin\PythonSlicer.EXE’, ‘H:\ProgramData\slicer.org\Slicer 5.3.0-2023-03-14\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Windows/Temp/Slicer/__SlicerTemp__2023-03-17_13+56+05.512/total-segmentator-input.nii’, ‘-o’, ‘C:/Windows/Temp/Slicer/__SlicerTemp__2023-03-17_13+56+05.512/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 2.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26754abc6eae17abd4cc9bc69737dff2310a8a08.png" data-download-href="/uploads/short-url/5udrk1Tjat5y1URJ4ECUMqqxe64.png?dl=1" title="Image 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26754abc6eae17abd4cc9bc69737dff2310a8a08.png" alt="Image 2" data-base62-sha1="5udrk1Tjat5y1URJ4ECUMqqxe64" width="690" height="177" data-dominant-color="D4E3ED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 2</span><span class="informations">953×245 11.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @rbumm (2023-03-18 16:30 UTC)

<p>Please post some more information:</p>
<ul>
<li>Operating system</li>
<li>Brand and model of your GPU, dedicated video RAM of your GPU</li>
</ul>
<p>and the log from here, please:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d433905544105bfa7f2b2f49242582521b3041a7.png" alt="image" data-base62-sha1="uhdHjGuA7bmYW4JCRMrz33tB00v" width="551" height="239"></p>

---
