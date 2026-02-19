---
topic_id: 18978
title: "Reducing Noise In Large Object Ct Scans"
date: 2021-07-29
url: https://discourse.slicer.org/t/18978
---

# Reducing noise in large object CT scans

**Topic ID**: 18978
**Date**: 2021-07-29
**URL**: https://discourse.slicer.org/t/reducing-noise-in-large-object-ct-scans/18978

---

## Post #1 by @CETUS (2021-07-29 18:19 UTC)

<p>Hi everyone, I am relatively new to Slicer. I was interested to inquire what options 3D slicer has for reducing noise in CT scans of large objects. In this case I am using archived scans of large animal specimens. My plan is to segment out various structures from these scans. I have noticed that in the thickest regions of the specimen, there appear to be scattered voxels in the soft tissue that are higher intensity than soft tissue, and scattered voxels in the bone that are lower intensity than bone. The result is a “grainy” loss of resolution in the image, and difficulty using automatic thresholding tools (as it will “grab” voxels that are actually not part of the structure).</p>
<p>While I recognize that this is an inherent limitation/flaw of this data, and I plan to use a significant amount of manual segmentation to get around it, I wanted to check if there are modules/functions in Slicer that might help reduce this kind of noise. Included is one of the more extreme examples in a bone window. Thank you for your help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01d4cd2d4249efeefd4e5d900487534fa3ea4278.jpeg" data-download-href="/uploads/short-url/gcoXi49xpDB0U3KhmtKOxWmM9W.jpeg?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01d4cd2d4249efeefd4e5d900487534fa3ea4278_2_690x386.jpeg" alt="Picture1" data-base62-sha1="gcoXi49xpDB0U3KhmtKOxWmM9W" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01d4cd2d4249efeefd4e5d900487534fa3ea4278_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01d4cd2d4249efeefd4e5d900487534fa3ea4278_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01d4cd2d4249efeefd4e5d900487534fa3ea4278.jpeg 2x" data-dominant-color="474747"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">1366×765 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-07-29 20:45 UTC)

<p>There are denoising options in the Filters section of the module panel, sometimes they work very well and sometimes you lose the features you were trying to preserve.  Gradient anisotropic diffusion can be good,  or a median filter.  You might ask on the ITK forum for suggestions.  These days I would expect a deep learning algorithm would outperform the traditional approaches but I haven’t seen one yet.</p>

---

## Post #3 by @CETUS (2021-08-04 13:18 UTC)

<p>Thank you so much-I will definitely try out those functions and check out the ITK forum. Thank you for your help!</p>

---
