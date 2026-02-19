---
topic_id: 431
title: "Image With Hardened Transform Returns To Original When Opene"
date: 2017-06-02
url: https://discourse.slicer.org/t/431
---

# Image with hardened transform returns to original when opened outside Slicer

**Topic ID**: 431
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/image-with-hardened-transform-returns-to-original-when-opened-outside-slicer/431

---

## Post #1 by @jrobin (2017-06-02 19:16 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.6.2<br>
Expected behaviour: After hardening transform, saved image volume will preserve transformed state when opened outside Slicer<br>
Actual behaviour: Image returns to original (un-transformed) orientation when opened outside Slicer</p>
<p>Hello,</p>
<p>I am trying to perform a simple rotation transformation to a .mha volume and then save the transformed result to be available outside of Slicer; however, when I open the saved result outside of Slicer, the image returns to its original orientation.</p>
<p>I have hardened the transform before saving and I have also tried using “Resample Scalar Volume” on the transformed image but it both cases the image returns to its original orientation when opened in a variety of programs (ex. VolView, MATLAB,…) outside of Slicer. It should be noted that when the saved volumes are re-opened in Slicer, the transform is applied. Additionally, the transform does appear in the .mha TransformMatrix header field.</p>
<p>I also tried exporting the transformed/resampled images as DICOM series, in case it was an incompatibility with the .mha format but this had the same un-transformed result outside of Slicer. I also tried all options with the “Ignore Orientation” option selected and deselected on data import (suggestion found from a similar question from 2012 online: <a href="http://slicer-users.65878.n3.nabble.com/Non-warping-fiducial-transform-not-present-in-saved-volume-td4025526.html" rel="noopener nofollow ugc">http://slicer-users.65878.n3.nabble.com/Non-warping-fiducial-transform-not-present-in-saved-volume-td4025526.html</a>).</p>
<p>I appreciate any help you can offer and thank you!</p>
<p>Sincerely,<br>
Jessica</p>
<p>Summary of approaches tried:<br>
Hardening transform and saving as .mha and DICOM<br>
Resampling transformed image and saving as .mha and DICOM<br>
Import data with/without “Ignore Orientation” option selected and repeating 2 items above</p>

---

## Post #2 by @pieper (2017-06-02 19:57 UTC)

<p>Hi Jessica -</p>
<p>If the external program (e.g. matlab) is ignoring the transformmatrix field of the metaheader then what you are seeing is expected behavior for the harden step.</p>
<p>Instead of Resample Scalar Volume, which only changes the pixel data, you can use Resample Image (BRAINS) which allows you to set the input image, the transform, and a reference image that defines the output pixel grid that you want.  Then the pixel matrix should work in matlab.</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #3 by @jrobin (2017-06-02 20:27 UTC)

<p>Thanks so much, Steve! This solved the problem for me!</p>
<p>P.S. Do you know why this one is called BRAINS!? (Doesn’t seem like an intuitive place to look!)</p>
<p>Thank you!<br>
Jessica</p>

---

## Post #4 by @pieper (2017-06-02 21:09 UTC)

<aside class="quote no-group" data-username="jrobin" data-post="3" data-topic="431">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jrobin/48/663_2.png" class="avatar"> jrobin:</div>
<blockquote>
<p>P.S. Do you know why this one is called BRAINS!? (Doesn’t seem like an intuitive place to look!)</p>
</blockquote>
</aside>
<p>Good point - the <a href="https://github.com/BRAINSia">BRAINSTools</a> are provided by our colleagues so we keep the name, but I can see how it’s confusing!</p>

---

## Post #5 by @lassoan (2017-06-03 18:01 UTC)

<p>I found it very confusing, too. The project indeed started off as a collection of tools for brain images, but over time it has become a generic toolkit. The name was kept for preserving “brand” identity.</p>

---
