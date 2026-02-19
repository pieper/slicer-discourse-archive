---
topic_id: 28881
title: "Export Stl Issue With Meshmixer Or Other Softwares"
date: 2023-04-13
url: https://discourse.slicer.org/t/28881
---

# Export stl issue with meshmixer or other softwares

**Topic ID**: 28881
**Date**: 2023-04-13
**URL**: https://discourse.slicer.org/t/export-stl-issue-with-meshmixer-or-other-softwares/28881

---

## Post #1 by @ortho3d (2023-04-13 11:52 UTC)

<p>Operating system:<br>
Slicer version:503<br>
why the export in stl is not done as before see pictures<br>
thank you<br>
should I reinstall 3Dslicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e331e1b96833f6b7e8ba935ea499a347e6d58454.jpeg" data-download-href="/uploads/short-url/wpRfVAw42PAcYEZNOM1xXxg9bhO.jpeg?dl=1" title="2023-04-13_13h45_02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e331e1b96833f6b7e8ba935ea499a347e6d58454.jpeg" alt="2023-04-13_13h45_02" data-base62-sha1="wpRfVAw42PAcYEZNOM1xXxg9bhO" width="690" height="467" data-dominant-color="534948"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-04-13_13h45_02</span><span class="informations">1144×775 47.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-04-13 12:16 UTC)

<p>It looks like the surface normals are inside out. Perhaps you applied a transform to the model in Slicer that turned the model inside out. Anyway, you can always recompute/reorient normals in Surface Toolbox module.</p>
<p>Always use the latest version of Slicer. In general, use the latest Slicer Stable Release, but if you need some most recent feature or fixe then the latest Slicer Preview Release.</p>

---

## Post #3 by @ortho3d (2023-04-14 08:57 UTC)

<p>Thanks a lot</p>
<p>Envoyé de mon iPhone</p>

---
