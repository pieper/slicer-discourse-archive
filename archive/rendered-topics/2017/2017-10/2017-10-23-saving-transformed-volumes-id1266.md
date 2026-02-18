# Saving transformed Volumes

**Topic ID**: 1266
**Date**: 2017-10-23
**URL**: https://discourse.slicer.org/t/saving-transformed-volumes/1266

---

## Post #1 by @stevenagl12 (2017-10-23 16:06 UTC)

<p>Hi, I am trying to save binary labelmaps that I have transformed with specific transform files. The problem is that I have clicked the harden transform button, but when I go to save the files, they do not save in the correct orientation, but rather the initial orientation. Is there an easy way to save the new matrices corresponding to the transformed labelmaps?</p>

---

## Post #2 by @stevenagl12 (2017-10-23 16:19 UTC)

<p>In addition, is there a way to save a transformed segmentation? Again, I have tried hardening the renasform and saving the seg.nrrd file, but the outcome is the original segmentation orientation, and not the transformed orientation.</p>

---

## Post #3 by @lassoan (2017-10-23 17:24 UTC)

<p>Hardening linear transforms on volumes don’t require changing voxel values, you’ll only see result of hardening as an update in axis direction information. This operation is fast, reversible, and no information is lost.</p>
<p>To deal with software that don’t work in physical space (ignores axis direction information, etc) you can export the segmentation into a labelmap volume. You can specify any volume as a reference volume and voxels will be resampled into that voxel grid. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations</a> for details.</p>

---

## Post #4 by @stevenagl12 (2017-10-23 19:51 UTC)

<p>How would you go about saving the volume that is transformed then?</p>

---

## Post #5 by @lassoan (2017-10-23 21:14 UTC)

<p>To resample volumes, use Resample Scalar Volume and similar resample modules.</p>

---

## Post #6 by @jcfr (2017-10-24 05:14 UTC)

<p>Here is a summary of the great answers of <a class="mention" href="/u/lassoan">@lassoan</a> :</p>
<h3><a name="p-5259-what-is-the-effect-of-hardening-linear-transforms-1" class="anchor" href="#p-5259-what-is-the-effect-of-hardening-linear-transforms-1" aria-label="Heading link"></a>What is the effect of Hardening linear transforms ?</h3>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1266">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Hardening linear transforms on volumes don’t require changing voxel values, you’ll only see result of hardening as an update in axis direction information. This operation is fast, reversible, and no information is lost.</p>
</blockquote>
</aside>
<h3><a name="p-5259-how-to-deal-with-software-that-dont-work-in-physical-space-2" class="anchor" href="#p-5259-how-to-deal-with-software-that-dont-work-in-physical-space-2" aria-label="Heading link"></a>How to deal with software that don’t work in physical space ?</h3>
<h4><a name="p-5259-for-segmentations-3" class="anchor" href="#p-5259-for-segmentations-3" aria-label="Heading link"></a>For segmentations</h4>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="3" data-topic="1266">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To deal with software that don’t work in physical space (ignores axis direction information, etc) you can export the segmentation into a labelmap volume. You can specify any volume as a reference volume and voxels will be resampled into that voxel grid. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" class="inline-onebox">Documentation/Nightly/Modules/Segmentations - Slicer Wiki</a> for details.</p>
</blockquote>
</aside>
<h4><a name="p-5259-for-volumes-4" class="anchor" href="#p-5259-for-volumes-4" aria-label="Heading link"></a>For Volumes</h4>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="1266" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To resample volumes, use Resample Scalar Volume and similar resample modules.</p>
</blockquote>
</aside>

---

## Post #7 by @Trang (2021-09-10 16:33 UTC)

<p>Hi there, don’t know have you resolved your dilemma or not. I faced the same trouble when trying to save transformed model. It turned out that we need to select the files ( right click) in the transformed object box before hitting the hardening button. After clicking hardening, the files from the transformed object box will move back to the transformable box. Then you can save the transformed files.<br>
Hope it helps^^</p>

---

## Post #8 by @Saima (2022-02-24 07:23 UTC)

<p>how to do harden transform  using python script?</p>
<p>regards,<br>
Saima</p>

---

## Post #9 by @ebrahim (2022-02-24 12:09 UTC)

