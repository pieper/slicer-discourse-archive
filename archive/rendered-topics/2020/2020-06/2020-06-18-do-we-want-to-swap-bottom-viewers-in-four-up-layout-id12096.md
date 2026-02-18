# Do we want to swap bottom viewers in four-up layout?

**Topic ID**: 12096
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/do-we-want-to-swap-bottom-viewers-in-four-up-layout/12096

---

## Post #1 by @ungi (2020-06-18 15:55 UTC)

<p>I find myself often swapping the bottom 2D views in default four-up layout. Currently, sagittal plane is displayed under axial by default. But it can be more intuitive to have the coronal plane under axial, and sagittal to the right side. More anatomical landmarks line up this way in adjacent views. I think section views are also arranged similarly in technical drawings to make better visual connection between points.<br>
I know habits are a strong reason to keep the layout consistent, but I thought this might be a good time to discuss this in the community, before a major release.<br>
Here is a picture of the proposed new default four-up layout with some lines showing why I think this could be considered.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac1872b1339484a0d29b08feb6c0a30b77f053c4.jpeg" data-download-href="/uploads/short-url/oyqvhuzxR4AqX18MscEhhBnwO5S.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac1872b1339484a0d29b08feb6c0a30b77f053c4_2_663x500.jpeg" alt="image" data-base62-sha1="oyqvhuzxR4AqX18MscEhhBnwO5S" width="663" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac1872b1339484a0d29b08feb6c0a30b77f053c4_2_663x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac1872b1339484a0d29b08feb6c0a30b77f053c4_2_994x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac1872b1339484a0d29b08feb6c0a30b77f053c4.jpeg 2x" data-dominant-color="5D5864"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1210×912 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-06-18 16:03 UTC)

<p>This makes complete sense. We can keep the current default of Red=axial, Yellow=Sagittal, Green=Coronal and just make the green view appear on the left and yellow on the right. If there are no objections then I can implement this very easily.</p>

---

## Post #3 by @pieper (2020-06-18 16:11 UTC)

<p>Yes, that sounds very reasonable to me. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #4 by @cpinter (2020-06-18 16:27 UTC)

<p>I found myself confused about the sagittal being under the axial many times now that I think about it. But never formulated the possibility of switching the sagittal and the coronal. I say do it. Good timing right before 5.0 as well.</p>

---

## Post #5 by @lassoan (2020-06-19 13:12 UTC)

<p>Yellow and green views are now swapped: <a href="https://github.com/Slicer/Slicer/commit/e1b3dbec8ea491fbcd69bc8b67d87e4a95065f3a">https://github.com/Slicer/Slicer/commit/e1b3dbec8ea491fbcd69bc8b67d87e4a95065f3a</a></p>

---
