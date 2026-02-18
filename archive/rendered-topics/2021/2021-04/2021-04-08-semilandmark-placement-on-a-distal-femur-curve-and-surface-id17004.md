# Semilandmark placement on a distal femur (curve and surface)

**Topic ID**: 17004
**Date**: 2021-04-08
**URL**: https://discourse.slicer.org/t/semilandmark-placement-on-a-distal-femur-curve-and-surface/17004

---

## Post #1 by @aotero54 (2021-04-08 17:16 UTC)

<p>Operating system:<br>
Slicer version: 4.11<br>
Expected behavior: Resampled curve constrained to the surface between two points.<br>
Actual behavior: Resampled curve is underneath the 3D model and not constrained to the surface (with constrain to surface option selected).</p>
<p>Another issue I am having is placing surface semilandmarks on the distal articular surface of a femur. I a not sure if I need to have the curves delineated first or save the landmarks together in one dataset.</p>

---

## Post #2 by @aotero54 (2021-04-08 17:16 UTC)

<p>I am having trouble placing curve and surface semilandmarks. For the curve, when I resample the resampled curve is underneath the 3D model instead of constrained to the surface (with the constrain to surface option selected).</p>
<p>For the surface, I am having trouble placing semilandmarks just on the distal articular surface. I am not sure if this is because I do not have a singular landmark data set or because the curves have not been delineated yet</p>

---

## Post #3 by @aotero54 (2021-04-08 17:16 UTC)

<p>I am having trouble placing curved semilandmarks through resampling. After creating my curve and resampling (making sure to select constrain to surface), the new curve is beneath the model.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/048b5bae3ffd433ba2e9bf0c9c1c3d2a43465e53.png" data-download-href="/uploads/short-url/EctXMi6BIRyWvSlmTIvW2nfPnZ.png?dl=1" title="Screenshot (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/048b5bae3ffd433ba2e9bf0c9c1c3d2a43465e53_2_690x388.png" alt="Screenshot (1)" data-base62-sha1="EctXMi6BIRyWvSlmTIvW2nfPnZ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/048b5bae3ffd433ba2e9bf0c9c1c3d2a43465e53_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/048b5bae3ffd433ba2e9bf0c9c1c3d2a43465e53_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/048b5bae3ffd433ba2e9bf0c9c1c3d2a43465e53_2_1380x776.png 2x" data-dominant-color="B7B9D7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (1)</span><span class="informations">1920×1080 368 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/021ba9e0522e073a222739997e973f7a79eaf14c.png" data-download-href="/uploads/short-url/iEdSCfY1ixJUoGtnRtbHu2GrY8.png?dl=1" title="Screenshot (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/021ba9e0522e073a222739997e973f7a79eaf14c_2_690x388.png" alt="Screenshot (2)" data-base62-sha1="iEdSCfY1ixJUoGtnRtbHu2GrY8" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/021ba9e0522e073a222739997e973f7a79eaf14c_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/021ba9e0522e073a222739997e973f7a79eaf14c_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/021ba9e0522e073a222739997e973f7a79eaf14c_2_1380x776.png 2x" data-dominant-color="B6B8DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (2)</span><span class="informations">1920×1080 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also, I am unsure of how to place surface semilandmarks only on the distal articular surface. I am not sure if I need to combine the landmarks into a single dataset or place the curved semilandmarks first to delineate the surface I want covered.</p>

---

## Post #4 by @muratmaga (2021-04-08 19:53 UTC)

<aside class="quote no-group" data-username="aotero54" data-post="3" data-topic="17004">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a183cd/48.png" class="avatar"> aotero54:</div>
<blockquote>
<p>I am having trouble placing curved semilandmarks through resampling. After creating my curve and resampling (making sure to select constrain to surface), the new curve is beneath the model.</p>
</blockquote>
</aside>
<p>Couple comments:</p>
<ol>
<li>You are using an older version of Slicer. Please switch to the latest stable to get the most recent bug fixes and improvement (<a href="https://download.slicer.org">https://download.slicer.org</a>)</li>
<li>You seem to create individual points for your anatomical LMs, which is fine. However, you will need to keep them in a single node, if your ultimate goal is shape analysis.</li>
<li>You can play with the projection distance parameter of resampling curves (Expand the advanced option). Default might be too high region of high curvature. Assuming first screenshot is the manual curve drew, almost all of it is already on the surface. If you bring it down, I think it will solve your problem.</li>
</ol>
<p>What is curious to me in the second screen capture the start and end points seems modified. We typically assume (at least for collecting data for shape analysis) that the start and end points of the curve is fixed (anchored to anatomical LM) and then resample everything in between to generate equidistant points on the drawn curve. Process really shouldn’t modify the very first and last point on the curve.</p>
<p>If you want to draw additional curves in this manner, but bring them together so that they are in a single markup node (and redundant points are removed), you can use the MergeMarkups utility in SlicerMorph. Make sure you install the latest stable and get the SlicerMorph, as those updates will not be in the version you are using.</p>
<p>This <a href="https://discourse.slicer.org/t/markups-creating-a-single-file-including-landmarks-fixed-and-curves-semilandmarks-problem-while-resampling/16158/8">thread (and tutorial at the end)</a> might be also of use to you.</p>

---

## Post #5 by @aotero54 (2021-04-08 20:28 UTC)

<p>Thank you! Updating to the latest version helped with some other issues I was having. Regarding placement of the curve, how do I anchor it to the anatomical LM? I do not see that option anywhere, I thought the user placed the points and then resampled to either increase or decrease the number of semilandmarks and to have the be equidistant. The reason for the difference in start and end points was I placed the first and last points at the anatomical landmarks and was going to delete them later so that they did not overlap with the anatomical landmark.</p>

---

## Post #6 by @muratmaga (2021-04-08 20:49 UTC)

<aside class="quote no-group" data-username="aotero54" data-post="5" data-topic="17004">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a183cd/48.png" class="avatar"> aotero54:</div>
<blockquote>
<p>thought the user placed the points and then resampled to either increase or decrease the number of semilandmarks and to have the be equidistant.</p>
</blockquote>
</aside>
<p>Yes, that’s the workflow. We just don’t move the very first and last points on the curve during resampling assuming those are the intended starting and ending points. Implicit in that logic is that those are fixed LMs (i.e., to answer first question, you don’t have to do anything like anchoring).</p>

---

## Post #7 by @aotero54 (2021-04-08 20:59 UTC)

<p>Okay, I think the best option would be for me to create several different curves and then merge them using the MergeMarkups tool. However, wouldn’t there still be redundancy with each landmark having a corresponding semilandmark in the same position? Would I then just delete those overlapping semilandmarks?</p>

---

## Post #8 by @muratmaga (2021-04-08 22:06 UTC)

<aside class="quote no-group" data-username="aotero54" data-post="7" data-topic="17004">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a183cd/48.png" class="avatar"> aotero54:</div>
<blockquote>
<p>However, wouldn’t there still be redundancy with each landmark having a corresponding semilandmark in the same position?</p>
</blockquote>
</aside>
<p>That is a more of a workflow issue.</p>
<ol>
<li>You can choose to exclude the fixed landmarks when you are merging final list of points for shape analysis</li>
<li>You can delete the control points on the curves that has a matching fixed LM prior to merging.</li>
<li>If you end up using our GPA module, you can specify LMs to exclude at the time of the superimposition.</li>
</ol>
<p>The point is, if you are do this systematically with the tools provided, it will be quiet simple to exclude points (as long as they are consistent).</p>

---
