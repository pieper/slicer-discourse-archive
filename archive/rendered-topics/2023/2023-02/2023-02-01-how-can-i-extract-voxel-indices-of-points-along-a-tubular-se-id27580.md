---
topic_id: 27580
title: "How Can I Extract Voxel Indices Of Points Along A Tubular Se"
date: 2023-02-01
url: https://discourse.slicer.org/t/27580
---

# How can I extract voxel indices of points along a tubular segmentation obtained by Draw Tube?

**Topic ID**: 27580
**Date**: 2023-02-01
**URL**: https://discourse.slicer.org/t/how-can-i-extract-voxel-indices-of-points-along-a-tubular-segmentation-obtained-by-draw-tube/27580

---

## Post #1 by @calici (2023-02-01 11:54 UTC)

<p>Hi everyone!</p>
<p>I am trying to create synthetic Catheter insertion data.</p>
<p>First I create synthetic catheter label inside CT via segmentation by Draw Tube as shown below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/546bd07f3282f890712bb3e4c061df90619ecdf5.png" data-download-href="/uploads/short-url/c2P688J6jLCoHxZCgTL7sIhFpjL.png?dl=1" title="IMG000129" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/546bd07f3282f890712bb3e4c061df90619ecdf5_2_690x302.png" alt="IMG000129" data-base62-sha1="c2P688J6jLCoHxZCgTL7sIhFpjL" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/546bd07f3282f890712bb3e4c061df90619ecdf5_2_690x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/546bd07f3282f890712bb3e4c061df90619ecdf5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/546bd07f3282f890712bb3e4c061df90619ecdf5.png 2x" data-dominant-color="AAACAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG000129</span><span class="informations">979×429 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After that, I convert it to Binary Label Map.<br>
I would like to crop this label map by following the curve along control points iteratively such that it looks like the insertion of the catheter as below GIF:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5d1ab5ddce6a071cc2baf0a396e3c245b29fd1a.gif" alt="ezgif.com-gif-maker(4)" data-base62-sha1="uvwUMqRjWwU3z3WdZsimWuFusu6" width="306" height="411" class="animated"></p>
<p>I could extract the world coordinates of the control points I used in Draw Tube and I also tried Extract Centerline. The latter gave me world coordinates of the points along the curve but I could not figure out how I can crop label maps according to those coordinates.</p>
<p>TL;DR: I am trying to order voxel indices in a binary label map according to their positions along the curve.</p>
<p>I would appreciate any hints, thank you!</p>

---

## Post #2 by @lassoan (2023-02-01 12:06 UTC)

<p>You can use <a href="https://examples.itk.org/src/filtering/fastmarching/createdistancemapfromseeds/Documentation">fast marching algorithm</a> to create a distance map. You can then simply extract a binary image of a given catheter length using global thresholding.</p>
<p>However, a catheter is not solid but a thin shell, often with one or few ring markers near the tip. You can simulate them more realistically by rendering as a semi-transparent surface instead of a volume.</p>

---

## Post #3 by @calici (2023-02-28 14:13 UTC)

<p>Dear Andras Lasso,</p>
<p>Thank you very much for your answer!</p>
<p>Would it be possible to a bit further explain how to use the fast marching algorithm for this purpose?</p>
<p>Would the steps be like this: convert world coordinates of the center line to voxel coordinates =&gt; calculate distance map for surrounding voxels with fast marching algorithm =&gt; obtain binary mask with threshold?</p>
<p>Is it the method of how tubular shape is segmented in Slicer with draw tube in segment editor extra effects?</p>
<p>Thank you for your suggestion! However, I am using <a href="https://github.com/arcadelab/deepdrr" rel="noopener nofollow ugc">deepDRR</a> to simulate catheters by using a volume mask which looks like below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f360e2fa7af0aadffc098fc45edef47266a87821.jpeg" data-download-href="/uploads/short-url/yJ1BrGrXUgccRFvATFDvEDBx2Kd.jpeg?dl=1" title="Screenshot_20230228_030308" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f360e2fa7af0aadffc098fc45edef47266a87821_2_497x500.jpeg" alt="Screenshot_20230228_030308" data-base62-sha1="yJ1BrGrXUgccRFvATFDvEDBx2Kd" width="497" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f360e2fa7af0aadffc098fc45edef47266a87821_2_497x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f360e2fa7af0aadffc098fc45edef47266a87821_2_745x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f360e2fa7af0aadffc098fc45edef47266a87821_2_994x1000.jpeg 2x" data-dominant-color="5A5959"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20230228_030308</span><span class="informations">1322×1329 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am trying to create synthetic Xray images of catheter insertion by sampling volume mask along the centerline.</p>
<p>Thank you.</p>

---
