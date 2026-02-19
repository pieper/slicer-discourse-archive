---
topic_id: 34029
title: "Make 3D View Quality Independent Of Corresponding 2D Slice"
date: 2024-01-29
url: https://discourse.slicer.org/t/34029
---

# Make 3D view quality independent of corresponding 2D slice

**Topic ID**: 34029
**Date**: 2024-01-29
**URL**: https://discourse.slicer.org/t/make-3d-view-quality-independent-of-corresponding-2d-slice/34029

---

## Post #1 by @keri (2024-01-29 19:14 UTC)

<p>Hi,</p>
<p>I’ve always been wondering is it possible to make 3D visualization quality independent of how many pixels are actually shown of the corresponding slice in the slice view?<br>
See the picture for example.<br>
If slice is far from the camera then the 3D view is poor.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb307b356813e1cd568281bb8bb566944e56e18b.jpeg" data-download-href="/uploads/short-url/qHX9LZggz4U08Qiz3HAmUfX2pCP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb307b356813e1cd568281bb8bb566944e56e18b_2_690x357.jpeg" alt="image" data-base62-sha1="qHX9LZggz4U08Qiz3HAmUfX2pCP" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb307b356813e1cd568281bb8bb566944e56e18b_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb307b356813e1cd568281bb8bb566944e56e18b_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb307b356813e1cd568281bb8bb566944e56e18b_2_1380x714.jpeg 2x" data-dominant-color="544F62"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1495×774 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-01-29 23:04 UTC)

<p>There are options for that:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc4d7f6a43c16cacfc377c5d41bd7bffe5af299.png" data-download-href="/uploads/short-url/46v6uirUqTcTcsmCYofTFczG9yp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc4d7f6a43c16cacfc377c5d41bd7bffe5af299_2_690x385.png" alt="image" data-base62-sha1="46v6uirUqTcTcsmCYofTFczG9yp" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc4d7f6a43c16cacfc377c5d41bd7bffe5af299_2_690x385.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc4d7f6a43c16cacfc377c5d41bd7bffe5af299.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc4d7f6a43c16cacfc377c5d41bd7bffe5af299.png 2x" data-dominant-color="D3D8CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">896×500 77.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @keri (2024-01-30 07:54 UTC)

<p>Thank you very much!<br>
The first option <code>FOX, Spacing match Volumes</code> was exactly what I was looking for!<br>
Haven’t tried these options before.</p>

---
