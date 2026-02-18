# Rendering artifact

**Topic ID**: 24065
**Date**: 2022-06-27
**URL**: https://discourse.slicer.org/t/rendering-artifact/24065

---

## Post #1 by @rprueckl (2022-06-27 14:07 UTC)

<p>Hi,</p>
<p>I am experiencing rendering artifacts in a custom vtk renderer/render window in a dialog box.<br>
I manually load an obj and a texture and want to display this. The result is as follows:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b687fb4736208eb813627268305e7c6b4beeff0c.png" alt="image" data-base62-sha1="q2KeNNifgZrNZhjDULTjgYQ4yTi" width="619" height="182"><br>
When I use the same code, but add the actor to one of the standard slicer 3d views, the result looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c4c65061bb428d54ae237d57a0b07af4aed66dd.png" data-download-href="/uploads/short-url/k18wh9o3RAAJ1A2lL1P8m4b41SR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c4c65061bb428d54ae237d57a0b07af4aed66dd.png" alt="image" data-base62-sha1="k18wh9o3RAAJ1A2lL1P8m4b41SR" width="690" height="156" data-dominant-color="303030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×219 1009 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Does anybody know where this difference could come from?</p>
<p>thanks in advance</p>

---

## Post #2 by @lassoan (2022-06-28 03:30 UTC)

<p>The artifact does not look familiar. If the problem is not reproducible in Slicer views but it is reproducible in a stock VTK renderer outside Slicer then it may be better to report it on the VTK forum.</p>

---

## Post #3 by @rprueckl (2022-06-29 14:41 UTC)

<p>I didn’t find the root-cause for the artifact, but I managed to remove it.</p>
<p>The object in question basically only has two colors. So I initially created the texture mapping such that triangles of the same color would map to the same texture coordinates. This means that texture coordinates of the same-color triangles overlapped. This is when I saw the artifact.</p>
<p>I changed mapping such that each triangle now has its own space on the texture (i.e. no overlap anymore), and the artifact was gone.</p>
<p>I will post this also in the VTK forum.</p>

---
