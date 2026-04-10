---
topic_id: 46702
title: "Please Help Me Ive Tried Everything I Known"
date: 2026-04-09
url: https://discourse.slicer.org/t/46702
---

# Please help me. I've tried everything i known

**Topic ID**: 46702
**Date**: 2026-04-09
**URL**: https://discourse.slicer.org/t/please-help-me-ive-tried-everything-i-known/46702

---

## Post #1 by @Tech-Liuxy (2026-04-09 15:27 UTC)

<p>#<span class="hashtag-raw">#MAC</span> TAHOE26</p>
<p>Processing started</p>
<p>Writing input file to /private/var/folders/c2/7ytv4ycx59z72y4bcl8dfplh0000gn/T/Slicer-liuxy/__SlicerTemp__2026-04-09_14+44+48.430/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘/private/var/folders/c2/7ytv4ycx59z72y4bcl8dfplh0000gn/T/Slicer-liuxy/__SlicerTemp__2026-04-09_14+44+48.430/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/c2/7ytv4ycx59z72y4bcl8dfplh0000gn/T/Slicer-liuxy/__SlicerTemp__2026-04-09_14+44+48.430/segmentation’, ‘–device’, ‘cpu’, ‘–ml’, ‘–task’, ‘total’]</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator”, line 8, in </p>
<p>sys.exit(main())</p>
<p>^^^^^^</p>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/bin/TotalSegmentator.py”, line 201, in main</p>
<p>totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,</p>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/python_api.py”, line 156, in totalsegmentator</p>
<p>from totalsegmentator.nnunet import nnUNet_predict_image # this has to be after setting new env vars</p>
<p>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/nnunet.py”, line 29, in </p>
<p>from totalsegmentator.custom_trainers import (nnUNetTrainer_MOSAIC_1k_QuarterLR_NoMirroring,</p>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/custom_trainers.py”, line 35, in </p>
<p>from nnunetv2.training.dataloading.data_loader import nnUNetDataLoader</p>
<p>ModuleNotFoundError: No module named ‘nnunetv2.training.dataloading.data_loader’</p>

---

## Post #2 by @lassoan (2026-04-10 01:08 UTC)

<p>TotalSegmentator has just been fixed on macOS today. Go to nnUNet module and install nnUNet version <code>&gt;=2.7</code>:</p>
<p>                    <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb9db9b16a6ee6eba74973bdd88822bfc8c8155.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb9db9b16a6ee6eba74973bdd88822bfc8c8155.png" width="553" height="403">
          </a>

</p>

---
