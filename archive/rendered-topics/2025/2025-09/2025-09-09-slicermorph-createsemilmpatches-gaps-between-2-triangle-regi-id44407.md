# SlicerMorph CreateSemiLMPatches gaps between 2 triangle regions

**Topic ID**: 44407
**Date**: 2025-09-09
**URL**: https://discourse.slicer.org/t/slicermorph-createsemilmpatches-gaps-between-2-triangle-regions/44407

---

## Post #1 by @kuoi (2025-09-09 13:15 UTC)

<p>Hello, I am new to 3D Slicer and SlicerMorph. I want to use the <em>CreateSemiLMPatches</em> module in the SlicerMorph extension to map semi-landmarks on a surface. However, after following <a href="https://youtu.be/SArudRq-M4A?si=AcfRCZ-dkPy7hQzP" rel="noopener nofollow ugc">tutorial 1</a> and <a href="https://youtu.be/UD2tmFuaSJg?si=b7havGQ-kRX-rAWn" rel="noopener nofollow ugc">tutorial 2</a>, I still cannot figure out how to fix the gaps between the two triangular regions. This might be related to the curvature of the surface.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80774b2ea3dab3c4d033d7a727a52bf4f50e0f0d.jpeg" data-download-href="/uploads/short-url/iksHvwruseGro0xWFFrappqUROt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80774b2ea3dab3c4d033d7a727a52bf4f50e0f0d.jpeg" alt="image" data-base62-sha1="iksHvwruseGro0xWFFrappqUROt" width="498" height="487"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">498×487 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a85d9adb43100c49e8ee6e37c73afe255c71ab1.jpeg" data-download-href="/uploads/short-url/1v5xXdHo4TvoaBtPKpJkt7jTm25.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a85d9adb43100c49e8ee6e37c73afe255c71ab1.jpeg" alt="image" data-base62-sha1="1v5xXdHo4TvoaBtPKpJkt7jTm25" width="399" height="498"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">399×498 81.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-09-09 14:41 UTC)

<p>When you stitch these individual patches into a single markup object (the merge highlighted nodes), the module will create interppolated points in these gaps. But it will not fully fill it. I don’t think it will work well for you.</p>

---
