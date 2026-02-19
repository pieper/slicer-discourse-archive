---
topic_id: 11371
title: "Removing Legacy Modules And Rarely Used Features From Slicer"
date: 2020-04-30
url: https://discourse.slicer.org/t/11371
---

# Removing legacy modules and rarely used features from Slicer5

**Topic ID**: 11371
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/removing-legacy-modules-and-rarely-used-features-from-slicer5/11371

---

## Post #1 by @lassoan (2020-04-30 20:42 UTC)

<p>We plan to release Slicer 5.0 soon. This is a major version change, which happens in about every 5 years and brings lots of new features and also trimming of old features that have been replaced by alternative solutions.</p>
<p>We are considering removing the following modules/features:</p>
<ul>
<li>Editor module: old module for editing labelmaps, superseded by Segment Editor module
<ul>
<li>Label Statistics module: superseded by Segment Statistics module</li>
</ul>
</li>
<li>Charts infrastructure: replaced by Plots module
<ul>
<li>DoubleArrays module: superseded by Tables module (that can store one or more arrays)</li>
</ul>
</li>
<li>Annotations: being replaced by Markups module - we will keep this around until we add markups ROI widget.</li>
<li>MultiVolume infrastructure: being replaced by Sequences module - we will keep this around until all features are implemented in Sequences (currently missing importing from folder, plotting of two volumes)</li>
<li>
<a href="https://github.com/Slicer/Slicer/issues/4864">Unused CLI modules</a>: ExpertAutomatedRegistration (replaced by BRAINS and Elastix), Fiducial Registration (replaced by Landmark registration and Fiducial registration wizard modules), Resample Scalar Volume (there are 2 other image resample modules), DiffusionTensorTest, TestGridTransformRegistration, BSplineToDeformationField (it is available in Transforms module’s Convert section)</li>
<li>Lightbox view: replaced by Screen Capture module’s lightbox view mode</li>
</ul>
<p>Let us know within a week if you have any concerns or questions.</p>

---

## Post #2 by @muratmaga (2020-04-30 23:26 UTC)

<p>Among these, I only care for ResampleScalarVolume, because of its simplicity for downsampling. Other resampling modules require reference images and whole bunch of other parameters. While CropVolume is also simple, it doesn’t let me specify downsampling as flexible as ResampleScalarVolume.</p>

---

## Post #3 by @lassoan (2020-05-01 02:04 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="11371">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>it doesn’t let me specify downsampling as flexible as ResampleScalarVolume</p>
</blockquote>
</aside>
<p>Crop volume allows resampling by a constant, with option of forcing to isotropic output spacing. Is there any other resampling strategy that you would use?</p>

---

## Post #4 by @muratmaga (2020-05-01 03:02 UTC)

<p>I like the ability to give the spacing independently for all three axis, which CropVolume lacks. Also, I have encountered axis rotations with CropVolume with interpolated cropping (an ROI fit to the volume extend, but not under a transform), which causes external programs to see it in a different space than the original one.</p>
<p>We use ANTs/ANTsR a lot and it causes problems for us:</p>
<pre><code>&gt; orig=antsImageRead('/scratch/MRHead.nrrd')
&gt; rot=antsImageRead('/scratch/cropped.nrrd')

&gt; orig
antsImage
  Pixel Type          : float 
  Components Per Pixel: 1 
  Dimensions          : 256x256x130 
  Voxel Spacing       : 1x1x1.29999542236328 
  Origin              : 86.6449 -133.9286 116.7857 
  Direction           : 0 1 0 0 0 -1 -1 0 0 
  Filename           : /scratch/MRHead.nrrd 

&gt; rot
antsImage
  Pixel Type          : float 
  Components Per Pixel: 1 
  Dimensions          : 130x256x256 
  Voxel Spacing       : 1.29999542236328x1x1 
  Origin              : 86.6449 121.071 -138.214 
  Direction           : -1 0 0 0 -1 0 0 0 1 
  Filename           : /scratch/cropped.nrrd 

&gt; test = antsAverageImages(list(orig, rot))
========================================Error in avg + img * weights[ct] : 
  Images do not occupy the same physical space</code></pre>

---

## Post #5 by @lassoan (2020-05-01 03:22 UTC)

