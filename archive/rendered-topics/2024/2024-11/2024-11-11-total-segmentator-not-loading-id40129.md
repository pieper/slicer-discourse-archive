# Total segmentator not loading

**Topic ID**: 40129
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/total-segmentator-not-loading/40129

---

## Post #1 by @john.barriga (2024-11-11 18:34 UTC)

<p>I’ve have been trying to load total segmentator for 4 hours and even multiple computers but I keep getting this error and it is so frustrating<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3ddd2609597e48e87758bdb9b34217881e850333.png" data-download-href="/uploads/short-url/8PgVVCCLotwgYwioFbMCEq4Alcn.png?dl=1" title="Screenshot (113)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3ddd2609597e48e87758bdb9b34217881e850333_2_690x494.png" alt="Screenshot (113)" data-base62-sha1="8PgVVCCLotwgYwioFbMCEq4Alcn" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3ddd2609597e48e87758bdb9b34217881e850333_2_690x494.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3ddd2609597e48e87758bdb9b34217881e850333_2_1035x741.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3ddd2609597e48e87758bdb9b34217881e850333.png 2x" data-dominant-color="76757A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (113)</span><span class="informations">1226×878 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\Johnd\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/Johnd/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 307, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/Johnd/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1002, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/Users/Johnd/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1076, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/Users/Johnd/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 848, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/Johnd/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\Johnd\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/Johnd/AppData/Local/Temp/Slicer/__SlicerTemp__2024-11-10_00+32+39.986/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Johnd/AppData/Local/Temp/Slicer/__SlicerTemp__2024-11-10_00+32+39.986/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @lassoan (2024-11-11 18:36 UTC)

<p>Probably you have run into this issue:</p>
<aside class="quote" data-post="8" data-topic="38142">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alireza-hokmabadi/48/78475_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-returned-non-zero-exit-status-1/38142/8">TotalSegmentator Failed to compute results....returned non-zero exit status 1</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    To resolve the issue temporarily, you can downgrade acvl_utils until the nnUNet team includes the missing crop_to_bbox function in a future update. 
Run the following command to downgrade: 
pip install acvl_utils==0.2
  </blockquote>
</aside>


---
