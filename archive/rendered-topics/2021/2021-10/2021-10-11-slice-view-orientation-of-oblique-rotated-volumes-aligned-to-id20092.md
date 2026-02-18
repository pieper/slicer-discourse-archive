# Slice view orientation of oblique/rotated volumes - aligned to volume or anatomical axes?

**Topic ID**: 20092
**Date**: 2021-10-11
**URL**: https://discourse.slicer.org/t/slice-view-orientation-of-oblique-rotated-volumes-aligned-to-volume-or-anatomical-axes/20092

---

## Post #1 by @Sharada (2021-10-11 05:15 UTC)

<p>I have a Sagittal volume (DICOM) that is displayed obliquely in Slicer (because it is an oblique sagittal reconstruction) and it makes perfect sense.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1cb35c2c213b1746a1af570a3bb648e0b061d5c.jpeg" data-download-href="/uploads/short-url/rEnwGDl1JL2FyptW2wnt8YSL5yA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1cb35c2c213b1746a1af570a3bb648e0b061d5c_2_690x475.jpeg" alt="image" data-base62-sha1="rEnwGDl1JL2FyptW2wnt8YSL5yA" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1cb35c2c213b1746a1af570a3bb648e0b061d5c_2_690x475.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1cb35c2c213b1746a1af570a3bb648e0b061d5c_2_1035x712.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1cb35c2c213b1746a1af570a3bb648e0b061d5c.jpeg 2x" data-dominant-color="5C5D68"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1265×872 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here is the volume information:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73ad18ffbb7bb51cddd3a13c6f64e20753de3128.png" alt="image" data-base62-sha1="gvjLGsGPRVgvnOFK9WXLZ9Rsk3e" width="529" height="180"></p>
<p>The same image, when converted from DICOM to NIFTI and loaded to SPM is displayed “upright”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dca949d72ee7ac26ce495bc2c91102fd27b15a73.png" data-download-href="/uploads/short-url/vu3K1qNr94yZtYZ6Ey7DNgJxEKD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dca949d72ee7ac26ce495bc2c91102fd27b15a73_2_425x500.png" alt="image" data-base62-sha1="vu3K1qNr94yZtYZ6Ey7DNgJxEKD" width="425" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dca949d72ee7ac26ce495bc2c91102fd27b15a73_2_425x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dca949d72ee7ac26ce495bc2c91102fd27b15a73_2_637x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dca949d72ee7ac26ce495bc2c91102fd27b15a73.png 2x" data-dominant-color="C2C2C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">775×911 57.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am wondering if someone can explain this difference in functionality to me. Is there a way I can get this behavior in Slicer?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2021-10-13 02:56 UTC)

<p>In earlier Slicer versions, slice views were initialized to be aligned with anatomical axes (as defined when the patient was scanned). In recent Slicer Preview Releases we switched to aligning slice views with voxel arrays because this seems to be what most users expect.</p>
<p>You can switch between the two orientations using <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">slice view controls</a>:</p>
<ul>
<li>choose an anatomical plane using the “Slice orientation” selector to align with anatomical axes</li>
<li>click “Rotate to volume plane” button to snap the slice plane to volume axes</li>
</ul>
<p>In recent Slicer Preview Releases, clicking on the eye icon in Data module automatically rotates to volume plane, unless the features is turned off (by right-clicking on the eye icon and unchecking “Reset view orientation on show”).</p>

---

## Post #3 by @Sharada (2021-10-16 19:05 UTC)

<p>Thank you for the helpful explanation! I have a related follow-up question:<br>
When I reformat images as axial, coronal, and sagittal, I see that I can scroll through and view orthogonal slices. But the volume is not really resliced orthogonally - does Slicer have functionality to do this?</p>

---

## Post #4 by @lassoan (2021-10-17 00:20 UTC)

<aside class="quote no-group" data-username="Sharada" data-post="3" data-topic="20092">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ba8739/48.png" class="avatar"> Sharada:</div>
<blockquote>
<p>But the volume is not really resliced orthogonally - does Slicer have functionality to do this?</p>
</blockquote>
</aside>
<p>Yes, when you scroll the slices they are all resliced along the chosen axis. This can be an arbitrary direction. You can change the direction by showing slice intersections and then Ctrl+Alt+Left-click-and-drag in a slice view.</p>

---

## Post #5 by @Sharada (2021-10-17 00:48 UTC)

<p>I see, but I meant that the volume is not resliced orthogonally or my preferred orientation when I export it as a dicom. So it’s not really altering the ras2ijk matrices, but only visually.</p>
<p>Sorry for being unclear in my first question. What I’m trying to achieve is to convert an obliquely acquired volume with a direction cosine matrix not equal to the true Sagittal/axial/coronal orientations to be orthogonally resliced.</p>
<p>Is there a way to do this in slicer?</p>
<p>Thanks,<br>
Sharada</p>

---

## Post #6 by @lassoan (2021-10-17 01:50 UTC)

<p>Yes, sure, you can resample the volume with arbitrary axis directions and create a new volume from that. Probably the simplest is to use Crop volume module and using an ROI box with with axes aligned with RAS axes.</p>
<p>You can also use the ACPC transform module to accurately orient the head into standard orientation (the head orientation on the CT table is just approximately aligned with anatomical axes) and use the computed transform as input in an image resampling module.</p>

---

## Post #7 by @Sharada (2021-10-17 23:51 UTC)

