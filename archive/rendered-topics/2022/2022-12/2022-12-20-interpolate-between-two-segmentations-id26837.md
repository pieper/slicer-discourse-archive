# Interpolate between two segmentations

**Topic ID**: 26837
**Date**: 2022-12-20
**URL**: https://discourse.slicer.org/t/interpolate-between-two-segmentations/26837

---

## Post #1 by @ifried01 (2022-12-20 03:00 UTC)

<p>Hi,</p>
<p>I have two chest CT scans captured at different time points (ex. inspiration and expiration) from which I segment the same anatomical structure (ex. airways). Given these two instances of the same object (with slight differences, so no obvious one-to-one correspondence), is it possible in Slicer to interpolate between the two shapes (ex. get instances of the deforming airway between inspiration and expiration)?</p>
<p>I looked around on discourse and online and didn’t find an obvious way to do this (I apologize if I missed something). Any pointers (or if this is a naive question, an explanation of why this is not a reasonable thing to do) would be greatly appreciated.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2022-12-20 05:50 UTC)

<p>You can register the two time points using SlicerElastix or SlicerANTs extensions. You get a full displacement field as a result, which tells exactly where each voxel go between the two images. You can compute statistics of the displacement values, warp one image and/or segmentation to match the other image, etc.</p>
<p>What information would you like to get from these images?</p>

---

## Post #3 by @ifried01 (2022-12-20 22:19 UTC)

<p>Thanks for the pointer. I used Elastix to get the displacement values (and referred to <a href="https://discourse.slicer.org/t/calculating-the-displacement-between-two-models/4012">this post</a> and <a href="https://discourse.slicer.org/t/computing-airway-motion-from-4dct/12971">this post</a> for additional tips). I also tried the SegmentRegistration module directly on the segmentations, but the Elastix output on cropped versions of the original images looks better.</p>
<p>I am able to apply the displacement vectors, but am getting stuck downstream. Here is my current workflow:</p>
<p>(a) I get the KJI coordinates of my segmented object from timestep1 (airway at expiration)<br>
(b) I convert to IJK and then to RAS using the IJK-to-RAS matrix from timestep1’s labelVolmeNode<br>
(c) I apply the deformation displacement to each voxel from its corresponding voxel in the displacement field<br>
(d) I convert the transformed RAS coordinates to IJK using the RAS-to-IJK matrix from timestep2’s volume (airway at inspiration)<br>
(e) I convert to KJI and write the matrix as an image (with some modification to handle Q1 below)</p>
<p>Q1: Some of the values I am getting from step (e) for the KJI coordinates are outside the boundary of timestep2’s image. Why would this be happening? When I convert from RAS to IJK using timestep1’s RAS-to-IJK matrix they are also outside the boundary (with some negative KJI indices).</p>
<p>Q2: I am following the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates" rel="noopener nofollow ugc">code</a> from the script page to convert from RAS to IJK, but the conversion to <code>int</code> causes my image to get chopped up between slices. I can recover the segmentation by filling holes, but is this expected?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="26837" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What information would you like to get from these images?</p>
</blockquote>
</aside>
<p>I want to create intermediate instances of the deforming airway between the inspiratory and expiratory airway segmentation instances.</p>
<p>I hope that all makes sense. Thanks for your help, I really appreciate it.</p>

---

## Post #4 by @lassoan (2022-12-20 23:28 UTC)

