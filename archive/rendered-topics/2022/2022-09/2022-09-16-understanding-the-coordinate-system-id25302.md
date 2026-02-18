# Understanding the coordinate system

**Topic ID**: 25302
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/understanding-the-coordinate-system/25302

---

## Post #1 by @jegberink (2022-09-16 09:41 UTC)

<p>Hello Everyone,</p>
<p>If possible i would like some help in understanding the coordinate system of Slicer.<br>
I’ve read the documentation on the coordinate system: <a href="https://www.slicer.org/wiki/Coordinate_systems" class="inline-onebox" rel="noopener nofollow ugc">Coordinate systems - Slicer Wiki</a><br>
As well as some other sources.</p>
<p>I do not have a background relating to anything technical or computer science related so any help would be appreciated.</p>
<p>From what i understand right now, please correct me if i’m wrong:<br>
You have the world coordinate system in mm related to the scanner with a origin at the center of the scanner as set by the manufacturer. This is the XYZ axis.</p>
<p>You have the anatomical coordinate system in mm, which is in relation to the patient. From what i’ve gathered the origin is arbitrarily chosen by the technitian/physician, in relation to the world coordinate system. This is saved in the DICOM files and used as the 0,0,0 when viewing a file in Slicer. These are LPS coordinates, while slicer works in the RAS system (both still part of the anatomical system, just relating to positive and negative values).</p>
<p>You have the image coordinate system, which is the actual scanned data, which is unitless and contains the voxels along the IJK axes with the density data per voxel. The spacing between each voxel is stored with its data and is a chosen parameter by the technitian. Together with the origin at the top left this can be used to calculate the anatomical coordinates.</p>
<p>To go from the IJK axes to the anatomical axes an affine transformation is used. From what i understand is that for instance if the patient is not alligned with the axes, for instance due to gantry tilt, the spacing in the ijk axes would not coincide with the coordinates in the anatomical axes, so this transformation is needed to correct it. Is this done automatically in slicer/the DICOM files when viewing things in the coronal, axial and sagittal planes?</p>
<p>Moreover, any measurements you make would be around the predifined anatomical axes?</p>
<p>Now this is where i’m truly doubting myself, as my understanding doesn’t hold up to what i see in my DICOM files.</p>
<p>I have a preoperative and postoperative CT scan of the lower body, relating to an osteotomy of the proximal femur, with a reorientation of the femoral head. My final goal is to overlap the left femur of pre and postoperative, create a model of the femur, then measure the angle at which the proximal part of the femur has moved so we can compare it with the original planned model for the operation. I’ve come as far as the measurement, so i wanted to understand the axes along which the measurements take place a little better.</p>
<p>So after reading up i started to compare the scans. Now, unfortunately the CT scans were not created equally.</p>
<p>To see if my understanding held up, i loaded up the preoperative scan of 1 patient, put a point right in the center and saw that what i thought to be true could indeed be so. 0,0,0 seems to be at an anatomical origin, left is left, right is right, etc.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a17daeda9820c7af5c2a7ff0e12b6a01bedcf00.jpeg" data-download-href="/uploads/short-url/8hUNLVXAPro7oRMkKR7h5raWLFC.jpeg?dl=1" title="pre op" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a17daeda9820c7af5c2a7ff0e12b6a01bedcf00_2_487x500.jpeg" alt="pre op" data-base62-sha1="8hUNLVXAPro7oRMkKR7h5raWLFC" width="487" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a17daeda9820c7af5c2a7ff0e12b6a01bedcf00_2_487x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a17daeda9820c7af5c2a7ff0e12b6a01bedcf00.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a17daeda9820c7af5c2a7ff0e12b6a01bedcf00.jpeg 2x" data-dominant-color="A287A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pre op</span><span class="informations">606×622 31 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Now when i open up the postoperative in a new instance of slicer is were i started to doubt myself. The scan seems to be placed far to the back and right of the origin and tilted slightly, as if lying on the left side. I also noticed the slices where not oriented in the anatomical planes, instead it says “reformat” and i have to put them in the correct view. this does not change the position of anything else.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e15b26617908e0c055d3dd21f71c7b8af414ff22.jpeg" data-download-href="/uploads/short-url/w9AIyxP9A83PyNoF4w93Uaxq6Do.jpeg?dl=1" title="postop1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e15b26617908e0c055d3dd21f71c7b8af414ff22_2_424x500.jpeg" alt="postop1" data-base62-sha1="w9AIyxP9A83PyNoF4w93Uaxq6Do" width="424" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e15b26617908e0c055d3dd21f71c7b8af414ff22_2_424x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e15b26617908e0c055d3dd21f71c7b8af414ff22.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e15b26617908e0c055d3dd21f71c7b8af414ff22.jpeg 2x" data-dominant-color="9C8AB0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">postop1</span><span class="informations">633×746 43.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/520e5314a663c59e559d7d5e1b5a034edcd13efd.jpeg" alt="postop" data-base62-sha1="bHTQfwGYT0F7clFN87YZUwEFM29" width="362" height="350"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e814ef09a553f84d97d8ac140ce7bb5ac4188c3.jpeg" data-download-href="/uploads/short-url/bcuhDUrCvK8eaoPdqkWWAw0op0v.jpeg?dl=1" title="postop2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e814ef09a553f84d97d8ac140ce7bb5ac4188c3.jpeg" alt="postop2" data-base62-sha1="bcuhDUrCvK8eaoPdqkWWAw0op0v" width="690" height="438" data-dominant-color="444445"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">postop2</span><span class="informations">712×452 35 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is my understanding correct and is this scan just incorrect, or am i completely missing the right way to look at the data/coordinate systems?</p>
<p>Sorry for the long post and thank you kindly in advance</p>

---
