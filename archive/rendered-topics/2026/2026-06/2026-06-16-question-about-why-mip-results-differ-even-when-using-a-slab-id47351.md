---
topic_id: 47351
title: "Question about why MIP results differ even when using a Slab Thickness large enough to cover the entire volume in the Slice Viewer"
date: 2026-06-16
url: https://discourse.slicer.org/t/47351
last_bumped: 2026-06-16T13:20:05.063Z
---

# Question about why MIP results differ even when using a Slab Thickness large enough to cover the entire volume in the Slice Viewer

**Topic ID**: 47351
**Date**: 2026-06-16
**URL**: https://discourse.slicer.org/t/question-about-why-mip-results-differ-even-when-using-a-slab-thickness-large-enough-to-cover-the-entire-volume-in-the-slice-viewer/47351

---

## Post #1 by @Changyoon_Lee (2026-06-16 05:21 UTC)

<p>Hello,</p>
<p>I have a question about an unexpected behavior I observed while checking MIP results using Slab Reconstruction in the 3D Slicer Slice Viewer.</p>
<p>I tested this using the MRHead volume provided with 3D Slicer. The actual height of the volume is approximately 256 mm, and I tested slab thickness values of 300 mm and 500 mm, which should be large enough to fully cover the entire volume.</p>
<p>My expectation was that if the slab thickness is large enough to include the entire volume, the MIP result should be identical.</p>
<p>However, I observed the following behavior:</p>
<ol>
<li>
<p>Even when the slab thickness is large enough to fully include the volume, the MIP image changes when the slab thickness is changed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bbc2eaefa25bf1b4df62e937dbad46b9592879e.jpeg" data-download-href="/uploads/short-url/3Xm4naupP8HuANrScs5X3HNSMj4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bbc2eaefa25bf1b4df62e937dbad46b9592879e_2_514x499.jpeg" alt="image" data-base62-sha1="3Xm4naupP8HuANrScs5X3HNSMj4" width="514" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bbc2eaefa25bf1b4df62e937dbad46b9592879e_2_514x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bbc2eaefa25bf1b4df62e937dbad46b9592879e_2_771x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bbc2eaefa25bf1b4df62e937dbad46b9592879e.jpeg 2x" data-dominant-color="252420"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">896×870 81.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cec3b4fddf9fab7bd282c545b5d039adcdb5aaa9.jpeg" data-download-href="/uploads/short-url/tv7ES3s6TFupYkx1U15KmafhwXT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/cec3b4fddf9fab7bd282c545b5d039adcdb5aaa9_2_505x500.jpeg" alt="image" data-base62-sha1="tv7ES3s6TFupYkx1U15KmafhwXT" width="505" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/cec3b4fddf9fab7bd282c545b5d039adcdb5aaa9_2_505x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/cec3b4fddf9fab7bd282c545b5d039adcdb5aaa9_2_757x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cec3b4fddf9fab7bd282c545b5d039adcdb5aaa9.jpeg 2x" data-dominant-color="292723"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">888×878 77.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>The result appears as if the actual behavior does not match the specified slab thickness.</p>
</li>
<li>
<p>Even when the slab thickness is large enough to cover the entire volume, changing the current slice offset / slice index changes the MIP result.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c21c2c303e854b2225a7675a9aced41191329a35.jpeg" data-download-href="/uploads/short-url/rHaZiYF7dwatDMwsBOWUjYn2cL3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c21c2c303e854b2225a7675a9aced41191329a35_2_508x500.jpeg" alt="image" data-base62-sha1="rHaZiYF7dwatDMwsBOWUjYn2cL3" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c21c2c303e854b2225a7675a9aced41191329a35_2_508x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c21c2c303e854b2225a7675a9aced41191329a35_2_762x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c21c2c303e854b2225a7675a9aced41191329a35.jpeg 2x" data-dominant-color="262621"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">888×874 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/948d0f305a9b527a62380455b03c47c1419e5809.jpeg" data-download-href="/uploads/short-url/lc8SNwkwJEKeEXxWHcjkpYBg9KN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/948d0f305a9b527a62380455b03c47c1419e5809_2_504x500.jpeg" alt="image" data-base62-sha1="lc8SNwkwJEKeEXxWHcjkpYBg9KN" width="504" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/948d0f305a9b527a62380455b03c47c1419e5809_2_504x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/948d0f305a9b527a62380455b03c47c1419e5809_2_756x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/948d0f305a9b527a62380455b03c47c1419e5809.jpeg 2x" data-dominant-color="292723"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">884×876 76.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Exceptionally, when I set the slab thickness to 1000 mm, the result was identical to the result with 500 mm. Based on this, I suspect that I may be misunderstanding the range covered by the specified slab thickness. However, from any perspective, I find this behavior unintuitive and confusing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9f5d527126f3616d42cc84124a12c4f0a53e641.jpeg" data-download-href="/uploads/short-url/v6aiUEYeO51c0wVQKaK3UIgs0BH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9f5d527126f3616d42cc84124a12c4f0a53e641_2_507x500.jpeg" alt="image" data-base62-sha1="v6aiUEYeO51c0wVQKaK3UIgs0BH" width="507" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9f5d527126f3616d42cc84124a12c4f0a53e641_2_507x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9f5d527126f3616d42cc84124a12c4f0a53e641_2_760x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9f5d527126f3616d42cc84124a12c4f0a53e641.jpeg 2x" data-dominant-color="282723"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">894×880 77 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>I would like to know whether this is the intended behavior, or whether I am misunderstanding how Slab MIP works.</p>
<p>I have attached sample videos showing the differences caused by changing the slab thickness or slice offset.</p>
<p>Environment:</p>
<ul>
<li>3D Slicer version: 5.10.0 r34045 / a2b6d08</li>
<li>Data type: MRI volume</li>
<li>Slice view: Any view</li>
<li>Projection mode: MIP</li>
</ul>
<p>Thank you.</p>

---

## Post #2 by @pieper (2026-06-16 13:20 UTC)

<p>You’re right, that looks like a bug.  It might be due to the orientation of the MRHead being a sagittal acquisition.  Can you try the same experiments with a CT?  This should probably be converted into a bug report on github.</p>

---
