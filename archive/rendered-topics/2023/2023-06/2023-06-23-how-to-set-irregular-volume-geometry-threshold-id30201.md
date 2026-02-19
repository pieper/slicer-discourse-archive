---
topic_id: 30201
title: "How To Set Irregular Volume Geometry Threshold"
date: 2023-06-23
url: https://discourse.slicer.org/t/30201
---

# How to set "Irregular volume geometry" threshold?

**Topic ID**: 30201
**Date**: 2023-06-23
**URL**: https://discourse.slicer.org/t/how-to-set-irregular-volume-geometry-threshold/30201

---

## Post #1 by @mikebind (2023-06-23 20:50 UTC)

<p>Hello, our clinical DICOM images very often seem to end up having “irregular volume geometry” detected just above the threshold of 0.001 mm.</p>
<p>This is a typical message I got today:<br>
<code>[Python] Irregular volume geometry detected (maximum error of 0.0010596 mm is above tolerance threshold of 0.001 mm).  Adding acquisition transform to regularize geometry.</code></p>
<p>I am never making measurements at a much finer scale than a voxel, which is at least 250x larger than this threshold (0.25 mm at the smallest for images I work with). This results in creation of an unnecessary (for me) nonlinear “acquisition transform”.   Is there a way I could increase the threshold to avoid this?  I don’t want to turn the warning off entirely because I want to know if there is a large irregularity in something I try to load, but this threshold is a little too sensitive for the data I work with.</p>

---

## Post #2 by @lassoan (2023-06-25 17:39 UTC)

<p>Clinical scanners do not usually have such problems. What kind of scanners do you use? Do you see this error on the data that comes directly from the scanner or is it introduced during reprocessing/anonymization of the images?</p>
<p>The tolerance values are specified in <code>DICOMScalarVolumePlugin.py</code> and you can modify this file on your computer as you see fit. If we find that clinical scanners violate these tolerances then we may consider making them adjustable in application settings, but it is simpler and safer to keep them as constant values.</p>

---

## Post #3 by @mikebind (2023-06-26 15:44 UTC)

<p>The image volume which generated that error message came from a Siemens Avanto Fit, on DICOM images downloaded directly from our clinical PACS (no reprocessing before importing to Slicer).</p>
<p>Thanks for the reference to the threshold location, I will modify the threshold to bump it up a little to 0.005 mm.</p>

---

## Post #4 by @lassoan (2023-06-26 16:03 UTC)

<p>It would be interesting to know that it is due to rounding (the manufacturer thinks it is OK to use 3 digits after the decimal); or there is some inconsitency at the first or last slice; or there is an issue somewhere in the middle.</p>
<p>Could you copy here the <code>ImagePositionPatient</code> tag values for the series? (right-click <code>View DICOM metadata</code>, type <code>ImagePositionPatient</code> in the filter, click <code>Copy all files metadata</code>, save to file, upload the file somewhere and post the link here)</p>

---

## Post #5 by @mikebind (2023-06-26 16:09 UTC)

<p>Here you go: <a href="https://drive.google.com/file/d/1m1NkeFUQr8zfVjmMOM_EitBwDbRYL1sL/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">IrregularImagePositionPatientExample.txt - Google Drive</a>  Let me know if you have any trouble accessing.</p>

---

## Post #6 by @pieper (2023-06-26 16:55 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> are these for a rotated MR volume?  I think sometimes there are limits on what the gradients can achieve so the slicer prescription gets clamped to a nearest value or something.  In that case I’m not sure if it’s good to ignore the spacing irregularity or apply the geometry correction (or maybe the difference is negligible).</p>
<p>In any case for batch processing I have found it useful to auto-apply the acquisition transform and maybe we should expose that as a user setting in addition to making the tolerance settable.</p>

---

## Post #7 by @mikebind (2023-06-26 17:43 UTC)

<p>My apologies!  I just realized I grabbed the wrong series metadata.  I had loaded both an MR and a CT for this patient and misremembered which one had the irregularity error message.  It was the CT which was warned as irregularly spaced.  Here is the image position patient data for that image volume: <a href="https://drive.google.com/file/d/1Chaqe6mXqx_y6up_JdMVghdmWCfSc1TA/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">IrregularImagePositionPatientExample_CT.txt - Google Drive</a></p>
<p><a class="mention" href="/u/pieper">@pieper</a>, to your question about whether it is a rotated volume, this is the volume information<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b25aea11dfbfcef4ff5ca447ecb4b5ab46e0868d.png" data-download-href="/uploads/short-url/prNLUF22LqbaJqhif1rpFliWkAl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b25aea11dfbfcef4ff5ca447ecb4b5ab46e0868d_2_690x221.png" alt="image" data-base62-sha1="prNLUF22LqbaJqhif1rpFliWkAl" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b25aea11dfbfcef4ff5ca447ecb4b5ab46e0868d_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b25aea11dfbfcef4ff5ca447ecb4b5ab46e0868d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b25aea11dfbfcef4ff5ca447ecb4b5ab46e0868d.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">712×229 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I understand where you are coming from correctly, yes, this is a rotated volume because the IJK to RAS directions are not exactly aligned.</p>

---

## Post #8 by @lassoan (2023-06-27 03:34 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> There seems to be a rounding of the position offset between neighbor frames to 3 digits (0.032 or 0.033). This corresponds to 0.001/0.032 = 3.1% error in slice spacing, which is quite small, but not necessarily negligible. Also, the rounding is a bit unexpected, because the position values have 6 digits after the decimal point. I would recommend to report this problem to the manufacturer.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> It seems that currently we use absolute tolerance values. What do you think about setting the tolerance as percentage of the slice spacing? Maybe we could then be a bit more permissive and say we allow up to 5% variation in slice spacing?</p>

---

## Post #9 by @mikebind (2023-06-27 04:33 UTC)

<p>Thanks for looking into it. A relative tolerance threshold sounds like a good idea to me. I will work on figuring out how to report the problem to Siemens.</p>

---

## Post #10 by @pieper (2023-06-27 06:44 UTC)

<p>It would be good to talk to someone who could give insight into why these small differences occur to decide if resampling is more accurate or leaving them as-is is more accurate (i.e. are the positions incorrectly recorded or do the correctly denote irregularly spaced slices).</p>
<p>But yes, a relative error sounds reasonable in any case.</p>

---

## Post #11 by @mikebind (2023-06-27 07:34 UTC)

<p>I was thinking exactly the same thing: if the slices are equally spaced but the recorded slice locations are being rounded, then the right thing to do is to treat the slices as equally spaced despite the rounding errors. The alternative is that the slice locations reported are measured more accurately than the scanner’s ability to space slices equally. In that case, the theoretically right thing to do is to treat the slices as unequally spaced and have a transform applied to achieve that. Either of those options seems somewhat plausible to me, so I agree it would be good to talk to some who would know which is actually the case.</p>

---
