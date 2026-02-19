---
topic_id: 21051
title: "Trouble In Depthimagetopointcloud"
date: 2021-12-14
url: https://discourse.slicer.org/t/21051
---

# Trouble in DepthImageToPointCloud

**Topic ID**: 21051
**Date**: 2021-12-14
**URL**: https://discourse.slicer.org/t/trouble-in-depthimagetopointcloud/21051

---

## Post #1 by @KWLee (2021-12-14 12:52 UTC)

<p>Hello,</p>
<p>I tried to register point cloud using realsense camera.<br>
However, the input volume is not activated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45a78cb13d5f6fef4055fc339d2bf0b5bbbe30e6.png" data-download-href="/uploads/short-url/9WbUXMRoJOFkds2H5pxWlwim24S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45a78cb13d5f6fef4055fc339d2bf0b5bbbe30e6_2_690x352.png" alt="image" data-base62-sha1="9WbUXMRoJOFkds2H5pxWlwim24S" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45a78cb13d5f6fef4055fc339d2bf0b5bbbe30e6_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45a78cb13d5f6fef4055fc339d2bf0b5bbbe30e6_2_1035x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45a78cb13d5f6fef4055fc339d2bf0b5bbbe30e6_2_1380x704.png 2x" data-dominant-color="ABACC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1557×795 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-12-14 14:15 UTC)

<p>Please try with the latest Slicer Preview Release. If there are still problems then please share the scene file with us (save the scene as .mrb file, upload it to dropbox/onedrive/gdrive/etc. and post the link here) so that we can investigate.</p>

---

## Post #3 by @KWLee (2021-12-15 00:32 UTC)

<p>Thank you for your reply.<br>
The cause of the problem was the Plus profile. It was solved by changing the setting value of UseRealSenseColorizer from “True” to “False”.</p>

---
