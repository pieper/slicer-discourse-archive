---
topic_id: 17965
title: "About The Angle Threshold For Dti"
date: 2021-06-05
url: https://discourse.slicer.org/t/17965
---

# About the angle threshold for DTI?

**Topic ID**: 17965
**Date**: 2021-06-05
**URL**: https://discourse.slicer.org/t/about-the-angle-threshold-for-dti/17965

---

## Post #1 by @timeanddoctor (2021-06-05 13:40 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5263f49d1fca3d2bbf27b2b3eb597d219764d36.png" alt="image" data-base62-sha1="s840mWKIfDkaYj41LU39WPWwpPU" width="551" height="120"><br>
Just as the pic, Can I set the angel in slicer?</p>

---

## Post #2 by @pieper (2021-06-08 20:15 UTC)

<p>Slicer uses Radius of Curvature to control that parameter.  Perhaps <a class="mention" href="/u/ljod">@ljod</a> knows the exact mapping to angle, but I believe it’s <code>arcsin</code>, so .5 radius curvature would be 30 degrees.</p>

---
