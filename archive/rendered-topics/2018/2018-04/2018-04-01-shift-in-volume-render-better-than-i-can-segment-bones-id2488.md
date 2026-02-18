# Shift in Volume Render - Better than I can segment bones

**Topic ID**: 2488
**Date**: 2018-04-01
**URL**: https://discourse.slicer.org/t/shift-in-volume-render-better-than-i-can-segment-bones/2488

---

## Post #1 by @brockgs (2018-04-01 15:24 UTC)

<p>Scenario: When I load a DICOM series of a head, If I go straight to Volume Render and use one of the bone presents, and then slide the “Shift” slider all the way to the right, I get an almost perfectly cleaned up view of all the bones, surgical implants and orthodontics. When I go to the Segment Editor and follow along with the various tutorials to attempt to segment out the bones and implants, I can get something somewhat close…but really no where near the sharpness and accuracy of what the “Shift” operation produces on the unsegmented volume using either of the bone presets.</p>
<p>Question: Is there a way to create a model (or a segment) of what is rendered in Volume Render screen after tweaking the presents and “Shift”?</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2018-04-01 17:46 UTC)

<p>Hi -</p>
<p>This question comes up from time to time - have a look at this discussion for background on this:</p>
<aside class="quote quote-modified" data-post="6" data-topic="524">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524/6">Save volume rendering as STL file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Semi-transparent volumetric cloud = your image data, so you already have it. No processing is performed on the data, it is visualized directly using <a href="https://en.wikipedia.org/wiki/Volume_rendering">raycasting</a>. Volume rendering visualization parameters are mostly defined by transfer functions (opacity, color, gradient), which are saved in the Slicer scene. 
STL file cannot store volumetric cloud, it only stores a surface mesh = hard boundary of your printed object. 
What confuses most people that volume rendering may give the illusion that ther…
  </blockquote>
</aside>


---

## Post #3 by @brockgs (2018-04-01 18:34 UTC)

<p>Thank you for pointing me to that thread. I remembered as soon as I clicked over to it, that I had read it a few weeks ago and forgotten about those “small” but critical differences between volumetric rendering and the creation of actual 3d meshes that are the output of segmentation.</p>

---
