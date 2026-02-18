# Odd appearance of model in slice view in projection mode

**Topic ID**: 13988
**Date**: 2020-10-11
**URL**: https://discourse.slicer.org/t/odd-appearance-of-model-in-slice-view-in-projection-mode/13988

---

## Post #1 by @riep (2020-10-11 18:10 UTC)

<p>Hi everyone,<br>
I have spotted a strange behavior of models with slice display in projection mode. (Slicer 11)<br>
If you look at the yellow slice scene you should not see the model as it is out of range. This is well displayed for other scenes.<br>
If I have time I will look into it  but people with more experience will solve to problem way faster than me.</p>
<p>Cheers,<br>
Pierre</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0858782e10fbb4611be0ff8a48108af7a2119ed.png" data-download-href="/uploads/short-url/w2d2oF3TrfWbMd6eYD9MaPLOy3H.png?dl=1" title="SceneView" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0858782e10fbb4611be0ff8a48108af7a2119ed_2_690x353.png" alt="SceneView" data-base62-sha1="w2d2oF3TrfWbMd6eYD9MaPLOy3H" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0858782e10fbb4611be0ff8a48108af7a2119ed_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0858782e10fbb4611be0ff8a48108af7a2119ed_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0858782e10fbb4611be0ff8a48108af7a2119ed.png 2x" data-dominant-color="5B7E70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView</span><span class="informations">1376×705 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-10-11 19:42 UTC)

<p>This looks correct. Simple “Projection” mode shows the model in the current slice:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fecbe72ea6a18be1312adfb4b8d413ff21456e3.jpeg" data-download-href="/uploads/short-url/4yq1qWttEBceRFvMFDSX3LiUagr.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1fecbe72ea6a18be1312adfb4b8d413ff21456e3_2_476x500.jpeg" alt="image" data-base62-sha1="4yq1qWttEBceRFvMFDSX3LiUagr" width="476" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1fecbe72ea6a18be1312adfb4b8d413ff21456e3_2_476x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1fecbe72ea6a18be1312adfb4b8d413ff21456e3_2_714x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1fecbe72ea6a18be1312adfb4b8d413ff21456e3_2_952x1000.jpeg 2x" data-dominant-color="4F5759"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1165×1222 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In most cases you want to use “Intersection” mode instead:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cec35fabef4b355c07200298155e8b019359168d.jpeg" data-download-href="/uploads/short-url/tv6WBeLWecWyU44wvspFY5rKgBT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cec35fabef4b355c07200298155e8b019359168d_2_477x500.jpeg" alt="image" data-base62-sha1="tv6WBeLWecWyU44wvspFY5rKgBT" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cec35fabef4b355c07200298155e8b019359168d_2_477x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cec35fabef4b355c07200298155e8b019359168d_2_715x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cec35fabef4b355c07200298155e8b019359168d_2_954x1000.jpeg 2x" data-dominant-color="494B53"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1166×1220 364 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In case you want to show the whole model or a thick slice of the model in the slice view then use “Distance encoded projection” mode:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cbd57ffd063cdd25a06c1fb0e4a384b63306656.jpeg" data-download-href="/uploads/short-url/aWRXcues3W5u7tptrAXbgfW2LL8.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cbd57ffd063cdd25a06c1fb0e4a384b63306656_2_477x500.jpeg" alt="image" data-base62-sha1="aWRXcues3W5u7tptrAXbgfW2LL8" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cbd57ffd063cdd25a06c1fb0e4a384b63306656_2_477x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cbd57ffd063cdd25a06c1fb0e4a384b63306656_2_715x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cbd57ffd063cdd25a06c1fb0e4a384b63306656_2_954x1000.jpeg 2x" data-dominant-color="4A3E5C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1165×1221 514 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You get a number of additional slice view display options if you convert the model to segmentation node.</p>

---

## Post #3 by @riep (2020-10-11 19:55 UTC)

<p>I see my bad,<br>
Your last point will answer my needs<br>
Thanks!</p>

---
