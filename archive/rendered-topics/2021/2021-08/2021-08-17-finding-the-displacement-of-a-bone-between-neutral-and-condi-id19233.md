# Finding the displacement of a bone between neutral and condition

**Topic ID**: 19233
**Date**: 2021-08-17
**URL**: https://discourse.slicer.org/t/finding-the-displacement-of-a-bone-between-neutral-and-condition/19233

---

## Post #1 by @matsuba8 (2021-08-17 15:43 UTC)

<p>Hello!<br>
I’m still quite new to Slicer and wanted to post in this forum to see if someone could assist me.<br>
I am using Slicer to perform some analysis for a research project. Our objective is to examine the displacement of a bone graft placed in the femur at the knee, when subjected to specific loads (i.e. how much the bone graft moves from neutral to loaded).<br>
So far, I have registered the volumes based on the position of the femur, and now would like to compute the difference in positions of the femoral bone blocks between the neutral and loaded scans.</p>
<p>Based on what I’ve gathered, the best way to do this is to manually segment the bone block in each scan, export them to models, and use IGT Model Registration to find the displacement. While this was a successful method, we would like the outcome measures to be in terms of a axes system which is oriented based on the bone block rather than the global coordinate system. Please see images below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/010147bea38170fff5263fc82655baec2f04c094.jpeg" data-download-href="/uploads/short-url/8TdFdhFC1boDoMzdJoI8sI2AAs.jpeg?dl=1" title="axes of global coordinate system" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/010147bea38170fff5263fc82655baec2f04c094_2_690x431.jpeg" alt="axes of global coordinate system" data-base62-sha1="8TdFdhFC1boDoMzdJoI8sI2AAs" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/010147bea38170fff5263fc82655baec2f04c094_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/010147bea38170fff5263fc82655baec2f04c094_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/010147bea38170fff5263fc82655baec2f04c094_2_1380x862.jpeg 2x" data-dominant-color="A2A2A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axes of global coordinate system</span><span class="informations">2880×1800 278 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf9387b3b182c7a57a64aa87b2aae0982c00c6cf.jpeg" data-download-href="/uploads/short-url/tCiUViYfe0JE1uR4tXoitkaVU9F.jpeg?dl=1" title="axes oriented based on bone block" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf9387b3b182c7a57a64aa87b2aae0982c00c6cf_2_690x431.jpeg" alt="axes oriented based on bone block" data-base62-sha1="tCiUViYfe0JE1uR4tXoitkaVU9F" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf9387b3b182c7a57a64aa87b2aae0982c00c6cf_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf9387b3b182c7a57a64aa87b2aae0982c00c6cf_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf9387b3b182c7a57a64aa87b2aae0982c00c6cf_2_1380x862.jpeg 2x" data-dominant-color="A2A2A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axes oriented based on bone block</span><span class="informations">2880×1800 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
The reason for this is because we want the rotational values to be based off of the true axes of the bone block.</p>
<p>I have tried manually/visually rotating and translating the bone block in the global space, but I believe there is too much human error involved to make this a reliable method.<br>
I would greatly appreciate it if anybody could offer some advice.<br>
Thank you.</p>
<p>Michele</p>

---

## Post #2 by @lassoan (2021-09-03 01:47 UTC)

<p>For future reference the issue is discussed in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="19446">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/59ef9b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/creating-a-new-coordinate-system/19446">Creating a new coordinate system</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello all, 
I am trying to create a local coordinate system within the global coordinate system in order to compute the displacement of a bone block between two different scans. The reason why the global coordinate system does not suffice is because I would like the rotational displacement of the bone block to be in terms of the orientation of the reference bone block rather than the global space. 
Could someone please provide some guidance on how to create a local coordinate system? 
Thank you …
  </blockquote>
</aside>


---
