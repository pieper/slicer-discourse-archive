---
topic_id: 19443
title: "Gantry Tilt Correction In Ct Dicoms"
date: 2021-08-31
url: https://discourse.slicer.org/t/19443
---

# Gantry tilt correction in CT DICOMS

**Topic ID**: 19443
**Date**: 2021-08-31
**URL**: https://discourse.slicer.org/t/gantry-tilt-correction-in-ct-dicoms/19443

---

## Post #1 by @Sharada (2021-08-31 18:11 UTC)

<p>Hello,</p>
<p>I am working on gantry tilt correction for CT images and was directed to 3D Slicer through Steve Pieper’s comment <a href="https://discourse.vtk.org/t/correcting-the-gantry-tilt-in-ct-scans/5526/4" rel="noopener nofollow ugc">here</a>. And I have run into the following issues -</p>
<ol>
<li>
<p>According to the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html?highlight=tilt#panels-and-their-use" rel="noopener nofollow ugc">documentation</a>, there should be an option to choose the plugins that examine a series while being imported. I am using Slicer 4.11 and don’t see that option.</p>
</li>
<li>
<p>I inferred from <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0" rel="noopener nofollow ugc">here</a> that the module “DICOMScalarVolumePlugin” accounts for gantry tilt and irregular slice spacing correction and made sure it is checked as a loaded module. But when I try to click on it after loading my (uncorrected) images, nothing happens.</p>
</li>
</ol>
<p>Can someone please help with this? How do I go about correcting gantry tilted CT images with Slicer?<br>
Thanks in advance!</p>

---

## Post #2 by @lassoan (2021-08-31 18:18 UTC)

<p>You need to enable <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#basic-usage">“Acquisition geometry regularization”</a> in application settings before you load the data set.</p>
<p>The plugin selector is on the left (“DICOM plugins” section), but you don’t need to touch those settings, as Scalar Volume plugin is enabled by default.</p>

---

## Post #3 by @Sharada (2021-08-31 19:00 UTC)

<p>Hi Andras,</p>
<p>I had enabled that before I attempted to load the DICOM images. I followed your comment <a href="https://discourse.slicer.org/t/actual-size-of-stl-models/5005/17">here</a>.</p>
<ol>
<li>When I load my images through the “DCM” module, I cannot even see my image volumes. I am not sure why this is happening? But this creates a transform which allows me to go to ‘Transform Hierarchy &gt; Harden Transform’</li>
<li>When I load it through “Data” module, I see the image volumes, but the view is not corrected. And this does not create a transform.<br>
Please see below - the following image was obtained at a gantry tilt of +21.5 degrees.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1b7665c4cf2868cfc25c500b2d9e3bbb45bcfa5.jpeg" data-download-href="/uploads/short-url/yuk0aw25MI8hvtcV6M8Lim08HwV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1b7665c4cf2868cfc25c500b2d9e3bbb45bcfa5_2_667x500.jpeg" alt="image" data-base62-sha1="yuk0aw25MI8hvtcV6M8Lim08HwV" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1b7665c4cf2868cfc25c500b2d9e3bbb45bcfa5_2_667x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1b7665c4cf2868cfc25c500b2d9e3bbb45bcfa5_2_1000x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1b7665c4cf2868cfc25c500b2d9e3bbb45bcfa5.jpeg 2x" data-dominant-color="555660"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1151×862 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>
<p>Please advise!</p>

---

## Post #4 by @lassoan (2021-08-31 19:09 UTC)

<p>You need to use the DICOM module for loading images. Click <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Reset field of view” button</a> to make sure your volume is in the field of view.</p>

---
