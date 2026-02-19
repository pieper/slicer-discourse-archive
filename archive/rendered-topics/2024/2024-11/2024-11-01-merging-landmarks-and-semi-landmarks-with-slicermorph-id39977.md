---
topic_id: 39977
title: "Merging Landmarks And Semi Landmarks With Slicermorph"
date: 2024-11-01
url: https://discourse.slicer.org/t/39977
---

# Merging landmarks and semi-landmarks with SlicerMorph

**Topic ID**: 39977
**Date**: 2024-11-01
**URL**: https://discourse.slicer.org/t/merging-landmarks-and-semi-landmarks-with-slicermorph/39977

---

## Post #1 by @Ruiqi-CUB (2024-11-01 11:06 UTC)

<p>I am Slicer 5.6.2. My project use 1) 5 homologous landmarks 2) semilandmarks on a open curve 3) semilandmarks on a closed curve, My goal is to merge them and create a PCA plot in R with merged data.</p>
<p>I tried to use MergeMarkups function in SlicerMorph. But it is not showing all the landmarks. Under Markup tab, I can see all 3 types of landmarks:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f7d99d95b3e69d98596da7ac372872db0b2b877.png" data-download-href="/uploads/short-url/93Fb7Vtzfbr7EW3niQ6XIJXKjRR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f7d99d95b3e69d98596da7ac372872db0b2b877.png" alt="image" data-base62-sha1="93Fb7Vtzfbr7EW3niQ6XIJXKjRR" width="627" height="360"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">627×360 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, under MergeMarkups-Merge landmark Sets, I can only see homologous landmarks:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33127e4579966748500a45f48ca70cf4dee00a0.png" data-download-href="/uploads/short-url/yHnl9yhFLepkAEr50g4e1NLSoEM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33127e4579966748500a45f48ca70cf4dee00a0.png" alt="image" data-base62-sha1="yHnl9yhFLepkAEr50g4e1NLSoEM" width="625" height="291"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">625×291 23.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can see the two curves under Merge Curves tab, but not the homologous landmarks:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1885c663ecb1038df5685231fa34fe4cb5ed4b05.png" data-download-href="/uploads/short-url/3uW4ofHzrkSUtoyO1DPKk7DSmfH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1885c663ecb1038df5685231fa34fe4cb5ed4b05.png" alt="image" data-base62-sha1="3uW4ofHzrkSUtoyO1DPKk7DSmfH" width="619" height="307"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">619×307 27.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My question is: how do I merge those three different landmarks (point list, curve, open curve), and save one file, so I can do a PCA and subsequent analyses in R? I guess I still would like to keep all the information, such as if this is a homologous landmark, or a semi-landmark; and which curve it belongs to. Would you mind helping me have a look? Thank you!</p>

---

## Post #2 by @muratmaga (2024-11-01 18:56 UTC)

<p>So in <code>MergeMarkups</code> you can stitch multiple curves that share beginning and ending points into a single curve (Merge Curves tab), or you can Merge fixed landmarks with the semiLMs SlicerMorph generated (Merge Landmark set).</p>
<p>We haven’t seen a use case or a request like your, but we can add that feature. However, it will take a few weeks to be available as we are busy with other things. You can track its progress at: <a href="https://github.com/SlicerMorph/SlicerMorph/issues/357" class="inline-onebox" rel="noopener nofollow ugc">Expand the Functionality of MergeMarkups with other markup types. · Issue #357 · SlicerMorph/SlicerMorph · GitHub</a></p>
<p>Meanwhile, the simplest solution for you is to:</p>
<ol>
<li>Copy a blank pointList (e.g., called MergedPoints)</li>
<li>Copy and paste control points from other type (fixedLMs, open and closed curves), into the MergedPoints pointList.</li>
</ol>
<p>Then everything will be together.</p>

---

## Post #3 by @Ruiqi-CUB (2024-11-20 16:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="39977">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>you can Merge fixed landmarks with the semiLMs SlicerMorph generated (Merge Landmark set)</p>
</blockquote>
</aside>
<p>Thank you! What do you mean by semiLMs SlicerMorph generated? Are they differ from the semiLMs that I placed and resampled on a curve? I can’t see the curves under  Merge Landmark set?</p>

---

