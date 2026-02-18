# A problem with USING SPHARM-PDM generator

**Topic ID**: 25668
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/a-problem-with-using-spharm-pdm-generator/25668

---

## Post #1 by @wael_telha (2022-10-13 08:01 UTC)

<p>the steps is the out of the DICOM i made a model that was saved as STL for the mandible as follow<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40ef3dac5b63dbff88d29fb47b83604fb471717b.jpeg" data-download-href="/uploads/short-url/9gr81oWj03sRAdBkYx0qt5x97wT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40ef3dac5b63dbff88d29fb47b83604fb471717b_2_690x388.jpeg" alt="image" data-base62-sha1="9gr81oWj03sRAdBkYx0qt5x97wT" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40ef3dac5b63dbff88d29fb47b83604fb471717b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40ef3dac5b63dbff88d29fb47b83604fb471717b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40ef3dac5b63dbff88d29fb47b83604fb471717b_2_1380x776.jpeg 2x" data-dominant-color="C9C9DC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 279 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>then i clipped a condyle and saved as a vtk for further work on SPHARM PDM-generator<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f9b4dd4f209afea9150f955aec93cc4d3ca2b16.png" data-download-href="/uploads/short-url/bmesmGX8ZWyM7K84aHPUX3jw26a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9b4dd4f209afea9150f955aec93cc4d3ca2b16_2_690x388.png" alt="image" data-base62-sha1="bmesmGX8ZWyM7K84aHPUX3jw26a" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9b4dd4f209afea9150f955aec93cc4d3ca2b16_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9b4dd4f209afea9150f955aec93cc4d3ca2b16_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f9b4dd4f209afea9150f955aec93cc4d3ca2b16_2_1380x776.png 2x" data-dominant-color="CACAE0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>when i took this saved VTK to the slicer SALT for further SPHARM PDM-generator  i always ended with an error<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8182f20448e7cfcf8a4cdb3f4d20b2c600d065ad.jpeg" data-download-href="/uploads/short-url/itI8Rb0m7F7bSXMAhIsUcWrlB9z.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8182f20448e7cfcf8a4cdb3f4d20b2c600d065ad_2_690x388.jpeg" alt="image" data-base62-sha1="itI8Rb0m7F7bSXMAhIsUcWrlB9z" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8182f20448e7cfcf8a4cdb3f4d20b2c600d065ad_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8182f20448e7cfcf8a4cdb3f4d20b2c600d065ad_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8182f20448e7cfcf8a4cdb3f4d20b2c600d065ad_2_1380x776.jpeg 2x" data-dominant-color="D2DBE8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 257 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @SAO (2022-11-05 06:10 UTC)

<p>Hi <a class="mention" href="/u/wael_telha">@wael_telha</a></p>
<p>I think SPHARM-PDM will only accept VTK file of models (with no gaps). For consistency between the models, and to make sure there is no gaps in the models, you can use data-importer module (in SlicerSALT). <strong><strong>This module should be helpful for checking the models, before running SPHARM-PDM</strong>.</strong></p>
<p>N.B.:<br>
After trimming the condyle, the model will have a gap (that need to be covered before exporting to SlicerSALT). <strong>In 3D slicer, you need to cover the exposed-region of the models (so the model does not have any gap).</strong></p>
<p>I hope this be helpful.</p>
<p>Regards,<br>
Sultan</p>

---

## Post #4 by @wael_telha (2022-11-14 13:13 UTC)

<p>I am really grateful to you<br>
thanks a million the problem was solved accordingly and things went then too smooth</p>

---

## Post #5 by @SAO (2022-11-14 14:51 UTC)

<p>I am glad that the problem was solved.<br>
All the best <a class="mention" href="/u/wael_telha">@wael_telha</a></p>

---
