---
topic_id: 3105
title: "Questions About Using 3D Slicer Coordinates Viewer"
date: 2018-06-07
url: https://discourse.slicer.org/t/3105
---

# Questions about using 3D Slicer. ( coordinates , viewer )

**Topic ID**: 3105
**Date**: 2018-06-07
**URL**: https://discourse.slicer.org/t/questions-about-using-3d-slicer-coordinates-viewer/3105

---

## Post #1 by @HwangJeongUk (2018-06-07 07:29 UTC)

<p>There are a few questions about using 3D Slicer.</p>
<ol>
<li>Can I change the coordinates of the model shown in 3Dveiwer before extracting with stl?</li>
<li>Can we match the stl model to the CT and extract the model with its coordinates?</li>
<li>Can I view the 2D viewer as a panorama? Is there a function that can extract nerve in 3D in that state?</li>
</ol>

---

## Post #2 by @pieper (2018-06-07 18:44 UTC)

<p>Look at the Transforms module and hardening the transform - your exported model will be in the new space.</p>
<p>For the panorama view, see this post:</p>
<aside class="quote" data-post="1" data-topic="2203">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/df705f/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/panoramic-image-view/2203">Panoramic image/view</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Is it possible to reconstruct a panoramic view as is often used in dentistry and if not, are there any plans to add that capability? Thank you. 
Operating system: MAC 10.13 (High Sierra) 
Slicer version: 4.6.2 
Expected behavior: 
Actual behavior:
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2018-06-07 19:15 UTC)

<p>Since nerves are linear structures, you should be able to quite easily generate a 3D model of them just by from a few points along the curve. Drop a couple of markup fiducials along the nerve and then use Markups to model extension to draw a curve between those points in 3D.</p>
<aside class="quote no-group" data-username="HwangJeongUk" data-post="1" data-topic="3105">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/977dab/48.png" class="avatar"> HwangJeongUk:</div>
<blockquote>
<p>Can I view the 2D viewer as a panorama? Is there a function that can extract nerve in 3D in that state?</p>
</blockquote>
</aside>
<p>If you set up reslicing along a curve (as described in the post that Steve linked above), then you can use the segment editor to segment in those oblique slices. I would recommend to use Paint tool with <em>sphere brush</em> option enabled, to avoid gaps between reformatted slices.</p>
<p>Currently, there is no module in Slicer that would create a panoramic view. It would just take a couple of weeks of work, but seems that it has never been important enough for anybody to allocate that much funding to get it done. If somebody implements it, then it will be possible to use the Segment editor to segment structures in the panoramic-warped image and transfer it back to regular 3D space when the segmentation is completed.</p>

---

## Post #4 by @HwangJeongUk (2018-06-08 04:58 UTC)

<p>Thank you for answer.<br>
So, is there any function (eg dental model) to match the plaster model to the CT?<br>
And I want to extract the model coordinates extracted from 3D Slicer with z = 0, y = 0, x = 0. What should I do?<br>
I am using geomagic freeform. CT is extracted with stl, and the model extracted from 3D slicer is out of coordinates.<br>
Another thing is, can I change the coordinates in 3D Slicer to save CT? I want to relocate the angle of the patient on CT.</p>

---

## Post #5 by @lassoan (2018-06-08 15:01 UTC)

<aside class="quote no-group" data-username="HwangJeongUk" data-post="4" data-topic="3105">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/977dab/48.png" class="avatar"> HwangJeongUk:</div>
<blockquote>
<p>So, is there any function (eg dental model) to match the plaster model to the CT?</p>
</blockquote>
</aside>
<p>A good approach can be to create a segment of the same anatomical structure from both CT and plaster model and then use SegmentRegistration extension to register them.</p>
<aside class="quote no-group" data-username="HwangJeongUk" data-post="4" data-topic="3105">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/977dab/48.png" class="avatar"> HwangJeongUk:</div>
<blockquote>
<p>And I want to extract the model coordinates extracted from 3D Slicer with z = 0, y = 0, x = 0. What should I do?</p>
</blockquote>
</aside>
<p>Could you explain this with a bit more details? Maybe add an image to illustrate what you would like to do.</p>
<aside class="quote no-group" data-username="HwangJeongUk" data-post="4" data-topic="3105">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/977dab/48.png" class="avatar"> HwangJeongUk:</div>
<blockquote>
<p>Another thing is, can I change the coordinates in 3D Slicer to save CT? I want to relocate the angle of the patient on CT.</p>
</blockquote>
</aside>
<p>You can use the Transforms module for this as Steve wrote above (create transform, apply to model or segmentation, adjust the transform, harden the transform on the node).</p>

---
