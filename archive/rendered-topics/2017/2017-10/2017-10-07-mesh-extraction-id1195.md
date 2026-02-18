# Mesh extraction

**Topic ID**: 1195
**Date**: 2017-10-07
**URL**: https://discourse.slicer.org/t/mesh-extraction/1195

---

## Post #1 by @Patrick_Braga (2017-10-07 14:15 UTC)

<p>Hi folks,</p>
<p>I´ve been trying to separate parts of the head to use on Maya software for medicine purposes. The thing is that<br>
I would like to separate the skin from the bones and export every part separately to further work on Maya and<br>
I am unable to do it just using the volumetric rendering settings.</p>
<p>Does anyone knows how I can achieve that please?</p>

---

## Post #2 by @ihnorton (2017-10-07 14:15 UTC)

<p>Please see</p>
<aside class="quote" data-post="2" data-topic="524">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524/2">Save volume rendering as STL file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Volume rendering is just a display technique - to get an STL file you need to segment the volume using Segment Editor module. 

Tutorial: <a href="https://www.slicer.org/wiki/Documentation/4.6/Training#Segmentation_for_3D_printing">https://www.slicer.org/wiki/Documentation/4.6/Training#Segmentation_for_3D_printing</a>

Reference: <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a>
  </blockquote>
</aside>


---
