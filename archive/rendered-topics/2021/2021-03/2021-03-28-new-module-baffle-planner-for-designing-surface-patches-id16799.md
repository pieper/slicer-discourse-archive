# New module: Baffle planner - for designing surface patches

**Topic ID**: 16799
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/new-module-baffle-planner-for-designing-surface-patches/16799

---

## Post #1 by @lassoan (2021-03-28 16:47 UTC)

<p>A new <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/BafflePlanner.md">Baffle planner module</a> has been added to <strong><a href="https://github.com/SlicerHeart/SlicerHeart#slicerheart-extension-for-3d-slicer">SlicerHeart extension</a></strong> that can be generally used whenever a <strong>smooth surface patch needed that conforms to pre-existing anatomical boundary</strong>. By default a “soap-bubble” surface is created for the specified curve but the surface <strong>shape can be edited</strong> by specifying additional surface points in either slice or 3D views.</p>
<p>The module can generate an infinitely thin open surface, or a closed <strong>surface with specified thickness</strong>.</p>
<p>The module can also generate a <strong>flattened</strong> shape, which reproduces the shape and size of the 3D surface patch with a planar shape, with minimal distortion. This is useful as a cutout template for fabric (e.g., dacron mesh).</p>
<p>The module was originally designed for surgical repair of heart walls, but it can be used universally anywhere where a smooth 3D surface needs to be generated that conforms to the patient anatomy. See more information in <a href="https://www.annalsthoracicsurgery.org/article/S0003-4975(21)00457-4/pdf">this paper</a>.</p>
<p>An example of an alternative application is generating bone flap models:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="AigTwMYRI1Y" data-video-title="Design surface patches using new Baffle Planner module" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=AigTwMYRI1Y" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/AigTwMYRI1Y/maxresdefault.jpg" title="Design surface patches using new Baffle Planner module" width="" height="">
  </a>
</div>


---

## Post #2 by @manjula (2021-03-28 17:46 UTC)

<p>Thank you for this. It is a wonderful tool.</p>

---

## Post #3 by @juangdiosa (2021-03-28 18:05 UTC)

<p>Excellent tool !!</p>
<p>is this tool available right now ? I am working in something where this tool could be very useful. I have downloaded the Slicer-Heart extension in the stable Slicer version and I did not find it.</p>

---

## Post #4 by @juangdiosa (2021-03-28 19:31 UTC)

<p>My mistake, I had the stable version from November. I have installed the March 2021 version and it works. Thanks a lot for this improvement</p>

---

## Post #5 by @juangdiosa (2021-04-05 17:30 UTC)

<p>Thanks a lot for this new tool, it is very useful and It has saved me a lot of time. After a week using it. I suggest to allow add or delete nodes on any position of the base curve [contour points] and not base on the last node added.</p>

---

## Post #6 by @lassoan (2021-04-06 13:03 UTC)

<aside class="quote no-group" data-username="juangdiosa" data-post="5" data-topic="16799">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juangdiosa/48/717_2.png" class="avatar"> juangdiosa:</div>
<blockquote>
<p>I suggest to allow add or delete nodes on any position of the base curve [contour points] and not base on the last node added.</p>
</blockquote>
</aside>
<p>This is already available: you can right-click on any control points and choose to delete that point.</p>
<aside class="quote no-group" data-username="juangdiosa" data-post="5" data-topic="16799">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juangdiosa/48/717_2.png" class="avatar"> juangdiosa:</div>
<blockquote>
<p>it is very useful and It has saved me a lot of time</p>
</blockquote>
</aside>
<p>It would be great if you could write a few sentences and maybe post a nice picture in the <a href="https://discourse.slicer.org/c/community/success-stories/29">Success stories category</a>.</p>

---

## Post #7 by @hagop_hovaguimian (2021-06-22 04:13 UTC)

<p>I have the slicer V4.13 version and can’t find the baffle planner module in the extensions .Help…</p>
<p>Hagop Hovaguimian</p>

---

## Post #8 by @lassoan (2021-06-22 04:29 UTC)

<p>See above - the module is in SlicerHeart extension.</p>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="16799">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A new module has been added in <a href="https://github.com/SlicerHeart/SlicerHeart#slicerheart-extension-for-3d-slicer">SlicerHeart extension </a> that can be generally used whenever a <strong>smooth surface patch needed that conforms to pre-existing anatomical boundary</strong> .</p>
</blockquote>
</aside>

---

## Post #9 by @hagop_hovaguimian (2021-06-22 04:49 UTC)

<p>Found it. Thanks for the amazingly prompt response, and thank you for this sorely needed module.</p>
<p>Hagop</p>

---
