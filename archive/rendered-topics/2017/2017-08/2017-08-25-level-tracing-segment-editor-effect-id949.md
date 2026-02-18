# Level tracing segment editor effect

**Topic ID**: 949
**Date**: 2017-08-25
**URL**: https://discourse.slicer.org/t/level-tracing-segment-editor-effect/949

---

## Post #1 by @stevenagl12 (2017-08-25 18:08 UTC)

<p>I was wondering if there was a way to get an option in level tracing for the Segment Editor to allow for the corrections to the segmentation performed in the 3rd dimension so that the level tracing can happen outside of the plane you are working with? Also possibly an effect to thread a tubelike segmentation into a gap of a prior segmentation that isn’t straight. I know there is the scizzors option to fill straight lines but it would be useful to start a tubelike segmentation for something like the spinal cord?</p>

---

## Post #2 by @lassoan (2017-08-25 18:42 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="1" data-topic="949">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>I was wondering if there was a way to get an option in level tracing for the Segment Editor to allow for the corrections to the segmentation performed in the 3rd dimension so that the level tracing can happen outside of the plane you are working with?</p>
</blockquote>
</aside>
<p>There is a 3D version of the level tracing algorithm, which may be usable, but integration would take some time and display of 3D preview may be slow. The level trace effect is ported from the legacy Editor module, but compared to all the other effects, I don’t find it very useful. We probably have to either have to improve it or move out from the core (and have it available in some optional extension, for those who find it useful).</p>
<p>For what kind of segmentation did you find level tracing effect useful?</p>
<aside class="quote no-group" data-username="stevenagl12" data-post="1" data-topic="949">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>possibly an effect to thread a tubelike segmentation into a gap of a prior segmentation that isn’t straight. I know there is the scizzors option to fill straight lines but it would be useful to start a tubelike segmentation for something like the spinal cord?</p>
</blockquote>
</aside>
<p>You can create a tube-like segmentation using scissors with circle shape. If you draw in a slice view, you can even limit the depth.</p>

---

## Post #3 by @stevenagl12 (2017-08-25 19:01 UTC)

<p>I find the level tracing useful for my noisy images of the lungs to get a little more of the details, as well as the airways. Every time I use the scissors effect in the slice viewers the effect just generates a tube through the entire 3d structure. Is there an option I should be choosing? Also besides the surface cut is there a way to expand or contract a certain region of a segmentation by like pushing or pulling the 3d or 2d visualization if the segmentation is missing a portion?</p>

---

## Post #4 by @lassoan (2017-08-25 20:43 UTC)

<p>You can restrict the Scissors effect cut “thickness” by the Slice cut option.</p>

---

## Post #5 by @lassoan (2017-08-25 22:17 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="3" data-topic="949">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>is there a way to expand or contract a certain region of a segmentation by like pushing or pulling the 3d or 2d visualization if the segmentation is missing a portion?</p>
</blockquote>
</aside>
<p>One obvious way is to use interpolate between segments. You segment on two or more slices in 2D and this effect fills all the other slices in 3D in between.</p>
<p>You can also expand or contract a segment using Margin effect. You can combine it with masking options to restrict the growth in various ways (stay inside/outside certain segments or intensity regions, etc).</p>
<p>If you can describe what is the exact problem that you try to solve, I can give more specific advice.</p>

---

## Post #6 by @fedorov (2017-08-26 13:57 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="3" data-topic="949">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>I find the level tracing useful for my noisy images of the lungs to get a little more of the details, as well as the airways.</p>
</blockquote>
</aside>
<p>Did you know there is an extension specifically for lung images processing, and it can segment lungs automatically? Check out Chest imaging platform.</p>

---

## Post #7 by @stevenagl12 (2017-08-26 22:23 UTC)

<p>So the problem is that my images are non-contrast enhanced ct images of cadavers donated to my school. I’m slowly working on segmenting all the major organ systems.</p>

---

## Post #9 by @stevenagl12 (2017-08-28 22:50 UTC)

<p>Hey Andrey Federov, so I’m not finding the extension either for the chest imaging platform to install it on the nightly build I already have?</p>