<p>To force a volume to have the same geometry as another one, the proper way is to specify a reference volume. Typing many floating-point values manually is tedious and very error-prone.</p>
<p>There should be really no reason to manually specify arbitrary spacing values, but we can put it in advanced section somewhere in the resampling module that we finally keep.</p>

---

## Post #6 by @muratmaga (2020-05-01 03:34 UTC)

<p>But in this case we do have a reference volume; the original image.</p>

---

## Post #7 by @lassoan (2020-05-01 04:59 UTC)

<p>Exactly. So, the basic use cases are:</p>
<ul>
<li>resampling using a reference volume =&gt; use resampling module</li>
<li>cropping &amp; resampling using ROI =&gt; use crop volume module</li>
</ul>
<p>Using an ROI and reference volume at the same time rarely makes sense, but if there is some use case when this is needed then you can do an additional resample step after cropping. If only axis permutation is needed (e.g., because the ROI cropping resulted in an axis order that you don’t want) then this extra resampling will not cause any data loss: voxel values are not interpolated, they are only reordered.</p>

---

## Post #8 by @pieper (2020-05-01 18:25 UTC)

<p>It’s worth noting that the MRHead is a sagittal acquisition and the cropped result is axial.  The CropVolume outputs are kind of arbitrary and based on the origin and orientation of the ROI box.  It does make sense to me that we should try to match pixel orientation if possible, at least in the case when the orientations match.  Also independent controls of the axis spacings makes sense for some use cases.</p>

---

## Post #9 by @muratmaga (2020-05-01 23:43 UTC)

<p>OK. I don’t think I am following.</p>
<p>I have a very simple use case. I want to have MRHead.nrrd, or any volume to be downsampled in place without changing anything except for dimensions and spacing accordingly. ResampleScalarVolume does exactly that. CropVolume requires a ROI and causes a flip in axis, and ResampleScalarVector/DWI causes creates an cropped volume (see screenshot). So, unless we have a direct replacement of this behavior without our tools, I don’t think we can call ResampleScalar as redundant.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be81c7d49391b0727eef1b903e22df86fb0141da.png" data-download-href="/uploads/short-url/rbiLVshhfG84tJDu0kGzaXEMMz0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be81c7d49391b0727eef1b903e22df86fb0141da_2_682x500.png" alt="image" data-base62-sha1="rbiLVshhfG84tJDu0kGzaXEMMz0" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be81c7d49391b0727eef1b903e22df86fb0141da_2_682x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be81c7d49391b0727eef1b903e22df86fb0141da_2_1023x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be81c7d49391b0727eef1b903e22df86fb0141da.png 2x" data-dominant-color="9FA6AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1167×855 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2020-05-02 00:41 UTC)

<p>There is clearly redundancy, but as is, I agree that each resampling module has some unique features. See more information here: See detailed analysis/comparison of resampling modules here: <a href="https://github.com/Slicer/Slicer/issues/2393" class="inline-onebox">Consolidate the image resample modules · Issue #2393 · Slicer/Slicer · GitHub</a></p>
<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="11371">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I have a very simple use case. I want to have MRHead.nrrd, or any volume to be downsampled in place without changing anything except for dimensions and spacing accordingly.</p>
</blockquote>
</aside>
<p>This is indeed a simple use case, but this should almost never be done. Anisotropic spacing negatively affects almost all processing and analysis operations, so it should be avoided as much as possible. Resampling is a lossy operation, so it should be avoided as much as possible, too. Therefore, if you decide to resample an image then you should almost always use isotropic sampling (if you want to do any 3D analysis or processing) or match an existing volume’s spacing (so that the two volumes can be processed/visualized together without any additional resampling).</p>
<p>Resampling with arbitrarily chosen spacing values rarely makes sense, as it would combine both disadvantages: result would be not well suited for 3D analysis and another resampling would be needed later if geometry must be matched to another volume’s geometry. It is fine to have this option somewhere on the GUI but it should not be easy to find, to prevent novice users from using it just because they don’t know any better.</p>
<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="11371">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It does make sense to me that we should try to match pixel orientation if possible</p>
</blockquote>
</aside>
<p>Yes, it could be useful, but it would need some extra GUI (to choose between using closest input volume axes / using ROI axes directions) and implementation workload.</p>

---

## Post #11 by @muratmaga (2020-05-02 02:02 UTC)

