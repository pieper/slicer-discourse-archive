# Displaying Brain Aneurysm in 3D from Mask

**Topic ID**: 31496
**Date**: 2023-09-01
**URL**: https://discourse.slicer.org/t/displaying-brain-aneurysm-in-3d-from-mask/31496

---

## Post #1 by @Vineet_Saravanan (2023-09-01 02:37 UTC)

<p>Hello, I have some aneurysm masks I want to visualize in 3D. I have imported them into the 3D slicer and first tried to use the thresholding tool, but I only see green when the threshold is less than 1, and then the whole screen is green/selected. If I increase it just a bit, nothing is green, not even the aneurysm. I can manually select the aneurysm using the paint tool, but that doesn’t seem accurate around the aneurysm due to pixel size.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5647dea8bb556a99712fe6f99ce9ab075fa7d83a.png" data-download-href="/uploads/short-url/cjh2EbUl8CMw6BXxCVD1DmIyrvs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5647dea8bb556a99712fe6f99ce9ab075fa7d83a_2_690x342.png" alt="image" data-base62-sha1="cjh2EbUl8CMw6BXxCVD1DmIyrvs" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5647dea8bb556a99712fe6f99ce9ab075fa7d83a_2_690x342.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5647dea8bb556a99712fe6f99ce9ab075fa7d83a_2_1035x513.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5647dea8bb556a99712fe6f99ce9ab075fa7d83a_2_1380x684.png 2x" data-dominant-color="6F6F6B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2858×1418 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Vineet_Saravanan (2023-09-03 18:27 UTC)

<p>Does the threshold not work for something like this?</p>

---

## Post #3 by @pieper (2023-09-03 19:55 UTC)

<p>It may not work well if your scalar range is very small.  Maybe if you post some example data someone can give you advice.</p>

---
