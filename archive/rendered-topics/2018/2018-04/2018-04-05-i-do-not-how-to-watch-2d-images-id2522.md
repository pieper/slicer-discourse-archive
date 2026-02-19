---
topic_id: 2522
title: "I Do Not How To Watch 2D Images"
date: 2018-04-05
url: https://discourse.slicer.org/t/2522
---

# I do not how to watch 2D images

**Topic ID**: 2522
**Date**: 2018-04-05
**URL**: https://discourse.slicer.org/t/i-do-not-how-to-watch-2d-images/2522

---

## Post #1 by @Neil_Rozas_Gaete (2018-04-05 16:54 UTC)

<p>Operating system: Solus OS<br>
Slicer version: 4.8.1<br>
Expected behavior: I want to my 2D images was showing in the way of I acquired them, some studies like Shoulder MRI I do somes axial due to the articulation itself, no to Z axis of pacient.<br>
Actual behavior: I open 2D images and the disposition of transverse, sagital and coronal images are made by patient, not to the raw acquisition position.</p>
<p>Sorry for my english, I’m using 3D Slicer for teaching purposes in University of La Frontera in the South of Chile, I’m Linux user along 1 year.</p>
<p>Thanks in advance</p>

---

## Post #2 by @pieper (2018-04-05 20:06 UTC)

<p>Maybe you need to do this:</p>
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

<p>If that’s not it, maybe you can post some screenshots of what you are seeing.</p>

---