<p>There some use cases for this.</p>
<p>Affine registration being one of the most common use cases. Most of the times for large volumes I find a low-res version of target and source images register very well and also very quickly with affine registration. I can take the output from this registration and then  apply to the full resolution image using the other resamplevector module (in fact I think it was you showed me that trick) with resampling artifacts minimized (also a lot faster than had I register the full-resolution images).</p>
<p>Most microCT datasets are also isotropic to begin with, so concern for anisotropic data don’t apply most of our users.</p>

---

## Post #12 by @pll_llq (2020-05-02 08:48 UTC)

<p>Hi! Thank you very much for maintaining and perfecting Slicer. It is a unique tool that opens a whole universe of opportunities for researchers around the world.</p>

---

## Post #13 by @rbumm (2020-05-02 09:10 UTC)

<p>As far as I know, the editor module is needed to edit the result of the airway segmentation module of the chest imaging suite. I was not able to edit the Label Map with the segment editor.<br>
Best regards rudolf</p>

---

## Post #14 by @cyufu (2020-05-02 09:43 UTC)

<p>In the DATA module, right-click on airway-lable, select Convert labelmap to Segmentiong node, and then you can edit it in the Segment Editor module.I hope it helps you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fdf194fadf8dad6b3562590bd0045b8c503fde5.png" data-download-href="/uploads/short-url/fXEZ9wx7b1fpAqYdKWWlvUTCKb3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fdf194fadf8dad6b3562590bd0045b8c503fde5.png" alt="image" data-base62-sha1="fXEZ9wx7b1fpAqYdKWWlvUTCKb3" width="690" height="467" data-dominant-color="E7ECF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">753×510 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @rbumm (2020-05-02 12:52 UTC)

<p>Thank you SIr, that should solve the airway segmentation problem.</p>

---

## Post #16 by @njh (2020-05-02 17:59 UTC)

<p>That’s exciting!<br>
When do you think you will roll it out?</p>

---

## Post #17 by @raul (2020-05-03 00:06 UTC)

<p>Hi All,</p>
<p>We use the Editor module and the Charts infrastructure within the CIP modules.  Is there a tutorial about the migration to the Segment Editor tool and the Charts infrastructure?</p>
<p>/R</p>

---

## Post #18 by @mangotee (2020-05-03 00:32 UTC)

<p>I agree that this is a rare use-case, and as such, this functionality can and maybe should be more “hidden” in the UI, but I find anisotropic resampling tp be valuable in the UI nonetheless. Just a few days ago, we wanted to test the behaviour of a pre-processing pipeline we are working on if (highly) anisotropic volumes were being processed. Since I only had isotropic images at hand, I used the “Resample Scalar Volume” module to quickly generate an anisotropic version of a few test samples I had. Helped us tremendously to anticipate errors/issues if such data was to be processed in future. It may be a rare thing to do, but I appreciate if it stays within the UI in some form, otherwise, I’d need to get out of Slicer, use a 3rd party tool etc… I like to stay within Slicer as much as I can during the prototyping stage.</p>

---

## Post #19 by @Fernando (2020-05-04 16:01 UTC)

<p>I also use <code>Resample Scalar Volume</code> often, mostly to try algorithms with smaller versions of the target image without having to create a new volume programmatically.</p>

---

## Post #20 by @lassoan (2020-05-05 20:50 UTC)

<p><a class="mention" href="/u/raul">@raul</a> since it affects only a handful of modules, we will not provide a detailed migration guide, but we can help you with any specific questions or help updating selected modules/features that you have problems with. SlicerCIP has other issues caused by Python3 and other API changes, which needs some work but will greatly simplify maintenance and development of CIP. Due to the expected surge of chest disease cases due to COVID-19, it would be a good time to make SlicerCIP work in current Slicer.</p>

---

## Post #21 by @muratmaga (2020-05-08 04:01 UTC)

<p>As you guys working towards Slicer 5, can I make the suggestion to start calling the 4.11 stream as as 5.0 preview?</p>
<p>There are few reasons for this. Primary reason is people new slicer do not initially appreciate how different current stable and the preview versions are under the hood. UI wise they look identical, but some of the changes, such as model coordinate system difference, python version, fiducial infrastructure etc, I think are more than you would anticipate in a minor version update.</p>
<p>I am not following the discussion closely, but Slicer 5 appears to have nebulous and rolling release timeline. As far as I can see most of the big changes is already there, the rest seems more like testing and removing functionality. So I see no harm calling the current preview as 5.0 preview.</p>

---
