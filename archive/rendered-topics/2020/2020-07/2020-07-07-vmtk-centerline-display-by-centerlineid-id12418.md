# VMTK Centerline Display by CenterlineId

**Topic ID**: 12418
**Date**: 2020-07-07
**URL**: https://discourse.slicer.org/t/vmtk-centerline-display-by-centerlineid/12418

---

## Post #1 by @szhang (2020-07-07 14:48 UTC)

<p>Hello<br>
I have been using the 4.11.0-2020-06-30 version of the Slicer, and would like to know how to display the centerline by the attribute CenterlineId, e.g. the picture below should display 8 centerlines for the user to pick and choose<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82e235d8862b12f22aa2e036fd83efad304e482d.png" data-download-href="/uploads/short-url/iFQIVeq2VYNpOFPlqebwa5plXmB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82e235d8862b12f22aa2e036fd83efad304e482d.png" alt="image" data-base62-sha1="iFQIVeq2VYNpOFPlqebwa5plXmB" width="327" height="500" data-dominant-color="9B9ED4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">354×540 3.01 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @szhang (2020-07-07 21:33 UTC)

<p>Hi Andras, <a class="mention" href="/u/lassoan">@lassoan</a><br>
Could you kindly provide some insights? So far I see the curves are broken into segments based on the vtkPolydata cell numbers, but would prefer to have the ability to select a whole path from the top to an endpoint. Thank you!</p>

---

## Post #3 by @lassoan (2020-07-08 12:22 UTC)

<p>If you don’t want to extract a whole tree then just specify a start point and end point, as shown in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #4 by @szhang (2020-07-08 14:01 UTC)

<p>Thanks, <a class="mention" href="/u/lassoan">@lassoan</a><br>
So far my experience at 4.11.0-2020-06-30 version is that with two endpoints manually clicked (I made sure they are within the segmentation, as otherwise they can be clicked anywhere in the space), the result shows the whole tree (see below) broken up by 15 segments<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb6d219277f855cd603bbeafd0b4ccadcc50b02f.png" data-download-href="/uploads/short-url/qK369XBUwFnLzxElCLsAcY2tRrp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb6d219277f855cd603bbeafd0b4ccadcc50b02f_2_690x373.png" alt="image" data-base62-sha1="qK369XBUwFnLzxElCLsAcY2tRrp" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb6d219277f855cd603bbeafd0b4ccadcc50b02f_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb6d219277f855cd603bbeafd0b4ccadcc50b02f_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb6d219277f855cd603bbeafd0b4ccadcc50b02f_2_1380x746.png 2x" data-dominant-color="B9BBDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 72.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, back to my original question, I would love to have the whole tree extracted, but visualize them labeled by the attribute “CenterlineId”, i.e. each curves composed of points from the beginning point to each corresponding end point, hence,  eight(8) centerlines in this example.<br>
Would really appreciate your advice!</p>

---

## Post #5 by @lassoan (2020-07-08 14:33 UTC)

<p>Choose “Centerline curve” and not “Network curve” to extract centerline between selected endpoints.</p>
<p>If you extract all the branches then you can use markups curves to find path between two arbitrary points: go to Markups module, drop two points of a curve on the tree, open Curve Settings section, choose Curve type → “Shortest distance on surface” and Model node → the tree model. See this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="UpfDP6ejCjg" data-video-title="Finding shortest path between two points in the bronchial tree" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UpfDP6ejCjg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UpfDP6ejCjg/maxresdefault.jpg" title="Finding shortest path between two points in the bronchial tree" width="" height="">
  </a>
</div>


---

## Post #6 by @szhang (2020-07-08 17:17 UTC)

<p>Thanks a lot for the tutorial video, <a class="mention" href="/u/lassoan">@lassoan</a><br>
I don’t quite follow this step, could you please elaborate more?</p>
<blockquote>
<p>drop two points of a curve on the tree</p>
</blockquote>

---

## Post #7 by @lassoan (2020-07-08 17:35 UTC)

<p>I mean place two markup curve points close to the centerline/network model. If you enable “Shortest distance on surface” option then the curve will be constrained to connect these two points via lines of the chosen model node.</p>

---

## Post #8 by @szhang (2020-07-08 21:18 UTC)

<p>Got it, thank you, <a class="mention" href="/u/lassoan">@lassoan</a>, it is quite a convenient way to visualize the centerline!</p>

---
