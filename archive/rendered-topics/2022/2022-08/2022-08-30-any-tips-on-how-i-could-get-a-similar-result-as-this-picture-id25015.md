# Any tips on how I could get a similar result as this picture?

**Topic ID**: 25015
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/any-tips-on-how-i-could-get-a-similar-result-as-this-picture/25015

---

## Post #1 by @HT1997 (2022-08-30 19:47 UTC)

<p>Hi, I am trying to segment the vessels from the public data LADAF-2020-27 left kidney, given from the Human Organ Atlas website. Is it possible to segment vessels of any kind from these datasets and make a similar result as the first picture? Any tips would be appreciated. Thank you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4232173fda58433dce1505c8e8c43a0fe2fbee72.jpeg" data-download-href="/uploads/short-url/9rAPAIrUpGfOunRYGfoTb4PNjMu.jpeg?dl=1" title="_pictures_LADAF_2020-27_kidney-left_25.08um_complete-organ" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/4232173fda58433dce1505c8e8c43a0fe2fbee72_2_690x352.jpeg" alt="_pictures_LADAF_2020-27_kidney-left_25.08um_complete-organ" data-base62-sha1="9rAPAIrUpGfOunRYGfoTb4PNjMu" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/4232173fda58433dce1505c8e8c43a0fe2fbee72_2_690x352.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/4232173fda58433dce1505c8e8c43a0fe2fbee72_2_1035x528.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/4232173fda58433dce1505c8e8c43a0fe2fbee72_2_1380x704.jpeg 2x" data-dominant-color="CFBAB1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">_pictures_LADAF_2020-27_kidney-left_25.08um_complete-organ</span><span class="informations">1920×982 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54e99011746d9ce399922d37b689e24566c0d276.jpeg" data-download-href="/uploads/short-url/c7avPEm01m0YtReLx6EoZdJBwMe.jpeg?dl=1" title="Screenshot from 2022-08-30 15-10-41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54e99011746d9ce399922d37b689e24566c0d276_2_690x383.jpeg" alt="Screenshot from 2022-08-30 15-10-41" data-base62-sha1="c7avPEm01m0YtReLx6EoZdJBwMe" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54e99011746d9ce399922d37b689e24566c0d276_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54e99011746d9ce399922d37b689e24566c0d276_2_1035x574.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54e99011746d9ce399922d37b689e24566c0d276_2_1380x766.jpeg 2x" data-dominant-color="8A8BA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-08-30 15-10-41</span><span class="informations">1920×1067 94.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-08-30 20:27 UTC)

<p>Thanks for pointing out that collection (<a href="https://human-organ-atlas.esrf.eu/">https://human-organ-atlas.esrf.eu/</a>).  There is some amazing data there.</p>
<p>Because the data is such high resolution and relatively clean you may be able to get good results with just the threshold tool in the segment editor.  It’s possible that a smoothing filter first might reduce the noise.</p>
<p>Everything at that resolution is going to be slow.  Loading an ROI with ImageStacks from SlicerMorph would allow you to explore techniques efficiently that could then be applied to the full volume.</p>

---

## Post #3 by @HT1997 (2022-09-02 18:48 UTC)

<p>Thank you for the reply. As you mention the threshold tool in the segment editor, do you mean to use a local threshold or a simple threshold?</p>

---

## Post #4 by @pieper (2022-09-02 19:13 UTC)

<p>I’d suggest the regular threshold tool at least to start since the data is huge.  The local threshold could be a big help with the vessels but it would require a lot of computation and probably some manual work for the seeding which really would not be feasible on that data.  Definitely practice on cropped subsets to see what kind of operations work.</p>

---
