# Q- Surface area reported from Models: outward facing polys only?

**Topic ID**: 11795
**Date**: 2020-05-30
**URL**: https://discourse.slicer.org/t/q-surface-area-reported-from-models-outward-facing-polys-only/11795

---

## Post #1 by @hherhold (2020-05-30 14:27 UTC)

<p>I have a quick question on the surface area number reported by the Models module. I did a quick exercise where I made a 5cm sphere (well, as close as I could get by hand using the ruler) and compared reported values to hand-computed values -  4<em>pi</em>r^2, etc.</p>
<p>The value I get for surface area is what I would expect, but I was a little confused from earlier posts (<a href="https://discourse.slicer.org/t/using-surface-cut-of-segment-editor-to-measure-area/5990" class="inline-onebox">Using surface cut of segment editor to measure area</a>) regarding counting front-facing and back-facing polygons in the area calculation, and needing to divide by 2.</p>
<p>For a “closed surface representation”, such as a segment converted to a model, it seems that the computed surface area is the outward-facing polygons only, and one does not need to divide the reported quantity by 2. Is this correct?</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #2 by @jamesobutler (2020-05-30 14:41 UTC)

<p>I think what was meant for surface cut is that on a 2D image if you draw say a circle then your 3D surface is like a circle disc shaped object. Therefore the surface area includes both the front side and the back side so you would divide by 2 to get the area of the circle. I guess technically there is an edge to the disc which has surface area, but dividing by 2 will get you close.</p>

---

## Post #3 by @lassoan (2020-05-31 01:02 UTC)

<p>You only need to divide the surface area by 2 if you want to measure area of an <em>open</em> surface by creating a very flat <em>closed</em> surface around it (as the closed surface wraps around both sides of the open surface).</p>
<p>For open surface measurements I would no longer recommend creating a closed surface and divide by 2, but instead you have better options, such as:</p>
<p>A. Use closed curve markups:</p>
<aside class="quote quote-modified" data-post="4" data-topic="1549">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-can-i-calculate-an-area-on-a-ct-image-i-can-calculate-volumes-mm-3-but-not-areas-mm-2/1549/4">How can I calculate an area on a CT image. I can calculate volumes (mm^3) but not areas (mm^2)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In recent Slicer Preview Releases, you can draw curves and get their surface area (2D surface, as you would expect - only one side, no thickness). 
Select “Closed Curve” from the “Create and place” toolbar button: 
[image] 
Left-click on the image to place curve control points and right-click to finish placement: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afbfca82fc601e6495718a98b3c4735dc5f340bd.jpeg" data-download-href="/uploads/short-url/p4Kt09z7g2nQyXrcfHragp55kPb.jpeg?dl=1" title="image">[image]</a> 
Measurements on curves are still work in progress, but you can open the Python console (Ctrl-3) and copy-paste the code below to see the surface area: 
curves=slicer.util.get…
  </blockquote>
</aside>

<p>B. Use cross section area measurement module:</p>
<aside class="quote" data-post="1" data-topic="11293">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-for-measuring-cross-section-area-of-segments/11293">New module for measuring cross-section area of segments</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A new module - “Segment cross-section area” - has been added to Slicer. It can compute cross-sectional area of segmented structures along a chosen axis direction. Results are available both as a table and can be shown in a plot, too. Short demo video: 

For now, the module is available by installing “Sandbox” extension in the extension manager in a recent 3D Slicer Preview Release. 
If you have any comments and suggestions then please post it here.
  </blockquote>
</aside>


---