<aside class="quote no-group" data-username="ifried01" data-post="3" data-topic="26837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9bd4f/48.png" class="avatar"> ifried01:</div>
<blockquote>
<p>Some of the values I am getting from step (e) for the KJI coordinates are outside the boundary of timestep2’s image. Why would this be happening? When I convert from RAS to IJK using timestep1’s RAS-to-IJK matrix they are also outside the boundary (with some negative KJI indices).</p>
</blockquote>
</aside>
<p>That is not a problem but a feature. In order to transform images you need resampling transform (fixed to moving), to transform everything else - models, point sets, etc. - you need the modeling transform, which is the inverse of the resampling transform (moving to fixed). You can only compute the inverse of a transform if it is continuously changing around that position, so you must be able to extrapolate the transform outside  the fixed image’s domain. In fact, Slicer uses VTK transforms, which can extrapolate all transforms to the entire 3D domain.</p>
<aside class="quote no-group" data-username="ifried01" data-post="3" data-topic="26837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9bd4f/48.png" class="avatar"> ifried01:</div>
<blockquote>
<p>I am following the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates">code</a> from the script page to convert from RAS to IJK, but the conversion to <code>int</code> causes my image to get chopped up between slices. I can recover the segmentation by filling holes, but is this expected?</p>
</blockquote>
</aside>
<p>I don’t understand what you mean by “chopped up between slices”. You don’t need to apply a transform to a node by iterating through all the points of a model or all voxels of an image yourself (as it would be error-prone and extremely slow). Instead, you can set a transform node as parent to a node and Slicer takes care takes care of everything.</p>
<aside class="quote no-group" data-username="ifried01" data-post="3" data-topic="26837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9bd4f/48.png" class="avatar"> ifried01:</div>
<blockquote>
<p>I want to create intermediate instances of the deforming airway between the inspiratory and expiratory airway segmentation instances.</p>
</blockquote>
</aside>
<p>The easiest solution is to use linear interpolation. For the bulk rigid transform component you can use <a href="https://github.com/z6zou/PlusBuild-Openhaptics/blob/d37700432d3a93b9b1f4e8eaae421d5029a7e3b5/IGSIO/Source/IGSIOCommon/igsioMath.cxx#L37">SLERP interpolation</a> for the orientation and linear interpolation for the position. You can represent all the remaining warping transform as a grid transform (displacement field) and you can interpolate it using scaling between 0.0 (starting point) to and 1.0 (endpoint).</p>

---

## Post #5 by @ifried01 (2022-12-21 15:33 UTC)

<p>Hi Andras,</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26837" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t understand what you mean by “chopped up between slices”.</p>
</blockquote>
</aside>
<p>I attached an image to help explain what I meant by chopped up. I am guessing this might partly be because there is no one-to-one correspondence between the two shapes since there is a deformation going on between the inspiratory segmentation which is larger and the expiratory segmentation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d303b15273f283a4f7ea6976c675bc788fac0003.png" data-download-href="/uploads/short-url/u6IEMr1TtxjGe7yxgVNGAwmrp0n.png?dl=1" title="Screenshot from 2022-12-21 10-08-40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d303b15273f283a4f7ea6976c675bc788fac0003_2_389x500.png" alt="Screenshot from 2022-12-21 10-08-40" data-base62-sha1="u6IEMr1TtxjGe7yxgVNGAwmrp0n" width="389" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d303b15273f283a4f7ea6976c675bc788fac0003_2_389x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d303b15273f283a4f7ea6976c675bc788fac0003_2_583x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d303b15273f283a4f7ea6976c675bc788fac0003.png 2x" data-dominant-color="949AC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-12-21 10-08-40</span><span class="informations">767×984 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26837" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The easiest solution is to use linear interpolation. For the bulk rigid transform component you can use <a href="https://github.com/z6zou/PlusBuild-Openhaptics/blob/d37700432d3a93b9b1f4e8eaae421d5029a7e3b5/IGSIO/Source/IGSIOCommon/igsioMath.cxx#L37" rel="noopener nofollow ugc">SLERP interpolation</a> for the orientation and linear interpolation for the position. You can represent all the remaining warping transform as a grid transform (displacement field) and you can interpolate it using scaling between 0.0 (starting point) to and 1.0 (endpoint).</p>
</blockquote>
</aside>
<p>How can I go about doing this for the Elastix transform? I read some other posts that talk about the “Split” functionality in Transforms, but from my understanding this can only be applied to composite transforms (after hardening?).</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26837" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You don’t need to apply a transform to a node by iterating through all the points of a model or all voxels of an image yourself (as it would be error-prone and extremely slow). Instead, you can set a transform node as parent to a node and Slicer takes care takes care of everything.</p>
</blockquote>
</aside>
<p>I don’t want to just set the transform node as a parent because I want to be able to interpolate through the transformation. In step (c) from my previous post, I had a scaling factor I was applying to the displacement field (from 0 to 1) to simulate this interpolation. I am doing this all in Python and it wasn’t prohibitively slow (was roughly 1-2 seconds).</p>

---

