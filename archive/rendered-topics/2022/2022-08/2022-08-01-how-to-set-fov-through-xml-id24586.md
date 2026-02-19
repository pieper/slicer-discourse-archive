---
topic_id: 24586
title: "How To Set Fov Through Xml"
date: 2022-08-01
url: https://discourse.slicer.org/t/24586
---

# How to set FOV through XML

**Topic ID**: 24586
**Date**: 2022-08-01
**URL**: https://discourse.slicer.org/t/how-to-set-fov-through-xml/24586

---

## Post #1 by @michabermoy (2022-08-01 02:58 UTC)

<p>I have written code that generates a customized tabbed layout based on the number of segments as shown below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9f4e6e0cbf9a64a3260b9f1fbb5e368dde762f7.png" data-download-href="/uploads/short-url/sOAFCPsetjE9loZYvhnLcOYQs8T.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9f4e6e0cbf9a64a3260b9f1fbb5e368dde762f7.png" alt="image" data-base62-sha1="sOAFCPsetjE9loZYvhnLcOYQs8T" width="432" height="500" data-dominant-color="65657C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">545×630 9.85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f39ff21aa218220d50b7a2e06caee54ca765217.png" data-download-href="/uploads/short-url/i9uTxRkWN8ivLXyxWzjpnGzq1b9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f39ff21aa218220d50b7a2e06caee54ca765217_2_432x500.png" alt="image" data-base62-sha1="i9uTxRkWN8ivLXyxWzjpnGzq1b9" width="432" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f39ff21aa218220d50b7a2e06caee54ca765217_2_432x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f39ff21aa218220d50b7a2e06caee54ca765217.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f39ff21aa218220d50b7a2e06caee54ca765217.png 2x" data-dominant-color="303035"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">547×633 44.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, the field of view for the Red (Axial), Green (Coronal), and Yellow (Sagittal) view windows is not centered and zoomed in so that you can see the volume and its segments. As you can see from the images attached, none of the segments are visible in any of the slice windows. Is there a way to fix this issue so that whenever I generate the customized view, the segments are centered on each window like so:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06173fcfa49c5e1291c73a75196794297556cb7e.png" data-download-href="/uploads/short-url/RSFV4oIb2Ee9mSRRDL28ZZycOi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06173fcfa49c5e1291c73a75196794297556cb7e_2_427x500.png" alt="image" data-base62-sha1="RSFV4oIb2Ee9mSRRDL28ZZycOi" width="427" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06173fcfa49c5e1291c73a75196794297556cb7e_2_427x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06173fcfa49c5e1291c73a75196794297556cb7e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06173fcfa49c5e1291c73a75196794297556cb7e.png 2x" data-dominant-color="363639"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">544×637 90.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jay1987 (2022-08-01 05:24 UTC)

<p>it can be done with python or C++ code,i don’t known how to do through XML</p>

---

## Post #3 by @michabermoy (2022-08-01 12:16 UTC)

<p>How would you do it through python? My code is a mix of python and some XML.</p>

---

## Post #4 by @jay1987 (2022-08-01 12:36 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c344f08df0cece90f0a8b6fb21b2794311387ff0.png" alt="image" data-base62-sha1="rRqOaUzp5zGWKcl4CEyWUi2DfFu" width="623" height="161"></p>
<p>try these codes</p>

---
