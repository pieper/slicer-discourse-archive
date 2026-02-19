---
topic_id: 5577
title: "Dicom Import And Image Does Not Appear"
date: 2019-01-30
url: https://discourse.slicer.org/t/5577
---

# DICOM import and image does not appear

**Topic ID**: 5577
**Date**: 2019-01-30
**URL**: https://discourse.slicer.org/t/dicom-import-and-image-does-not-appear/5577

---

## Post #1 by @choudhry23 (2019-01-30 09:14 UTC)

<p>Operating system: Mac<br>
Slicer version: 4.10<br>
Expected behavior: load the DICOM data and image appears<br>
Actual behavior:<br>
I load the DICOM file into slicer but not all three planes of the image appear. only partial images of each plane appear in the slicer.<br>
it is as if the image is present but is not aligned/focused.</p>

---

## Post #2 by @lassoan (2019-01-31 00:38 UTC)

<p>Probably rotating slice views to be aligned with volume plane will give you the expected views:</p>
<aside class="quote quote-modified" data-post="4" data-topic="1459">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459/4">Segmentation Editor - How to disable painting on adjacent slices?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If the acquisition was tilted you may need to rotate to volume plane (click the “pushpin” icon in the top-left corner of the slice view, then click the double-arrow button on the left, then the “Rotate to volume plane” icon appears): 
[image] 
Here’s an example drawing on the original slice (patient space) 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee6244f649d4f68c2cd1a14c4e489972a0a5755e.jpeg" data-download-href="/uploads/short-url/y0Qb6Ef1694zMHYIT45Xx6cE0bQ.jpg?dl=1" title="image">[image]</a> 
And here the paint stroke on the right is after rotating the red slice into the acquisition plane and only one plane is painted in the other views. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27e575499b56b012ea2cc088c24f38cb43202281.jpeg" data-download-href="/uploads/short-url/5GWesknjInRIylPfDboX3rTkF8Z.jpg?dl=1" title="image">[image]</a>
  </blockquote>
</aside>


---
