---
topic_id: 36924
title: "Brain Segmentation In Mr"
date: 2024-06-20
url: https://discourse.slicer.org/t/36924
---

# Brain Segmentation in MR

**Topic ID**: 36924
**Date**: 2024-06-20
**URL**: https://discourse.slicer.org/t/brain-segmentation-in-mr/36924

---

## Post #1 by @BDhoth (2024-06-20 19:48 UTC)

<p>Operating system: Windows<br>
Slicer version:5.6.2<br>
Expected behavior: I have been trying to get a good brain segmentation for quite a while and have attempted the skull stripping without much success. I have watched several other videos as well, but still can’t get it to look complete or without the face/dura/etc. Any tips for this? Thank you!<br>
Actual behavior:</p>

---

## Post #2 by @JASON (2024-07-17 04:27 UTC)

<p><a class="mention" href="/u/bdhoth">@BDhoth</a> Have you tried HDBET? I’ve had success with the 3D Slicer extension on MRI<br>
<a href="https://extensions.slicer.org/view/HDBrainExtraction/32919/win" class="onebox" target="_blank" rel="noopener nofollow ugc">https://extensions.slicer.org/view/HDBrainExtraction/32919/win</a></p>

---

## Post #3 by @BDhoth (2024-07-19 13:48 UTC)

<p>I have not tried that. I installed it. I really wish there were better instructions of how to use these extensions.</p>

---

## Post #4 by @JASON (2024-07-19 13:55 UTC)

<p>HDBET is pretty easy.  It asks for input volume that you want to skull strip, and you can set two outputs for the new stripped volume and the new<br>
brain mask segmentation.  Set both of these outputs to “Create New…” and hit ‘Apply’.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64d48e18779ca00ee5d24edb4d66013ea33eb9cb.jpeg" alt="HDBET" data-base62-sha1="enZ8W9XlhLp75LYjSXfM6WhyIfV" width="366" height="334"></p>

---

## Post #5 by @BDhoth (2024-07-19 15:22 UTC)

<p>Weird, that was what I did the first time and it came up with a weird “torch” error and failed. It worked this second time; however, how do I handle it in segment editor to have just the brain and no skull/face?<br>
Thank you so much for your help!</p>
<details>
<summary>
(attachments)</summary>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c8b3e705256938a4109a52d2d7849ef215a5e13.png" data-download-href="/uploads/short-url/dcGfRVqyr98dJD3k0WCyYKT2XiH.png?dl=1" title="Screenshot 2024-07-19 102043.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c8b3e705256938a4109a52d2d7849ef215a5e13_2_690x388.png" alt="Screenshot 2024-07-19 102043.png" data-base62-sha1="dcGfRVqyr98dJD3k0WCyYKT2XiH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c8b3e705256938a4109a52d2d7849ef215a5e13_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c8b3e705256938a4109a52d2d7849ef215a5e13_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c8b3e705256938a4109a52d2d7849ef215a5e13_2_1380x776.png 2x" data-dominant-color="727775"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-07-19 102043.png</span><span class="informations">1849×1040 339 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</details>

---

## Post #6 by @JASON (2024-07-19 19:00 UTC)

<p>It looks like you correctly created a brain mask segmentation in white, and a new skull-stripped volume.  The green segment looks like it is from a different segmentation node created from threshold of the image before skull stripping.</p>
<p>If you go back to the data view, you can turn off the node named ‘Segmentation’ with the green head label to see only the brain mask label in white.</p>

---
