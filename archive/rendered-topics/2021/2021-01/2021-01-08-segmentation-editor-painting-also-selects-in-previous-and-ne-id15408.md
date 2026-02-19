---
topic_id: 15408
title: "Segmentation Editor Painting Also Selects In Previous And Ne"
date: 2021-01-08
url: https://discourse.slicer.org/t/15408
---

# Segmentation Editor - painting also selects in previous and next image

**Topic ID**: 15408
**Date**: 2021-01-08
**URL**: https://discourse.slicer.org/t/segmentation-editor-painting-also-selects-in-previous-and-next-image/15408

---

## Post #1 by @willi (2021-01-08 15:14 UTC)

<p>Hello,</p>
<p>I am fairly new to 3D Slicer. It looks really good to me and I want to use it for my research.<br>
I did some segmentation with data I had from previous studies and everything worked pretty good and as expected!<br>
Unfortunately, I encountered problems with a new dataset this week and I can’t figure out why it doesn’t work. I spent a lot of time trying to solve it but I couldn’t find any tutorial or thread on this issue…</p>
<p>I have DICOM files which were captured from coronal plane with isometric voxels. The import and alignment looks.<br>
When trying to paint or draw in sementation editor on any of the planes the selection is a bit messed up.<br>
On the slice, which I painted, the selection shows some irregularities (holes) and additionally, previous and next slices has partial selection. I put together some screenshots to clarify what I mean. Unfortunately, if I have these parial selections, other tools like “Fill between slices” don’t work as expected.</p>
<p>This is what the slice with the selection looks like:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45449190d5ce84d2d5fd7c0b63551853dfadb0a3.jpeg" alt="slice_selection.PNG" data-base62-sha1="9SLQT6dFgn6nJ0ozus7Zyb7FdvB" width="445" height="439"></p>
<p>This is the previous slice:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06ff4ed507e05fd02ce4dc78aea1b02b99c9e3df.jpeg" alt="slice_previous.PNG" data-base62-sha1="ZTRi8A6JphZRHtr67fneo9N0fR" width="445" height="443"></p>
<p>This is the next slice:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47cd9fa9baa2ba06ea15be6cb47d2831a1118667.jpeg" alt="slice_next.PNG" data-base62-sha1="afcrIHmDPthCOA36wC72F1bmmF1" width="444" height="442"></p>
<p>I tried using the same DICOM files with Materialise Mimics, this works as expected, so, I don’t think that there is a problem with the data files.</p>
<p>As I already mentioned, I am quite new to 3D Slicer. Maybe, I am just missing a necessary step which has to be done <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"></p>
<p>Can somebody please help me out on how to solve this issue?</p>
<p>Thanks in advance, best regards,<br>
Willi</p>

---

## Post #2 by @lassoan (2021-01-08 15:26 UTC)

<p>This is expected if you segment on oblique slices. See this segmentation recipe for details:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" target="_blank" rel="noopener">3D Slicer segmentation recipes</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" target="_blank" rel="noopener">Overview</a></h3>

<p>Recipes for common medical image segmentation tasks using 3D Slicer</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @willi (2021-01-08 15:40 UTC)

<p>Thanks a lot, it seems to work now perfectly!</p>

---
