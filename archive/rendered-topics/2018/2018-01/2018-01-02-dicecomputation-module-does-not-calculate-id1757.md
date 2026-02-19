---
topic_id: 1757
title: "Dicecomputation Module Does Not Calculate"
date: 2018-01-02
url: https://discourse.slicer.org/t/1757
---

# DiceComputation module does not calculate

**Topic ID**: 1757
**Date**: 2018-01-02
**URL**: https://discourse.slicer.org/t/dicecomputation-module-does-not-calculate/1757

---

## Post #1 by @aharris (2018-01-02 20:31 UTC)

<p>I have segmented label maps from two imaging modalities (3D ultrasound and MRI), and have performed a registration and transformation between them.  When the Hausdorff distance option is clicked in the DiceComputation module I get numbers in the results matrix.  However, with the Dice option clicked, clicking the Compute button doesn’t do anything.  Any suggestions?</p>

---

## Post #2 by @lassoan (2018-01-03 00:37 UTC)

<p>You can also try Segment Comparison module in SlicerRT extension. It computes both Dice and Hausdorff.</p>

---

## Post #3 by @pieper (2018-01-03 12:48 UTC)

<p>I tried the DiceComputation extension and it worked fine for me with two labelmaps generated from the same source volume (using the legacy editor on the MRHead from SampleData).  <a class="mention" href="/u/aharris">@aharris</a> perhaps your volume data is not in the same pixel space and needs to be resampled.  Check in the error log for clues.</p>

---

## Post #4 by @lassoan (2018-01-03 15:32 UTC)

<p>Segment comparison module in SlicerRT extension takes care of all transformations and resampling. It works on segmentation nodes, if you have labelmaps or models then you can convert them into segmentation using Import section of Segmentations module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab06d212ac93bcfd32af00ac8649b4c5638c1a60.png" data-download-href="/uploads/short-url/ooYg9oGHdraSD7FEfnTbyNlimL6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab06d212ac93bcfd32af00ac8649b4c5638c1a60_2_564x500.png" alt="image" data-base62-sha1="ooYg9oGHdraSD7FEfnTbyNlimL6" width="564" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab06d212ac93bcfd32af00ac8649b4c5638c1a60_2_564x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab06d212ac93bcfd32af00ac8649b4c5638c1a60_2_846x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab06d212ac93bcfd32af00ac8649b4c5638c1a60_2_1128x1000.png 2x" data-dominant-color="BBBBBF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1529×1355 551 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @aharris (2018-01-05 17:43 UTC)

<p>This worked, thanks!</p>

---

## Post #6 by @carnico (2020-09-21 09:17 UTC)

<p>Dear Slicer users,</p>
<p>I post here to not open a new discussion.</p>
<p>I just try to use the Segment Comparison module in SlicerRT, but the calculated Dice coefficient is always 1. I’m using latest Slicer nightly on macOS.</p>
<p>How can I resolve this problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1baaf13c6732ef3cf458aae2c330acf9b031f26c.jpeg" data-download-href="/uploads/short-url/3WL8iUbmUTBQxiCvLLpmAlBXwFC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1baaf13c6732ef3cf458aae2c330acf9b031f26c_2_690x345.jpeg" alt="image" data-base62-sha1="3WL8iUbmUTBQxiCvLLpmAlBXwFC" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1baaf13c6732ef3cf458aae2c330acf9b031f26c_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1baaf13c6732ef3cf458aae2c330acf9b031f26c_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1baaf13c6732ef3cf458aae2c330acf9b031f26c_2_1380x690.jpeg 2x" data-dominant-color="363538"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3356×1680 654 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks a lot.</p>
<p>Best Regards</p>
<p>P.s.: I also cannot find on slicer extension manager the <a href="http://slicer.kitware.com/midas3/slicerappstore/extension/view?extensionId=39201" rel="noopener nofollow ugc">DiceComputation</a> extension, which I would like to try.</p>

---

## Post #7 by @cpinter (2020-09-21 09:41 UTC)

