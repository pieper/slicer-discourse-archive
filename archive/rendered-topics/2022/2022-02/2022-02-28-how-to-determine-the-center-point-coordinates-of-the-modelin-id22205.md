---
topic_id: 22205
title: "How To Determine The Center Point Coordinates Of The Modelin"
date: 2022-02-28
url: https://discourse.slicer.org/t/22205
---

# How to determine the center point coordinates of the modeling area?

**Topic ID**: 22205
**Date**: 2022-02-28
**URL**: https://discourse.slicer.org/t/how-to-determine-the-center-point-coordinates-of-the-modeling-area/22205

---

## Post #1 by @zhuyingxinxs (2022-02-28 07:50 UTC)

<p>Can Slicer read the coordinates of the center point of the region that he modeled?<br>
Let’s say I modeled the kidney ,Can I read what the RAS coordinates are for the center of the kidney region?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8993e64ea43bb8d95272dc429a5f1a3a6f9fc09b.jpeg" data-download-href="/uploads/short-url/jD4hN5pGA16WOnsZo8NsOFZvnBh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8993e64ea43bb8d95272dc429a5f1a3a6f9fc09b_2_690x479.jpeg" alt="image" data-base62-sha1="jD4hN5pGA16WOnsZo8NsOFZvnBh" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8993e64ea43bb8d95272dc429a5f1a3a6f9fc09b_2_690x479.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8993e64ea43bb8d95272dc429a5f1a3a6f9fc09b_2_1035x718.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8993e64ea43bb8d95272dc429a5f1a3a6f9fc09b.jpeg 2x" data-dominant-color="747495"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1094×760 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jumbojing (2022-03-01 01:10 UTC)

<p>这个应该能够帮到你</p>
<aside class="quote quote-modified" data-post="9" data-topic="6209">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/centering-on-a-segment-from-a-script/6209/9">Centering on a segment from a script</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Using a custom extension is certainly a solution, but in the long term I would recommend developers to use Slicer core functions if available. 
Slicer-4.10 returning a swig pointer (such as _000001bfd4897340_p_void) is a minor inconvenience. You can still access the values using the helper function below (in the nightly version the VTK hint is there so the position is directly returned as a Python tuple). 
def getListFromPointer(bufferPtr, scalarType=vtk.VTK_DOUBLE, numberOfElements=3):
  """Con…
  </blockquote>
</aside>


---

## Post #3 by @MAURICIO_ALBERTO_LED (2023-02-24 07:36 UTC)

<p>Hello,<br>
It is possible to move a segment using code and not transformations? Thanks</p>

---

## Post #4 by @lassoan (2023-02-24 16:03 UTC)

<p>Yes, you can create any transform type and set its parameters using Python scripting.</p>

---

## Post #5 by @MAURICIO_ALBERTO_LED (2023-02-25 17:25 UTC)

<p>Thank you, Mr. Lasso. Can you give me a link where this was done? thanks</p>

---
