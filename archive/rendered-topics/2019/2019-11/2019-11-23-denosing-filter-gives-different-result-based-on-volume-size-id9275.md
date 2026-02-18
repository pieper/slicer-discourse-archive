# Denosing filter gives different result based on volume size

**Topic ID**: 9275
**Date**: 2019-11-23
**URL**: https://discourse.slicer.org/t/denosing-filter-gives-different-result-based-on-volume-size/9275

---

## Post #1 by @Amine (2019-11-23 02:15 UTC)

<p>Hi, in an attempt to get a preview of what CurvatureAnisotropicDiffusion will produce with less processing time i tried to run it in on a cropped volume to serve as a sample, however the final result on the complete volume (with the same parameters) is a lot stronger and produces a blurry image.<br>
is there any way to predict the target parameters(conductance and time step) relative to those of a smaller volume based on their size difference? or is there any way to preview what a filter will produce?<br>
The only way i could produce a sufficiently close preview was by setting the cropping roi to cover the full axial plane and a thick (40+ voxel) vertical axis, wich still takes a lot of time to compute<br>
Thanks for any inputs.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6db27073f75892757c4a51a66af847c078d122d.jpeg" data-download-href="/uploads/short-url/zdMZmoQHnRVyAazH5gwf6uWiy1n.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6db27073f75892757c4a51a66af847c078d122d_2_256x500.jpeg" alt="Capture" data-base62-sha1="zdMZmoQHnRVyAazH5gwf6uWiy1n" width="256" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6db27073f75892757c4a51a66af847c078d122d_2_256x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6db27073f75892757c4a51a66af847c078d122d_2_384x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6db27073f75892757c4a51a66af847c078d122d_2_512x1000.jpeg 2x" data-dominant-color="7D7D7D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">567×1104 75.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-11-23 21:08 UTC)

<p>I suspect that’s probably inherent in the algorithm itself.  Slicer just exposes the basic ITK class, so you might try asking on the ITK forum.  Perhaps there’s a way to compensate.</p>

---

## Post #3 by @Amine (2019-11-23 22:54 UTC)

<p>Thanks for your answer.<br>
Indeed, only hoped that someone here would have experience with this issue first, i asked on itk forum.<br>
If this works well it could help many users. I made a module to preview more than 40 different filter strenghts using a slider to interactively evaluate the output blurriness then apply the most appropriate one on the full volume (and the computing time is less than a minute for all of them).<br>
Applying the selected stenght is the only remaining issue.</p>

---

## Post #4 by @pieper (2019-11-26 01:30 UTC)

<p>Sounds like a neat module!  I saw your post on the ITK list.  I hope you get a good response there.</p>

---

## Post #5 by @Amine (2019-11-26 12:47 UTC)

<p>Hopefully, otherwise it would be unusable, here is a preview of how the module works if you’re interested: <a href="https://youtu.be/ODBjnNSwsQo" rel="nofollow noopener">https://youtu.be/ODBjnNSwsQo</a></p>

---

## Post #6 by @pieper (2019-11-26 13:43 UTC)

<p>Yes, that looks really nice and should be helpful.</p>
<p>It would be nice if someone from the ITK community is already familiar with the algorithm and the implementation, but if not you could probably go back to the original publications and look at the code to see if it’s expected that the volume size should be a factor in the result.  With your tool you should have the basis to explore the impact of this - that could help people in parameter selection.</p>

---

## Post #7 by @lassoan (2019-11-26 15:40 UTC)

<aside class="quote no-group" data-username="Amine" data-post="1" data-topic="9275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>a thick (40+ voxel) vertical axis</p>
</blockquote>
</aside>
<p>Requiring padding around the region of interest may be normal. I’ve added some more details to the <a href="https://discourse.itk.org/t/curvatureanisotropicdiff-creates-different-result-relative-to-volume-size/2437/4?u=lassoan">discussion on ITK forum</a>.</p>

---
