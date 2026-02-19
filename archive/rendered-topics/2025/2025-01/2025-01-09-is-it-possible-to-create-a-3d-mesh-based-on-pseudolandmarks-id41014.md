---
topic_id: 41014
title: "Is It Possible To Create A 3D Mesh Based On Pseudolandmarks"
date: 2025-01-09
url: https://discourse.slicer.org/t/41014
---

# Is it possible to create a 3D mesh based on pseudolandmarks from pseudoLMGenerator

**Topic ID**: 41014
**Date**: 2025-01-09
**URL**: https://discourse.slicer.org/t/is-it-possible-to-create-a-3d-mesh-based-on-pseudolandmarks-from-pseudolmgenerator/41014

---

## Post #1 by @lv_xiao (2025-01-09 16:22 UTC)

<p>Dear all,</p>
<p>I am using pseudoLMGenerator to create pseudolandmarks based on a 3D mesh of human mandible. Is it possible to triangulate the created pseudolandmarks to form a mesh of human mandible? I wish the created new mesh to maximally respect the shape of the original mesh of human mandible.</p>
<p>I understand there are some algorithms for creating mesh purely from point cloud. But I wish the original mandible mesh could be leveraged to construct the new mandible mesh. Not sure if this is possible.</p>
<p>If this is not possible, may I learn if there is any recommended point cloud-based triangulation algorithm?</p>
<p>Best regards,<br>
Lv</p>

---

## Post #2 by @muratmaga (2025-01-09 16:29 UTC)

<p>Can you explain what you want to do with that mesh?</p>
<p>PseudoLMGenerator is already giving you that sparse mesh, it is just turned off not to clutter the 3D Scene.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ce098ffd1f37f26646deeab7baeeed06351e7d7.png" data-download-href="/uploads/short-url/k6g2JA8nONjPM4oFuNu3D00gymX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ce098ffd1f37f26646deeab7baeeed06351e7d7.png" alt="image" data-base62-sha1="k6g2JA8nONjPM4oFuNu3D00gymX" width="690" height="395" data-dominant-color="8988BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1091×625 92.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In fact that sparse mesh is where the points are coming from.</p>

---
