# How to keep continuity when surface smoothing

**Topic ID**: 16598
**Date**: 2021-03-17
**URL**: https://discourse.slicer.org/t/how-to-keep-continuity-when-surface-smoothing/16598

---

## Post #1 by @xiang_luo (2021-03-17 15:52 UTC)

<p>When i smooth the pulmonary artery, i find that the vessel continuity had beed destoryed sharply. Like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ed9a9e1f641e4218f3f35719be08e232f6c26a5.png" alt="smooth" data-base62-sha1="fOCRyIxxHzd2U68XGGw1aypVifP" width="480" height="158"><br>
Also i find this happend in Mimics when i set the prefer to accuracy, while the default value is continuity, which make no continutity destoryed. How can i do this in Slicer? Any simple way to change the quality for smoothing?</p>

---

## Post #2 by @xiang_luo (2021-03-18 06:55 UTC)

<p>Sorry, I forget add some instructions. Here is the different 3D Reconstruction in Mimics with two option.<br>
Reconstruction options:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5b1ed6e677ddf46f5ff154b71e122b898f53aa1.jpeg" data-download-href="/uploads/short-url/wLYy0HGgz5JeVHLLMmFtvqwU25z.jpeg?dl=1" title="options" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5b1ed6e677ddf46f5ff154b71e122b898f53aa1_2_549x500.jpeg" alt="options" data-base62-sha1="wLYy0HGgz5JeVHLLMmFtvqwU25z" width="549" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5b1ed6e677ddf46f5ff154b71e122b898f53aa1_2_549x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5b1ed6e677ddf46f5ff154b71e122b898f53aa1_2_823x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5b1ed6e677ddf46f5ff154b71e122b898f53aa1.jpeg 2x" data-dominant-color="E7E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">options</span><span class="informations">1044×950 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Option: accuracy<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db0ba0d52de4927da9ad8bf9b2075cc0a8f6ffcb.png" data-download-href="/uploads/short-url/vfLtIZddZO4rWNTXthClDoIFmQz.png?dl=1" title="mimics_accuracy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db0ba0d52de4927da9ad8bf9b2075cc0a8f6ffcb_2_425x500.png" alt="mimics_accuracy" data-base62-sha1="vfLtIZddZO4rWNTXthClDoIFmQz" width="425" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db0ba0d52de4927da9ad8bf9b2075cc0a8f6ffcb_2_425x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db0ba0d52de4927da9ad8bf9b2075cc0a8f6ffcb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db0ba0d52de4927da9ad8bf9b2075cc0a8f6ffcb.png 2x" data-dominant-color="EFF5ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mimics_accuracy</span><span class="informations">476×560 62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Option: continutiy<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f1d78b8594a2a716db52ec8b97ffd5ca77f9f67.png" data-download-href="/uploads/short-url/90ldPROUMi1UoyOc4BBUE7CrXbF.png?dl=1" title="mimics_continuity" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f1d78b8594a2a716db52ec8b97ffd5ca77f9f67_2_425x500.png" alt="mimics_continuity" data-base62-sha1="90ldPROUMi1UoyOc4BBUE7CrXbF" width="425" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f1d78b8594a2a716db52ec8b97ffd5ca77f9f67_2_425x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f1d78b8594a2a716db52ec8b97ffd5ca77f9f67.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f1d78b8594a2a716db52ec8b97ffd5ca77f9f67.png 2x" data-dominant-color="EAF2E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mimics_continuity</span><span class="informations">476×560 77.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @xiang_luo (2021-03-22 12:19 UTC)

<p>Can you help me with this? <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #4 by @xiang_luo (2021-03-24 11:26 UTC)

<p>I have tried the source code about smoothing label in Slicer Preview, but it doesn’t work while the speed is faster.</p>

---

## Post #5 by @lassoan (2021-03-24 15:42 UTC)

<p>I’ve searched on the web about what Mimics means by Continuity vs Accuracy and found the description <a href="https://www.researchgate.net/profile/Yousof-Mohandes/post/can_anyone_suggest_me_any_appropriate_resources_for_Learning_MIMICS_and_3Matic/attachment/59d635f579197b80779936d1/AS%3A386294325760004%401469111153225/download/Mimics+Research+17.0+Reference+Guide.pdf">here</a>. In short, these parameters control “matrix reduction” i.e., image downsampling. I would not recommend to use “continuity” mode ever.</p>
<p>In Slicer, the simplest, most transparent way of adjusting sampling distance is in Crop volume module. You can choose the spacing scale value to upsample (scale&lt;1.0) or downsample (scale&gt;1.0) and force isotropic spacing. In general, I would recommend to force isotropic spacing because many image processing operations work better if voxels are approximately cubic shape. Downsampling should be avoided, as it may remove relevant details and make measurements less accurate. If there are small details that you cannot represent at the native image resolution then you can fix the problem by upsampling the image. Upsampling can increase memory need and computation time by magnitudes, therefore it often makes sense to combine it with cropping the image to minimum size (that’s why all these features are implemented in one module).</p>
<p>With a croppping and resampling the module with a isotropic spacing and well-chosen scaling factor the vasculature will look perfect. You can also adjust smoothing factor to fine-tune appearance. If you prefer to optimize for visual appearance rather than accuracy then you can also apply Smoothing or Margin effects in Segment Editor to make the vessels thicker.</p>
<aside class="quote no-group" data-username="xiang_luo" data-post="4" data-topic="16598" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xiang_luo/48/9305_2.png" class="avatar"> xiang_luo:</div>
<blockquote>
<p>I have tried the source code about smoothing label in Slicer Preview, but it doesn’t work while the speed is faster.</p>
</blockquote>
</aside>
<p>Which module or feature do you mean exactly?</p>

---

## Post #6 by @xiang_luo (2021-03-25 02:40 UTC)

<p>Exactly, i have tried code in <a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/LabelMapSmoothing/LabelMapSmoothing.cxx" class="inline-onebox" rel="noopener nofollow ugc">Slicer/LabelMapSmoothing.cxx at master · Slicer/Slicer · GitHub</a> and <a href="https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Libs/vtkSegmentationCore/vtkClosedSurfaceToBinaryLabelmapConversionRule.cxx" class="inline-onebox" rel="noopener nofollow ugc">Slicer/vtkClosedSurfaceToBinaryLabelmapConversionRule.cxx at 08789e8f2224f89206b2d6a49d1d452d4e677994 · Slicer/Slicer · GitHub</a></p>

---

## Post #7 by @xiang_luo (2021-03-25 02:53 UTC)

<p>I have read the Mimics documentions <a href="https://www.researchgate.net/profile/Yousof-Mohandes/post/can_anyone_suggest_me_any_appropriate_resources_for_Learning_MIMICS_and_3Matic/attachment/59d635f579197b80779936d1/AS%3A386294325760004%401469111153225/download/Mimics+Research+17.0+Reference+Guide.pdf" rel="noopener nofollow ugc">here</a>, i mentioned the “contour interpolation” and the “matrix reduction algorithm”, i want to know if there exist simility algrithm or function in Sliver or VTK to implement this, any demo?</p>

---

## Post #8 by @lassoan (2021-07-18 03:00 UTC)

<p>“Contour interpolation” in Mimics → “Fill between slices” segment editor effect in Slicer.<br>
“Matrix reduction algorithm” in Mimics → “Crop volume” and “Resample scalar/vector/dwi volume” module in Slicer.</p>

---
