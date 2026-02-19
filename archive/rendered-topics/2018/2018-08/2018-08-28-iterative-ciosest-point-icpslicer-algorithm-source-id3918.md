---
topic_id: 3918
title: "Iterative Ciosest Point Icpslicer Algorithm Source"
date: 2018-08-28
url: https://discourse.slicer.org/t/3918
---

# Iterative CIosest Point (ICPSlicer) algorithm source

**Topic ID**: 3918
**Date**: 2018-08-28
**URL**: https://discourse.slicer.org/t/iterative-ciosest-point-icpslicer-algorithm-source/3918

---

## Post #1 by @Ricardo_Mesquita (2018-08-28 09:29 UTC)

<p>Hi all,<br>
i’m trying to figure out if the ICP implemented in slicer is the standard ICP algorithm or some kind of modified ICP algorithm. The standard ICP algorithm lacks in some important aspects that will increase the registration error. As so, i intended to improve surface registration accuracy and for that i have to know the source algorithm of ICP implemented in slicer in order to compare the results.<br>
Does anybody know if the ICPSlicer algorithm is the standard algorithm? Or if there’s other algorithm implemented in slicer that is an optimized version of standard ICP to improve accuracy?</p>
<p>Thanks for you attention.</p>

---

## Post #2 by @ihnorton (2018-08-28 13:39 UTC)

<p>Which module(s) are you referring to?</p>

---

## Post #3 by @pieper (2018-08-28 13:47 UTC)

<p>Maybe you want this info:</p>
<aside class="quote quote-modified" data-post="2" data-topic="3343">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andinet_enquobahrie/48/75_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/details-on-icp-registration-implementation/3343/2">Details on ICP registration implementation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
The Surface Registration module which is part of the CMFreg extension uses vtkIterativeClosestPointTransform. You can look into the details in the following links. 
Surface registration python script 
 
 
vtkIterativeClosestPointTransform 
<a href="https://www.vtk.org/doc/nightly/html/classvtkIterativeClosestPointTransform.html#details" class="onebox" target="_blank" rel="noopener">https://www.vtk.org/doc/nightly/html/classvtkIterativeClosestPointTransform.html#details</a> 
HTH, 
Andinet
  </blockquote>
</aside>


---
