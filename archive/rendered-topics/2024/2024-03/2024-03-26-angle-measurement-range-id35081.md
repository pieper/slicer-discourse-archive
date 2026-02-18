# Angle measurement range

**Topic ID**: 35081
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/angle-measurement-range/35081

---

## Post #1 by @learn_shape (2024-03-26 00:17 UTC)

<p>Hello, the calculated values for both angles here are 0-90 degrees. Is there a way to change the range of values to 0-180 degrees in 3d?</p>

---

## Post #2 by @muratmaga (2024-03-26 04:03 UTC)

<p>Not entirely sure what you mean. You can have angles &gt;90 degrees…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a73eb2cb90d5f7f016c2dabc273f1608fbf19d8.png" data-download-href="/uploads/short-url/3M0LFfHW7P9zJ0N4cJM46WI8U0U.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a73eb2cb90d5f7f016c2dabc273f1608fbf19d8_2_690x315.png" alt="image" data-base62-sha1="3M0LFfHW7P9zJ0N4cJM46WI8U0U" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a73eb2cb90d5f7f016c2dabc273f1608fbf19d8_2_690x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a73eb2cb90d5f7f016c2dabc273f1608fbf19d8_2_1035x472.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a73eb2cb90d5f7f016c2dabc273f1608fbf19d8_2_1380x630.png 2x" data-dominant-color="9695CD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1552×710 53.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2024-03-26 04:48 UTC)

<p>I split the topic because I interpreted the same way it as you <a class="mention" href="/u/muratmaga">@muratmaga</a> but I’ve read it again and realized that maybe <a class="mention" href="/u/learn_shape">@learn_shape</a> refers to the C-arm angles?</p>
<p>Those <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.7.5.html#sect_C.8.7.5.1.2">angles are defined in DICOM</a>. The primary positioner angle is indeed allowed to be in the +/-180deg range, while the secondary angle is always between +/-90deg. You can get the +/-180deg range if you switch to use atan2 in the <a href="https://discourse.slicer.org/t/get-c-arm-angles-from-3d-view-orientation/24435/3">script</a>. The end result will be something like this:</p>
<pre data-code-wrap="python"><code class="lang-python">    nx = viewNormal[0]  # R
    ny = viewNormal[1]  # A
    nz = viewNormal[2]  # S
    import math
    if abs(ny) &gt; 1e-6:
      primaryAngleDeg = math.atan2(nx, -ny) * 180.0 / math.pi
    elif nx &gt;= 0:
      primaryAngleDeg = 90.0
    else:
      primaryAngleDeg = -90.0
    secondaryAngleDeg = math.asin(nz) * 180.0 / math.pi
    return [primaryAngleDeg, secondaryAngleDeg]
</code></pre>

---

## Post #9 by @lassoan (2024-03-27 11:39 UTC)

<p>In the image above the patient coordinate system is left-handed. In DICOM, patient coordinate system is right-handed (LPS). Therefore, it is quite likely thay you have fed wrong input to the code snippet.</p>

---

## Post #10 by @learn_shape (2024-03-27 12:12 UTC)

<p>sorry,i am a student. your code can match the body position(A P L R H F)？for example ，when body position A, lao/rao is 0 degree, and cra/cau is 0 degree</p>

---

## Post #11 by @lassoan (2024-03-27 13:13 UTC)

<aside class="quote no-group" data-username="learn_shape" data-post="10" data-topic="35081">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/35a633/48.png" class="avatar"> learn_shape:</div>
<blockquote>
<p>your code can match the body position(A P L R H F)？</p>
</blockquote>
</aside>
<p>DICOM names for patient coordinate system axis directions are anterior, posterior, left, right, superior, inferior.</p>
<aside class="quote no-group" data-username="learn_shape" data-post="10" data-topic="35081">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/35a633/48.png" class="avatar"> learn_shape:</div>
<blockquote>
<p>when body position A, lao/rao is 0 degree, and cra/cau is 0 degree</p>
</blockquote>
</aside>
<p>Patient position is generally assumed to be head-first-supine on the C-arm table.<br>
Primary and secondary positioner angles refer to the viewing direction (orientation of the C-arm).</p>

---

## Post #12 by @learn_shape (2024-03-28 06:29 UTC)

<p>but in fact the secondaryAngleDeg is allowed to be +/-180. in C arm. I wanted to modify your code to achieve an angle above 90 degrees, but it failed.</p>

---

## Post #13 by @lassoan (2024-03-28 11:43 UTC)

<p>Secondary positioner angle field cannot go beyond +/-90 degrees. See the <a href="https://dicom.innolitics.com/ciods/x-ray-angiographic-image/xa-positioner/00181511">DICOM standard</a>.</p>

---