<p>Based on your screenshot the two segments do not overlap, so the calculation based on this is correct.</p>
<p>In order to have two segments that have overlapping parts and meaningful dice, you need to either</p>
<ol>
<li>Enable overlapping in Segment Editor before drawing the second segment, or</li>
<li>Use different segmentations for the two regions</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/036c0639de1dd81812ab58a7ad1ddb9d2aa38cef.png" alt="image" data-base62-sha1="ugS9xJAgnhaGhGZn1E1yZuRQar" width="289" height="146"></p>

---

## Post #8 by @lassoan (2020-09-21 14:57 UTC)

<p>DSC should be 0 if there is no overlap, so indeed there is something wrong here.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> I suspect that Segment Comparison module was not updated to handle  merged labelmaps. Could you please check if this and other SlicerRT modules use the correct API for getting labelmap representations?</p>

---

## Post #9 by @Sunderlandkyl (2020-09-21 15:27 UTC)

<p>OK, I need to re-compile SlicerRT and then I can submit a PR.</p>
<p>Most of the modules in SlicerRT seem to be fine, except for a couple (SegmentComparison, RoomsEyeView, SegmentMorphology) that use vtkSlicerSegmentationsModuleLogic::GetSegmentRepresentation() / GetSegmentBinaryLabelmapRepresentation().</p>
<p>I can fix this in SegmentComparison (and vtkSlicerRoomsEyeViewModuleLogic) by getting the individual non-shared labelmap with vtkSegmentationNode::GetBinaryLabelmapRepresentation().</p>

---

## Post #10 by @lassoan (2020-09-21 15:32 UTC)

<p>Thank you <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>.</p>
<p>It seems that SegmentMorphology module does the same as Margin effect and Logical operators effect. Maybe we could just remove it, to reduce SlicerRT maintenance burden. <a class="mention" href="/u/cpinter">@cpinter</a> what do you think?</p>

---

## Post #11 by @cpinter (2020-09-21 15:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="1757">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>DSC should be 0 if there is no overlap</p>
</blockquote>
</aside>
<p>Yes this is actually true. Thanks <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> for fixing this!</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="1757">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems that SegmentMorphology module does the same as Margin effect and Logical operators effect. Maybe we could just remove it, to reduce SlicerRT maintenance burden.</p>
</blockquote>
</aside>
<p>I have thought about this as well, but didn’t have time to check if some workflow or other extension relies on this etc. But in theory I agree, it is basically a duplication of features.</p>

---

## Post #12 by @lassoan (2020-09-21 16:10 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="11" data-topic="1757">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I have thought about this as well, but didn’t have time to check if some workflow or other extension relies on this etc. But in theory I agree, it is basically a duplication of features.</p>
</blockquote>
</aside>
<p>SegmentMorphology module was developed when Segment Editor did not have these features, so it made sense then, but not necessary now. We have the option of A. fix it now and commit to its maintenance, 2. remove it now and fix&amp;maintain if it turns out that somebody needs it. I would vote for B.</p>

---

## Post #13 by @cpinter (2020-09-21 16:14 UTC)

<p>Absolutely, I agree.</p>
<p>I just said I haven’t removed the Segment Morphology module because for that I wanted to check if another extension used that particular module. You have a build machine so doing that check should be easy. If nobody else uses the module, then it can be removed.</p>

---

## Post #14 by @lassoan (2020-09-21 16:21 UTC)

<p>SegmentMorphology module is not used in any other extensions. It is not used either in SlicerRT workflow tests. So, removing it should not disrupt anything.</p>

---

## Post #15 by @lassoan (2020-09-21 18:17 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, since you already have a SlicerRT build configured, would you mind submitting a pull request that removes SegmentMorphology module? Thank you!</p>

---

## Post #16 by @Sunderlandkyl (2020-09-21 18:30 UTC)

<p>OK, PR made here: <a href="https://github.com/SlicerRt/SlicerRT/pull/156" rel="noopener nofollow ugc">https://github.com/SlicerRt/SlicerRT/pull/156</a>.</p>

---
