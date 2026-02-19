---
topic_id: 9268
title: "Upside Down Images"
date: 2019-11-22
url: https://discourse.slicer.org/t/9268
---

# Upside down images

**Topic ID**: 9268
**Date**: 2019-11-22
**URL**: https://discourse.slicer.org/t/upside-down-images/9268

---

## Post #1 by @prorai (2019-11-22 13:08 UTC)

<p>Hello,<br>
Why slicer reads images upside down, as my Dicom scan images are upside down in real , but when i open this in slicer it always flips it.<br>
how can i set to open the images\scans as it is?</p>
<p>Actual image:-</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fc9e38060c9160c89eb8fdf8328a901bbf967ce.jpeg" data-download-href="/uploads/short-url/6OKZ6G0cV0JoM9qAgc1fcdwlkhE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fc9e38060c9160c89eb8fdf8328a901bbf967ce_2_477x375.jpeg" alt="image" data-base62-sha1="6OKZ6G0cV0JoM9qAgc1fcdwlkhE" width="477" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fc9e38060c9160c89eb8fdf8328a901bbf967ce_2_477x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fc9e38060c9160c89eb8fdf8328a901bbf967ce_2_715x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fc9e38060c9160c89eb8fdf8328a901bbf967ce_2_954x750.jpeg 2x" data-dominant-color="222222"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1124×882 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>image loaded in Slicer -</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7ba5e264945d370aee521bfffec79f5fc37ba2ae.png" alt="image" data-base62-sha1="hDQ8kMPgaOwWefNk5DGCmB9oQhg" width="477" height="315"><br>
Thanks,</p>

---

## Post #2 by @lassoan (2019-11-22 13:51 UTC)

<p>Slicer displays images in correct anatomical orientation (based on patient position specified during scanning).</p>
<aside class="quote no-group" data-username="prorai" data-post="1" data-topic="9268">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>my Dicom scan images are upside down in real</p>
</blockquote>
</aside>
<p>The image above shows that the patient was lying on the table in supine position, and the image is oriented accordingly in the axial view in Slicer. I don’t know what you mean by “upside down in real”, but to me everything looks correct.</p>
<p>It is unusual to show axial images with their posterior side “up” (patient hanging down from the table), but you can do that by reorienting the view using Reformat module (Rotation section).</p>

---

## Post #3 by @prorai (2019-11-22 14:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9268">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is unusual to show axial images with their posterior side “up” (patient hanging down from the table), but you can do that by reorienting the view using Reformat module (Rotation section).</p>
</blockquote>
</aside>
<p>i totally agree with you, but is it possible to load the images as it is or without flipping the orientation , though it is necessary ?</p>

---

## Post #4 by @lassoan (2019-11-22 14:19 UTC)

<p>The image is always loaded correctly. You can reorient slice views as I described above (using Reformat module).</p>

---
