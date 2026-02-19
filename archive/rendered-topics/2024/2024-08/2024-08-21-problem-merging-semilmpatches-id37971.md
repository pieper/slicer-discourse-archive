---
topic_id: 37971
title: "Problem Merging Semilmpatches"
date: 2024-08-21
url: https://discourse.slicer.org/t/37971
---

# Problem merging SemiLMPatches

**Topic ID**: 37971
**Date**: 2024-08-21
**URL**: https://discourse.slicer.org/t/problem-merging-semilmpatches/37971

---

## Post #1 by @zifangx (2024-08-21 02:19 UTC)

<p>Hi, I am trying to apply surface landmarks across a region of interest in a lizard cranium, utilizing the CreateSemiLMPatches module of SlicerMorph. When I try to merge the SemiLMPatches (screenshot1) into one single node, some of the merged nodes (specifically, those generated along the edges of the triangular patches, circled red in screenshot2) “sink in” to the underside of the mesh. Is there any way to correct this behaviour? Do I need to manually adjust these points to get them back to the mesh surface? I’m looking to apply SemiLMPatches onto many other specimens, so ideally would like to reduce the amount of manual adjustment if possible.<br>
I’d really appreciate any insights, thank you in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88651f05e35684ef4fe3327844d6b3b555576c65.jpeg" data-download-href="/uploads/short-url/jsBAoSAXNQjEn0pSmZEKKL6yOvH.jpeg?dl=1" title="screenshot1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88651f05e35684ef4fe3327844d6b3b555576c65_2_690x303.jpeg" alt="screenshot1.PNG" data-base62-sha1="jsBAoSAXNQjEn0pSmZEKKL6yOvH" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88651f05e35684ef4fe3327844d6b3b555576c65_2_690x303.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88651f05e35684ef4fe3327844d6b3b555576c65_2_1035x454.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88651f05e35684ef4fe3327844d6b3b555576c65_2_1380x606.jpeg 2x" data-dominant-color="8E9062"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot1.PNG</span><span class="informations">1920×845 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9aea28723106338bfeed1021a6ed0832a99f4b98.jpeg" data-download-href="/uploads/short-url/m6rd7wlXkv0gO2OKnelHEzctoKs.jpeg?dl=1" title="screenshot2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aea28723106338bfeed1021a6ed0832a99f4b98_2_690x302.jpeg" alt="screenshot2.PNG" data-base62-sha1="m6rd7wlXkv0gO2OKnelHEzctoKs" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aea28723106338bfeed1021a6ed0832a99f4b98_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aea28723106338bfeed1021a6ed0832a99f4b98_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aea28723106338bfeed1021a6ed0832a99f4b98_2_1380x604.jpeg 2x" data-dominant-color="827F6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot2.PNG</span><span class="informations">1920×843 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-08-21 20:28 UTC)

<aside class="quote no-group" data-username="zifangx" data-post="1" data-topic="37971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zifangx/48/77050_2.png" class="avatar"> zifangx:</div>
<blockquote>
<p>“sink in” to the underside of the mesh.</p>
</blockquote>
</aside>
<p>This is controlled by the projection parameter of the module. Unfortunately for us, microCT derived surface models has an internal surface. So if the points are projected a little too much along the normal, sometimes it gets snapped by the internal surface. Expand the Advanced options, and try incrementally reducing the projection value (or disable it).</p>
<p>Also you may want to give our new module PlaceLandmarkGrid, which eventually replace the module you are using. You can draw arbitrary patches (using 4 control points) and sample semi-landmarks inside it. It is still work in progress, so it is a good time to give feedback as well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/387d976360e9b5046a6d70a117e1c32fdb30f457.jpeg" data-download-href="/uploads/short-url/83JOCZ2LbgLAubFQBGHbs3tLsa3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387d976360e9b5046a6d70a117e1c32fdb30f457_2_690x472.jpeg" alt="image" data-base62-sha1="83JOCZ2LbgLAubFQBGHbs3tLsa3" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387d976360e9b5046a6d70a117e1c32fdb30f457_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387d976360e9b5046a6d70a117e1c32fdb30f457_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387d976360e9b5046a6d70a117e1c32fdb30f457_2_1380x944.jpeg 2x" data-dominant-color="BDBEC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1315 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @zifangx (2024-08-22 20:54 UTC)

<p>Thank you for your reply!<br>
Unfortunately, I had no luck playing around with the two projection parameters with different combinations. The triangular patches themselves were not a problem, it was when I hit the “merge highlighted nodes” which, I believe, generates additional points along the edges of the triangle, those points are acting funky, regardless of what parameter combinations I tried.<br>
And thanks for the suggestion! I’ll give the new module a try!</p>

---

## Post #4 by @smrolfe (2024-08-26 21:17 UTC)

<p>Hi <a class="mention" href="/u/zifangx">@zifangx</a> is it possible for you to share a model with the landmark patches so I can give this a try?</p>

---

## Post #5 by @zifangx (2024-10-04 15:29 UTC)

<p>Hi Sara,</p>
<p>Sorry for the late reply but yes, absolutely! I’ll send you a link via message.</p>

---
