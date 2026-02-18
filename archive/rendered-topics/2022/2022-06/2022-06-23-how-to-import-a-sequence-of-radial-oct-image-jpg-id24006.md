# How to import a sequence of radial OCT image(.jpg)

**Topic ID**: 24006
**Date**: 2022-06-23
**URL**: https://discourse.slicer.org/t/how-to-import-a-sequence-of-radial-oct-image-jpg/24006

---

## Post #1 by @coastcode (2022-06-23 07:33 UTC)

<p>I’m new to 3D Slicer. I have a sequence of radial OCT images(as jpg). How can I load it to slicer and reconstruct it?<br>
Really appreciate your help.</p>

---

## Post #2 by @lassoan (2022-06-24 05:01 UTC)

<p>Please follow the method described in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="20734">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/96bed5/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/3d-reconstruction-of-radial-oct-slices/20734">3D reconstruction of radial OCT slices</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everyone! 
I’m working on radial OCT scans of the optic nerve head (eye), and the slices are rotated from each other by 15°. 
Since I don’t have parallel slices, I’m struggling to construct the 3D model of the optic nerve head using those rotational slices. Is there a way that I could do it in 3D Slicer? 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a807de4acbf0796e1343a1bb1a4be9ce9482b501.jpeg" data-download-href="/uploads/short-url/nYt4w2I0bW5IIBBFvfpntjIRrJT.jpeg?dl=1" title="radial_oct_scans" rel="noopener nofollow ugc">[radial_oct_scans]</a> 
Thanks in advance
  </blockquote>
</aside>


---

## Post #3 by @coastcode (2022-06-24 09:10 UTC)

<p>Thanks for your reply. I read this method, but there are many details that confuse me. For example, how to use the Transforms module to set the origin, spacing, and axis directions for each image slice? Also, is it right to run the code line by line in the python interactor window?</p>

---

## Post #4 by @lassoan (2022-06-24 13:00 UTC)

<aside class="quote no-group" data-username="coastcode" data-post="3" data-topic="24006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coastcode/48/15762_2.png" class="avatar"> coastcode:</div>
<blockquote>
<p>how to use the Transforms module to set the origin, spacing, and axis directions for each image slice?</p>
</blockquote>
</aside>
<p>You can set spacing by modifying the first 3 diagonal elements of the transformation matrix.</p>
<p>You can set the origin and axis direction by using the transform sliders. It takes time, maybe one minute for each image slice, but if you have a few dozens then you can finish it within half an hour. Of course it can be automated using Python scripting, but it may be easier to get started with just using the GUI.</p>
<aside class="quote no-group" data-username="coastcode" data-post="3" data-topic="24006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coastcode/48/15762_2.png" class="avatar"> coastcode:</div>
<blockquote>
<p>is it right to run the code line by line in the python interactor window?</p>
</blockquote>
</aside>
<p>Yes, you can copy-paste code into the Python interactor.</p>
<p>The main concern is what you can get out of these 3D reconstructions. If you only have 12 images as in the linked topic above, then 3D information will be very sparse. You would need 5-10x more images to get a nice complete 3D volume. How many images do you have (what is the angle increment between each slice)?</p>

---

## Post #5 by @coastcode (2022-06-25 05:40 UTC)

<p>I have 128 images, rotated 180 degrees in total, with the rotation axis in the middle.</p>

---
