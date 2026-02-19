---
topic_id: 14564
title: "Error When Generate Centerline Wih My Own Fbx"
date: 2020-11-12
url: https://discourse.slicer.org/t/14564
---

# Error when generate centerline wih my own fbx.

**Topic ID**: 14564
**Date**: 2020-11-12
**URL**: https://discourse.slicer.org/t/error-when-generate-centerline-wih-my-own-fbx/14564

---

## Post #1 by @Yang_Yu (2020-11-12 13:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f550fd363df8fd5a2ca2d54cd8b5e71f11f229b1.png" data-download-href="/uploads/short-url/z0auUIrFcDJCKPAmBOyGnGmyWsN.png?dl=1" title="code" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f550fd363df8fd5a2ca2d54cd8b5e71f11f229b1.png" alt="code" data-base62-sha1="z0auUIrFcDJCKPAmBOyGnGmyWsN" width="690" height="295" data-dominant-color="717171"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">code</span><span class="informations">973×416 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I converted the fbx to obj, then used the ParaView software to convert obj to vtp file, then used VMTK like above, but no matter which fbx I chose, the above error always occured . Why is that?</p>

---

## Post #2 by @lassoan (2020-11-12 14:56 UTC)

<p>There is a non-ASCII character in one of the paths or file contents. As I see, the issue is that instead of simple quote (<code>"</code>) character you use some special character in your command.</p>

---

## Post #3 by @Yang_Yu (2020-11-13 01:15 UTC)

<p>Oh, thanks, indeed. The path has non-AscII characters.</p>

---
