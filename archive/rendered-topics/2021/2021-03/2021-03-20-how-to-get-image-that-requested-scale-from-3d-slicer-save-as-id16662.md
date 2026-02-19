---
topic_id: 16662
title: "How To Get Image That Requested Scale From 3D Slicer Save As"
date: 2021-03-20
url: https://discourse.slicer.org/t/16662
---

# How to get image that requested scale from 3d slicer (save as NITFI)? 

**Topic ID**: 16662
**Date**: 2021-03-20
**URL**: https://discourse.slicer.org/t/how-to-get-image-that-requested-scale-from-3d-slicer-save-as-nitfi/16662

---

## Post #1 by @KAMONCHAT_APIVANICHK (2021-03-20 22:55 UTC)

<p>I am researching about segmentation by deep learning via python then I would like to save CT Scan in .png or .jpg for using as input dataset but pictures what I got is bone-scale like the first picture. Have any way I can get picture like the second picture.</p>
<p>The first picture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bd60aa12a318ba8e8f5975eaad1ecd1c60468dc.jpeg" data-download-href="/uploads/short-url/aOSojliHo1NkPA2RiXhz605QpfC.jpeg?dl=1" title="6_im000056" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bd60aa12a318ba8e8f5975eaad1ecd1c60468dc_2_500x500.jpeg" alt="6_im000056" data-base62-sha1="aOSojliHo1NkPA2RiXhz605QpfC" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bd60aa12a318ba8e8f5975eaad1ecd1c60468dc_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bd60aa12a318ba8e8f5975eaad1ecd1c60468dc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bd60aa12a318ba8e8f5975eaad1ecd1c60468dc.jpeg 2x" data-dominant-color="232323"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6_im000056</span><span class="informations">512×512 29.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The second picture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/584f4eae442d8d74001512e4f68d82f3c083bd66.jpeg" data-download-href="/uploads/short-url/cBdVOW6TE15P0gSDG6gKv6KQGTI.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/584f4eae442d8d74001512e4f68d82f3c083bd66_2_690x386.jpeg" alt="Untitled" data-base62-sha1="cBdVOW6TE15P0gSDG6gKv6KQGTI" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/584f4eae442d8d74001512e4f68d82f3c083bd66_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/584f4eae442d8d74001512e4f68d82f3c083bd66_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/584f4eae442d8d74001512e4f68d82f3c083bd66.jpeg 2x" data-dominant-color="999895"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1370×768 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-03-25 13:53 UTC)

<aside class="quote no-group" data-username="KAMONCHAT_APIVANICHK" data-post="1" data-topic="16662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kamonchat_apivanichk/48/10368_2.png" class="avatar"> KAMONCHAT_APIVANICHK:</div>
<blockquote>
<p>I would like to save CT Scan in .png or .jpg for using as input dataset</p>
</blockquote>
</aside>
<p>I would not recommend to export as png or jpg but instead use deep learning frameworks that are properly equipped to work with medical images (and can load commonly used medical image file formats), such as <a href="https://monai.io/">monai</a>.</p>

---
