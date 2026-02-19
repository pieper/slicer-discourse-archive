---
topic_id: 44644
title: "Non Orthogonal Ijk To Ras Direction Matrix"
date: 2025-10-01
url: https://discourse.slicer.org/t/44644
---

# Non-orthogonal IJK to RAS Direction Matrix

**Topic ID**: 44644
**Date**: 2025-10-01
**URL**: https://discourse.slicer.org/t/non-orthogonal-ijk-to-ras-direction-matrix/44644

---

## Post #1 by @mwirtz (2025-10-01 15:39 UTC)

<p>Hey there!<br>
I am trying to load CT scans via the DICOM module, which have a non-zero GantryDetectorTilt (not 100% sure it is related) and it seems to cause a non-orthogonal IJK to RAS matrix (see screenshot). Also the case appear “skewed”, i.e. with a shearing angle, in 3D Slicer (see screenshot).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8.jpeg" data-download-href="/uploads/short-url/hEltERRYSQCzAJTM0nNp4hkkZZe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8_2_690x230.jpeg" alt="image" data-base62-sha1="hEltERRYSQCzAJTM0nNp4hkkZZe" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8_2_690x230.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8_2_1035x345.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bb48396f2e74f01fba018c8fcac4e50412ac8c8_2_1380x460.jpeg 2x" data-dominant-color="464646"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2152×718 273 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For this case, the ImageOrientationPatient in the DICOM file is:<br>
<code>(0020,0037) DS [1\0\0\0\0.99357185567659-0.1132032137679] #  42, 6 ImageOrientationPatient</code></p>
<p>I would’ve expected that 3DSlicer complements the perpendicular axis by the cross product, which would lead to an IJK to RAS Direction Matrix of e.g.:<br>
```<br>
<code>[-1, 0, 0]</code><br>
<code>[0 -0.9936, -0.1132]</code><br>
<code>[0, -0.1132, 0.9936]</code><br>
```<br>
I already played a bit around with the settings in Edit→Settings→DICOM (acquisition geometry reularization) but could not make it orthogonal.</p>
<p>Any ideas?</p>

---

## Post #2 by @pieper (2025-10-01 16:08 UTC)

<p>That should be handled directly with the acquisition transform when you load from DICOM.  Did you try hardening the volume through the transform?</p>

---

## Post #3 by @pieper (2025-10-01 16:13 UTC)

<p>Also this looks suspicious - there should be only numbers and backslashes in this value.</p>
<aside class="quote no-group" data-username="mwirtz" data-post="1" data-topic="44644">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/3da27b/48.png" class="avatar"> mwirtz:</div>
<blockquote>
<p>(0020,0037) DS [1\0\0\0\0.99357185567659-0.1132032137679] # 42, 6</p>
</blockquote>
</aside>
<p>Was this data processed by some other software or did it come straight from a scanner?</p>

---

## Post #4 by @mwirtz (2025-10-01 18:35 UTC)

<p>Yes, I tried the option <code>harden regularization transform</code> without success.</p>
<p>Sorry, the DICOM tag was copied from a DICOM visualization software, no clue why a backslash got lost… Accessing the tag directly via <code>pydicom.dcmread()</code> shows no apparent issue though - as far as I can see:</p>
<pre><code class="lang-auto">Python 3.12.10 (main, Apr  9 2025, 04:03:51) [Clang 20.1.0 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import pydicom
&gt;&gt;&gt; pydicom.dcmread("ffc7e0e2fe27516c387ca0e908a40b25.dcm").ImageOrientationPatient
[1, 0, 0, 0, 0.99357185567659, -0.1132032137679]
</code></pre>

---

## Post #5 by @pieper (2025-10-01 18:53 UTC)

<p>Can you answer this question and provide any other context?</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="44644">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Was this data processed by some other software or did it come straight from a scanner?</p>
</blockquote>
</aside>
<p>I ask because I’m surprised the acquisition transform didn’t work since it relies on the per-slice position and orientation data from the dicom header.  Is the scan perhaps a multiframe image? (all slices are in one file?)</p>

---

## Post #6 by @lassoan (2025-10-02 21:19 UTC)

<p>Loading of tilted-gantry images should work well. There must be something unusual in your image that prevents this mechanism to work. Is the file stored in enhanced multiframe format (single file for the entire 3D stack)? Could you copy all messages related to acquisition normalization that are logged when you load the image (you can access the logs in menu: Help → Report a bug).</p>

---
