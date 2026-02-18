# Draw segment contour with attracted to edges

**Topic ID**: 333
**Date**: 2017-05-17
**URL**: https://discourse.slicer.org/t/draw-segment-contour-with-attracted-to-edges/333

---

## Post #1 by @brhoom (2017-05-17 12:22 UTC)

<p>One more question <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=5" title=":grin:" class="emoji" alt=":grin:">, is it possible to make the drawing attracted to the edge while drawing (something like LeveltracingEffect)?</p>

---

## Post #2 by @lassoan (2017-05-21 17:49 UTC)

<p>If there are actual edges (intensity differences) then you don’t want to segment slice-by-slice. In that case, use the Grow from seeds effect. It allows you to just approximately segment on a couple of slices and you automatically get a full 3D segmentation. You can always make adjustments (by adding a few more strokes) if you don’t like the automatic segmentation results at some places.</p>

---

## Post #3 by @brhoom (2017-05-24 13:57 UTC)

<p>Sometimes the edges are clear but the inside region is not. So drawing this way is a good idea.</p>

---

## Post #4 by @lassoan (2017-05-24 14:12 UTC)

<p>Grow from seeds fills inside the region correctly, even if inside and outside has the same intensity.</p>

---

## Post #5 by @lassoan (2017-05-24 14:19 UTC)

<p>You may also try Watershed effect, it also correctly fills in less dense parts inside bones. You need to install SegmentEditorExtraEffects extension and it will show up in Segment Editor.</p>

---

## Post #6 by @brhoom (2017-05-25 19:43 UTC)

<p>Thanks a lot, I will try this soon.</p>

---

## Post #7 by @brhoom (2017-05-26 07:10 UTC)

<p>Either I am doing it wrong or the tools are not suitable for this task. Have you tried to segment a CT image of the human spine?<br>
I am trying to segment a single separatley but so far only tools worked for me are the paint and the draw as there is always touching area between the vertebrae.<br>
BTW, it would be nice if the tools developers provide a tutorial as a demo video with sample data to use the tool efficiently.</p>
<p>Have a wonderful day!<br>
Ibraheem</p>

---

## Post #8 by @lassoan (2017-05-26 11:38 UTC)

<p>Yes, we often segment spine CTs. Depending on image quality and the accuracy you need, it may be tedious, but these semi-automated tool help. We are in the process of creating a video tutorial series, expected to release the first one in a few weeks.</p>
<p>Until then, a few tips:</p>
<ul>
<li>Always start with cropping your volume to the region of interest (if your volume is larger than needed, all processing will be slower) and resampling your volume to have an isotropic voxels size (otherwise you may not be able to have a smooth and detailed segmentation). For this, use Crop volume module: specify your <strong>ROI</strong> (as small as possible), select <strong>Isotropic spacing</strong>, select sufficiently low <strong>spacing scale</strong> value (the lower the value, the more details you can preserve during segmentation, but more memory and processing time you will need; typically 0.5 … 0.8 work well, but you may go down to 0.2 or keep the original 1.0), select <strong>bspline interpolator</strong>.</li>
<li>If you use Grow from seeds or Watershed, after you have the initial segmentation (“Initialize”), you need to keep painting more small strokes where the segmentation is not correct. The full segmentation is automatically recomputed based on the additional inputs within a few seconds. Repeat this, until you have a good enough segmentation.</li>
<li>You can create initial bone seeds by Thresholding with a high value and shrink it a bit using Margin effect (it is very important to not paint seeds into an incorrect area; incomplete seed is not a problem at all)</li>
</ul>

---
