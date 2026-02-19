---
topic_id: 10381
title: "Segmenting A Entire Slice"
date: 2020-02-21
url: https://discourse.slicer.org/t/10381
---

# Segmenting a Entire Slice!

**Topic ID**: 10381
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/segmenting-a-entire-slice/10381

---

## Post #1 by @manjula (2020-02-21 13:33 UTC)

<p>The my Micro CT data are reformated with " Fit slice plane to markup fiducials " script. I expected to fill the entire selected slice with Scissor effect by drawing a rectangle. (Same with the paint). However there are areas of unfilled areas which corresponds to the slice below.  !</p>
<p>Is this has to do with reformatting ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccadafe2a8021e1cbf906d53770da3b3411dbe09.png" data-download-href="/uploads/short-url/tcFwESOhURdCpESscR1vho3vrM5.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccadafe2a8021e1cbf906d53770da3b3411dbe09_2_690x366.png" alt="2" data-base62-sha1="tcFwESOhURdCpESscR1vho3vrM5" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccadafe2a8021e1cbf906d53770da3b3411dbe09_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccadafe2a8021e1cbf906d53770da3b3411dbe09_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccadafe2a8021e1cbf906d53770da3b3411dbe09.png 2x" data-dominant-color="989A98"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1176×624 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4bd31f8ee5db2db860d0698dd9cecef1e7b0725.jpeg" data-download-href="/uploads/short-url/yV3QNJ6gQXQuQSsvc7IDMUzD5rf.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4bd31f8ee5db2db860d0698dd9cecef1e7b0725_2_690x183.jpeg" alt="1" data-base62-sha1="yV3QNJ6gQXQuQSsvc7IDMUzD5rf" width="690" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4bd31f8ee5db2db860d0698dd9cecef1e7b0725_2_690x183.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4bd31f8ee5db2db860d0698dd9cecef1e7b0725_2_1035x274.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4bd31f8ee5db2db860d0698dd9cecef1e7b0725_2_1380x366.jpeg 2x" data-dominant-color="5E5F5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1906×507 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And when we do the segment growing etc… the final results in the last two slice are not very good becuase of this.</p>
<p>. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4551e6354ff5f8c11d118c576a535f1ebd06986.jpeg" data-download-href="/uploads/short-url/s0PWUwwXlaoWhEvQW6ndNiBUpcG.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4551e6354ff5f8c11d118c576a535f1ebd06986_2_593x500.jpeg" alt="3" data-base62-sha1="s0PWUwwXlaoWhEvQW6ndNiBUpcG" width="593" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4551e6354ff5f8c11d118c576a535f1ebd06986_2_593x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4551e6354ff5f8c11d118c576a535f1ebd06986_2_889x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4551e6354ff5f8c11d118c576a535f1ebd06986_2_1186x1000.jpeg 2x" data-dominant-color="5E5E70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1309×1102 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to make a very nice clean cut ?  because when we try with segment effects always the changes in this slice will be reflect in the above slice so on…</p>
<ol>
<li>
<p>Why is this happening ?</p>
</li>
<li>
<p>Is there a better way of obtaining a clean cut segment of predictable height ? ( we want to make sure the segment height is always 2 mm. )</p>
</li>
</ol>

---

## Post #2 by @lassoan (2020-02-21 13:49 UTC)

<p>This looks normal. See explanation here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/</a></p>

---

## Post #3 by @manjula (2020-02-21 14:19 UTC)

<p>Thank you proffesor <a class="mention" href="/u/lassoan">@lassoan</a>  the oversampling (by 2 ) works well.</p>
<p>I do not understand about oversampling. Does this affect volume calculations ?</p>
<p>What does oversampling actually does ?</p>
<p>What are the advantage/ disadvantages of this ?</p>

---

## Post #4 by @lassoan (2020-02-21 14:39 UTC)

<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="10381">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>I do not understand about oversampling. Does this affect volume calculations ?</p>
</blockquote>
</aside>
<p>It should not significantly affect volume calculations, probably the difference is well below 1%.</p>
<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="10381">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>What does oversampling actually does ?</p>
</blockquote>
</aside>
<p>Subdivides the original voxels to smaller ones.</p>
<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="10381">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>What are the advantage/ disadvantages of this ?</p>
</blockquote>
</aside>
<p>Advantage is that you can represent finer details. Disadvantage is that it increases memory usage and computation time.</p>

---
