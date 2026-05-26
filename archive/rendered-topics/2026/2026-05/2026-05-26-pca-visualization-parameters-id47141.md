---
topic_id: 47141
title: "PCA visualization parameters"
date: 2026-05-26
url: https://discourse.slicer.org/t/47141
last_bumped: 2026-05-26T16:44:20.231Z
---

# PCA visualization parameters

**Topic ID**: 47141
**Date**: 2026-05-26
**URL**: https://discourse.slicer.org/t/pca-visualization-parameters/47141

---

## Post #1 by @Stephan_Collins (2026-05-26 16:44 UTC)

<p>Hi everyone,<br>
I am working with the GPA module from slicermorph and I noticed some changes which are most likely intentional and for good reasons but I need to ask.</p>
<p>When you have a PCA showing segregation thanks to multiple axes such as here (not the best significant example I guess), the Interactive 3D visualization tab from the GPA module would allow you to play with two PCs simultaneously. This has changed in the latest version I think and I can only use one at a time. I suppose I can show the effect of one composant on one axis (show a distance to distance map for small values on PC1 vs high values and then do the same on the second axis (pc2). More work but possibly more accurate to describe what may be going on ? Conceptually, though, combining PC1 and PC2 absolutely makes sense when data separate “diagonally”. but a scaled displacements along PC1 and PC2 is not really like applying two transforms in sequence, is it ?<br>
Is this why this approach was removed. What should we do in these cases ?<br>
My apologies if this was discussed elsewhere</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a97d38601c5002b18886d4425b30da3a70c919.png" data-download-href="/uploads/short-url/ucrSfN1njIvcQTZYbWeVvWNP7Lz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a97d38601c5002b18886d4425b30da3a70c919.png" alt="image" data-base62-sha1="ucrSfN1njIvcQTZYbWeVvWNP7Lz" width="436" height="372"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">436×372 41.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
