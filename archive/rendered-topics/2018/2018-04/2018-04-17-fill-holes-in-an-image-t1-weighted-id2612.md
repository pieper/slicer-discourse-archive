---
topic_id: 2612
title: "Fill Holes In An Image T1 Weighted"
date: 2018-04-17
url: https://discourse.slicer.org/t/2612
---

# Fill “holes” in an image (T1-weighted)

**Topic ID**: 2612
**Date**: 2018-04-17
**URL**: https://discourse.slicer.org/t/fill-holes-in-an-image-t1-weighted/2612

---

## Post #1 by @Frederic (2018-04-17 17:10 UTC)

<p>Hi all!<br>
I would like to fill holes of a binary input 3D image (cf. image and the code on it).<br>
It’s possible with Scipy (<a href="https://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.ndimage.morphology.binary_fill_holes.html" rel="noopener nofollow ugc">link</a>), but Scipy is not installed in slicer.</p>
<p>How could I do that?</p>
<p>Thanks in advance.!<br>
<a href="/uploads/short-url/sxD0d6EDuni3kFocpJZFIZ2V8to.png">Slicer_holes|690x310</a></p>

---

## Post #2 by @pieper (2018-04-17 18:46 UTC)

<p>Dd you try the SimpleFilters module?  There are a lot of hole filling options.</p>
<p><a href="https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1BinaryFillholeImageFilter.html" class="onebox" target="_blank">https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1BinaryFillholeImageFilter.html</a></p>
<p><a href="https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1VotingBinaryIterativeHoleFillingImageFilter.html" class="onebox" target="_blank">https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1VotingBinaryIterativeHoleFillingImageFilter.html</a></p>
<p><a href="https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1GrayscaleFillholeImageFilter.html" class="onebox" target="_blank">https://itk.org/SimpleITKDoxygen/html/classitk_1_1simple_1_1GrayscaleFillholeImageFilter.html</a></p>

---

## Post #3 by @lassoan (2018-04-17 21:28 UTC)

<p>Hole filling using morphological operator is also available directly in Segment editor (in Smoothing effect).</p>

---

## Post #4 by @Frederic (2018-04-18 17:31 UTC)

<p>Perfect. Thanks <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a><br>
For the next, the script is:</p>
<blockquote>
<pre><code>segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "MORPHOLOGICAL_CLOSING")
effect.setParameter("KernelSizeMm", 20)
</code></pre>
</blockquote>

---

## Post #5 by @Frederic (2018-05-16 16:15 UTC)

<p>I allow myself to come back to your reply <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a>  .<br>
This answer works but take a long time, is there a quicker way to fill the holes of a 3d model (or remove “the back-facing element”)?<br>
Thanks in advance.</p>

---

## Post #6 by @lassoan (2018-05-16 17:35 UTC)

<p>Kernel size of 20mm is extremely large! It is normal that it takes very long time to compute.</p>
<p>To remove internal holes from a segment, you may apply smoothing, then invert the segment, keep largest island, invert it back to get rid of most internal structures. If there are structures that are connected to the outside air (e.g., airways) then you can manually seal them off, to make them internal (disconnected from outside).</p>
<p>To extract skin, you should be able to use Flood fill effect (in SegmentEditorExtraEffects extension). Click in the air to create a segment (you can adjust neighborhood size to prevent leaking inside the body through small holes, like airways) and then invert the segment to get the skin surface.</p>
<p>I’ve created a repository where I’ll upload segmentation recipes and added detailed description of skin segmentation: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface/">https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface/</a></p>

---

## Post #7 by @Frederic (2018-05-17 08:08 UTC)

<p>Nice process and example Andras, thanks.<br>
However, I use your <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="nofollow noopener">previous script</a> routinely and I do not want to make it manually (scissors, …).<br>
Best.</p>

---

## Post #8 by @lassoan (2018-05-17 17:54 UTC)

<p>If you find that Flood fill works better than thresholding, then you can use that from script, too. Scissors, smoothing, etc. are all optional post-processing that may improve quality of thresholding or flood-filling results.</p>

---

## Post #9 by @Frederic (2018-05-18 13:05 UTC)

<p>Ok, I will try the two options.<br>
thanks Andras.</p>

---
