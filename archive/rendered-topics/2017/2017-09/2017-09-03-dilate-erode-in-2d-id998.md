# Dilate/Erode in 2d

**Topic ID**: 998
**Date**: 2017-09-03
**URL**: https://discourse.slicer.org/t/dilate-erode-in-2d/998

---

## Post #1 by @bp_pb (2017-09-03 19:35 UTC)

<p>Hi,</p>
<p>I would like to dilate a labelmap only in 2d. The option dilate four/eight unfortunately also take the upper and lower slice into account. Is there any possibility to do this. Thanks for the answer.</p>

---

## Post #2 by @lassoan (2017-09-03 19:37 UTC)

<p>Try the new Segment Editor in the latest nightly version. It has sophisticated margin growing/eroding and masking options that should help to segment anything you need. If you describe what your endgoal is then we can give you specific advice which effects to use and in what combination.</p>

---

## Post #3 by @bp_pb (2017-09-03 20:00 UTC)

<p>HI,</p>
<p>Thank you very much for your quick answer. Basically I segmented the lateral ventricles using a threshold and would like now to examine the 1 or 2 milimeters next to the ventricle. I tried this with “dilate” however this also segments the pixel on the upper and lower slices which falsifies the result . I will try with the new segement editor.</p>

---

## Post #4 by @lassoan (2017-09-03 21:01 UTC)

<aside class="quote no-group" data-username="bp_pb" data-post="3" data-topic="998">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/f07891/48.png" class="avatar"> bp_pb:</div>
<blockquote>
<p>examine the 1 or 2 milimeters next to the ventricle</p>
</blockquote>
</aside>
<p>What do you mean by examine? Measure the surface or volume?</p>
<p>Ventricles are 3d structures, so you should be able to properly segment them in 3D quite easily,  for example,  using the Grow from seeds effect.</p>
<p>If you need to smooth the segment, then use Smoothing effect. If you need to expand the segment then use the Margin effect. To restrict editing to a single slice, fill a single slice (using Paint or Scissors effect) and use that as a mask.</p>

---

## Post #5 by @bp_pb (2017-09-08 07:49 UTC)

<p>Hey again,</p>
<p>Unfortunately it didn’t work as I hopped with the segment editor.<br>
By examine I mean segment. Maybe I reexpose my problem:<br>
I segmented the ventricles only in the Axial view. Now, from this segmentation (in the axial view), I would like to expand it by 2 - 4 pixels outwards. As the dilate option also takes into account the upper and lower pixel, this could falsify the result, as I only segmented the ventricles in axial view.<br>
Is there a possibility (as I think there used to be in the older Slicer Versions) to dilate my axial segmentation only in the 2d plane.<br>
Thanks again</p>

---

## Post #6 by @cpinter (2017-09-08 12:06 UTC)

<p>Segmenting strictly in 2D does not seem more useful then real 3D segmentation. What is the reason why you don’t want to take into account the inferior-superior direction?</p>
<p>Other than that, you can define a mask segment. You can create large blocks using scissors for example, then set it as a mask when you do the dilation.<br>
I just noticed <a class="mention" href="/u/lassoan">@lassoan</a> wrote the same. However, it is still the easiest way.</p>

---

## Post #7 by @Mgi (2021-11-01 06:27 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> ! The segmentation strictly in 2D is important when you want to simulate two different segmentation of the same volume to evaluate the inter-observer variability and reproducibility. In that case, taking into account the inferior-superior direction could create new areas segmented in the inferior/superior slices that could be out of the tumour, then they cause errors.</p>
<p>Is possible to do the dilation 2D now? <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #8 by @cpinter (2021-11-02 09:14 UTC)

<p>It is still not possible, because there were no driving use cases. If you have at least a little Python and VTK experience, you could try to copy and modify the current dilation tool to perform it slice by slice.</p>

---

## Post #9 by @lassoan (2021-11-09 03:28 UTC)

<p>If you want to simulate random displacements then you can do that already. For example, export the segment to another segmentation, apply a transform with random displacement, and then import the moved segment back into the original segmentation. You can repeat that as many times as needed to simulate any probability distribution.</p>
<p>You can also very easily shift, copy, combine slices or regions within slices of segments using numpy indexing.  See example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">script repository</a>.</p>

---
