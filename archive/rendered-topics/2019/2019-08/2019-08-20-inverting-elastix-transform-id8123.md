# Inverting Elastix transform

**Topic ID**: 8123
**Date**: 2019-08-20
**URL**: https://discourse.slicer.org/t/inverting-elastix-transform/8123

---

## Post #1 by @labixin (2019-08-20 03:38 UTC)

<p>Hi all,</p>
<p>I have some questions about the inverse of transformation.</p>
<p>Now I have contours in fixed volume and would like to get transformed one in moving volume. I first created linear transformation (moving2fixed, rigid+scale+affine) using General Registration (BRAINS). I clicked “Invert” button in “Edit” section, but found that only when the “Information” was “Transform from parent” did the inverse transform be correct. This was totally different from the transform created by elastix and also bspline transform in General (BRAINS) (“Transform to parent” be correct which I think is probably the right one?).</p>
<p>Besides, only when I ticked “Force grid output transform” square box in elastix “Advanced” section (I recently find it in nightly 4.11.0-2019-08-10) did the inverse transform be correct. If I did not click on the box then I got linear and b-spline registration results separately using “generic (all)” preset (shown in transform “Information” section). And the inverse transform also went wrong. The results are shown below.</p>
<p>I am not quite sure about the cause. Could you give some ideas? Thanks a lot!</p>
<p>Crayon</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a70f480640f66ff5472962ad60f29c5bc7e31723.png" alt="01" data-base62-sha1="nPStCgt0f4svO6b4oR0AojE57Bp" width="545" height="262"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a75e19ed6342a95a3b5e59f6b413c38265015db9.png" alt="02" data-base62-sha1="nSBlC6WD3Odx8ma7M3PbLMjPW41" width="410" height="403"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae4f4fdc59da75f6b33a6ec24ba361ef50e8fb17.png" alt="03" data-base62-sha1="oS10iZoZnuyOMI6zQQ3MFnx4caH" width="541" height="336"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c508605cafb3784ba92cd4540a2d0a545c772a7.png" alt="04" data-base62-sha1="42tTbhlbsAJJMD2uScLCma4wC2j" width="407" height="476"></p>

---

## Post #2 by @lassoan (2019-08-21 16:16 UTC)

<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="8123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>hen I ticked “Force grid output transform” square box in elastix “Advanced” section (I recently find it in nightly 4.11.0-2019-08-10) did the inverse transform be correct</p>
</blockquote>
</aside>
<p>Parsing Elastix transform files and retrieving native linear and bspline transform is a very new feature. Based on our testing so far, it works well, but there may be still issues with certain transforms. We have made a couple of fixes since August 10, so please try again with the latest Slicer preview version (or update your SlicerElastix extension in latest Slicer stable version).</p>
<p>By the way, why do you need the inverse transform manually? Slicer uses the forward/inverse transform as appropriate, depending on what nodes you need to transform (e.g., uses “from parent” transform for images and “to parent” for models and points).</p>

---

## Post #3 by @labixin (2019-08-22 02:01 UTC)

<p>Thank you for your efforts. This problem does not exist in the latest Slicer preview version (Slicer-4.11.0-2019-08-13-win-amd64 revision 28438).</p>
<p>Besides, I am sorry that I don’t quite understand your answer. I think “from parent” and “to parent” indicate the transform direction (“from parent” means from moving to fixed while “to parent” means from fixed to moving?), regardless of the nodes you need to transform (image, segment or point)?</p>
<p>For example, I have contours in fixed volume and would like to get transformed one in moving volume. Then only when the “Transform Information” was “Transform to parent” did the transform be correct (If not I need to manually click “Invert” button in “Edit” section).</p>
<p>I wonder if I have misused the function. Thanks a lot.</p>
<p>Crayon</p>

---

## Post #4 by @lassoan (2019-08-22 19:05 UTC)

<aside class="quote no-group" data-username="labixin" data-post="3" data-topic="8123">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>For example, I have contours in fixed volume and would like to get transformed one in moving volume. Then only when the “Transform Information” was “Transform to parent” did the transform be correct (If not I need to manually click “Invert” button in “Edit” section).</p>
</blockquote>
</aside>
<p>The registration module assumes that the <em>fixed image = parent</em> and <em>moving image = child</em> in the transform tree.</p>
<p>Therefore, if you have contours defined in the parent’s coordinate system and you need that in the child’s coordinate system then you need to invert the transform and apply it to the contour in the parent’s coordinate system.</p>
<p>Note that internally a transform can store “to parent” (and compute “from parent”) or store “from parent” (and compute “to parent”). Since computation of inverse can take magnitudes more time, usually image registration methods compute the “from parent”, because images require the “from parent” transform for resampling (points and meshes require “to parent” transform, as you don’t resample them but directly transform their point coordinates).</p>

---
