# How to export a red slice view while keeping the pixel value according to the Color Scalar Bar?

**Topic ID**: 23955
**Date**: 2022-06-20
**URL**: https://discourse.slicer.org/t/how-to-export-a-red-slice-view-while-keeping-the-pixel-value-according-to-the-color-scalar-bar/23955

---

## Post #1 by @user4 (2022-06-20 09:51 UTC)

<p>Hi all,<br>
This is a sample data,I want to do some quantitative analysis so I need the pixel values.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ada128dd0d1b5070797fe033d6e74c0f03168a5a.jpeg" data-download-href="/uploads/short-url/oLZST2NfG0JZRgm5wAGlpY5ROvE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ada128dd0d1b5070797fe033d6e74c0f03168a5a_2_690x388.jpeg" alt="image" data-base62-sha1="oLZST2NfG0JZRgm5wAGlpY5ROvE" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ada128dd0d1b5070797fe033d6e74c0f03168a5a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ada128dd0d1b5070797fe033d6e74c0f03168a5a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ada128dd0d1b5070797fe033d6e74c0f03168a5a_2_1380x776.jpeg 2x" data-dominant-color="7B7A7A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 98.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I can use data probe to see the pixel value marked in blue.Now I want to save this picture,but if I use screen capture to save it as a png file,the pixel value becomes between 0-255.<br>
There is a color bar marked in green, I want to know if I can save the whole 2D view while keeping the original pixel values?<br>
Thank you in advance for your help!</p>

---

## Post #2 by @pieper (2022-06-20 19:28 UTC)

<p>You can’t fit the original pixel values into a png file.  You would need to use a different format, such as nrrd.</p>

---

## Post #4 by @user4 (2022-06-21 07:24 UTC)

<p>Thanks Steve,<br>
If I want to save the 2D view as a nrrd file,<strong>not the whole volume</strong>,just only the slice,does Slicer4.13 currently have an existing GUI or does script repository have relevant python code?</p>

---

## Post #5 by @lassoan (2022-06-21 17:09 UTC)

<p>You can get access to the resliced image before intensity rescaling as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-randomly-oriented-slabs-of-given-shape-from-a-volume">this code snippet</a>.</p>

---
