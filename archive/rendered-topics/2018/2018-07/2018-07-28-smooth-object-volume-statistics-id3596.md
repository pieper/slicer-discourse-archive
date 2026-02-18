# Smooth Object volume statistics 

**Topic ID**: 3596
**Date**: 2018-07-28
**URL**: https://discourse.slicer.org/t/smooth-object-volume-statistics/3596

---

## Post #1 by @F_Karl (2018-07-28 01:42 UTC)

<p>Hi there,</p>
<p>with the help of this forum I have made my first steps through the software and so far it’s been wonderful. As a background - I am using the software to make 3D measurements of brain tumors from MRI for my thesis.</p>
<p>For this I use the Segment Editor and Threshold painting, which works great for me. My problem is that my objects are around 1-2 cm3 max and the images I have are not that many pixels. Therefore I end up with a very “unnatural looking” segment because of the pixels.</p>
<p>I found a function in the software (Model Maker) where I can follow the same process, but in the end - after the threshold + painting - can make a model, where the surface is smoothed out via Laplacian. It then renders into a 3D object that appears to be a fairly realistic depiction of a tumor.</p>
<p>Is there any possibility to use this smoothed out object for the Segment Statistics (i.e. to get the volume of the smooth object). I think it is just a simple thing probably, but I cannot seem to figure it out. The segmentations always end up being just the pixels and I cannot use the smooth object (“model”) for the volume statistics.</p>
<p>Any tip/help is much appreciated. Thanks very much in advance!<br>
Florian</p>

---

## Post #2 by @lassoan (2018-07-28 16:32 UTC)

<aside class="quote no-group" data-username="F_Karl" data-post="1" data-topic="3596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/f19dbf/48.png" class="avatar"> F_Karl:</div>
<blockquote>
<p>My problem is that my objects are around 1-2 cm3 max and the images I have are not that many pixels. Therefore I end up with a very “unnatural looking” segment because of the pixels.</p>
</blockquote>
</aside>
<p>Probably your MRI has low and/or highly anisotropic spacing. In this case, it is better to make the segmentation higher resolution than the input volume. You may crop and resample the MRI before segmentation using “Crop and resample” module (select isotropic spacing and use spacing scale 0.3 or 0.5). Alternatively, in recent nightly builds there is an even better way of addressing this:</p>
<ol>
<li>Click “specify geometry” button in Segment editor module</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e441f8d6b6a06453ddb0a9e465f8ba0dd0631e84.png" data-download-href="/uploads/short-url/wzgcSjbY8MUp6yWGKgecdplDxUU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e441f8d6b6a06453ddb0a9e465f8ba0dd0631e84_2_689x438.png" alt="image" data-base62-sha1="wzgcSjbY8MUp6yWGKgecdplDxUU" width="689" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e441f8d6b6a06453ddb0a9e465f8ba0dd0631e84_2_689x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e441f8d6b6a06453ddb0a9e465f8ba0dd0631e84_2_1033x657.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e441f8d6b6a06453ddb0a9e465f8ba0dd0631e84.png 2x" data-dominant-color="D5D3D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1283×816 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>In the displayed popup, select your input volume, oversampling factor (higher value means the segmentation will have finer resolution; value of 2 to 3 is typically enough), check “isotropic” option, and click OK.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a15f70fefc420d7e444725260b525c56c63b229.png" data-download-href="/uploads/short-url/1rdPKx5whNxw4Jxru6D5BxcC6k9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a15f70fefc420d7e444725260b525c56c63b229.png" alt="image" data-base62-sha1="1rdPKx5whNxw4Jxru6D5BxcC6k9" width="665" height="500" data-dominant-color="F7F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">908×682 28.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After this, you can have much finer (less blocky) segmentation.</p>
<hr>
<aside class="quote no-group" data-username="F_Karl" data-post="1" data-topic="3596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/f19dbf/48.png" class="avatar"> F_Karl:</div>
<blockquote>
<p>I found a function in the software (Model Maker) where I can follow the same process,</p>
</blockquote>
</aside>
<p>Segmentation infrastructure includes making of 3D representation and models. I would recommend not to use Model Maker for converting segmentations.</p>
<aside class="quote no-group" data-username="F_Karl" data-post="1" data-topic="3596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/f19dbf/48.png" class="avatar"> F_Karl:</div>
<blockquote>
<p>Is there any possibility to use this smoothed out object for the Segment Statistics</p>
</blockquote>
</aside>
<p>“Segment statistics” module can already compute volume from 3D model. Just click “Show 3D” button in Segment editor before you compute statistics.</p>

---

## Post #3 by @F_Karl (2018-08-21 20:52 UTC)

<p>Thank you so much! This really helped me!</p>

---
