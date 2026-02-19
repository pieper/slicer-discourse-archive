---
topic_id: 31502
title: "Monailabel And Slicer Segmentation Label Number"
date: 2023-09-01
url: https://discourse.slicer.org/t/31502
---

# Monailabel and slicer segmentation label number

**Topic ID**: 31502
**Date**: 2023-09-01
**URL**: https://discourse.slicer.org/t/monailabel-and-slicer-segmentation-label-number/31502

---

## Post #1 by @Ylim (2023-09-01 10:17 UTC)

<p>Hi all, sorry if this is a rather trivial question.<br>
I have slicer and monailabel. Found the label number to be very confusing.</p>
<p>Within \monilabel\apps\radiology\main.py<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5481faed8ec99ff1adf47a204f4a77dad698f55b.png" data-download-href="/uploads/short-url/c3AAvhTu7IfeHSDbqWQypljZsNB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5481faed8ec99ff1adf47a204f4a77dad698f55b_2_345x500.png" alt="image" data-base62-sha1="c3AAvhTu7IfeHSDbqWQypljZsNB" width="345" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5481faed8ec99ff1adf47a204f4a77dad698f55b_2_345x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5481faed8ec99ff1adf47a204f4a77dad698f55b_2_517x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5481faed8ec99ff1adf47a204f4a77dad698f55b.png 2x" data-dominant-color="F9F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">667×966 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Within slicer’s segmentation<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68c324c15bd11a7fb3f411f25321fa8fa2e2e32d.png" alt="image" data-base62-sha1="eWLKvpVPUBFcO6r5LGv8TosvIJf" width="618" height="294"></p>
<p>I have the impression that the main.py sets the label value/number but they do not agree or reads similar.<br>
Please advise.</p>

---

## Post #2 by @rbumm (2023-09-02 01:58 UTC)

<p>Just make sure you use consistent label numbering throughout your project and that you remove all labels that you won’t need.</p>

---

## Post #3 by @Ylim (2023-09-02 12:28 UTC)

<p>Thanks. Resolved, a very trivial issue.</p>

---
