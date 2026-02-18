# Segmentation criteria for using SegmentGeometry to calculate 2nd moments

**Topic ID**: 37461
**Date**: 2024-07-19
**URL**: https://discourse.slicer.org/t/segmentation-criteria-for-using-segmentgeometry-to-calculate-2nd-moments/37461

---

## Post #1 by @chz31 (2024-07-19 01:28 UTC)

<p>I am planning to use Segment Geometry from SlicerBiomech Extension to calculate 2nd moments of area for mouse mandibles based on cross sections. Mouse have large incisors, should I remove them and other teeth or include them for calculating 2nd moments of area?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e839554179f690fdd8a7f01f3563f9d9cf64eede.jpeg" data-download-href="/uploads/short-url/x8lBJrgMMPuXkOgZGMNpz7L9oyW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e839554179f690fdd8a7f01f3563f9d9cf64eede_2_270x249.jpeg" alt="image" data-base62-sha1="x8lBJrgMMPuXkOgZGMNpz7L9oyW" width="270" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e839554179f690fdd8a7f01f3563f9d9cf64eede_2_270x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e839554179f690fdd8a7f01f3563f9d9cf64eede_2_405x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e839554179f690fdd8a7f01f3563f9d9cf64eede_2_540x498.jpeg 2x" data-dominant-color="605E50"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1774 424 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I saw that in the <a href="https://www.youtube.com/watch?v=fI5xFT7_81I" rel="noopener nofollow ugc">tutorial video</a> for a cat mandible, the teeth were kept there. Perhaps teeth do not matter?</p>
<p>My second question is, how accurate the cross-section segmentation should be?  I can’t find an efficient way to segment out the small cavities (see picture below), particularly those in the trabecular bone. If these small holes are filled, would it impact much of the second moments of area calculation?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2edcd498bd055d86abdcec8eae07bf0aaa474ad3.png" data-download-href="/uploads/short-url/6Gz5CGFGztnh2cXDvqSofyovhPJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2edcd498bd055d86abdcec8eae07bf0aaa474ad3_2_345x148.png" alt="image" data-base62-sha1="6Gz5CGFGztnh2cXDvqSofyovhPJ" width="345" height="148" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2edcd498bd055d86abdcec8eae07bf0aaa474ad3_2_345x148.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2edcd498bd055d86abdcec8eae07bf0aaa474ad3_2_517x222.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2edcd498bd055d86abdcec8eae07bf0aaa474ad3_2_690x296.png 2x" data-dominant-color="676455"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1564×675 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0580bf006c216f2aac641b7462a9842994069a75.png" data-download-href="/uploads/short-url/MGdVmpBeH2juJ0wnG7RshjHBzL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0580bf006c216f2aac641b7462a9842994069a75_2_345x153.png" alt="image" data-base62-sha1="MGdVmpBeH2juJ0wnG7RshjHBzL" width="345" height="153" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0580bf006c216f2aac641b7462a9842994069a75_2_345x153.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0580bf006c216f2aac641b7462a9842994069a75_2_517x229.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0580bf006c216f2aac641b7462a9842994069a75_2_690x306.png 2x" data-dominant-color="626262"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1523×679 69.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any suggestions would be appreciated! Thanks in advance! <a class="mention" href="/u/jmhuie">@jmhuie</a></p>

---

## Post #2 by @jmhuie (2024-07-19 15:41 UTC)

<aside class="quote no-group" data-username="chz31" data-post="1" data-topic="37461">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chz31/48/77363_2.png" class="avatar"> chz31:</div>
<blockquote>
<p>Mouse have large incisors, should I remove them and other teeth or include them for calculating 2nd moments of area?</p>
</blockquote>
</aside>
<p>That really depends on your question. You’re going to get different results depending on whether you keep the teeth in or not. Same goes for the functional teeth that have already emerged. One argument is that the large incisor in the jaw is going to add structure and reinforcement in the real world so removing it may give an inaccurate idea of how stiff the jaw is.</p>
<aside class="quote no-group quote-modified" data-username="chz31" data-post="1" data-topic="37461">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chz31/48/77363_2.png" class="avatar"> chz31:</div>
<blockquote>
<p>My second question is, how accurate the cross-section segmentation should be?..If these small holes are filled, would it impact much of the second moments of area calculation?</p>
</blockquote>
</aside>
<p>I would not worry so much about the small cavities. That is in part a resolution problem. First, holes that are only a few pixels large will not impact your results greatly. Especially since it looks like your scan is high resolution. Second, if you are comparing 2nd moment across many scans with similar resolutions then you will still get comparable patterns. I’d be more concerned about not being able to segment small cavities if you’re comparing a low resolution scan with a high resolution scan.</p>
<p>Hope this helps!</p>

---

## Post #3 by @chz31 (2024-07-19 18:48 UTC)

<p>Thanks, Jonathan <a class="mention" href="/u/jmhuie">@jmhuie</a>! These are really helpful.</p>
<p>It makes sense to keep the incisors there since they keep growing and mice need to constant bite on it. I need to do some experiments with or without teeth.</p>

---
