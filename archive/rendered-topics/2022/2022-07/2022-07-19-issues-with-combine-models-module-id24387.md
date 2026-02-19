---
topic_id: 24387
title: "Issues With Combine Models Module"
date: 2022-07-19
url: https://discourse.slicer.org/t/24387
---

# Issues with Combine models module

**Topic ID**: 24387
**Date**: 2022-07-19
**URL**: https://discourse.slicer.org/t/issues-with-combine-models-module/24387

---

## Post #1 by @SegmentedYannig (2022-07-19 07:59 UTC)

<p>Hello 3DSlicer community !</p>
<p>I’ve been experiencing weird behaviors with the Combine models module, as it sometimes returns an empty mesh and I can’t figure out why as it sometimes does work.</p>
<p>I’m trying to compute the intersection of those two blue cones, into the white volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0ce4d91097674a0b51fe050336ee85ef2c318dc.png" data-download-href="/uploads/short-url/mWyoDBf6R1WPuK99gAznbrhVRww.png?dl=1" title="doesntWork1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0ce4d91097674a0b51fe050336ee85ef2c318dc.png" alt="doesntWork1" data-base62-sha1="mWyoDBf6R1WPuK99gAznbrhVRww" width="473" height="499" data-dominant-color="010418"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">doesntWork1</span><span class="informations">503×531 21.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/951fabc3f3103eff1bf2e29fe0f494954ad60ca1.png" data-download-href="/uploads/short-url/lhcZRALVdAWtBbAhGRHVcPB8DfP.png?dl=1" title="doesntWork2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/951fabc3f3103eff1bf2e29fe0f494954ad60ca1.png" alt="doesntWork2" data-base62-sha1="lhcZRALVdAWtBbAhGRHVcPB8DfP" width="442" height="500" data-dominant-color="040616"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">doesntWork2</span><span class="informations">473×534 18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For the bigger picture, I’m trying to optimize the placement of robotic arms to avoid collision using the volume of the intersection as a part of my optimization formula.</p>
<p>Can someone help me figure out what’s happening and what I can do ?</p>
<p>Thank you for your attention and have a good day !</p>
<p>PS : It looks like the sandbox extension is no longer available</p>

---

## Post #2 by @lassoan (2022-07-19 10:44 UTC)

<p>It is practically impossible to implement binary operations on polygonal meshes that works on ill-shaped polygons. When cones are meshed in a trivial way, they tend to have extremely elongated triangles, therefore binary operations can easily fail. <code>vtkConeSource</code> creates such a trivial mesh because the main use is just visualization.</p>
<p>One simple option is reduce the resolution of the cone along the circumference, but if the resolution is lowered too much then the cone will appear faceted, which may not be acceptable. You can improve the triangle shapes while keeping the smooth appearance by remeshing the cone source output - maybe subdivide filter followed by quadric decimation would work.</p>
<aside class="quote no-group" data-username="SegmentedYannig" data-post="1" data-topic="24387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/segmentedyannig/48/16010_2.png" class="avatar"> SegmentedYannig:</div>
<blockquote>
<p>It looks like the sandbox extension is no longer available</p>
</blockquote>
</aside>
<p>The extension is available for latest stable and preview releases, on all platforms. If you don’t see it on your computer then check out <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extension-is-not-found-for-current-slicer-version">this page</a>.</p>

---

## Post #3 by @SegmentedYannig (2022-07-19 13:58 UTC)

<p>Thank you for your answer !<br>
Hmm, I see the problem, I’ll try to do what you suggested.</p>
<p>I’ll also update to the latest version for Slicer, I’m on 5.1.0 2022-05-04 right now</p>

---
