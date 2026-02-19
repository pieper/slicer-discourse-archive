---
topic_id: 42395
title: "Totalsegmentator Returned Non Zero Exit Status 1"
date: 2025-04-01
url: https://discourse.slicer.org/t/42395
---

# TotalSegmentator + "returned non-zero exit status 1."

**Topic ID**: 42395
**Date**: 2025-04-01
**URL**: https://discourse.slicer.org/t/totalsegmentator-returned-non-zero-exit-status-1/42395

---

## Post #1 by @Camille_Guillerminet (2025-04-01 13:22 UTC)

<p>Operating system: Windows 10<br>
Slicer version:5.6.2 + CPU</p>
<p>Dear support,</p>
<p>I tried to run totalsegmentator but it failed after a while with the “returned non-zero exit status 1”.<br>
Could you help me to understand what is the probleme?</p>
<p>I copied below the message error of the pop-up window.</p>
<p>“Processing started<br>
Writing input file to C:/Users/c.guillerminet/AppData/Local/Temp/Slicer/__SlicerTemp__2025-04-01_14+46+42.002/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/c.guillerminet/AppData/Local/Temp/Slicer/__SlicerTemp__2025-04-01_14+46+42.002/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/c.guillerminet/AppData/Local/Temp/Slicer/__SlicerTemp__2025-04-01_14+46+42.002/segmentation’, ‘–task’, ‘body’, ‘–fast’]<br>
Traceback (most recent call last):<br>
File “C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
return <em>run_code(code, main_globals, None,<br>
File “C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
exec(code, run_globals)<br>
File "C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe_<em>main</em></em>.py", line 7, in <br>
File “C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 141, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 127, in totalsegmentator<br>
from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars<br>
File “C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 40, in <br>
from totalsegmentator.dicom_io import dcm_to_nifti, save_mask_as_rtstruct<br>
File “C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\dicom_io.py”, line 13, in <br>
import dicom2nifti<br>
File "C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\dicom2nifti_<em>init</em></em>.py”, line 19, in <br>
from dicom2nifti.convert_dicom import dicom_series_to_nifti<br>
File “C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\dicom2nifti\convert_dicom.py”, line 17, in <br>
import dicom2nifti.common as common<br>
File “C:\Users\c.guillerminet\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\dicom2nifti\common.py”, line 16, in <br>
from pydicom.pixels import apply_modality_lut<br>
ModuleNotFoundError: No module named ‘pydicom.pixels’<br>
No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ or the <code>--roi_subset</code> option can help to reduce runtime.</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a>"</p>
<p>Sincerely yours,<br>
Camille</p>

---

## Post #2 by @jamesobutler (2025-04-01 14:00 UTC)

<aside class="quote quote-modified" data-post="2" data-topic="42386">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-slicer-5-8-1-modulenotfounderror-no-module-named-pydicom-pixels/42386/2">TotalSegmentator + Slicer 5.8.1 - "ModuleNotFoundError: No module named 'pydicom.pixels'"</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for reporting. The issue is due to an unused Python package (dicom2nifti) released a corrupted version for Python-3.9 a few days ago. The <a href="https://github.com/icometrix/dicom2nifti/issues/155" rel="noopener nofollow ugc">error is reported to dicom2nifti developers</a> and a <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/72" rel="noopener nofollow ugc">fix is already implemented in TotalSegmentator extension</a>. 
The fix will be available in the Extensions Manager from tomorrow. If you use the latest Slicer Preview Release (currently Slicer-5.8.1), then tomorrow you can go to the Extensions Manager and click “Check for updates” and then “Update all” to ge…
  </blockquote>
</aside>

<p>^ Please try using latest Slicer stable 5.8.1 as the fix should be available now.</p>

---
