# Strange results in model segmentation to label map

**Topic ID**: 4518
**Date**: 2018-10-24
**URL**: https://discourse.slicer.org/t/strange-results-in-model-segmentation-to-label-map/4518

---

## Post #1 by @Niels (2018-10-24 11:52 UTC)

<p>Hello, I installed Slicer 4.11.0-2018-10-20 (revision 27509) macosx-amd64. I imported a model as a segmentation and exported this to a labelmap. Using these steps:</p><aside class="quote quote-modified" data-post="1" data-topic="4256">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ebca7d/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/intersection-between-model-and-volume-to-select-voxels/4256">Intersection between model and volume to select voxels</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I have a generated a surface model by applying vtkMarchingCubes on a loaded volume. The next step I would like to perform is to identify which voxels intersect with the triangles that were generated. I was thinking of starting with iterating the vertices to see which voxels overlap and do some triangle intersect from there but I am not sure if that is the best method. Doe anybody know if there is a better way to select voxels that are inside, outside or on the contour of  a model? I am using pyt…
  </blockquote>
</aside>

<p>Does anybody have an idea where is coming from?</p>

---

## Post #2 by @cpinter (2018-10-24 11:58 UTC)

<p>I feel like I miss some key information to understand what the problem is. What was the strange result? The topic you point to seems not to contain such information.</p>

---

## Post #3 by @Niels (2018-10-24 12:12 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10cc769b0151bcc98e22bdc0ef6e2e3a00a9d787.png" alt="48" data-base62-sha1="2oBHpjgLWYR7DLO9oycjcUqiwTB" width="500" height="318"></p>
<p>Some nightly builds ago I used the windows version and it worked ok. this nightly build is macosx.</p>

---

## Post #4 by @cpinter (2018-10-24 12:22 UTC)

<ol>
<li>Did you use the same input and method <em>exactly</em> in the two scenarios you’re describing?</li>
<li>Do you have an anatomical image that you used as reference? (The screenshot just shows the labelmap)</li>
</ol>

---

## Post #5 by @lassoan (2018-10-24 17:49 UTC)

<p>Most likely faces in the model are defined inconsistently. The referenced post above was long and it is not clear how you ended up creating the model. If you create it using Segment Editor then the model should be correct and you should be able to import it and visualize it correctly. If you created it using Segment Editor but you still have problems then please share the .seg.nrrd file and the exported model file so that we can investigate.</p>

---
