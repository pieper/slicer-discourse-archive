---
topic_id: 16541
title: "How To Find Pixel Size Voxel Depth On 3D Slicer"
date: 2021-03-15
url: https://discourse.slicer.org/t/16541
---

# How to find Pixel Size/ Voxel Depth on 3D slicer? 

**Topic ID**: 16541
**Date**: 2021-03-15
**URL**: https://discourse.slicer.org/t/how-to-find-pixel-size-voxel-depth-on-3d-slicer/16541

---

## Post #1 by @simple (2021-03-15 03:26 UTC)

<p>Hello,<br>
I was hoping someone can help me find the CT scans parameters. Specifically, I know that this CT scan has an acquisition matrix of 512 x 512 pixels. However, how do I find the pixel size and voxel depth of this CT scan? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efbdedc19ee27c02392b71e9b0dece2912794536.jpeg" data-download-href="/uploads/short-url/ycR2dUrxkKPP1LOZTX6txWHPENw.jpeg?dl=1" title="Screen Shot 2021-03-14 at 8.54.44 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efbdedc19ee27c02392b71e9b0dece2912794536_2_460x500.jpeg" alt="Screen Shot 2021-03-14 at 8.54.44 PM" data-base62-sha1="ycR2dUrxkKPP1LOZTX6txWHPENw" width="460" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efbdedc19ee27c02392b71e9b0dece2912794536_2_460x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efbdedc19ee27c02392b71e9b0dece2912794536_2_690x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efbdedc19ee27c02392b71e9b0dece2912794536_2_920x1000.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-14 at 8.54.44 PM</span><span class="informations">1070×1162 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @JanWitowski (2021-03-15 03:33 UTC)

<p>What do you mean by pixel size and voxel depth? If I understand correctly, you are looking for values that are displayed in the Image Spacing field: (0.46875,0.46875,0.5). You might find <a href="https://simpleitk.readthedocs.io/en/master/fundamentalConcepts.html" rel="noopener nofollow ugc">SimpleITK’s Fundamental Concepts page</a> as well as 3D Slicer’s <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="noopener nofollow ugc">coordinate systems wiki page</a> helpful with regards to pixel spacing.</p>

---

## Post #3 by @lassoan (2021-03-15 04:57 UTC)

<p>Bit depth for original (not-postprocessed) CT images is almost always 16 bits. This is true for this image, too, since scalar type is <code>short</code>, which means “short integer” = 16 bits.</p>

---