<p>Once you have a transformable node that has an associated transform (e.g. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-a-transform-to-a-transformable-node" rel="noopener nofollow ugc">like this</a>), you can call the <code>HardenTransform()</code> method on that node: <code>transformableNode.HardenTransform()</code>.</p>

---

## Post #10 by @Tiberiu (2023-06-13 09:54 UTC)

<p>This does not work for me.</p>

---

## Post #11 by @bserrano (2024-01-11 16:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="1266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>resample</p>
</blockquote>
</aside>
<p>Has anyone solved this issue? I want to transform a volume and create another one with the same size. So then I can export it in dcm format and open it with pydicom or export the slices in .npy format. How can I do it?</p>
<p>Now I’m:</p>
<ol>
<li>Creating the transformation matrix and applying it with the Transformation module.</li>
<li>In data module right click and harden transform</li>
<li>Export as DICOM</li>
</ol>

---

## Post #12 by @lassoan (2024-01-11 17:04 UTC)

<p>I don’t think there is an issue. There are many ways to apply a transform to a volume and you need to use the tools in Slicer that correspond to what you would like to achieve.</p>
<blockquote>
<p>I want to transform a volume and create another one with the same size.</p>
</blockquote>
<p>Do you want to resample the transformed volume into the same geometry (origin, spacing, axis direction, and extents) as the original volume? Then you can use “Resample scalar/vector/DWI volume” module and set the original volume as “Reference volume” and set the transform as “Transform node”.</p>

---

## Post #13 by @muratmaga (2024-01-11 18:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="1266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you want to resample the transformed volume into the same geometry (origin, spacing, axis direction, and extents) as the original volume? Then you can use “Resample scalar/vector/DWI volume” module and set the original volume as “Reference volume” and set the transform as “Transform node”.</p>
</blockquote>
</aside>
<p>How do you deal with cases when the transformed volume gets cropped? Because this procedure takes the image size from the input node.</p>

---

## Post #14 by @pieper (2024-01-11 19:02 UTC)

<p>You can create a larger target volume using the CropVolume module.</p>
<p>It would be an interesting feature to consider automatically creating a target volume that includes all of the transformed range of the volume, but I don’t think we have that.</p>

---

## Post #15 by @muratmaga (2024-01-11 19:05 UTC)

<p>Yes, i tried that. it turns into a multi-step process, where you do one resample, notice that it is cut, use the CropVolume to expand in the regions where there is cut. Go back to resample, set the new volume as the reference volume, and repeat the procedure until FOV is no longer cut.</p>
<p>While it works, it is a quite tedious. Would be nice to automatically figure out what the resultant image size need to be.</p>

---

## Post #16 by @pieper (2024-01-11 19:15 UTC)

<p>If you apply the transform to the volume you can look at it in the slice views and adjust the ROI to fit it, so it shouldn’t be too hard.  But I agree, the process could be automated.</p>

---

## Post #17 by @muratmaga (2024-01-11 20:23 UTC)

<p>It would be great, if this is actually a feature of CropVolume. A third option, which will create a resampled output image using the ROI.</p>
<p>Resample DWI has so many options that is intimidating to begin with.</p>

---

## Post #18 by @lassoan (2024-01-11 22:31 UTC)

<p>When you harden a transform on a volume, <a href="https://github.com/Slicer/Slicer/blob/d8c2d883412c0aaf7a6fa8dcfb3703d4dce91dae/Libs/MRML/Core/vtkMRMLVolumeNode.cxx#L892-L979">Slicer performs this extent computation automatically</a>. It takes into account all translation/rotarion/warping of the volume and does not compute the new extent based on only the 8 corners but many points on the bounding box of the volume.</p>
<p>This automatic extent computation is used by Crop volume module, too, when the “Fit to volume” button is pressed. However, when you transform and resample you most often want to cut into the volume (to cut off the wavy sides of the warped volume). Maybe what is needed would be to have an option to reset the ROI size without changing its orientation. Or maybe to have a minimal ROI option (where the ROI is the largest box that fits within the warped volume).</p>

---

## Post #19 by @bserrano (2024-01-15 08:36 UTC)

<p>Thanks, that’s what I wanted.<br>
I have another question. I’ve noticed that when I apply a transformation to a volume via the Transforms module, Slicer selects automatically a “Reformat” view in the red slice. How can I use this “Reformat” view as the axial view and save the volume accordingly?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f871c4d639f4b23077fcb41c29ba98780ef8410.png" alt="image" data-base62-sha1="mLfoemhrJ1tEhuH90sXotcQbl0k" width="659" height="416"></p>
<p>Many thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
