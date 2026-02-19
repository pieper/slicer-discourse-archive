---
topic_id: 43647
title: "Segmenting Thin Spaces Sparse Contours"
date: 2025-07-08
url: https://discourse.slicer.org/t/43647
---

# Segmenting Thin Spaces (Sparse Contours)

**Topic ID**: 43647
**Date**: 2025-07-08
**URL**: https://discourse.slicer.org/t/segmenting-thin-spaces-sparse-contours/43647

---

## Post #1 by @Ryan_Jones (2025-07-08 12:45 UTC)

<p>Hi, I need to segment the subarachnoid space in some canine MRIs. This space is extremely thin, however, I would like to maintain some of the information about variable thicknesses so simply segmenting an inner surface and thickening will not suffice in my case. I have significantly interpolated the grids isotropically, but the voxel density is still insufficient to generate a model from the segmentations, I have tried using the smoothing tool but the kernel size required to fix this is too large and overly inflates the space. Does anyone have any ideas to generate this model?</p>
<p>This model is only partially segmented, but I hope it communicates the issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1390d0ee5a764958d60e98a4379c115a1291ae1.png" data-download-href="/uploads/short-url/ypXiHlNXXraCwbaOSlQNtVOEPn3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1390d0ee5a764958d60e98a4379c115a1291ae1_2_690x211.png" alt="image" data-base62-sha1="ypXiHlNXXraCwbaOSlQNtVOEPn3" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1390d0ee5a764958d60e98a4379c115a1291ae1_2_690x211.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1390d0ee5a764958d60e98a4379c115a1291ae1_2_1035x316.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1390d0ee5a764958d60e98a4379c115a1291ae1.png 2x" data-dominant-color="959DCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1317×404 86.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thankyou for the help!!</p>

---

## Post #2 by @chz31 (2025-07-09 16:29 UTC)

<p>I recently learned that supersample the segments might be helpful for thin structures.<br>
Basically, you go to Segmentation Editor, click the cube:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a037b54524f883c5811592414cd3df77f83c00c2.png" data-download-href="/uploads/short-url/mRlKsii5b7VZRiiO7k1yvOSoXbc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a037b54524f883c5811592414cd3df77f83c00c2_2_517x159.png" alt="image" data-base62-sha1="mRlKsii5b7VZRiiO7k1yvOSoXbc" width="517" height="159" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a037b54524f883c5811592414cd3df77f83c00c2_2_517x159.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a037b54524f883c5811592414cd3df77f83c00c2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a037b54524f883c5811592414cd3df77f83c00c2.png 2x" data-dominant-color="CCD3D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">771×239 37.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can then increase the number of oversampling factor.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15152ef74ca5da195f9c191467fd3a59bd7e449f.png" data-download-href="/uploads/short-url/30vpyDd57CDRDkCmkWmjhFaCkKr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15152ef74ca5da195f9c191467fd3a59bd7e449f.png" alt="image" data-base62-sha1="30vpyDd57CDRDkCmkWmjhFaCkKr" width="486" height="368"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">648×491 42.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I haven’t evaluated the effect though, and I only used it for thin bones in CT images. Subarachnoid space sounds really challenging. Are you able to see the space &amp; structures clearly in MRI, like some blood vessels?</p>

---
