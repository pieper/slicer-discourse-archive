# Combining segmentation hierarchies

**Topic ID**: 16258
**Date**: 2021-02-27
**URL**: https://discourse.slicer.org/t/combining-segmentation-hierarchies/16258

---

## Post #1 by @YOZ (2021-02-27 13:30 UTC)

<p>Hi</p>
<p>I’m having issues with segmentations, for some reason during my work, I did too much segmentation hierarchy. And now within each layer or hierarchy there is a bit of changes I made as you can see in the picture</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe6ff24b97334846cb3e9233a25a73f5ff6f873e.png" data-download-href="/uploads/short-url/AiR7xMpgFZ4Fow4kXE2Cip2Dwaa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe6ff24b97334846cb3e9233a25a73f5ff6f873e_2_690x259.png" alt="image" data-base62-sha1="AiR7xMpgFZ4Fow4kXE2Cip2Dwaa" width="690" height="259" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe6ff24b97334846cb3e9233a25a73f5ff6f873e_2_690x259.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe6ff24b97334846cb3e9233a25a73f5ff6f873e_2_1035x388.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe6ff24b97334846cb3e9233a25a73f5ff6f873e_2_1380x518.png 2x" data-dominant-color="B2CED1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2553×961 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The segments within each hierarchy are the same (Renal pelvis, Renal cortex, DJ stent, other)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea30159cd15192c3cba5871e1e380ea4221f663.png" data-download-href="/uploads/short-url/rcrXj5H8daOpMzIQrVm6DocrEBB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea30159cd15192c3cba5871e1e380ea4221f663.png" alt="image" data-base62-sha1="rcrXj5H8daOpMzIQrVm6DocrEBB" width="690" height="142" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1019×210 8.95 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to combine the similar segments within each hierarchy into one hierarchy? because I’m having troubles smoothing out the model</p>

---

## Post #2 by @lassoan (2021-02-27 16:14 UTC)

<p>You can combine segments using Logical operators effect.</p>
<p>You can also move islands (connected parts) of a segment to another segment using Islands effect (“Add selected island” mode).</p>

---

## Post #3 by @YOZ (2021-03-22 19:35 UTC)

<p>Thank you so much! This helped.</p>

---
