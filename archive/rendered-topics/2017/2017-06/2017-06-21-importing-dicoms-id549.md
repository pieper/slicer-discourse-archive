---
topic_id: 549
title: "Importing Dicoms"
date: 2017-06-21
url: https://discourse.slicer.org/t/549
---

# Importing DICOMs

**Topic ID**: 549
**Date**: 2017-06-21
**URL**: https://discourse.slicer.org/t/importing-dicoms/549

---

## Post #1 by @victoria.rose (2017-06-21 21:13 UTC)

<p>Operating system: Microsoft Windows 7<br>
Slicer version: 4.6.2</p>
<p>I have a CD with the DICOM files and directory for about 40 MR images. I cannot manage to import the DICOM folder directly into 3D Slicer - the program iterates through all of the files over about 30 minutes and then displays that 0 patients have been added. If I export each MRI series individually as a .dcm from GearView, Slicer will upload the images but results in distorted coronal and sagittal images with the error “Geometric issues were found with 1 of the series. Please use caution”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e85a526e5a635054ed9afc231fbcfa79113e4635.png" data-download-href="/uploads/short-url/x9uhNIQZrJRpnMmbHTHGFzhcvFX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e85a526e5a635054ed9afc231fbcfa79113e4635_2_690x404.png" alt="image" data-base62-sha1="x9uhNIQZrJRpnMmbHTHGFzhcvFX" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e85a526e5a635054ed9afc231fbcfa79113e4635_2_690x404.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e85a526e5a635054ed9afc231fbcfa79113e4635.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e85a526e5a635054ed9afc231fbcfa79113e4635.png 2x" data-dominant-color="3E3D49"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">885×519 88.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am unfamiliar with DICOM files and am unsure how to successfully load these into Slicer. (I’ve tried loading the files with DICOMDiffusionVolumePlugin disables as well). Thanks for any help!</p>

---

## Post #2 by @lassoan (2017-06-21 22:03 UTC)

<p>Please try it again, with the latest nightly version of Slicer.</p>

---

## Post #3 by @fedorov (2017-06-22 02:25 UTC)

<p>Sometime Slicer DICOM database becomes unaccessible, or the database path is not writeable after installation. You can try resetting the database location to a new location that is writeable.</p>

---

## Post #4 by @victoria.rose (2017-06-22 21:01 UTC)

<p>Downloaded the nightly version of Slicer and the images are back to normal. Thank you!</p>

---

## Post #5 by @victoria.rose (2017-06-27 13:55 UTC)

<p>Slicer 4.7.0</p>
<p>All of the images have loaded, however they are not the quality expected and Slicer outputs the error: “Warning in DICOM plugin Scalar Volume when examining loadable 5: <em>File name</em> There is no pixel data attribute for the DICOM objects, but they might be readable as secondary capture images.” Any idea how to resolve this error?</p>
<p>Thanks!</p>

---

## Post #6 by @pieper (2017-06-28 06:56 UTC)

<p>Hi -</p>
<p>Can you try the steps described here [1] and report back?</p>
<p>-Steve</p>
<p>[1] <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---
