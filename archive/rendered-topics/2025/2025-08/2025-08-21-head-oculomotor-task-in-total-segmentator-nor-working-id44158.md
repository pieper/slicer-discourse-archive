# Head oculomotor task in total segmentator nor working

**Topic ID**: 44158
**Date**: 2025-08-21
**URL**: https://discourse.slicer.org/t/head-oculomotor-task-in-total-segmentator-nor-working/44158

---

## Post #1 by @philippepellerin (2025-08-21 08:06 UTC)

<p>I can’t operate total segmentator with the task oculomotor muscles, I got an error message when making any attempt.<br>
I am running Slicer 5,9,0 25-08-14 on a Mac Apple chip M2 Sequoia 15.6. What is wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a9fd50a512a3baea5f84792a4f2b7f9b7f2eb2c.png" data-download-href="/uploads/short-url/jMkkrMdvsiykDDM5tbDawqv5dH6.png?dl=1" title="PastedGraphic-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a9fd50a512a3baea5f84792a4f2b7f9b7f2eb2c.png" alt="PastedGraphic-1" data-base62-sha1="jMkkrMdvsiykDDM5tbDawqv5dH6" width="640" height="378"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1</span><span class="informations">640×378 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here after the error log: Processing started<br>
Writing input file to /private/var/folders/xw/49j5chs13nl_nzll7509jd5h0000gn/T/Slicer-philippe/__SlicerTemp__2025-08-16_16+49+21.069/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘/private/var/folders/xw/49j5chs13nl_nzll7509jd5h0000gn/T/Slicer-philippe/__SlicerTemp__2025-08-16_16+49+21.069/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/xw/49j5chs13nl_nzll7509jd5h0000gn/T/Slicer-philippe/__SlicerTemp__2025-08-16_16+49+21.069/segmentation’, ‘–ml’, ‘–task’, ‘oculomotor_muscles’]<br>
No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ or the <code>--roi_subset</code> option can help to reduce runtime.</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator”, line 8, in<br>
sys.exit(main())<br>
^^^^^^<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/bin/TotalSegmentator.py”, line 155, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/python_api.py”, line 142, in totalsegmentator<br>
from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars<br>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/nnunet.py”, line 29, in<br>
from totalsegmentator.custom_trainers import nnUNetTrainer_MOSAIC_1k_QuarterLR_NoMirroring<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/custom_trainers.py”, line 2, in<br>
from nnunetv2.training.nnUNetTrainer.variants.data_augmentation.nnUNetTrainerNoMirroring import nnUNetTrainerNoMirroring<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/training/nnUNetTrainer/variants/data_augmentation/nnUNetTrainerNoMirroring.py”, line 26, in<br>
from nnunetv2.training.nnUNetTrainer.nnUNetTrainer import nnUNetTrainer<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/training/nnUNetTrainer/nnUNetTrainer.py”, line 43, in<br>
from torch import GradScaler<br>
ImportError: cannot import name ‘GradScaler’ from ‘torch’ (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/<strong>init</strong>.py)</p>

---

## Post #2 by @philippepellerin (2025-08-27 13:59 UTC)

<p>Sorry, I tried it in the stable release and it is working fine. It was a disability only in the preview, but it was…</p>

---