<p>This is great! Thank you so much for your help. I noticed that the ROI which is added by default is already aligned with the RAS axes. So I have a two step procedure: 1) Crop the volume 2) ACPC transform to make the alignment perfect.</p>
<p>Here is what I am doing for cropping -</p>
<p>volumeNode = slicer.util.getNode(‘Sagittal resampled’)<br>
roiNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLAnnotationROINode”)</p>
<p>crop_module = slicer.vtkMRMLCropVolumeParametersNode()<br>
slicer.mrmlScene.AddNode(crop_module)</p>
<p>crop_module.SetInputVolumeNodeID(volumeNode.GetID())<br>
crop_module.SetROINodeID(roiNode.GetID())</p>
<p>slicer.modules.cropvolume.logic().FitROIToInputVolume(crop_module)<br>
slicer.modules.cropvolume.logic().Apply(crop_module)</p>
<p>And it works mostly as I expect it to. But I have one question: The ijk2ras direction matrices are set to identity for all my volumes after cropping. So if I start with a volume like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdd54833bc71c13c7b3ab37423d2c75fcc1e3262.png" data-download-href="/uploads/short-url/AdvKN0IyyxruGMeelCy0eBsdfNg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdd54833bc71c13c7b3ab37423d2c75fcc1e3262.png" alt="image" data-base62-sha1="AdvKN0IyyxruGMeelCy0eBsdfNg" width="690" height="258" data-dominant-color="E5E5E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">778×292 6.19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Why does the ijk2ras get reset to identity instead of  [[-1,0,0],[0,-1,0],[0,0,1]]?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50d54d900e12eca63635813532401bb80603d371.png" data-download-href="/uploads/short-url/bx5cdT72IbDr8xDt4R3QwMOQQ0x.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50d54d900e12eca63635813532401bb80603d371.png" alt="image" data-base62-sha1="bx5cdT72IbDr8xDt4R3QwMOQQ0x" width="690" height="294" data-dominant-color="EBECEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">769×328 6.51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also, I know this is minor - but I am so grateful to the people of Slicer development for having added a human orientation marker which adjusts itself according to the oblique acquisition matrices. It really helps beginners like me.</p>
<p>Best,<br>
Sharada</p>

---

## Post #8 by @lassoan (2021-10-18 00:08 UTC)

<p>There are 24 ways of choosing origin and axis directions (IJKtoRAS matrix) and reorder voxels in memory that results in having the same voxels at the same physical location. They are all equivalent.</p>
<p>The simplest IJKtoRAS mapping is identity matrix (<code>diag(1,1,1,1)</code>). However, IJKtoLPS mapping is used the most commonly in files, therefore a trivial IJKtoLPS mapping ends up as <code>diag(-1,-1,1,1)</code> when imported into Slicer.</p>
<p>If you need a specific geometry then you can use the image resampling modules (you can specify geometry using a reference volume, transform, or axes directions&amp;origin&amp;extents).</p>

---

## Post #9 by @Sharada (2021-10-18 00:41 UTC)

<p>Makes sense, I defined a transform and set the ijk2ras matrices after that. Thank you for your help with this!</p>

---

## Post #10 by @Sharada (2021-10-26 10:17 UTC)

<p>Hi Andras,</p>
<p>I have a follow-up question here. My workflow currently crops the volumes with ROIs aligned to the RAS axes, computes the ACPC transform, and then resamples the cropped volumes. I noticed that an offset (arrow in the image below) is introduced between the coronal and sagittal volumes after the transformation. Could you please help explain this? I have already tried specifying the AC as rotation point in the rigid/affine parameters section of the resample scalar/vector/dwi volume - the offset is still visible.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad7951d56be3d1d8630722553356968e8f488751.jpeg" data-download-href="/uploads/short-url/oKCwLObPb7H2oOdQZz3Tp0xctH3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad7951d56be3d1d8630722553356968e8f488751_2_638x500.jpeg" alt="image" data-base62-sha1="oKCwLObPb7H2oOdQZz3Tp0xctH3" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad7951d56be3d1d8630722553356968e8f488751_2_638x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad7951d56be3d1d8630722553356968e8f488751_2_957x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad7951d56be3d1d8630722553356968e8f488751.jpeg 2x" data-dominant-color="1D1E1D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1085×850 93.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Strangely, this is the case with only some of the scans I have.</p>
<p>I also noticed that if I apply the ACPC transform first, from the transforms module, harden it, and then crop the volumes, this issue does not arise.</p>
<p>Thanks!</p>

---

## Post #11 by @lassoan (2021-10-26 11:43 UTC)

<p>Can you share (upload somewhere and post the link here) an anonymized data set that has this issue?</p>

---

## Post #12 by @Sharada (2021-10-26 14:47 UTC)

<p>Unfortunately, I’m not able to share the anonymized data. I understand if we cannot proceed without it.</p>
<p>Does it make sense to apply, harden acpc transform, and crop volume instead of what cropping first and then resampling with the acpc transform?</p>

---

## Post #13 by @lassoan (2021-10-27 04:45 UTC)

<p>The ACPC transform is just a linear transform so it will not decrease the image quality, so if you find that hardening it improves the results then it should be fine to do it.</p>
<p>There are huge public brain MRI databases, so if you want us to investigate this difference in the border then you may try to reproduce it with a data set taken from those.</p>

---
