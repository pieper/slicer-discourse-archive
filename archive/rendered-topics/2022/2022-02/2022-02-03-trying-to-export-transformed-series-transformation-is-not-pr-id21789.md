# Trying to export transformed series, transformation is not present in exported series

**Topic ID**: 21789
**Date**: 2022-02-03
**URL**: https://discourse.slicer.org/t/trying-to-export-transformed-series-transformation-is-not-present-in-exported-series/21789

---

## Post #1 by @JuliusJ (2022-02-03 17:42 UTC)

<p>I’m new to Slicer and I’m trying to accomplish fairly simple things. Please explain things like I’m five years old. I’m using version 4.13.0-2022-01-28 r30570 / 0130983 on Mac OS Catalina.</p>
<p>I have an MRI study where the patient is in wrong orientation due to erroneous patient positioning parameters selected on the scanner. I’m trying to flip the series horizontally to correct this.</p>
<p>I am able to create the transformation, apply it to the images, and harden it as per the documentation. Transformation can be observed in the images in Slicer.</p>
<p>However, when I try to export the transformed series to DICOM, the transformation is not applied in these images when I open then in a DICOM viewer. What am I doing wrong?</p>
<p>Additionally, some of the DICOM tags that were present in the original series, such as series description etc, are erased in the process. Is there a way to prevent this from happening?</p>

---

## Post #2 by @lassoan (2022-02-04 05:23 UTC)

<aside class="quote no-group" data-username="JuliusJ" data-post="1" data-topic="21789">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/e19adc/48.png" class="avatar"> JuliusJ:</div>
<blockquote>
<p>However, when I try to export the transformed series to DICOM, the transformation is not applied in these images when I open then in a DICOM viewer. What am I doing wrong?</p>
</blockquote>
</aside>
<p>Linear transforms can be applied to a volume without modifying the voxel data. If you use a 2D image viewer then most likely there will be no visible difference other than image orientation indicators (A/P, L/R, I/S).</p>
<aside class="quote no-group" data-username="JuliusJ" data-post="1" data-topic="21789">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/e19adc/48.png" class="avatar"> JuliusJ:</div>
<blockquote>
<p>Additionally, some of the DICOM tags that were present in the original series, such as series description etc, are erased in the process. Is there a way to prevent this from happening?</p>
</blockquote>
</aside>
<p>Slicer creates a new series with only essential metadata.</p>
<p>If you want to “fix” a DICOM series keeping all data intact then it is a complex task, as you need to recompute image position and orientation tags and at least regenerate UIDs (series instance UID, SOP instance UIDs) for each DICOM file. If you are not sure how to do this then you can either try to find other software that would do such thing or use Slicer and accept that only essential fields will be set in the new series.</p>

---

## Post #3 by @JuliusJ (2022-02-15 07:13 UTC)

<p>Thank you for your response.</p>
<p>At this point, I would have been satisfied with just mirroring the images without fixing actual patient or image orientation tags in DICOM, but I can’t seem to be able to apply that simple transform to exported DICOM images.</p>
<p>So, if I were to recompute the tags (0020,0032)Image Position (Patient) and (0020,0037)Image Orientation (Patient), could you point me to a resource on how to approach this?</p>

---

## Post #4 by @lassoan (2022-02-18 16:55 UTC)

<p>Are you sure you want to actually mirror the image? If the patient was not scanned in the correct orientation then the image is not mirrored, but rotated by 180 degrees.</p>
<p>Probably the simplest way to edit DICOM tags is by using pydicom. See for example how it is done in the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPatcher/DICOMPatcher.py">DICOM Patcher module</a>.</p>

---
