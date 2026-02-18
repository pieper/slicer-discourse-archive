# Mirror in surface toolbox

**Topic ID**: 3297
**Date**: 2018-06-26
**URL**: https://discourse.slicer.org/t/mirror-in-surface-toolbox/3297

---

## Post #1 by @Arnaud (2018-06-26 08:22 UTC)

<p>Hi there.</p>
<p>I’m working on maxillo-facial surgical planning. I’d need to mirror a model. I use the surface toolbox with the mirror option.<br>
We can mirror above the 3 axes x,y,z. My question is : how to mirror above a specific plane that we could have created?<br>
Is it possible to use the angle plane module to creat a plane and use this plane as the reference for the mirror module?</p>
<p>thanks for helping me</p>

---

## Post #2 by @lassoan (2018-07-10 14:30 UTC)

<p>I would recommend to mirror first (the whole surface), then align the two sides (using Fiducial registration wizard and/or Surface registration modules in SlicerIGT extension), and finally cut the original and mirrored models using the same slice plane.</p>

---

## Post #3 by @fedorov (2019-03-08 21:44 UTC)

<p>A user was asking me for help via direct communication (in Russian), and one of the questions was how to mirror the model. I came across this post, which was helpful, and in the process I realized the documentation for Surface Toolbox is outdated (does not list the newly added functions, including mirror): <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/SurfaceToolbox" class="inline-onebox">Documentation/4.10/Modules/SurfaceToolbox - Slicer Wiki</a>. Considering this is a Slicer core module, it doesn’t look particularly good. Is that module supported? Figure below shows documentation for 4.10 on the left vs actual Surface Toolbox interface on the right in 4.10.1.</p>
<p>Also, on a related note (another question from the same user) - do we have a model subtract functionality somewhere?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f515536168b856957010d21895e273f0b76dc9.png" data-download-href="/uploads/short-url/hg2nRYFy0vKCDRm0JCPHLuq8TkR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f515536168b856957010d21895e273f0b76dc9_2_690x471.png" alt="image" data-base62-sha1="hg2nRYFy0vKCDRm0JCPHLuq8TkR" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f515536168b856957010d21895e273f0b76dc9_2_690x471.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f515536168b856957010d21895e273f0b76dc9_2_1035x706.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f515536168b856957010d21895e273f0b76dc9.png 2x" data-dominant-color="EDEDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1118×764 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2019-03-08 22:00 UTC)

<p>Hi <a class="mention" href="/u/fedorov">@fedorov</a> - I’m going to resist the temptation to say “wiki edits welcome” (oops, I said it!).</p>
<p>But regarding the model subtract, I suggest that the most robust approach would be to convert to a Segmentation and perform the subtraction in image space and then re-convert the result to a model.  The underlying issue is that boolean operations on meshes is a numerically unstable operation while image space operations are very robust.  The tradeoff of course is that you might need to make a very high res image or you’ll lose too much detail (depends on your models).</p>

---

## Post #5 by @brhoom (2019-03-08 22:03 UTC)

<p>Isn’t it possible to do the mirroring by Transforms module??? e.g. by changing the sign of one of the diagonal elements of the transformation matrix.</p>

---

## Post #6 by @fedorov (2019-03-08 22:08 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="3297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’m going to resist the temptation to say “wiki edits welcome” (oops, I said it!).</p>
</blockquote>
</aside>
<p>Well, I did have a temptation to update it, or at least a part of it, but it was not a trivial edit. Several new capabilities are missing, and I feel like I may not know enough about the module to make those edits. I have not used this module, never ever, and as always, there are many competing priorities.</p>
<p>I can’t resist the temptation to say “I kind of expected this response!” <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @lassoan (2019-03-08 22:26 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="5" data-topic="3297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Isn’t it possible to do the mirroring by Transforms module???</p>
</blockquote>
</aside>
<p>Mirroring using a transform turns the model inside out. Usually this is not desirable, so you need to reorient the cells of the mesh. Surface toolbox Mirror function performs these two steps.</p>

---
