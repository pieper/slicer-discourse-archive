# Low resolution when importing an STL segmentation

**Topic ID**: 37715
**Date**: 2024-08-05
**URL**: https://discourse.slicer.org/t/low-resolution-when-importing-an-stl-segmentation/37715

---

## Post #1 by @ludoludo (2024-08-05 20:35 UTC)

<p>Hey!</p>
<p>I have a Nifti volume with the following dimensions: 588 x 734 x 1095, with an isometric resolution of 0.033 mm.</p>
<p>I’ve got an STL (or OBJ) file that represents a segmentation I’ve already made.</p>
<p>I’d like to convert this segmentation into a binary map that I can edit at high resolution: image spacing ~ 0.01.</p>
<p>The problem is that when I import this file and convert it directly, I end up with a very pixelated mask even at this resolution.</p>
<p>I’ve tried different approaches as indicated on the forum:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough</a></p><aside class="quote" data-post="1" data-topic="1394">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andfor/48/822_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-resolution/1394/">Segmentation resolution</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello 
Can I select the pixel resolution of my segmentation? 
is it the same as native image resolution? 
thanks
  </blockquote>
</aside>
<aside class="quote" data-post="1" data-topic="22981">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/5fc32e/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-increase-the-segmentation-resolution/22981">How to increase the segmentation resolution?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everybody, 
How can I increase the resolution of the segmentation as the default one uses large size of voxels (cubes)? 
Is this called oversampling? how to do it without changing the volume as I need to calculate the volume afterwards? 
Thanks,
  </blockquote>
</aside>
<aside class="quote" data-post="1" data-topic="15939">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/increasing-segmentation-resolution/15939">Increasing segmentation resolution</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello all, 
How can I increase the resolution of a current segmentation? 
The master volume has its own quality and we cannot increase it but I want a segmentation with higher quality. I tried to crop the master volume with the spacing scale of 0.5 and with both linear and B-spline interpolators. However, it seems not to be working. Is this the correct way of doing what I am looking for or there other ways too? 
Thanks in advance.
  </blockquote>
</aside>

<p>I tested several versions by increasing the dimensions of the STL/OBJ file, but it doesn’t change anything <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>
<p>Here are a few images:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/916eaf29ac8327928a0cb89345023e940dd3d170.png" data-download-href="/uploads/short-url/kKyn88eleHFaLziYK9A60rqcaqs.png?dl=1" title="Before import" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/916eaf29ac8327928a0cb89345023e940dd3d170_2_690x415.png" alt="Before import" data-base62-sha1="kKyn88eleHFaLziYK9A60rqcaqs" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/916eaf29ac8327928a0cb89345023e940dd3d170_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/916eaf29ac8327928a0cb89345023e940dd3d170_2_1035x622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/916eaf29ac8327928a0cb89345023e940dd3d170_2_1380x830.png 2x" data-dominant-color="2D2E35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Before import</span><span class="informations">4264×2568 386 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41b4877b48174ff27a3bc99fc9b5c71f41d50695.jpeg" data-download-href="/uploads/short-url/9nfOH5c0SMLCWvLtcbNPW8O8Lch.jpeg?dl=1" title="After conversion" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41b4877b48174ff27a3bc99fc9b5c71f41d50695_2_690x427.jpeg" alt="After conversion" data-base62-sha1="9nfOH5c0SMLCWvLtcbNPW8O8Lch" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41b4877b48174ff27a3bc99fc9b5c71f41d50695_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41b4877b48174ff27a3bc99fc9b5c71f41d50695_2_1035x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41b4877b48174ff27a3bc99fc9b5c71f41d50695_2_1380x854.jpeg 2x" data-dominant-color="5E5C5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">After conversion</span><span class="informations">1920×1189 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The idea is to have a high-resolution 3D segmentation mask that I can register on my microCT so that it matches perfectly.</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2024-08-05 20:45 UTC)

<p>See step-by-step instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">here</a>.</p>
<p>Note that an image of 588 x 734 x 1095 at 0.033mm/pixel resampled to 0.01mm/pixel would result in a 12GB image. For processing a segmentation of this size it would be recommended to have about 100GB physical RAM for optimal performance.</p>

---
