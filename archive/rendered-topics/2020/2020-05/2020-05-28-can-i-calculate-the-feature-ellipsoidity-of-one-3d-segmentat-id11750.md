---
topic_id: 11750
title: "Can I Calculate The Feature Ellipsoidity Of One 3D Segmentat"
date: 2020-05-28
url: https://discourse.slicer.org/t/11750
---

# Can I calculate the feature "Ellipsoidity" of one 3D segmentation

**Topic ID**: 11750
**Date**: 2020-05-28
**URL**: https://discourse.slicer.org/t/can-i-calculate-the-feature-ellipsoidity-of-one-3d-segmentation/11750

---

## Post #1 by @yanpfei (2020-05-28 14:40 UTC)

<p>I am using pyRadiomics to analyzed 3D segmentation of tumors.</p>
<p>I noticed the feature " <strong>Sphericity</strong>" and it is very useful for tumor analysis. Besides this feauture, I want to calculate the " <strong>Ellipsoidity</strong>" of a tumor.<br>
When the tumor is in the shape of a very prolate or oblate ellipsoid, it would have a low sphericity but the ellipsoidity would be 1. So the featue “Ellipsoidity” could also be very useful.</p>
<p>Can I do this with pyRadiomics?<br>
Thank you in advance.</p>

---

## Post #2 by @lassoan (2020-05-28 16:19 UTC)

<p>I don’t know what pyradiomics can compute, but you can use Slicer’s segment statistics module to compute many shape metrics: roundness, flatness, elongation, principal moments, principal axis directions, oriented bounding box diameters, Feret diameter, etc. This allows rich shape characterization, including assessing “ellipsoidity”.</p>
<p>See some more information in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="10203">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203">New Segment Statistics: Oriented Bounding Box, Diameter and More</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    New statistics have been added to the Segment Statistics module: 

Centroid
Oriented bounding box
Feret diameter
Perimeter
Roundness
Flatness
Elongation
Principal axes/moments

These statistics are not enabled by default. To enable them, click on the “Options” button beside the “Labelmap Statistics” checkbox, and select the statistics that you would like calculated from the popup window. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1215fbf5a379c4665e2091ef31cba1e48ae25474.png" data-download-href="/uploads/short-url/2zZH7fLta4P90vWGbpxlusk3hqY.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
You can read the documentation for the Segment Statistics module <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmentstatistics.html" rel="noopener nofollow ugc">here</a>. 
Oriented bounding box: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72285939b0de724fdb92c1f2509b07eb474397a.jpeg" data-download-href="/uploads/short-url/wYIg0J7wFKzWP3CWq8W1fDzMzsm.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[…</a>
  </blockquote>
</aside>


---

## Post #3 by @JoostJM (2020-06-07 09:06 UTC)

<p>All shape features available in PyRadiomics can be found <a href="https://pyradiomics.readthedocs.io/en/latest/features.html#module-radiomics.shape">here</a>. This also includes principal axes length, but no specific “ellipsoidity” formula. Do you have a equation to calculate this?</p>

---

## Post #4 by @yanpfei (2020-06-07 11:31 UTC)

<p>Sorry for the late reply, I just noticed it.<br>
Thank you for  the information. I’ll check 3D slicer.</p>

---

## Post #5 by @yanpfei (2020-06-07 11:33 UTC)

<p>I read papers that says it equals the ratio of one 3D object’s volume to the volume to the object’s fitting ellipsoid. And the fitting ellipsoid can be calculated this way:</p>
<p>Chaudhuri, B. B., &amp; Samanta, G. P. (1991). Elliptic fit of objects in two and three dimensions by moment of inertia optimization.  <em>Pattern Recognition Letters</em> ,  <em>12</em> (1), 1-7.</p>

---
