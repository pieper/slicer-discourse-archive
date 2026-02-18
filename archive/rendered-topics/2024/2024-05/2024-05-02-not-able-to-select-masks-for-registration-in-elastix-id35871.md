# Not able to select masks for registration in elastix

**Topic ID**: 35871
**Date**: 2024-05-02
**URL**: https://discourse.slicer.org/t/not-able-to-select-masks-for-registration-in-elastix/35871

---

## Post #1 by @Chih-Ying-Huang (2024-05-02 12:49 UTC)

<p>Operating system: Windows10<br>
Slicer version: 5.6.2<br>
Expected behavior: Registration between 2 abdominal CT image with masks<br>
Actual behavior:<br>
After import my binary mask as segmentations in slicer, I was not able to find a mask to select, as the following image shows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaa0f2609d48981c05e12416aacb3e3b1f46b50f.png" data-download-href="/uploads/short-url/xtCypmxf4YnwtKIQGhUeIKAn1Kv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaa0f2609d48981c05e12416aacb3e3b1f46b50f_2_690x479.png" alt="image" data-base62-sha1="xtCypmxf4YnwtKIQGhUeIKAn1Kv" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaa0f2609d48981c05e12416aacb3e3b1f46b50f_2_690x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaa0f2609d48981c05e12416aacb3e3b1f46b50f_2_1035x718.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaa0f2609d48981c05e12416aacb3e3b1f46b50f.png 2x" data-dominant-color="F1F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1067×741 29.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-05-02 12:52 UTC)

<p>Mask must be a label volume or segmentation. You can either convert the scalar volume to labelmap volume in Volumes module; or when you select the data for loading in the “Add data” window, choose “Segmentation” in Description column, or keep the description “Volume” and check the “LabelMap” option.</p>

---

## Post #3 by @Chih-Ying-Huang (2024-05-02 13:10 UTC)

<p>Thank you for your prompt reply, but I think I have imported my binary mask as segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9218fc03f1797cdda5fe9e42a27ace5b17d0922.jpeg" data-download-href="/uploads/short-url/o8cB3JG01QLgBjxI3siCwSGbzNM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9218fc03f1797cdda5fe9e42a27ace5b17d0922.jpeg" alt="image" data-base62-sha1="o8cB3JG01QLgBjxI3siCwSGbzNM" width="690" height="485" data-dominant-color="353535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">696×490 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c316987650240457fee60e7b32c2865b94cd2960.png" data-download-href="/uploads/short-url/rPPw5eJ7Trie4wgi8uZzdoXhwJi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c316987650240457fee60e7b32c2865b94cd2960.png" alt="image" data-base62-sha1="rPPw5eJ7Trie4wgi8uZzdoXhwJi" width="690" height="302" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">934×409 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But still, I am unable to select it from the masks in the elastix module.</p>

---
