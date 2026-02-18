# MRI Data being reformatted

**Topic ID**: 3231
**Date**: 2018-06-19
**URL**: https://discourse.slicer.org/t/mri-data-being-reformatted/3231

---

## Post #1 by @ogdenk (2018-06-19 15:18 UTC)

<p>Operating system: Win7<br>
Slicer version: 4.8.1 Stable<br>
Expected behavior:  Would like to see the MRI images in the acquisition planes.  The images are from brain scans that are acquired with a rotated acquisition relative to the reference frame, so the direction cosines for the ‘axial’ images are not 1,0,0 0,1,0.  Here is an example set of direction cosines for an axial image:</p>
<p>0.99987566471099, 3.55340831447E-4, -0.0157645270228, 0.00368064129725, 0.96687048673629, 0.25524091720581</p>
<p>Actual behavior:  Slicer is showing interpolated planes that I assume correspond to the cardinal planes.  Is there a way to make Slicer not do this?  We are extracting Radiomics features and do not want this added complication.</p>

---

## Post #2 by @pieper (2018-06-19 15:36 UTC)

<p>The slice view is for display only (yes, it is the cardinal planes).  It won’t impact the radiomics features as long as your segmentation matches your source images.</p>
<p>You can see how to adjust the view here:</p>
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

## Post #3 by @lassoan (2018-06-19 15:39 UTC)

<p>I would just add that in latest nightly builds, if you go to Segment Editor, you’ll see a warning button if slice views are not aligned to segmentation volume axes. By clicking that button, slice views will be realigned. This is useful if you need to segment your volume.</p>

---

## Post #4 by @ogdenk (2018-06-19 15:51 UTC)

<p>That solves the issue, thanks!</p>

---
