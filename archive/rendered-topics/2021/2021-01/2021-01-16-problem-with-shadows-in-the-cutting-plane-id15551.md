# Problem with shadows in the cutting plane

**Topic ID**: 15551
**Date**: 2021-01-16
**URL**: https://discourse.slicer.org/t/problem-with-shadows-in-the-cutting-plane/15551

---

## Post #1 by @Andreas (2021-01-16 06:41 UTC)

<p>Hello everyone,</p>
<p>I have a problem with the representation of the cutting plane in a vessel section, it becomes very dark (shown in shadow)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91b809f9194a6eb50d4834ee7aa2eae6095344a1.jpeg" alt="Bild2" data-base62-sha1="kN5xa0GC36d5ga4mqgu09k3R0CB" width="605" height="472"></p>
<p>The cutting plane at the openings of the vessel are shown very clearly</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea4a27b12e8b8def8fb3fd5997fe9787d44fe17c.jpeg" alt="Bild1" data-base62-sha1="xqCBtR6FH0shd5u5wpvv1y1ZiPO" width="605" height="476"></p>
<p>I already tried to remove it with the Surface Toolbar box (Normals; Splitting), but without success.</p>
<p>Many thanks for your help</p>

---

## Post #2 by @lassoan (2021-01-16 06:59 UTC)

<p>To preserve sharp edges, you need to enable splitting when computing normals (auto-orientation may be useful, too).</p>
<p>You can change the material properties in Models module (make reflection less dependent on direction) or change lighting using Lighting editor module (in Sandbox extension).</p>

---
