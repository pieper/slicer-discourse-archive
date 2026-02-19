---
topic_id: 13690
title: "Showing Both The Background And Foreground Layer Volumes In"
date: 2020-09-24
url: https://discourse.slicer.org/t/13690
---

# Showing both the background and foreground layer volumes in their entirety

**Topic ID**: 13690
**Date**: 2020-09-24
**URL**: https://discourse.slicer.org/t/showing-both-the-background-and-foreground-layer-volumes-in-their-entirety/13690

---

## Post #1 by @jamesobutler (2020-09-24 17:55 UTC)

<p>I often find myself with two 3D ultrasound volumes that I want to overlay in a slice view, but having the background volume determine the extent of the foreground volume that is shown (using regular alpha blending) results in me losing some reference image data from the foreground that doesn’t overlap.</p>
<p>I found this one mention related to this topic in another thread linked below.  cc: <a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote" data-post="3" data-topic="9900">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slice-multiple-volumes/9900/3">Slice multiple volumes</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Background volume extents are used as mask, so if the volumes don’t overlap then you don’t see the foreground volume. This is often useful but I see that it can be inconvenient. We may revisit this decision later but until then you can expand the background volume using Crop Volume module.
  </blockquote>
</aside>

<p>What would the development effort be like and what areas of Slicer would need to be changed to support the ability to show both background and foreground volumes in their entirety in the slice views instead of one masking the other?</p>

---

## Post #2 by @pieper (2020-09-25 17:13 UTC)

<p>I haven’t looked at the slice view code in a very long time, but I believe we set the reslice outputs for all layers to have 0 alpha outside of the slice extents.  This makes sense for the foreground, but maybe not for the background.  For compositing the 0 alpha means that the foreground alpha is multiplied by zero and thus never shows up.</p>
<p>If that is the issue then it’s maybe a simple change in <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLSliceLayerLogic.cxx#L635-L811">this code</a>.</p>

---

## Post #3 by @lassoan (2020-09-25 18:43 UTC)

<p>We rely on this feature, for example when we want to apply a fan-shaped mask on ultrasound image display, so this masking should not be completely removed, but made optional.</p>
<p>I’ve mapped out the slice view pipelines a few years ago for some performance optimization investigation. These provide a general overview of how things work. Red indicates the old implementation (you can ignore it) and green the new (current) one.</p>
<hr>
<p>Scalar volumes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eced0f2722e9420606107d13beb296d94e47dc7.png" data-download-href="/uploads/short-url/8XCHHn5ZQPxW1EvwfEiVIRYZrnh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eced0f2722e9420606107d13beb296d94e47dc7_2_690x377.png" alt="image" data-base62-sha1="8XCHHn5ZQPxW1EvwfEiVIRYZrnh" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eced0f2722e9420606107d13beb296d94e47dc7_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eced0f2722e9420606107d13beb296d94e47dc7_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3eced0f2722e9420606107d13beb296d94e47dc7_2_1380x754.png 2x" data-dominant-color="EAEAEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1768×967 51.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<hr>
<p>Vector volumes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29218c174fa770e61671d71e53a8dc4781ce5e5c.png" data-download-href="/uploads/short-url/5RRrXfMKeH0ttwvxLIxnvlo0igk.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29218c174fa770e61671d71e53a8dc4781ce5e5c_2_690x372.png" alt="image" data-base62-sha1="5RRrXfMKeH0ttwvxLIxnvlo0igk" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29218c174fa770e61671d71e53a8dc4781ce5e5c_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29218c174fa770e61671d71e53a8dc4781ce5e5c_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29218c174fa770e61671d71e53a8dc4781ce5e5c_2_1380x744.png 2x" data-dominant-color="DDDFE5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1764×953 80.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<hr>
<p>I think the cropping to background region is due to AlphaLogic filter, which applies a stencil on the alpha component. Probably the cropping to background volume could be removed by removing the stencil input connection to this filter in the layer logic (or set empty input).</p>
<p>This could be controlled with a checkbox in the blending options submenu:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0527eff6b5ec9e5c113b3ebb7697cbfda4e3070.png" data-download-href="/uploads/short-url/p9OMtpJHAlpaxioMyE3YK0mJozu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0527eff6b5ec9e5c113b3ebb7697cbfda4e3070_2_690x408.png" alt="image" data-base62-sha1="p9OMtpJHAlpaxioMyE3YK0mJozu" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0527eff6b5ec9e5c113b3ebb7697cbfda4e3070_2_690x408.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0527eff6b5ec9e5c113b3ebb7697cbfda4e3070.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0527eff6b5ec9e5c113b3ebb7697cbfda4e3070.png 2x" data-dominant-color="E0DAD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">915×542 49.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When “Crop to background” (I’m not sure if this is the best name) option is disabled then you also need to pay attention to take into account all volume layers volume when “fit” button is clicked.</p>

---

## Post #4 by @jamesobutler (2020-09-26 00:56 UTC)

<p>Yes, I would also agree with making it a new option by maintaining current behavior. Thanks for the detailed information on the topic.</p>

---
