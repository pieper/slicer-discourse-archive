---
topic_id: 5288
title: "How To Merge Mri And Brain Atlas"
date: 2019-01-06
url: https://discourse.slicer.org/t/5288
---

# How to merge MRI and brain atlas

**Topic ID**: 5288
**Date**: 2019-01-06
**URL**: https://discourse.slicer.org/t/how-to-merge-mri-and-brain-atlas/5288

---

## Post #1 by @flashman (2019-01-06 12:46 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10</p>
<p>Hi all,<br>
I am relatively new to the 3D Slicer program and currently undergoing the<br>
precise localization of electrodes after deep brain stimulation (DBS) surgery.<br>
I’ve constructed the shape of the electrodes. But the precise localization in the brian is still unknown. The  targets the electrodes are bilateral subthalamic nucleus (STN).</p>
<p>How to merge the MRI images and the brain atlas to make the precise localization of electrodes?</p>
<p>Any advice for this? Thank for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0ac06f1c1ff2a789becf3f99ca7c870243faee1.png" data-download-href="/uploads/short-url/yl59SrVyxQbbIzUHAPneuxQwYX7.png?dl=1" title="SceneView" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0ac06f1c1ff2a789becf3f99ca7c870243faee1_2_690x238.png" alt="SceneView" data-base62-sha1="yl59SrVyxQbbIzUHAPneuxQwYX7" width="690" height="238" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0ac06f1c1ff2a789becf3f99ca7c870243faee1_2_690x238.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0ac06f1c1ff2a789becf3f99ca7c870243faee1_2_1035x357.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0ac06f1c1ff2a789becf3f99ca7c870243faee1.png 2x" data-dominant-color="8A8CB8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView</span><span class="informations">1251×433 68.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-01-06 16:38 UTC)

<p>This paper would be a good place to start:</p>
<p><a href="https://www.researchgate.net/publication/262075665_PyDBS_an_automated_image_processing_workflow_for_deep_brain_stimulation_surgery" class="onebox" target="_blank" rel="nofollow noopener">https://www.researchgate.net/publication/262075665_PyDBS_an_automated_image_processing_workflow_for_deep_brain_stimulation_surgery</a></p>

---

## Post #3 by @rkikinis (2019-01-06 17:07 UTC)

<p>STN might be easier to identify on the coronal views of your own data, if you used an isotropic resolution.</p>

---

## Post #4 by @wpgao (2019-01-07 06:16 UTC)

<p>Maybe you can refer to Lead-DBS, which has achieved such a goal! Some registration methods can be used to develop your own module for this!</p>

---

## Post #6 by @lassoan (2022-06-18 14:43 UTC)

<p>A post was split to a new topic: <a href="/t/register-leaddbs-atlas-with-patient-image/23926">Register LeadDBS atlas with patient image</a></p>

---
