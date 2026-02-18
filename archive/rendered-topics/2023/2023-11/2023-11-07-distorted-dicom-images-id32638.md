# Distorted DICOM images

**Topic ID**: 32638
**Date**: 2023-11-07
**URL**: https://discourse.slicer.org/t/distorted-dicom-images/32638

---

## Post #1 by @willi (2023-11-07 07:45 UTC)

<p>Hi all,<br>
I have a problem loading some DICOM images recorded as slices of the coronal plane where the axial images show up distorted.<br>
Let me give some more information. I have MRI scans of the femur with two different sequences captured at same time (no participant movement) with a SIEMENS machine:</p>
<ol>
<li>
<p>axial scans of the lower legs with:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6b800522b159f156d7d6b258147367bebd0170f.png" alt="image" data-base62-sha1="nMRtOORPYaKga61GlcqSpNrYcwL" width="462" height="26"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4ff37cc3120c6245372c24686af8dc3af3ff495.png" alt="image" data-base62-sha1="nxD6DJjaPXNanmRsLLVTwsrAovz" width="341" height="29"><br>
so, voxel size is 0.989 (med/lat) x 1 (sup(/inf) x 0.989mm (ant/post)</p>
</li>
<li>
<p>coronal scans of the femur with:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e850a7f737fd1c55c3a9e0d0272051cf835c8e0.png" data-download-href="/uploads/short-url/mCktIIlbnmJub2T0TiVFf1wYzcI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e850a7f737fd1c55c3a9e0d0272051cf835c8e0.png" alt="image" data-base62-sha1="mCktIIlbnmJub2T0TiVFf1wYzcI" width="690" height="23" data-dominant-color="529ECF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">844×29 2.98 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8bc35fb8440f69de00cbe691abe383f46d71cdc.png" data-download-href="/uploads/short-url/sDMJvyPsMcGKJueJ6HtDvhikMag.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8bc35fb8440f69de00cbe691abe383f46d71cdc.png" alt="image" data-base62-sha1="sDMJvyPsMcGKJueJ6HtDvhikMag" width="690" height="24" data-dominant-color="3F94CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">747×26 2.38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
so, voxel size of this volume is 0.92 (med/lat) x 0.92 (sup(/inf) x 0.9mm (ant/post)</p>
</li>
</ol>
<p>Both DICOM series load to Slicer and I can view images in all 3 planes, so far so good!<br>
However, the axial images in the coronal scans (sequence 2) are distorted and I cannot figure out why and how to fix it.</p>
<p>Images below show the axial plane approximately at the same height (femoral head). In sequence 1, the femoral head appears as a circle, that seems to be correct.<br>
In sequence 2, the femoral head is distorted an shows as an ellipse. It appears that the anterior/posterior axis is shrinked or something like that.</p>
<ol>
<li>
<p>Sequence 1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97eba93cc13f94e63bf3ffd30cd39c7ac36cb0d8.jpeg" data-download-href="/uploads/short-url/lFWZYnWHTDBnIkxI95YMV1HXUVO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97eba93cc13f94e63bf3ffd30cd39c7ac36cb0d8_2_690x222.jpeg" alt="image" data-base62-sha1="lFWZYnWHTDBnIkxI95YMV1HXUVO" width="690" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97eba93cc13f94e63bf3ffd30cd39c7ac36cb0d8_2_690x222.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97eba93cc13f94e63bf3ffd30cd39c7ac36cb0d8_2_1035x333.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97eba93cc13f94e63bf3ffd30cd39c7ac36cb0d8_2_1380x444.jpeg 2x" data-dominant-color="7C7C7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×619 75.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Sequence 2<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3392b0b15a31f03261e3e1ce3fb707134fbfc91.jpeg" data-download-href="/uploads/short-url/u8zea6wB7GOkJ8oraqpG6AYzRxn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3392b0b15a31f03261e3e1ce3fb707134fbfc91_2_690x217.jpeg" alt="image" data-base62-sha1="u8zea6wB7GOkJ8oraqpG6AYzRxn" width="690" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3392b0b15a31f03261e3e1ce3fb707134fbfc91_2_690x217.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3392b0b15a31f03261e3e1ce3fb707134fbfc91_2_1035x325.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3392b0b15a31f03261e3e1ce3fb707134fbfc91_2_1380x434.jpeg 2x" data-dominant-color="797979"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×604 66.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>I have some more coronal scans of femurs and it seems to be the case in all of them, i.e. femoral head is not a sphere. Unfortunately, I do not have the other sequence to prove that something is wrong.</p>
<p>Does anyone has an idea what could case the problem here and how I can fix this? Is this a common problem with DICOM files from SIEMENS?</p>
<p>Thank you in advance,<br>
Best regards,<br>
Willi</p>

---

## Post #2 by @pieper (2023-11-07 13:39 UTC)

<p>A couple things to consider: make sure you load the data via the DICOM module and pay attention to any warnings during the load process.</p>
<p>Also you should be aware that SliceThickness is not the same as the out of plane spacing.  That is you can have thick slices that are close together or thin slices that are far apart.  For volume reconstruction the out of plane spacing is determined by the differences between Image Position Patient in the series.  So if you manually adjusted the spacing based on the slice thickness it could explain the distortion.</p>
<p>It can also be the case that slices are acquired at irregular intervals, meaning they don’t form a regular volume.  In this case Slicer will create a nonlinear transform that in most cases will put the slices back into a regular volume (you can harden that transform if you want to resample the image data into the regular spacing).</p>
<p>Is there any chance you can share an anonymized example that demonstrates this issue?  We take geometric accuracy very seriously.  Whether it’s a problem with Slicer or the Siemens data we’d like to get to the bottom of it.</p>

---

## Post #3 by @willi (2023-11-07 13:57 UTC)

<p>Hi Steve,<br>
thank you for the immediate reply.</p>
<p>No warnings appear when I load sequence 2 via the dicom module. When I load sequence 1, a warning appears, but I am pretty sure that this sequence is loaded correct because it shows the anatomically correct representation of the femoral head as a sphere.</p>
<p>I did not consider that SliceThickness and out of plane spacing can differ, thank you for pointing that out. However, I did not change any of the values manually, therefore, I guess this is not the problem.</p>
<p>When importing sequence 2, no transform is created by Slicer, I guess it is forms a regular volume.</p>
<p>Of course, I can share those anonymized DICOM files to you, I’ll upload them and send you a link in a private message because they should not be published.</p>
<p>I just had a call with the radiologist and she says that in such big scans (wide field of view) the parts on the edges are always distorted. Therefore, it could be, that this is not really a problem with the DICOM images but just with the scanning procedure. If that is really the case, do you think it is possible to create a non-rigid transform to “correct” the coronal scans? I have two participants with axial and coronal scans which could be used to find the appropriate transform for all other coronal scans (same scanner, same procedure). Is there any type of transform (or module) which you could recommend for this case?</p>
<p>Best regards,<br>
Willi</p>

---

## Post #4 by @pieper (2023-11-07 22:33 UTC)

<p>Hi Willi -</p>
<p>Thanks for sharing the anonymized data though through a private message.  I looked through the coronal acquisition dicom geometry and it appears to be loading correctly, so I tend to agree with the hypothesis that there is distortion in the scan itself.  It’s possible you could correct for this with image-based registration.  Let us know if you find out more.</p>
<p>-Steve</p>

---