## Post #6 by @lassoan (2022-12-22 22:59 UTC)

<p>I see, the image is “chopped up” because you are trying to transform an image by transforming each voxel using the <em>modeling</em> (moving to fixed image) transform. Using the modeling transform is the correct way to transform points of a model and most other types of objects, except images. Images must be transformed using the <em>resampling</em> (fixed to moving image) transform, which provides for each output image voxel position the corresponding voxel position in the input image. Normally you don’t even need to think about this, because when you apply a transform to a node Slicer computes and uses the modeling or resampling transform.</p>
<aside class="quote no-group" data-username="ifried01" data-post="5" data-topic="26837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9bd4f/48.png" class="avatar"> ifried01:</div>
<blockquote>
<p>How can I go about doing this for the Elastix transform? I read some other posts that talk about the “Split” functionality in Transforms, but from my understanding this can only be applied to composite transforms (after hardening?).</p>
</blockquote>
</aside>
<p>You can do this using Elastix in two steps:</p>
<ol>
<li>Compute a rigid transform and get the result as a matrix (disable “force grid output transform” in advanced settings)</li>
<li>Harden the transform on the moving image</li>
<li>Compute deformable transform and get the result as a grid transform (enable “force grid output transform”)</li>
</ol>
<aside class="quote no-group" data-username="ifried01" data-post="5" data-topic="26837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9bd4f/48.png" class="avatar"> ifried01:</div>
<blockquote>
<p>I am doing this all in Python and it wasn’t prohibitively slow (was roughly 1-2 seconds).</p>
</blockquote>
</aside>
<p>It wasn’t slow because you only transformed a small fraction of the voxels, without proper interpolation. Transforming an image properly (computing interpolated value for each voxel) takes 10-100x more operations, but if you use one of the image resample modules then the computation time will be about the same. Note that although you scale the two transform components separately, you can use the composite transform to transform the input image all at once.</p>

---

## Post #7 by @ifried01 (2022-12-24 19:02 UTC)

<p>Hi Andras,</p>
<p>Thank you very much for your responses and explanations for each of those items. I will work through everything and write back in a couple days (hopefully with good results).</p>

---

## Post #8 by @ifried01 (2023-01-07 16:25 UTC)

