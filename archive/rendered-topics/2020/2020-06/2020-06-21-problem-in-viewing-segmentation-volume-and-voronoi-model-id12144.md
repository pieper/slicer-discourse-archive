---
topic_id: 12144
title: "Problem In Viewing Segmentation Volume And Voronoi Model"
date: 2020-06-21
url: https://discourse.slicer.org/t/12144
---

# Problem in viewing segmentation volume and voronoi model

**Topic ID**: 12144
**Date**: 2020-06-21
**URL**: https://discourse.slicer.org/t/problem-in-viewing-segmentation-volume-and-voronoi-model/12144

---

## Post #1 by @Deepa (2020-06-21 16:11 UTC)

<p>Hello Everyone,<br>
I’m trying out the features of <code>Extract centerlines</code> available in recent Preview release.</p>
<p>In the Windows version, I could view both centerline and Voronoi model after hitting  <code>Apply</code> (steps followed from <a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117">here</a>) . I am not able to view the Voronoi model in Linux version though.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb895fcb45008999a1d53623ccb223f6bc01625b.png" alt="image" data-base62-sha1="xBEwLdjKZCwQRpJ3DpQxCjOS1u3" width="345" height="223"> .</p>
<p>The problem is after using  <code>Extract Centerlines</code> I am not able to view the Voronoi model and segmentation volume (this can be seen in the snapshot posted above – the eye icon next to the segmentation node is open in the bottom image from Linux version).</p>
<p>Please note:  The segmentation volume is visible after loading the file i.e prior to centerline computation. The volume disappears after hitting Apply in  <code>Extract Centerlines</code> .</p>
<p>I have also tried to view the segmentation volume outside <code>VMTK</code> module, in the segment editor. It works absolutely fine and I am able to view the volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8017d1b2a59f06e93fb14ea8fad5da63727c5ddc.png" data-download-href="/uploads/short-url/iha9cJepOWzCx77UKWfVpHNYdFG.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8017d1b2a59f06e93fb14ea8fad5da63727c5ddc_2_345x110.png" alt="Untitled" data-base62-sha1="iha9cJepOWzCx77UKWfVpHNYdFG" width="345" height="110" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8017d1b2a59f06e93fb14ea8fad5da63727c5ddc_2_345x110.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8017d1b2a59f06e93fb14ea8fad5da63727c5ddc_2_517x165.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8017d1b2a59f06e93fb14ea8fad5da63727c5ddc_2_690x220.png 2x" data-dominant-color="D0D5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">964×310 76.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-06-21 16:42 UTC)

<p>Do the models appear correctly if you set their opacity to 1.0 (fully opaque)?<br>
Does disabling depth peeling make everything appear?<br>
How many points and cells are in the Voronoi model? (you can see it in the Models module Information section).</p>

---

## Post #3 by @Deepa (2020-06-22 02:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks a lot for the response.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12144">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do the models appear correctly if you set their opacity to 1.0 (fully opaque)?</p>
</blockquote>
</aside>
<p>Yes. The Voronoi model is visible only at 1. It is not visible for any value &lt;1 even after disabling depth peeling. There is no issue with the Windows version.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12144">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does disabling depth peeling make everything appear?</p>
</blockquote>
</aside>
<p>No</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12144">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How many points and cells are in the Voronoi model? (you can see it in the Models module Information section).</p>
</blockquote>
</aside>
<p>170983 .</p>

---

## Post #4 by @Deepa (2020-06-23 12:16 UTC)

<p>May I know if any update is available on this issue?</p>

---

## Post #5 by @Deepa (2020-07-11 07:47 UTC)

<p>This problem persists even in the latest preview release. Immediately after centerline model is generated<br>
the 3D geometry disappears and voronoi model is visible only at opacity =1. This makes it really difficult for tasks like branch deletion. I never faced these issues in the releases made in June.</p>
<p>Could you please look into this?</p>

---
