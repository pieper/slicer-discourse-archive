# Exporting outlines of segmented objects

**Topic ID**: 5771
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/exporting-outlines-of-segmented-objects/5771

---

## Post #1 by @Telfer (2019-02-13 22:38 UTC)

<p>I have set of previously segmented knee bones from MRI. In each slice, the segmented area is filled. I’d like to export the outline (external curve) of each segment for each slice in a specific plane, ideally as a list of 3D points.</p>
<p>I can export the solid models and work backwards from these to get the outlines, but was hoping that there was a quicker way to do this within Slicer?</p>
<p>Thanks,<br>
Scott</p>

---

## Post #2 by @pieper (2019-02-14 15:01 UTC)

<p>You can use the hollow effect to get the surface.  Then if you want the coordinates of the points you can export to labelmap and use numpy.where.</p>
<aside class="quote quote-modified" data-post="1" data-topic="2464">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-editor-effect-for-creating-hollow-objects/2464">New segment editor effect for creating hollow objects</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Making a solid segment hollow is useful in many applications, such as creating 3D-printable vessel walls from contrast-CT volumes. 
While it was possible to create hollow segments in 3D Slicer by using Margins and Logical operators effect, it was not very convenient. 
A new effect - Hollow - has been added to Segment editor to create hollow objects from solid objects in one simple step. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1.jpeg" data-download-href="/uploads/short-url/8ODYv3Esp7oHaIyuhVKlro8AbsZ.jpg?dl=1" title="image">[image]</a> 
Short demo video: 

  <a href="https://www.youtube.com/watch?v=jtDHTaAEilU" target="_blank" rel="noopener">
    [Make hollow - new segment editor effect in 3D Slicer]
  </a>
  </blockquote>
</aside>


---