<p>Hi Andras,</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="26837" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can do this using Elastix in two steps:</p>
</blockquote>
</aside>
<p>Thanks. I have been able to get the rigid transform and the deformable transform.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="26837" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It wasn’t slow because you only transformed a small fraction of the voxels</p>
</blockquote>
</aside>
<p>why is that wrong? I thought I could use the images to extract the deformation field, but then apply it only to the airways. I am not interested in getting the image states between start (exhalation) and end (inhalation), just the segmented airway states along that deformation spectrum (the figure from <a href="https://ieeexplore.ieee.org/document/4815234" rel="noopener nofollow ugc">this paper</a> I found might help show what I mean):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0d4ae4d44d52901e3c32f5284a0b665a379ed61.png" data-download-href="/uploads/short-url/w4WCrpQA8fOirSMa7QhidwaMmzL.png?dl=1" title="Screen Shot 2023-01-07 at 10.40.28 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0d4ae4d44d52901e3c32f5284a0b665a379ed61_2_690x234.png" alt="Screen Shot 2023-01-07 at 10.40.28 AM" data-base62-sha1="w4WCrpQA8fOirSMa7QhidwaMmzL" width="690" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0d4ae4d44d52901e3c32f5284a0b665a379ed61_2_690x234.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0d4ae4d44d52901e3c32f5284a0b665a379ed61_2_1035x351.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0d4ae4d44d52901e3c32f5284a0b665a379ed61.png 2x" data-dominant-color="7D96AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-01-07 at 10.40.28 AM</span><span class="informations">1202×408 335 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="ifried01" data-post="3" data-topic="26837" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9bd4f/48.png" class="avatar"> ifried01:</div>
<blockquote>
<p>(a) I get the KJI coordinates of my segmented object from timestep1 (airway at expiration)<br>
(b) I convert to IJK and then to RAS using the IJK-to-RAS matrix from timestep1’s labelVolmeNode<br>
(c) I apply the deformation displacement to each voxel from its corresponding voxel in the displacement field<br>
(d) I convert the transformed RAS coordinates to IJK using the RAS-to-IJK matrix from timestep2’s volume (airway at inspiration)<br>
(e) I convert to KJI and write the matrix as an image (with some modification to handle Q1 below)</p>
</blockquote>
</aside>
<p>when i use this workflow but with the <em>inverse transform</em> I get the following result (blue == exhalation, green == 50%, tan == inhalation) and the deformed segmentation is less chopped up (screenshot below). Is this conceptually wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67965fe28140893379eb9e1b67bfe64971617558.png" data-download-href="/uploads/short-url/eMnm2kaEtCKWrOSuCsYsmhDlvny.png?dl=1" title="Screenshot from 2023-01-07 11-23-14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67965fe28140893379eb9e1b67bfe64971617558_2_312x375.png" alt="Screenshot from 2023-01-07 11-23-14" data-base62-sha1="eMnm2kaEtCKWrOSuCsYsmhDlvny" width="312" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67965fe28140893379eb9e1b67bfe64971617558_2_312x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67965fe28140893379eb9e1b67bfe64971617558_2_468x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67965fe28140893379eb9e1b67bfe64971617558.png 2x" data-dominant-color="888AA8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-01-07 11-23-14</span><span class="informations">533×638 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb55bf16eebc59aa2b0e4f449dd897e2e72db3f7.png" data-download-href="/uploads/short-url/zRpytee4kSoS7zrvxv8LX6vejYz.png?dl=1" title="Screenshot from 2023-01-07 11-05-00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb55bf16eebc59aa2b0e4f449dd897e2e72db3f7_2_385x375.png" alt="Screenshot from 2023-01-07 11-05-00" data-base62-sha1="zRpytee4kSoS7zrvxv8LX6vejYz" width="385" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb55bf16eebc59aa2b0e4f449dd897e2e72db3f7_2_385x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb55bf16eebc59aa2b0e4f449dd897e2e72db3f7_2_577x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb55bf16eebc59aa2b0e4f449dd897e2e72db3f7_2_770x750.png 2x" data-dominant-color="8E97BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-01-07 11-05-00</span><span class="informations">952×925 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2023-01-07 16:42 UTC)

<aside class="quote no-group quote-modified" data-username="ifried01" data-post="8" data-topic="26837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/b9bd4f/48.png" class="avatar"> ifried01:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="26837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It wasn’t slow because you only transformed a small fraction of the voxels</p>
</blockquote>
</aside>
<p>why is that wrong?</p>
</blockquote>
</aside>
<p>It is wrong because the output can have many gaps in it.</p>
<p>To transform an image, you need to iterate through all the voxels of the output image and fill it with voxel values you get from the voxel position obtained from the resampling transform.</p>

---

## Post #10 by @ifried01 (2023-01-08 15:03 UTC)

<p>I understand why that is wrong. Thanks for bearing with me. (I am putting a few links to resources I found most useful in understanding this for anyone who might come across this discussion: <a href="https://simpleitk.readthedocs.io/en/master/fundamentalConcepts.html" rel="noopener nofollow ugc">link1</a>, <a href="https://itk.org/ITKSoftwareGuide/html/Book2/ITKSoftwareGuide-Book2ch3.html" rel="noopener nofollow ugc">link2</a>, <a href="https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks" rel="noopener nofollow ugc">link3</a>).</p>
<p>Based on those links and some of the <a href="https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks" rel="noopener nofollow ugc">notebooks</a> in the SimpleITK Github, I have an implementation that reads in the fixed and moving images, reads in the displacement field (saved from running Elastix in Slicer) and multiplies it by my desired interpolation scale (0.0 to 1.0), converts it to a <em>DisplacementFieldTransform</em>, and then generates a <em>ResampleImageFilter</em> using the transform. I then execute the resampler on my <em>moving</em> image to get my desired image.</p>
<p>From my current understanding, this new implementation addresses the errors I was making before. Does this sound reasonable? I am using the displacement field that I get by doing a direct nonrigid registration instead of breaking things down into the rigid transform component and the warping transform component like we discussed a couple posts back. Do I need to break things down and treat those independently?</p>
<p>I am learning a lot working through this. Thanks for all of your time and help.</p>

---