## Post #4 by @muratmaga (2024-11-20 16:36 UTC)

<aside class="quote no-group" data-username="Ruiqi-CUB" data-post="3" data-topic="39977">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/b38774/48.png" class="avatar"> Ruiqi-CUB:</div>
<blockquote>
<p>Are they differ from the semiLMs that I placed and resampled on a curve</p>
</blockquote>
</aside>
<p>Yes, for example semi landmark generated by landmark patch functionality or pseudoLMgenerator. As I said above, it only works for that type. Please use copy/paste method i described.</p>

---

## Post #5 by @Ruiqi-CUB (2024-11-20 16:43 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="39977">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Meanwhile, the simplest solution for you is to:</p>
<ol>
<li>Copy a blank pointList (e.g., called MergedPoints)</li>
<li>Copy and paste control points from other type (fixedLMs, open and closed curves), into the MergedPoints pointList.</li>
</ol>
<p>Then everything will be together.</p>
</blockquote>
</aside>
<p>Thank you. I was able to do it. But the “ids” are not changed, for example, the ids for primary is still 1-5 while for semiLMs are 1-30. Would that matter in the analyses in R (morph and geomorph)?</p>
<p>I think I will need to specify semilandmarks in the log files like “SemiLandmarks= 11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30”</p>
<p>That’s just the order of the LMs and semiLMs right? The ids shouldn’t matter? So as long as I paste them in a fixed order (for example, primary, open curve, closed curve), it should be fine?</p>

---

## Post #6 by @muratmaga (2024-11-20 16:45 UTC)

<aside class="quote no-group" data-username="Ruiqi-CUB" data-post="5" data-topic="39977">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/b38774/48.png" class="avatar"> Ruiqi-CUB:</div>
<blockquote>
<p>the ids for primary is still 1-5 while for semiLMs are 1-30. Would that matter in the analyses in R (morph and geomorph)?</p>
</blockquote>
</aside>
<p>No, it is the ordinal number not the ID.</p>
<aside class="quote no-group" data-username="Ruiqi-CUB" data-post="5" data-topic="39977">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/b38774/48.png" class="avatar"> Ruiqi-CUB:</div>
<blockquote>
<p>I think I will need to specify semilandmarks in the log files like “SemiLandmarks= 11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30”</p>
</blockquote>
</aside>
<p>Yes, use the ordinal values.</p>

---

## Post #7 by @Ruiqi-CUB (2024-11-20 17:02 UTC)

<p>Thanks! My understanding is SemiLMs slides along the curves.</p>
<p>Since I have two curves, how do I distinguish the two curves using the copy and paste method? or does it matter?</p>

---

## Post #8 by @muratmaga (2024-11-20 22:18 UTC)

<p>You don’t points are points. When you need to distinguish, you use the ordinal number associated with them (e.g., order such that first 10 are your fixed LMs, then next batch is your curves semiLM, and then next is patch so forth).</p>

---

## Post #9 by @Ruiqi-CUB (2024-11-20 22:31 UTC)

<p>Thank you! This is really helpful.</p>
<p>Another question: my two curves (one closed curve, and one open curve) do have two shared points and I am thinking combing them using MergeCurves Function. However, when I placing semilandmarks, I placed those two shared points next to each other so they are not really shared points. I did not find a way to placing curves semiLMs starting/ending at an existing point, it always placed at a nearby place. Is there a way to place curves semiLMs starting/ending at an existing point?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b5f0bc00e9513caef4092e48b388452386c06d6.png" data-download-href="/uploads/short-url/aKLrBhLfM4nzoXYIWU4SLuYnk6a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5f0bc00e9513caef4092e48b388452386c06d6_2_653x500.png" alt="image" data-base62-sha1="aKLrBhLfM4nzoXYIWU4SLuYnk6a" width="653" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5f0bc00e9513caef4092e48b388452386c06d6_2_653x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5f0bc00e9513caef4092e48b388452386c06d6_2_979x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5f0bc00e9513caef4092e48b388452386c06d6_2_1306x1000.png 2x" data-dominant-color="9F9DD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1394×1066 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @muratmaga (2024-11-21 17:50 UTC)

<p>As I recall, the MergeCurves copies the last point of the curve as the first point of the next one when merging. So in that sense it may not matter. Do try and see.</p>

---
