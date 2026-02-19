---
topic_id: 31072
title: "Unable To Load Philips Ge 3D Ultrasound In Slicer"
date: 2023-08-09
url: https://discourse.slicer.org/t/31072
---

# Unable to load Philips/GE 3D Ultrasound in Slicer

**Topic ID**: 31072
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/unable-to-load-philips-ge-3d-ultrasound-in-slicer/31072

---

## Post #1 by @Nihar_Parikh (2023-08-09 17:36 UTC)

<p>I am trying to load 3D Philips/GE Ultrasound DICOM datasets in Slicer 5.2.2 and facing issues with that. It is not able to render the volume from these datasets. I have installed SlicerHeart extension. On using the Examine option in slicer for these dataset I get this error<br>
“Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.Reference image in series does not contain geometry information. Please use caution.”</p>
<p>I can share these datasets for your troubleshooting. Also it would be of great help if you can share a valid 3D Ultrasound dicom datasets which can be loaded in Slicer with all volumetric data in the standard dicom fields.</p>

---

## Post #2 by @lassoan (2023-08-09 17:38 UTC)

<p>Each vendor implements 3D ultrasound storage completely differently, mostly in proprietary formats. All supported formats, capabilities and limitations for each are described in detail <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#importing-dicom-files">here</a>.</p>

---

## Post #3 by @Nihar_Parikh (2023-08-09 18:47 UTC)

<p>Thank you for the documentation link. So as I understand 3D Slicer does not natively support any 3D US format from Philps/GE? It relies on Image3D API library from each vendor?</p>
<p>When I am trying to examine these datasets I dont see ultrasound plugin being used. What does it mean?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a03132770871eabd76704ab0e0b0cad43383e4b3.png" data-download-href="/uploads/short-url/mR7NzNdkXlAdIAV36eERBk0R5gD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a03132770871eabd76704ab0e0b0cad43383e4b3_2_690x69.png" alt="image" data-base62-sha1="mR7NzNdkXlAdIAV36eERBk0R5gD" width="690" height="69" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a03132770871eabd76704ab0e0b0cad43383e4b3_2_690x69.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a03132770871eabd76704ab0e0b0cad43383e4b3_2_1035x103.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a03132770871eabd76704ab0e0b0cad43383e4b3_2_1380x138.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1464×148 39.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2023-08-09 19:24 UTC)

<p>Both Philips and Siemens uses several different formats for 3D ultrasound. Slicer can use Image3dAPI and other methods to read them.</p>
<p>What data do you have?</p>

---

## Post #5 by @Nihar_Parikh (2023-08-09 19:48 UTC)

<p>Not sure If I will able to correctly answer that. I can share the datasets if that helps.</p>
<p>GE<br>
Manufacturer Model name  - Vivid E95<br>
Private tag group - GEMS_Ultrasound_MovieGroup_001</p>
<p>Philips<br>
Manufacturer Model name  - EPIQ CVx<br>
Private tag group - Philips Imaging DD XX series</p>

---

## Post #6 by @lassoan (2023-08-09 20:31 UTC)

<p>GE cardiovascular 3D ultrasound images can be read using the Image3dAPI interface. It is natively supported by Slicer and all you need to do is to get the codec from GE.</p>
<p>The situation is worse with Philips cardiac ultrasound business. They want to control the data <em>you</em> acquire. Currently, the only way they allow getting access to their 4D images (but only basic B-mode data, no Doppler flow, no ECG, …) is via QLab Cartesian export as described <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#import-philips-4d-cardiac-images">here</a>.</p>
<p>Philips seems to abuse its position as an ultrasound image acquisition device manufacturer to suppress competition in ultrasound processing software market. We’ll probably start a petition to raise awareness of this issue, but if hospitals keep buying Philips then they may keep ignoring the complaints.</p>

---

## Post #7 by @Nihar_Parikh (2023-08-09 20:58 UTC)

<p>Thanks for that information. Yeah that does not sound great if QLab Cartesian export is the only way to render US echo 3D studies from Philips. Is it the case that Philips don’t make Image3DAPI interface public or they just don’t implement it?<br>
SlicerHeart extension has couple of  Philips plugins to read private data. Do they support any particular format ?</p>

---

## Post #8 by @Nihar_Parikh (2023-08-10 17:29 UTC)

<p>Few questions if you can help to understand how to deal with Philips datasets</p>
<ol>
<li>SlicerHeart extension has couple of Philips plugins to read private data. Do they support any particular format or manufactures?</li>
<li>Is it possible to reverse engineer Philips 3D ultrasound images and build decoder for reading volumetric data if there is no support from them ?</li>
</ol>

---

## Post #9 by @lassoan (2023-08-10 22:32 UTC)

<p>There are a multiple of groups, who partially reverse-engineered the non-Cartesian (not-QLab-converted) Philips 4D ultrasound image file format. I’ll try to convince them to be nice and share what they have figured out so far.</p>

---

## Post #10 by @Nihar_Parikh (2023-08-10 23:01 UTC)

<p>Thanks that would help. I believe decoder for 3D image will be different than 4D image or we can use the same mechanism to decode 3D image as well?</p>
<p>I could see from the source code of DicomUltrasoundPlugin that it supports PhilipsAffinity 3D US image. Possible to share PhilipsAffinity 3D US image files just to see how a valid dataset looks like ?</p>

---
