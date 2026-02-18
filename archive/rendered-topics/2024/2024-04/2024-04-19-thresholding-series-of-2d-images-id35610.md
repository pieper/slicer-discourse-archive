# Thresholding series of 2D images

**Topic ID**: 35610
**Date**: 2024-04-19
**URL**: https://discourse.slicer.org/t/thresholding-series-of-2d-images/35610

---

## Post #1 by @muratmaga (2024-04-19 02:19 UTC)

<p>I have a series of 2D images, for which I would like to use the segment editor to mask out the background. It seems fine in the preview, but when I apply there is this ghost of other slices?</p>
<p>Is this because of interpolation between slices (this is not a 3D volume, but series of 2D images). If so, is there a chance to apply the threshold per slice basis?</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18e5f82e38b87d4155abac6828e204fac8ef19f3.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcbd35b0d6470ae0cef44a2243c69530ab9c6eaf.jpeg">
  </div><p></p>

---

## Post #2 by @pieper (2024-04-19 12:38 UTC)

<p>The thresholding would be at the pixel level, so slice/volume shouldn’t matter.  Are you sure this isn’t just a rendering issue?  Maybe turn off interpolation in the slice view.</p>

---

## Post #3 by @muratmaga (2024-04-19 19:33 UTC)

<p>Interesting, it seems like a rendering issue in my other computer. I can’t replicate it with a different computer. Thanks.</p>
<p>I do have one more question. There are small gaps, which I would like to fill. Normally I would use closing filter to do that. But when I do, due to 3D interpolation I get artifacts (i.e, mask extending into places where it shouldnt). Would it be possible to run this slice-by-slice somehow?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b000ba31099edb8844afddbb72a7440a51b72fa2.jpeg" data-download-href="/uploads/short-url/p6ZALHDYvCghy5h4YpQpe3JdLwu.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b000ba31099edb8844afddbb72a7440a51b72fa2_2_207x375.jpeg" alt="image" data-base62-sha1="p6ZALHDYvCghy5h4YpQpe3JdLwu" width="207" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b000ba31099edb8844afddbb72a7440a51b72fa2_2_207x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b000ba31099edb8844afddbb72a7440a51b72fa2_2_310x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b000ba31099edb8844afddbb72a7440a51b72fa2_2_414x750.jpeg 2x" data-dominant-color="5E6B5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">534×962 63.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b9b7a2deab1e88617c6da13f67f1d0e3f4c0301.jpeg" data-download-href="/uploads/short-url/3We00MarBG3utOrI5MPZveyTxvj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b9b7a2deab1e88617c6da13f67f1d0e3f4c0301_2_231x374.jpeg" alt="image" data-base62-sha1="3We00MarBG3utOrI5MPZveyTxvj" width="231" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b9b7a2deab1e88617c6da13f67f1d0e3f4c0301_2_231x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b9b7a2deab1e88617c6da13f67f1d0e3f4c0301_2_346x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b9b7a2deab1e88617c6da13f67f1d0e3f4c0301_2_462x748.jpeg 2x" data-dominant-color="596659"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">586×951 68.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2024-04-19 20:53 UTC)

<p>Yes, unlike thresholding, any of the 3d operations are going to have trouble with this kind of data (since it’s not a volume).  The thing I would look at doing would be to do some of these operations at the numpy array level.</p>
<p>Regarding the rendering issue, that really shouldn’t happen differently on different machines.  If you are able to replicate it in some small test maybe you can share the steps and others can try?</p>

---

## Post #5 by @muratmaga (2024-04-19 21:18 UTC)

<p>You can find the sample data here;<br>
<a href="https://osf.io/c3wsg">OSF | 39384_cropped_photos.zip</a></p>

---

## Post #6 by @pieper (2024-04-20 14:38 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="35610">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Interesting, it seems like a rendering issue in my other computer. I can’t replicate it with a different computer.</p>
</blockquote>
</aside>
<p>It didn’t happen for me either (on mac book air m2).  Is it repeatable on the machine where it happened?  What is different about that computer?</p>

---

## Post #7 by @muratmaga (2024-04-20 15:53 UTC)

<p>It is an older Macbook pro (intel chip), but funny thing I can’t reproduce it anymore.</p>

---
