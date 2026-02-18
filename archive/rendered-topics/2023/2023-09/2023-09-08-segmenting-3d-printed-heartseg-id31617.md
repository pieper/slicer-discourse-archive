# Segmenting 3D printed heartseg

**Topic ID**: 31617
**Date**: 2023-09-08
**URL**: https://discourse.slicer.org/t/segmenting-3d-printed-heartseg/31617

---

## Post #1 by @Raha_Sep (2023-09-08 09:25 UTC)

<p>Hello Lassoan,</p>
<p>Is the threshold effect the best tool for segmentation of a 3D printed heart from CT scan images? below you see the segmentation using threshold. I want to produce .vtk or stl. file formats of the endocardial RA, LA, LV and RV from CT images.<br>
TotalSegmentator (<a href="https://github.com/lassoan/SlicerTotalSegmentator#totalsegmentator" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body segmentation in 3D Slicer using "TotalSegmentator" AI model</a>) didn’t work properly in this case.</p>
<p>Thanks for your help!<br>
Best<br>
Rahi<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/576b0cb92236daaf7b848b95344fffd3f4e1b6b0.jpeg" data-download-href="/uploads/short-url/ctkTm7Xq4CowAQBnHsZqPa9XYHu.jpeg?dl=1" title="heart" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/576b0cb92236daaf7b848b95344fffd3f4e1b6b0_2_527x500.jpeg" alt="heart" data-base62-sha1="ctkTm7Xq4CowAQBnHsZqPa9XYHu" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/576b0cb92236daaf7b848b95344fffd3f4e1b6b0_2_527x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/576b0cb92236daaf7b848b95344fffd3f4e1b6b0_2_790x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/576b0cb92236daaf7b848b95344fffd3f4e1b6b0_2_1054x1000.jpeg 2x" data-dominant-color="635E73"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">heart</span><span class="informations">1867×1768 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-09-08 13:17 UTC)

<p>TotalSegmentator segments real patient images, which look completely different than the scan of a 3D-printed object. In your 3D object scan, segmenting the “heart wall” is trivial, using thresholding. You can limit segmenting the ventricles inside the heart using <a href="https://discourse.slicer.org/t/fill-or-extract-cavities-in-segmentations-using-the-new-wrap-solidify-effect/11248/2">“Wrap Solidify” effect</a> (provided by SurfaceWrapSolidify extension), then <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">splitting the ventricles</a> using Scissors effect. Once you learned how to use the tools, the whole process should take just a couple of minutes.</p>

---

## Post #3 by @Raha_Sep (2023-09-12 15:10 UTC)

<p>Thanks very much <a class="mention" href="/u/lassoan">@lassoan</a>!<br>
By using the Threshold effect, I can extract the entire 3D heart model or as you said the “heart wall” but I still need to practice “Wrap Solidify”.</p>
<p>from this video <a href="https://www.youtube.com/watch?v=IWo-QlU4J_c" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=IWo-QlU4J_c</a> I understood nothing <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"> but I have this extension now and will try to apply it. p.s. It’s quite difficult for non-physicians to identify each organ correctly <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2023-09-12 15:21 UTC)

<aside class="quote no-group" data-username="Raha_Sep" data-post="3" data-topic="31617">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raha_sep/48/15684_2.png" class="avatar"> Raha_Sep:</div>
<blockquote>
<p>from this video <a href="https://www.youtube.com/watch?v=IWo-QlU4J_c">https://www.youtube.com/watch?v=IWo-QlU4J_c</a> I understood nothing</p>
</blockquote>
</aside>
<p>This is just a demo video that shows the end results. To fill a cavity you need to create a small seed segment inside the cavity you want to segment (it can be a small sphere that you create with a single click using the Paint effect), then choose the “heart wall” segment in the segment list at the top, and choose your “seed” segment as “Custom” region, then click “Apply”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c220a6e190394453e2f058edfb5384b2c5b6660a.jpeg" data-download-href="/uploads/short-url/rHkAj1UgcS7beBw9BFMYwl4YcFI.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c220a6e190394453e2f058edfb5384b2c5b6660a_2_690x499.jpeg" alt="image" data-base62-sha1="rHkAj1UgcS7beBw9BFMYwl4YcFI" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c220a6e190394453e2f058edfb5384b2c5b6660a_2_690x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c220a6e190394453e2f058edfb5384b2c5b6660a_2_1035x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c220a6e190394453e2f058edfb5384b2c5b6660a_2_1380x998.jpeg 2x" data-dominant-color="4D5055"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1390 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Result after clicking apply: the seed region is expanded to fill the cavity</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/687d21e558c9644534a0912a53d8602c86c5e450.jpeg" data-download-href="/uploads/short-url/eUlKCbBhpCFiaYNu4T0XMiGstk4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/687d21e558c9644534a0912a53d8602c86c5e450_2_395x500.jpeg" alt="image" data-base62-sha1="eUlKCbBhpCFiaYNu4T0XMiGstk4" width="395" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/687d21e558c9644534a0912a53d8602c86c5e450_2_395x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/687d21e558c9644534a0912a53d8602c86c5e450.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/687d21e558c9644534a0912a53d8602c86c5e450.jpeg 2x" data-dominant-color="788674"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">567×716 45.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
