---
topic_id: 20659
title: "Problem To Save A Segmentation"
date: 2021-11-17
url: https://discourse.slicer.org/t/20659
---

# Problem to save a segmentation

**Topic ID**: 20659
**Date**: 2021-11-17
**URL**: https://discourse.slicer.org/t/problem-to-save-a-segmentation/20659

---

## Post #1 by @Lise_Kasperski (2021-11-17 13:35 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226</p>
<p>Actual behavior: I have a problem with how Slicer saves my files. I can’t save my segmentation with click on save icon after I creat the model. So, I can save my segmentation as .STL and .nrrd by Segmentations modul but I can’t save as .mrml and as .seg.nrrd. I try to reinstall 3D Slicer but it doesn’t work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89db5aba34d3fbfd215a844a5979be1b364cfd2c.png" data-download-href="/uploads/short-url/jFxnroqxl8geA9rM8RL5RtLYy60.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89db5aba34d3fbfd215a844a5979be1b364cfd2c_2_690x374.png" alt="Capture" data-base62-sha1="jFxnroqxl8geA9rM8RL5RtLYy60" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89db5aba34d3fbfd215a844a5979be1b364cfd2c_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89db5aba34d3fbfd215a844a5979be1b364cfd2c_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89db5aba34d3fbfd215a844a5979be1b364cfd2c_2_1380x748.png 2x" data-dominant-color="56586B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1920×1042 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can see in this picture what it shows me when I press the save button.</p>
<p>Thank you!</p>
<p>Lise</p>

---

## Post #2 by @lassoan (2021-11-17 18:24 UTC)

<p>When you use the menu File / Save, then <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">segmentation will be saved using the current master representation</a> to preserve original data. All other representations are computed from the master representation when needed.</p>
<p>If you set the segmentation’s master representation to binary labelmap, then you will be able to save it as .seg.nrrd. If not then it might be a bug, which is most likely already fixed in recent Slicer Preview Releases.</p>

---

## Post #3 by @Lise_Kasperski (2021-11-19 11:58 UTC)

<p>Thank you, you are right, with the Slicer Preview Releases it’s fixed.</p>

---