---

## Post #10 by @fedorov (2017-08-29 00:58 UTC)

<p><a class="mention" href="/u/stevenagl12">@stevenagl12</a> what platform are you on? Are you using the nightly package?</p>
<p><a class="mention" href="/u/jonieva">@jonieva</a> it appears that CIP has build errors on Windows - see <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1087165">http://slicer.cdash.org/viewBuildError.php?buildid=1087165</a>.</p>

---

## Post #11 by @stevenagl12 (2017-08-29 01:50 UTC)

<p>Yes I am using the nightly build. According to the CIP website I’m supposed to download the extension but it’s not there.</p>

---

## Post #12 by @fedorov (2017-08-29 02:32 UTC)

<p>What operating system do you have?</p>

---

## Post #13 by @stevenagl12 (2017-08-29 04:28 UTC)

<p>I have Windows 10  on a desktop with 32gbs of ram and an i7 processor.</p>

---

## Post #14 by @alireza (2021-07-05 04:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="949">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is a 3D version of the level tracing algorithm</p>
</blockquote>
</aside>
<p>Can you please point me to the 3D version of the level tracing algorithm? is it public?</p>

---

## Post #15 by @pieper (2021-07-05 17:55 UTC)

<p>The underlying ITK code is N-dimensional so you can try it out.  I never found the 3D mode very effective but it probably depends a lot on the data and task.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/master/Libs/vtkITK/itkLevelTracingImageFilter.h">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkITK/itkLevelTracingImageFilter.h" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkITK/itkLevelTracingImageFilter.h" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Libs/vtkITK/itkLevelTracingImageFilter.h</a></h4>


    <pre><code class="lang-h">#ifndef itkLevelTracingImageFilter_h
#define itkLevelTracingImageFilter_h

#include "itkImage.h"
#include "itkImageToImageFilter.h"
#include "itkSimpleDataObjectDecorator.h"
#include "itkChainCodePath.h"

namespace itk
{

/** \class LevelTracingImageFilter
 * \brief Trace a level curve/surface given a seed point on the level curve/surface.
 *
 * LevelTracingImageFilter traces a level curve (or surface) from a
 * seed point.  The pixels on this level curve "boundary" are labeled
 * as 1. Does nothing if seed is in uniform area.
 *
 * LevelTracingImageFilter provides a quick method to select a point
 * on a boundary of an object in a grayscale image and retrieve the
</code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkITK/itkLevelTracingImageFilter.h" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @ferhue (2022-06-09 09:10 UTC)

<p>Hi, I would welcome such a feature. Are there any plans of implementing this into 3D Slicer? I am segmenting a half cylinder that is not straight, so using the scissors is not working well for me. What I do now is go slice by slice using level tracing, but there are 200 slices, so it would be nice to have a checkbox that enables recursively spreading the level tracing to neighboring slices.</p>

---

## Post #17 by @lassoan (2022-06-13 13:55 UTC)

<p>You can use the scissors effect on arbitrary slice orientation. You can rotate slices by displaying slice intersections and Ctrl+Alt+Left-click-and-drag in a slice view.</p>
<p>If the cylinder is clearly distinguishable from the surroundings (which is very likely, if you find that level tracing works well) then you should be able to segment in 10-20 seconds using Grow from seeds, Local threshold, or Fast marching effects.</p>

---

## Post #18 by @Inka_Saraswati (2023-12-27 14:04 UTC)

<p>Is the three dimensional level tracing available in the current Slicer? If so, how to reach it?</p>

---

## Post #19 by @pieper (2023-12-27 18:19 UTC)

<p>Three-d level tracing never proved as useful as hoped.  Maybe it was just an implementation issue.  The underlying code should still exist in the low-level classes but some programming would be required to expose it.</p>

---

## Post #20 by @lassoan (2024-02-12 03:18 UTC)

<p>When you use Level Tracing, you use trial and error to find a mouse position that leads to acceptable segmentation. This trial and error would take several magnitudes longer time (minutes instead of seconds) in 3D because there are many more points and also takes much longer to check the segmentation result in dozens of slices than a quick visual check in a single slice</p>

---
