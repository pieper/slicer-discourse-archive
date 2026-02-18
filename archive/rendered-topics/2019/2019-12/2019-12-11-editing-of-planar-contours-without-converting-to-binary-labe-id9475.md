# Editing of planar contours without converting to binary label map

**Topic ID**: 9475
**Date**: 2019-12-11
**URL**: https://discourse.slicer.org/t/editing-of-planar-contours-without-converting-to-binary-label-map/9475

---

## Post #1 by @Jason_West (2019-12-11 21:59 UTC)

<p>Hi Everyone,<br>
I am currently attempting to edit a contour in the segmentation module but after the automatic conversion to a label map they appear very blocky (before and after images attached)<br>
Is there a way to edit just the planar contour points without doing this conversion?<br>
Thank you for your thoughts <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7a2325be101a82cc75c6717e41a68b52545e9c7.png" data-download-href="/uploads/short-url/x37NDf8H99F3s1BujVblmxHO76T.png?dl=1" title="contourBefore" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7a2325be101a82cc75c6717e41a68b52545e9c7_2_690x324.png" alt="contourBefore" data-base62-sha1="x37NDf8H99F3s1BujVblmxHO76T" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7a2325be101a82cc75c6717e41a68b52545e9c7_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7a2325be101a82cc75c6717e41a68b52545e9c7_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7a2325be101a82cc75c6717e41a68b52545e9c7.png 2x" data-dominant-color="5D525C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">contourBefore</span><span class="informations">1069×503 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-12-11 22:04 UTC)

<p>You can only edit binary labelmap representation, but you can oversample the labelmap so that you don’t lose any important details - see instructions here: <a href="https://discourse.slicer.org/t/surface-details-in-segmenting/4154/9" class="inline-onebox">Surface details in segmenting</a></p>

---

## Post #3 by @Jason_West (2019-12-13 13:32 UTC)

<p>Hello, Thank you for the tip, I am able to get decent results with an oversampling of 2 and even better with 3</p>
<p>The problem im having is this process takes a long time, this is a normal sized data set and with my 8th generation i7 processor running ubuntu the oversampling with a factor of 2 takes 45 secends and much longer with a 3.  I noticed all but one of the cores are idling during this.  Is there a configuration I could use to make Slicer utilize all the cores?<br>
Thanx!</p>

---

## Post #4 by @lassoan (2019-12-14 14:14 UTC)

<p>Algorithms that use one CPU core usually implemented so because it would not be easy to parallelize them. You can drastically reduce computation time if you don’t just resample but also crop your volume to the minimum necessary size.</p>

---
