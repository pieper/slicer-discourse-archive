---
topic_id: 29485
title: "3D Model Is Not Showing"
date: 2023-05-16
url: https://discourse.slicer.org/t/29485
---

# 3d model is not showing

**Topic ID**: 29485
**Date**: 2023-05-16
**URL**: https://discourse.slicer.org/t/3d-model-is-not-showing/29485

---

## Post #1 by @Reem_Alhashim (2023-05-16 04:35 UTC)

<p>Hello,<br>
I have a problem with my model. I made the model and exported it and closed the file.<br>
The nesxt day, I opened the file and nothing shows up, it was not like that.<br>
The 3d model disappeared and the thresholds are gone.</p>
<p>Here is how the file looks like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9648bd8972518a73c8f1113702cadfd7f9861ad0.png" data-download-href="/uploads/short-url/lrtsTIXMkkyOHlbdJaI79LOINPi.png?dl=1" title="Screenshot 2023-05-16 003151" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9648bd8972518a73c8f1113702cadfd7f9861ad0_2_608x500.png" alt="Screenshot 2023-05-16 003151" data-base62-sha1="lrtsTIXMkkyOHlbdJaI79LOINPi" width="608" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9648bd8972518a73c8f1113702cadfd7f9861ad0_2_608x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9648bd8972518a73c8f1113702cadfd7f9861ad0_2_912x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9648bd8972518a73c8f1113702cadfd7f9861ad0.png 2x" data-dominant-color="34343D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-16 003151</span><span class="informations">943×775 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Can someome help me restore it bake to normal,<br>
thanks</p>

---

## Post #2 by @lassoan (2023-05-16 04:38 UTC)

<p>It seems that you have loaded the file as a volume instead of a segmentation.</p>
<p>You can either save the file with the <code>.seg.nrrd</code> file extension to give a hint to the application to load it as a segmentation. Or you can keep using the <code>.nrrd</code> file extension but then you need to manually select <code>Description</code> → <code>Segmentation</code> in <code>Add data</code> window.</p>

---
