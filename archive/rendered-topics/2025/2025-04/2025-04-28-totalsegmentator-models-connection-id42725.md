# totalsegmentator models connection

**Topic ID**: 42725
**Date**: 2025-04-28
**URL**: https://discourse.slicer.org/t/totalsegmentator-models-connection/42725

---

## Post #1 by @yoyo1 (2025-04-28 17:22 UTC)

<p>Hi, I’m trying to activate the totalsegmentator on one of the examples of CT there’s in the slicer.<br>
I get an error that the ml models are not connected and the result failes.<br>
Thanks</p>

---

## Post #2 by @rbumm (2025-04-29 12:17 UTC)

<p>just tested and it works great in SLICER 5.8.1.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9dac9b88db742185ebbe9d18501e9f2814db22be.png" data-download-href="/uploads/short-url/muQLUOOs5XAMVxxPkYGqeEj0LOS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9dac9b88db742185ebbe9d18501e9f2814db22be.png" alt="image" data-base62-sha1="muQLUOOs5XAMVxxPkYGqeEj0LOS" width="345" height="328"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">345×328 89.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @yoyo1 (2025-04-30 06:56 UTC)

<p>Thanks for the reply, I’m pasting the error I got, hope you could help me solve it.</p>
<p>Processing started<br>
Writing input file to C:/Users/assaf/slicer.org/__SlicerTemp__2025-04-30_09+51+06.674/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/assaf/slicer.org/__SlicerTemp__2025-04-30_09+51+06.674/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/assaf/slicer.org/__SlicerTemp__2025-04-30_09+51+06.674/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
Traceback (most recent call last):<br>
File “C:\Users\assaf\slicer.org\Slicer 5.8.1\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
return _run_code(code, main_globals, None,<br>
File “C:\Users\assaf\slicer.org\Slicer 5.8.1\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
exec(code, run_globals)<br>
File "C:\Users\assaf\slicer.org\Slicer 5.8.1\lib\Python\Scripts\TotalSegmentator.exe_<em>main</em></em>.py", line 7, in <br>
File “C:\Users\assaf\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 143, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “C:\Users\assaf\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 137, in totalsegmentator<br>
from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars<br>
File “C:\Users\assaf\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 29, in <br>
from totalsegmentator.custom_trainers import nnUNetTrainer_MOSAIC_1k_QuarterLR_NoMirroring<br>
File “C:\Users\assaf\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\custom_trainers.py”, line 2, in <br>
from nnunetv2.training.nnUNetTrainer.variants.data_augmentation.nnUNetTrainerNoMirroring import nnUNetTrainerNoMirroring<br>
File “C:\Users\assaf\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\nnunetv2\training\nnUNetTrainer\variants\data_augmentation\nnUNetTrainerNoMirroring.py”, line 5, in <br>
from batchgeneratorsv2.helpers.scalar_type import RandomScalar<br>
ModuleNotFoundError: No module named ‘batchgeneratorsv2’</p>

---
