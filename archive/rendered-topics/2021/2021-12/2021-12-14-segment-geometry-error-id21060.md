# Segment Geometry error

**Topic ID**: 21060
**Date**: 2021-12-14
**URL**: https://discourse.slicer.org/t/segment-geometry-error/21060

---

## Post #1 by @hourglassnam (2021-12-14 19:37 UTC)

<p>Hello~everyone~<br>
I had a problem while using the segment geometry module.<br>
The module would work sometimes, but it will not work most of the time and show me an error message as below…<br>
Slicer has caught an application error, please save your work and restart.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: D:\D\P\Slicer-0-build\ITK\Modules\Segmentation\ConnectedComponents\include\itkConnectedComponentImageFilter.hxx:145:<br>
ITK ERROR: ConnectedComponentImageFilter(000002D6F17C9430): Number of objects (754) greater than maximum of output pixel type (255).</p>
<p>Does anyone have an idea why this might be happening?</p>

---

## Post #2 by @lassoan (2021-12-16 18:12 UTC)

<p>This error message suggests that your input segmentation is extremely noisy (contains many disconnected islands). You can apply Smoothing effect or Islands effect’s Keep largest island operation, or use more appropriate segmentation tools, which generate less noisy segment.</p>

---

## Post #3 by @jmhuie (2022-01-24 01:04 UTC)

<p>Hi <a class="mention" href="/u/hourglassnam">@hourglassnam</a>,</p>
<p>Did <a class="mention" href="/u/lassoan">@lassoan</a>’s suggestion help? I also suggest using the the Island tool to keep the largest island or the selected one.</p>

---

## Post #4 by @mau_igna_06 (2022-04-22 19:25 UTC)

<p>Hi. I’m creating a thresholdedImagesArray by thresholding an image with a fixed max value and an array of min values, then I do islandsMath effect and then another threshold to keep the largest island to each imageElement of the array.<br>
If the number of islands is big while processing an element of the array I wouldn’t need it (i.e. numberOfIslands&gt;255). And I want this because processing a unsignedChar image should be order of magnitudes faster than processing an unsignedShort image.<br>
But I cannot batch process this because Slicer keeps throwing the itk exception, could you help?</p>

---

## Post #5 by @lassoan (2022-04-22 22:44 UTC)

<p>Thresholding speed on unsigned char/short should be both very fast. Do you have any performance measurement results that shows how much faster unsigned char thresholding is? I would expect that it is 20-30% faster, not magnitudes (1000-10000%) faster.</p>
<p>Islands effect needs to be able to assign unique labels to each island, so if you have more than 255 islands then I don’t think you can use unsigned char.</p>
<p>However, you can both reduce the number of islands and hugely increase processing speed by processing the image at lower resolution (or at multiple resolutions).</p>

---

## Post #6 by @mau_igna_06 (2022-04-22 23:00 UTC)

<p>If I do a plot on the future I’ll share it here.</p>
<p>I think some of the previous post talk about about the exception being annoying and not useful… I would rather have the number of islands to be extracted that the exception informs rather than the overflow exception itself.<br>
The exception is problematic because it doesn’t allow batch processing.</p>
<p>Do you have any idea to on how to skip processing (and avoid the exception) while creating the labelMapsArray I described using unsigned char images?</p>
<p>I think there should be a way to handle the exception on IslandMath filter definition on C++ at least</p>
<p>Or maybe I could use itk connectivity filter on python myself. Would that allow me to manage the exception?</p>

---

## Post #7 by @lassoan (2022-04-23 03:35 UTC)

<p>The “Islands” effect <a href="https://github.com/Slicer/Slicer/blob/f776beeb281e14d981442ae9c59e018a21689e60/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L144-L146">uses <code>unsigned int</code> as input for the vtkITKIslandMath filter</a>, so it should not run out of label values. What Slicer version do you use?</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="6" data-topic="21060">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>The exception is problematic because it doesn’t allow batch processing</p>
</blockquote>
</aside>
<p>If you use <code>vtkITKIslandMath</code> from your own script and use an <code>unsigned char</code> input then you can run into the problem that the ITK exception is not caught. I agree that it would be better to catch the exception and log a VTK error instead (that can be captured in Python using an error sink). See an example <a href="https://github.com/Slicer/Slicer/blob/e7fdd8e712cb464468d218ec0508a4abc6c4e293/Libs/vtkITK/vtkITKImageThresholdCalculator.cxx#L102-L110">here</a>. If you have time, please make this change, check if it works for you and if it does then send a pull request.</p>
<p>Note that (depending on how the algorithm is implemented) more than 255 label values might be needed temporarily, even if in the final contains less than 255 islands.</p>

---
